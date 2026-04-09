#!/usr/bin/env python3
"""
Generate narration audio from 🎙️ blocks in source markdown files.
Uses ElevenLabs TTS API.

Usage:
    uv run --with elevenlabs python scripts/generate_narration.py
    uv run --with elevenlabs python scripts/generate_narration.py source/module-01-what-is-java.md
    uv run --with elevenlabs python scripts/generate_narration.py --regenerate-changed
    uv run --with elevenlabs python scripts/generate_narration.py --force
    uv run --with elevenlabs python scripts/generate_narration.py --all
    uv run --with elevenlabs python scripts/generate_narration.py --dry-run
    uv run --with elevenlabs python scripts/generate_narration.py --voice drew
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

from elevenlabs import ElevenLabs

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "source"
AUDIO_DIR = ROOT / "audio"

# Load API key from .env
ENV_PATH = ROOT / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")

VOICES = {
    "rachel": "21m00Tcm4TlvDq8ikWAM",
    "drew": "29vD33N1CtxCmqQRPOHJ",
    "paul": "5Q0t7uMcjvnagumLfvZi",
    "sarah": "EXAVITQu4vr4xnSDxMaL",
    "emily": "LcfcDJNUP1GQjkzn1xUU",
    "charlie": "IKne3meq5aSn9XLyUdCD",
    "george": "JBFqnCBsd6RMkjVDRZzb",
    "matilda": "XrExE9yKIg1WjnnlVkGX",
}

DEFAULT_VOICE = "rachel"
MODEL = "eleven_multilingual_v2"


def extract_narration_blocks(md_text: str) -> list[str]:
    """Extract text from 🎙️ blockquotes."""
    blocks = []
    pattern = re.compile(r'^>\s*🎙️\s*(.*?)(?=\n(?!>)|\Z)', re.MULTILINE | re.DOTALL)

    lines = md_text.split("\n")
    in_block = False
    current = []

    for line in lines:
        if line.startswith("> 🎙️"):
            in_block = True
            text = line.replace("> 🎙️", "").strip()
            if text:
                current.append(text)
        elif in_block and line.startswith("> "):
            current.append(line[2:].strip())
        else:
            if current:
                blocks.append(" ".join(current))
                current = []
            in_block = False

    if current:
        blocks.append(" ".join(current))

    return blocks


def clean_text(text: str) -> str:
    """Strip markdown formatting for natural speech."""
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)        # italic
    text = re.sub(r'`([^`]+)`', r'\1', text)          # inline code
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links
    text = re.sub(r'#{1,6}\s*', '', text)              # headers
    return text.strip()


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def generate_audio(client: ElevenLabs, text: str, voice_id: str) -> bytes:
    """Generate audio from text using ElevenLabs."""
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id=MODEL,
        output_format="mp3_44100_128",
    )
    # audio is a generator, collect it
    chunks = []
    for chunk in audio:
        chunks.append(chunk)
    return b"".join(chunks)


def process_module(source_path: Path, voice_name: str, force: bool = False,
                   dry_run: bool = False, regenerate_changed: bool = False):
    """Process a single module file."""
    md_text = source_path.read_text()
    blocks = extract_narration_blocks(md_text)

    if not blocks:
        print(f"  {source_path.name}: no narration blocks")
        return

    module_slug = source_path.stem
    audio_dir = AUDIO_DIR / module_slug
    manifest_path = audio_dir / "manifest.json"

    # Load existing manifest
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())

    voice_id = VOICES.get(voice_name, VOICES[DEFAULT_VOICE])
    client = None if dry_run else ElevenLabs(api_key=API_KEY)

    audio_dir.mkdir(parents=True, exist_ok=True)
    new_manifest = {"voice": voice_name, "voice_id": voice_id, "blocks": []}

    generated = 0
    skipped = 0

    for i, raw_text in enumerate(blocks, 1):
        clean = clean_text(raw_text)
        h = text_hash(clean)
        filename = f"{i:02d}_{module_slug}.mp3"
        filepath = audio_dir / filename

        # Check if we can skip
        existing = manifest.get("blocks", [])
        existing_entry = next((e for e in existing if e.get("index") == i), None)

        should_generate = force
        if not force:
            if not filepath.exists():
                should_generate = True
            elif regenerate_changed and existing_entry and existing_entry.get("hash") != h:
                should_generate = True

        entry = {
            "index": i,
            "filename": filename,
            "text": clean,
            "hash": h,
        }
        new_manifest["blocks"].append(entry)

        if dry_run:
            status = "WOULD GENERATE" if should_generate else "exists"
            print(f"    [{i}/{len(blocks)}] {status}: {clean[:60]}...")
            continue

        if should_generate:
            print(f"    [{i}/{len(blocks)}] Generating: {clean[:60]}...")
            audio_data = generate_audio(client, clean, voice_id)
            filepath.write_bytes(audio_data)
            generated += 1
        else:
            skipped += 1

    # Write manifest
    if not dry_run:
        manifest_path.write_text(json.dumps(new_manifest, indent=2))

    # Clean up orphan audio files
    if not dry_run:
        expected = {e["filename"] for e in new_manifest["blocks"]}
        for f in audio_dir.glob("*.mp3"):
            if f.name not in expected:
                f.unlink()
                print(f"    REMOVED orphan: {f.name}")

    print(f"  {source_path.name}: {len(blocks)} blocks ({generated} generated, {skipped} skipped)")


def main():
    parser = argparse.ArgumentParser(description="Generate narration audio")
    parser.add_argument("files", nargs="*", help="Specific source files to process")
    parser.add_argument("--voice", default=DEFAULT_VOICE, choices=VOICES.keys())
    parser.add_argument("--force", action="store_true", help="Regenerate all audio")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--regenerate-changed", action="store_true", help="Regenerate changed blocks")
    parser.add_argument("--all", action="store_true", help="Include extras and references")
    args = parser.parse_args()

    if not API_KEY and not args.dry_run:
        print("ERROR: ELEVENLABS_API_KEY not set. Add it to .env or environment.")
        sys.exit(1)

    if args.files:
        sources = [Path(f) for f in args.files]
    else:
        sources = sorted(SOURCE_DIR.glob("module-*.md"))

    print(f"Processing {len(sources)} files with voice '{args.voice}'...")
    for source in sources:
        process_module(source, args.voice, args.force, args.dry_run, args.regenerate_changed)

    print("\nDone!")


if __name__ == "__main__":
    main()
