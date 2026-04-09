#!/usr/bin/env python3
"""
Package the 1Z0-811 Java Foundations course for distribution.

Usage:
    uv run --with markdown --with pygments python scripts/deploy.py
    uv run --with markdown --with pygments python scripts/deploy.py --version 1.0
    uv run --with markdown --with pygments python scripts/deploy.py --skip-build
    uv run --with markdown --with pygments python scripts/deploy.py --out ~/Desktop
"""

import argparse
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT / "html"
DIST_DIR = ROOT / "dist"

COURSE_NAME = "1Z0-811-Java-Foundations"


def get_version(explicit: str | None = None) -> str:
    if explicit:
        return explicit
    date = datetime.datetime.now().strftime("%Y%m%d")
    try:
        git_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode().strip()
        return f"{date}-{git_hash}"
    except Exception:
        return date


def main():
    parser = argparse.ArgumentParser(description="Package course for distribution")
    parser.add_argument("--version", help="Explicit version string")
    parser.add_argument("--skip-build", action="store_true", help="Skip rebuilding HTML")
    parser.add_argument("--out", help="Output directory (default: dist/)")
    args = parser.parse_args()

    version = get_version(args.version)
    out_dir = Path(args.out) if args.out else DIST_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build first unless skipped
    if not args.skip_build:
        print("Building course...")
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_course.py")],
            cwd=ROOT
        )
        if result.returncode != 0:
            print("Build failed!")
            sys.exit(1)

    # Check HTML exists
    html_files = list(HTML_DIR.glob("*.html"))
    index_file = ROOT / "index.html"
    if not html_files:
        print("ERROR: No HTML files found. Run the build first.")
        sys.exit(1)

    # Create staging directory
    folder_name = f"{COURSE_NAME}-v{version}"
    stage = out_dir / folder_name
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)

    # Copy files
    print(f"Packaging {len(html_files)} modules...")
    shutil.copytree(HTML_DIR, stage / "html")
    if index_file.exists():
        shutil.copy2(index_file, stage / "index.html")

    # Write VERSION file
    (stage / "VERSION").write_text(
        f"Course: {COURSE_NAME}\n"
        f"Version: {version}\n"
        f"Built: {datetime.datetime.now().isoformat()}\n"
        f"Modules: {len(html_files)}\n"
    )

    # Create zip
    zip_path = out_dir / folder_name
    shutil.make_archive(str(zip_path), "zip", out_dir, folder_name)

    # Cleanup staging
    shutil.rmtree(stage)

    final_zip = out_dir / f"{folder_name}.zip"
    size_mb = final_zip.stat().st_size / (1024 * 1024)
    print(f"\nPackaged: {final_zip}")
    print(f"Size: {size_mb:.1f} MB")
    print(f"Version: {version}")


if __name__ == "__main__":
    main()
