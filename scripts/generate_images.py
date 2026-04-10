#!/usr/bin/env python3
"""
Batch generate all images from IMAGE-PLAN.md using Google Gemini (NanoBanana Pro).

Usage:
    uv run --with google-genai --with Pillow python scripts/generate_images.py
    uv run --with google-genai --with Pillow python scripts/generate_images.py --dry-run
    uv run --with google-genai --with Pillow python scripts/generate_images.py --module 01
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent.parent
IMAGE_PLAN = ROOT / "IMAGE-PLAN.md"
IMAGES_DIR = ROOT / "images"

# Load API key
ENV_PATH = ROOT / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = "gemini-3-pro-image-preview"
COST_PER_IMAGE_ESTIMATE = 0.04  # rough estimate per image


def parse_image_plan(plan_path: Path) -> list[dict]:
    """Parse IMAGE-PLAN.md and extract all image entries."""
    text = plan_path.read_text()
    images = []

    # Split by module sections
    module_sections = re.split(r'^## Module (\d+):', text, flags=re.MULTILINE)

    for i in range(1, len(module_sections), 2):
        module_num = module_sections[i].strip()
        section = module_sections[i + 1]

        # Split by image entries
        image_blocks = re.split(r'^### Image \d+:', section, flags=re.MULTILINE)

        for block in image_blocks[1:]:  # Skip content before first image
            entry = {"module": module_num}

            # Extract name from first line
            first_line = block.strip().split("\n")[0].strip()
            entry["name"] = first_line

            # Extract file path
            file_match = re.search(r'\*\*File\*\*:\s*`([^`]+)`', block)
            if file_match:
                entry["file"] = file_match.group(1)

            # Extract status
            status_match = re.search(r'\*\*Status\*\*:\s*(.*)', block)
            if status_match:
                entry["status"] = status_match.group(1).strip()

            # Extract the prompt block
            prompt_match = re.search(r'```\s*\n(.*?)\n\s*```', block, re.DOTALL)
            if prompt_match:
                entry["prompt_raw"] = prompt_match.group(1).strip()

                # Parse individual prompt fields
                for field in ["Goal", "Scene", "Style", "Aspect ratio", "Background",
                              "Text in image", "Avoid"]:
                    field_match = re.search(rf'{field}:\s*(.*?)(?:\n|$)', entry["prompt_raw"])
                    if field_match:
                        entry[field.lower().replace(" ", "_")] = field_match.group(1).strip()

            # Extract description
            desc_match = re.search(r'\*\*Description\*\*:\s*(.*)', block)
            if desc_match:
                entry["description"] = desc_match.group(1).strip()

            images.append(entry)

    return images


def generate_image(client, entry: dict, dry_run: bool = False) -> dict:
    """Generate a single image using Gemini."""
    # Assemble the full prompt
    scene = entry.get("scene", "")
    style = entry.get("style", "Head First book illustration style")
    goal = entry.get("goal", "editorial illustration for a programming textbook")
    aspect = entry.get("aspect_ratio", "16:9")
    bg = entry.get("background", "white")
    text_in_img = entry.get("text_in_image", "minimal or none")
    avoid = entry.get("avoid", "photorealistic, dark, scary, complex UI screenshots")

    assembled = (
        f"{goal}. {scene} "
        f"Style: {style}. "
        f"Aspect ratio: {aspect}. "
        f"Background: {bg}. "
        f"Text in image: {text_in_img}. "
        f"Avoid: {avoid}."
    )

    if dry_run:
        return {"status": "dry_run", "prompt": assembled, "tokens": 0}

    start = time.time()
    response = client.models.generate_content(
        model=MODEL,
        contents=assembled,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    elapsed = int((time.time() - start) * 1000)

    # Extract image from response
    result = {
        "status": "generated",
        "generation_time_ms": elapsed,
        "prompt": assembled,
    }

    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                result["image_data"] = part.inline_data.data
                result["mime_type"] = part.inline_data.mime_type
                break

    # Extract usage
    if hasattr(response, "usage_metadata") and response.usage_metadata:
        um = response.usage_metadata
        result["usage"] = {
            "prompt_tokens": getattr(um, "prompt_token_count", 0) or 0,
            "candidates_tokens": getattr(um, "candidates_token_count", 0) or 0,
            "total_tokens": getattr(um, "total_token_count", 0) or 0,
        }
    else:
        result["usage"] = {"prompt_tokens": 0, "candidates_tokens": 0, "total_tokens": 0}

    return result


def save_image(entry: dict, result: dict):
    """Save generated image and metadata."""
    file_path = IMAGES_DIR / entry["file"].replace("images/", "")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Save image
    if "image_data" in result:
        file_path.write_bytes(result["image_data"])

    # Save metadata JSON
    meta_path = file_path.with_suffix(".json")
    meta = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "prompt": result.get("prompt", ""),
        "output_file": file_path.name,
        "generation_time_ms": result.get("generation_time_ms", 0),
        "usage": result.get("usage", {}),
    }
    meta_path.write_text(json.dumps(meta, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Generate images from IMAGE-PLAN.md")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--module", help="Only generate for this module number (e.g. 01)")
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip images that already exist (default)")
    parser.add_argument("--force", action="store_true", help="Regenerate all images")
    args = parser.parse_args()

    if not API_KEY and not args.dry_run:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)

    # Parse the plan
    images = parse_image_plan(IMAGE_PLAN)
    print(f"Found {len(images)} images in plan")

    # Filter by module if specified
    if args.module:
        images = [img for img in images if img["module"] == args.module.zfill(2)]
        print(f"Filtered to {len(images)} images for module {args.module}")

    if not images:
        print("No images to generate")
        return

    # Initialize client
    client = None
    if not args.dry_run:
        client = genai.Client(api_key=API_KEY)

    total_tokens = 0
    total_cost = 0.0
    generated = 0
    skipped = 0
    failed = 0

    for i, entry in enumerate(images, 1):
        file_rel = entry.get("file", "unknown")
        file_path = IMAGES_DIR / file_rel.replace("images/", "")

        # Skip existing
        if file_path.exists() and not args.force:
            skipped += 1
            print(f"  [{i}/{len(images)}] SKIP (exists): {file_rel}")
            continue

        print(f"  [{i}/{len(images)}] {'DRY RUN' if args.dry_run else 'Generating'}: {file_rel}")

        try:
            result = generate_image(client, entry, args.dry_run)

            if args.dry_run:
                print(f"    Prompt: {result['prompt'][:80]}...")
                continue

            if "image_data" in result:
                save_image(entry, result)
                tokens = result.get("usage", {}).get("total_tokens", 0)
                total_tokens += tokens
                generated += 1
                print(f"    OK ({result['generation_time_ms']}ms, {tokens} tokens)")
            else:
                failed += 1
                print(f"    FAILED: No image in response")

            # Rate limiting — small delay between requests
            if i < len(images):
                time.sleep(2)

        except Exception as e:
            failed += 1
            print(f"    ERROR: {e}")
            time.sleep(5)  # longer delay on error

    # Summary
    total_cost = generated * COST_PER_IMAGE_ESTIMATE
    print(f"\n{'=' * 50}")
    print(f"Results:")
    print(f"  Generated: {generated}")
    print(f"  Skipped:   {skipped}")
    print(f"  Failed:    {failed}")
    print(f"  Total tokens: {total_tokens}")
    print(f"  Estimated cost: ${total_cost:.2f}")
    print(f"{'=' * 50}")

    # Write cost summary to a file
    cost_file = ROOT / "IMAGE-COSTS.md"
    cost_file.write_text(
        f"# Image Generation Costs\n\n"
        f"- **Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- **Model**: {MODEL}\n"
        f"- **Generated**: {generated}\n"
        f"- **Skipped**: {skipped}\n"
        f"- **Failed**: {failed}\n"
        f"- **Total tokens**: {total_tokens}\n"
        f"- **Estimated cost**: ${total_cost:.2f}\n"
        f"- **Cost per image**: ~${COST_PER_IMAGE_ESTIMATE:.2f}\n"
    )
    print(f"\nCost summary written to IMAGE-COSTS.md")


if __name__ == "__main__":
    main()
