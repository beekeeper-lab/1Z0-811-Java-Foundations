#!/usr/bin/env python3
"""Launch the Day 27 quiz."""

import subprocess
import sys
from pathlib import Path

quiz_app = Path(__file__).resolve().parent.parent.parent / "quiz_app.py"
subprocess.run([sys.executable, str(quiz_app), "1Z0-811_Java_Foundations", "27"])
