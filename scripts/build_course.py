#!/usr/bin/env python3
"""
Build script for 1Z0-811 Java Foundations Course.
Converts source markdown files into paginated, self-contained HTML pages.

Usage:
    uv run --with markdown --with pygments python scripts/build_course.py
    uv run --with markdown --with pygments python scripts/build_course.py --module module-01-what-is-java
    uv run --with markdown --with pygments python scripts/build_course.py --no-embed
"""

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path
from string import Template

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension


# ── Project paths ──────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "source"
HTML_DIR = ROOT / "html"
IMAGES_DIR = ROOT / "images"
AUDIO_DIR = ROOT / "audio"
QUIZ_DIR = ROOT / "Quiz"
TEMPLATE_PATH = ROOT / "scripts" / "module_template.html"

COURSE_TITLE = "1Z0-811 Java Foundations"


# ── Module registry ────────────────────────────────────────────────────────────

MODULES = [
    {"file": "module-01-what-is-java.md", "short": "Day 1", "title": "What Is Java?", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-02-java-basics-part-1.md", "short": "Day 2", "title": "Java Basics Part 1", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-03-java-basics-part-2.md", "short": "Day 3", "title": "Java Basics Part 2", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-04-basic-java-elements-part-1.md", "short": "Day 4", "title": "Basic Java Elements Part 1", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-05-basic-java-elements-part-2.md", "short": "Day 5", "title": "Basic Java Elements Part 2", "tier": "Start Here", "tier_css": "tier-start-here"},
    {"file": "module-06-java-data-types-part-1.md", "short": "Day 6", "title": "Java Data Types Part 1", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-07-java-data-types-part-2.md", "short": "Day 7", "title": "Java Data Types Part 2", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-08-java-data-types-part-3.md", "short": "Day 8", "title": "Java Data Types Part 3", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-09-java-operators-part-1.md", "short": "Day 9", "title": "Java Operators Part 1", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-10-java-operators-part-2.md", "short": "Day 10", "title": "Java Operators Part 2", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-11-string-class-part-1.md", "short": "Day 11", "title": "String Class Part 1", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-12-string-class-part-2.md", "short": "Day 12", "title": "String Class Part 2", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-13-random-and-math-classes.md", "short": "Day 13", "title": "Random and Math Classes", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-14-decision-statements-part-1.md", "short": "Day 14", "title": "Decision Statements Part 1", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-15-decision-statements-part-2.md", "short": "Day 15", "title": "Decision Statements Part 2", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-16-decision-statements-part-3.md", "short": "Day 16", "title": "Decision Statements Part 3", "tier": "Useful Soon", "tier_css": "tier-useful-soon"},
    {"file": "module-17-looping-statements-part-1.md", "short": "Day 17", "title": "Looping Statements Part 1", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-18-looping-statements-part-2.md", "short": "Day 18", "title": "Looping Statements Part 2", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-19-looping-statements-part-3.md", "short": "Day 19", "title": "Looping Statements Part 3", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-20-debugging-and-exceptions-part-1.md", "short": "Day 20", "title": "Debugging and Exceptions Part 1", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-21-debugging-and-exceptions-part-2.md", "short": "Day 21", "title": "Debugging and Exceptions Part 2", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-22-arrays-and-arraylists-part-1.md", "short": "Day 22", "title": "Arrays and ArrayLists Part 1", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-23-arrays-and-arraylists-part-2.md", "short": "Day 23", "title": "Arrays and ArrayLists Part 2", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-24-arrays-and-arraylists-part-3.md", "short": "Day 24", "title": "Arrays and ArrayLists Part 3", "tier": "When You're Ready", "tier_css": "tier-when-ready"},
    {"file": "module-25-classes-and-constructors-part-1.md", "short": "Day 25", "title": "Classes and Constructors Part 1", "tier": "Advanced", "tier_css": "tier-advanced"},
    {"file": "module-26-classes-and-constructors-part-2.md", "short": "Day 26", "title": "Classes and Constructors Part 2", "tier": "Advanced", "tier_css": "tier-advanced"},
    {"file": "module-27-classes-and-constructors-part-3.md", "short": "Day 27", "title": "Classes and Constructors Part 3", "tier": "Advanced", "tier_css": "tier-advanced"},
    {"file": "module-28-java-methods-part-1.md", "short": "Day 28", "title": "Java Methods Part 1", "tier": "Advanced", "tier_css": "tier-advanced"},
    {"file": "module-29-java-methods-part-2.md", "short": "Day 29", "title": "Java Methods Part 2", "tier": "Advanced", "tier_css": "tier-advanced"},
    {"file": "module-30-java-methods-part-3.md", "short": "Day 30", "title": "Java Methods Part 3 — Final Capstone", "tier": "Advanced", "tier_css": "tier-advanced"},
]

EXTRAS = []
REFERENCES = []


# ── Markdown processor ─────────────────────────────────────────────────────────

def get_md():
    return markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(css_class="highlight", linenums=False, guess_lang=False),
            TableExtension(),
            TocExtension(toc_depth="2-3"),
            "md_in_html",
        ]
    )


# ── Special block processors ──────────────────────────────────────────────────

# Emoji codepoints used by special markers
_MARKER_EMOJIS = [
    "\U0001F3F7\uFE0F",  # 🏷️ tier
    "\U0001F3AF",         # 🎯 teaching intent
    "\U0001F399\uFE0F",  # 🎙️ narration
    "\U0001F504",         # 🔄 cycle anchor
    "\U0001F4A1",         # 💡 remember
]
_MARKER_PATTERN = "|".join(re.escape(e) for e in _MARKER_EMOJIS)


def split_merged_blockquotes(html: str) -> str:
    """Split blockquotes that contain multiple emoji-marker paragraphs.

    Python-Markdown merges adjacent blockquotes (separated by blank lines in
    source) into a single <blockquote> with multiple <p> children.  The
    downstream regex processors expect each marker to live in its own
    <blockquote>.  This function splits them apart.
    """
    def _split(m):
        inner = m.group(1)
        # Split on </p>\n<p> boundaries
        paras = re.split(r'(</p>\s*<p>)', inner)

        # Reassemble into individual paragraphs
        rebuilt = []
        current = ""
        for part in paras:
            if re.match(r'</p>\s*<p>', part):
                current += "</p>"
                rebuilt.append(current)
                current = "<p>"
            else:
                current += part
        if current:
            rebuilt.append(current)

        # Check if any paragraph starts with a marker emoji
        has_markers = any(re.search(_MARKER_PATTERN, p) for p in rebuilt)
        if not has_markers or len(rebuilt) <= 1:
            return m.group(0)  # Nothing to split

        # Wrap each paragraph in its own blockquote
        result = ""
        for p in rebuilt:
            p = p.strip()
            if p:
                result += f"<blockquote>\n{p}\n</blockquote>\n"
        return result

    return re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        _split, html, flags=re.DOTALL
    )


def process_tier_badges(html: str) -> str:
    """Convert 🏷️ blockquotes into tier badges."""
    def replace_tier(m):
        text = m.group(1).strip()
        css_map = {
            "Start Here": "tier-start-here",
            "Useful Soon": "tier-useful-soon",
            "When You're Ready": "tier-when-ready",
            "Advanced": "tier-advanced",
        }
        css_class = css_map.get(text, "tier-start-here")
        return f'<span class="tier-badge {css_class}">{text}</span>'

    return re.sub(
        r'<blockquote>\s*<p>\U0001F3F7\uFE0F\s*(.*?)</p>\s*</blockquote>',
        replace_tier, html, flags=re.DOTALL
    )


def process_cycle_anchors(html: str) -> str:
    """Convert 🔄 blockquotes into cycle anchor blocks."""
    return re.sub(
        r'<blockquote>\s*<p>\U0001F504\s*(.*?)</p>\s*</blockquote>',
        r'<div class="cycle-anchor"><p>\1</p></div>',
        html, flags=re.DOTALL
    )


def process_remember_callouts(html: str) -> str:
    """Convert 💡 blockquotes into remember-one-thing callouts."""
    return re.sub(
        r'<blockquote>\s*<p>\U0001F4A1\s*(.*?)</p>\s*</blockquote>',
        r'<div class="remember-callout"><p>\1</p></div>',
        html, flags=re.DOTALL
    )


def process_teaching_intent(html: str) -> str:
    """Convert 🎯 blockquotes into teaching intent blocks."""
    return re.sub(
        r'<blockquote>\s*<p>\U0001F3AF\s*(.*?)</p>\s*</blockquote>',
        r'<div class="teaching-intent"><p>\1</p></div>',
        html, flags=re.DOTALL
    )


def process_narration_blocks(html: str, module_slug: str, embed: bool = True) -> str:
    """Convert 🎙️ blockquotes into narration audio players."""
    audio_dir = AUDIO_DIR / module_slug
    manifest_path = audio_dir / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        with open(manifest_path) as f:
            manifest = json.load(f)

    counter = [0]

    def replace_narration(m):
        counter[0] += 1
        text = m.group(1).strip()
        # Clean HTML tags for display
        display_text = text

        # Look for matching audio file
        audio_html = ""
        audio_files = sorted(audio_dir.glob("*.mp3")) if audio_dir.exists() else []
        if counter[0] <= len(audio_files):
            audio_file = audio_files[counter[0] - 1]
            if embed:
                with open(audio_file, "rb") as af:
                    b64 = base64.b64encode(af.read()).decode()
                audio_html = f'<audio class="narration-audio" preload="none"><source src="data:audio/mpeg;base64,{b64}" type="audio/mpeg"></audio>'
            else:
                rel = os.path.relpath(audio_file, ROOT)
                audio_html = f'<audio class="narration-audio" preload="none"><source src="../{rel}" type="audio/mpeg"></audio>'

        return f'''<div class="narration-block">
            <button class="narration-play-btn" onclick="toggleNarration(this)" aria-label="Play narration">&#9654;</button>
            <div class="narration-content">
                <p class="narration-text">{display_text}</p>
                {audio_html}
            </div>
        </div>'''

    return re.sub(
        r'<blockquote>\s*<p>\U0001F399\uFE0F\s*(.*?)</p>\s*</blockquote>',
        replace_narration, html, flags=re.DOTALL
    )


# ── Image embedding ───────────────────────────────────────────────────────────

def embed_images(html: str, embed: bool = True) -> str:
    """Replace image src paths with base64 data URIs."""
    if not embed:
        return html

    def replace_img(m):
        full_tag = m.group(0)
        src = m.group(1)
        # Resolve relative paths
        if src.startswith("../images/"):
            img_path = IMAGES_DIR / src.replace("../images/", "")
        elif src.startswith("images/"):
            img_path = IMAGES_DIR / src.replace("images/", "")
        else:
            img_path = ROOT / src

        if img_path.exists():
            ext = img_path.suffix.lower()
            mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                    "gif": "image/gif", "svg": "image/svg+xml", "webp": "image/webp"
                    }.get(ext.lstrip("."), "image/png")
            with open(img_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return full_tag.replace(src, f"data:{mime};base64,{b64}")
        return full_tag

    return re.sub(r'<img[^>]+src="([^"]+)"', replace_img, html)


# ── Pagination ─────────────────────────────────────────────────────────────────

def paginate(html: str) -> tuple[str, int]:
    """Split HTML at H2 boundaries into navigable pages."""
    parts = re.split(r'(<h2[^>]*>)', html)

    if len(parts) <= 1:
        return f'<div class="page" data-page="1">{html}</div>', 1

    pages = []
    current = parts[0]  # Content before first H2

    if current.strip():
        pages.append(current)

    i = 1
    while i < len(parts):
        if parts[i].startswith("<h2"):
            if i + 1 < len(parts):
                content = parts[i] + parts[i + 1]
            else:
                content = parts[i]
            pages.append(content)
            i += 2
        else:
            if pages:
                pages[-1] += parts[i]
            else:
                pages.append(parts[i])
            i += 1

    result = ""
    for idx, page in enumerate(pages, 1):
        result += f'<div class="page" data-page="{idx}">{page}</div>\n'

    return result, len(pages)


# ── Quiz generation ────────────────────────────────────────────────────────────

def generate_quiz_html(module_num: int, module_slug: str) -> str:
    """Generate interactive quiz HTML from the quiz JSON file for a given day."""
    quiz_path = QUIZ_DIR / f"Day_{module_num:02d}_Quiz_File" / f"day_{module_num:02d}_quiz.json"
    if not quiz_path.exists():
        return ""

    with open(quiz_path) as f:
        quiz = json.load(f)

    questions = quiz["questions"]
    passing = quiz.get("passing_score", 20)
    total = quiz.get("total_questions", len(questions))
    title = quiz.get("quiz_title", f"Day {module_num} Quiz")

    # Build quiz data JSON for the JS
    quiz_data = json.dumps({
        "moduleSlug": module_slug,
        "passingScore": passing,
        "totalQuestions": total,
    })

    # Build question HTML
    questions_html = ""
    for q in questions:
        qid = q["id"]
        options_html = ""
        for opt in q["options"]:
            safe_opt = opt.replace('"', '&quot;').replace("'", "&#39;")
            display_opt = opt.replace("<", "&lt;").replace(">", "&gt;")
            options_html += f'''<li>
                <label><input type="radio" name="q{qid}" value="{safe_opt}"> {display_opt}</label>
            </li>\n'''

        safe_answer = q["answer"].replace('"', '&quot;').replace("'", "&#39;")
        question_text = q["question"].replace("<", "&lt;").replace(">", "&gt;")

        questions_html += f'''<div class="quiz-question" data-answer="{safe_answer}">
            <div class="quiz-question-number">Question {qid}</div>
            <div class="quiz-question-text">{question_text}</div>
            <ul class="quiz-options">{options_html}</ul>
            <div class="quiz-feedback"></div>
        </div>\n'''

    return f'''<h2 id="quiz">Knowledge Check: {title}</h2>
<div class="quiz-container">
    <div class="quiz-header">
        <p class="quiz-meta">{total} questions &middot; {passing} correct to pass</p>
    </div>
    <script type="application/json" id="quizData">{quiz_data}</script>
    <div id="quizForm">
        {questions_html}
        <div class="quiz-submit-area">
            <button class="quiz-submit-btn" id="quizSubmitBtn">Submit Quiz</button>
        </div>
        <div class="quiz-results" id="quizResults">
            <div class="quiz-score" id="quizScoreValue"></div>
            <div class="quiz-label" id="quizResultLabel"></div>
            <div class="quiz-detail" id="quizResultDetail"></div>
            <button class="quiz-retry-btn" id="quizRetryBtn">Try Again</button>
        </div>
    </div>
</div>'''


# ── TOC generation ─────────────────────────────────────────────────────────────

def generate_toc(html: str) -> str:
    """Generate sidebar TOC from H2 and H3 headings, grouped by page.

    Each H2 starts a new page group. H3s are nested under their parent H2.
    Page groups get a visual container so users can see what belongs together.
    """
    # Try with id attributes first
    headings = re.findall(r'<h([23])[^>]*id="([^"]*)"[^>]*>(.*?)</h\1>', html)
    has_ids = True
    if not headings:
        has_ids = False
        raw = re.findall(r'<h([23])[^>]*>(.*?)</h\1>', html)
        headings = []
        for level, text in raw:
            clean = re.sub(r'<[^>]+>', '', text)
            slug = re.sub(r'[^a-z0-9]+', '-', clean.lower()).strip('-')
            headings.append((level, slug, clean))

    if not headings:
        return '<ul class="toc-list"></ul>'

    # Normalize to (level, id, clean_text)
    if has_ids:
        headings = [(lv, id_attr, re.sub(r'<[^>]+>', '', txt)) for lv, id_attr, txt in headings]

    # Group by page: each H2 starts a new group, H3s belong to previous H2
    page_num = 0
    groups = []  # list of (page_num, [(level, id, text), ...])
    current_group = []

    for lv, id_attr, text in headings:
        if lv == "2":
            # Close previous group
            if current_group:
                groups.append((page_num, current_group))
            page_num += 1
            current_group = [("2", id_attr, text)]
        else:
            current_group.append(("3", id_attr, text))

    if current_group:
        groups.append((page_num, current_group))

    # Build HTML with page groups
    result = '<ul class="toc-list">'
    for pg, items in groups:
        result += f'<li class="toc-page-group" data-toc-page="{pg}">'
        h2 = items[0]
        result += f'<a href="#{h2[1]}" class="toc-h2-link">{h2[2]}</a>'
        if len(items) > 1:
            result += '<ul class="toc-subsections">'
            for item in items[1:]:
                result += f'<li><a href="#{item[1]}" class="toc-h3-link">{item[2]}</a></li>'
            result += '</ul>'
        result += '</li>'
    result += '</ul>'

    return result


# ── Module navigation ─────────────────────────────────────────────────────────

def build_module_nav(all_modules: list, current_idx: int) -> str:
    """Build module-to-module navigation dropdown as a list of links."""
    items = []
    for i, mod in enumerate(all_modules):
        slug = mod["file"].replace(".md", "")
        active = ' class="active"' if i == current_idx else ""
        items.append(f'<a href="{slug}.html"{active}>{mod["short"]}: {mod["title"]}</a>')

    return "\n".join(items)


# ── Build a single module ─────────────────────────────────────────────────────

def build_module(mod: dict, idx: int, all_modules: list, template: str, embed: bool = True):
    """Build a single module HTML file."""
    source_path = SOURCE_DIR / mod["file"]
    if not source_path.exists():
        print(f"  SKIP {mod['file']} (not found)")
        return

    with open(source_path) as f:
        md_text = f.read()

    # Convert markdown to HTML
    md_processor = get_md()
    html = md_processor.convert(md_text)

    # Module slug for audio lookup
    module_slug = mod["file"].replace(".md", "")

    # Split merged blockquotes so each emoji marker gets its own <blockquote>
    html = split_merged_blockquotes(html)

    # Process special blocks (order matters)
    html = process_tier_badges(html)
    html = process_cycle_anchors(html)
    html = process_remember_callouts(html)
    html = process_teaching_intent(html)
    html = process_narration_blocks(html, module_slug, embed)

    # Embed images
    html = embed_images(html, embed)

    # Append quiz as the last section (before pagination splits it into a page)
    module_num_match = re.search(r'module-(\d+)', module_slug)
    if module_num_match:
        module_num = int(module_num_match.group(1))
        quiz_html = generate_quiz_html(module_num, module_slug)
        if quiz_html:
            html += quiz_html

    # Generate TOC before pagination
    toc = generate_toc(html)

    # Paginate at H2 boundaries
    html, total_pages = paginate(html)

    # Navigation links
    prev_link = ""
    next_link = ""
    if idx > 0:
        prev_slug = all_modules[idx - 1]["file"].replace(".md", "")
        prev_title = all_modules[idx - 1]["short"]
        prev_link = f'<a href="{prev_slug}.html" class="nav-btn prev-btn">&larr; {prev_title}</a>'
    if idx < len(all_modules) - 1:
        next_slug = all_modules[idx + 1]["file"].replace(".md", "")
        next_title = all_modules[idx + 1]["short"]
        next_link = f'<a href="{next_slug}.html" class="nav-btn next-btn">{next_title} &rarr;</a>'

    # Module nav dropdown
    module_nav = build_module_nav(all_modules, idx)

    # Fill template
    title = f"{mod['short']}: {mod['title']}"
    output = Template(template).safe_substitute(
        title=title,
        toc=toc,
        content=html,
        prev_link=prev_link,
        next_link=next_link,
        module_nav=module_nav,
        total_pages=str(total_pages),
    )

    # Write output
    out_path = HTML_DIR / f"{module_slug}.html"
    with open(out_path, "w") as f:
        f.write(output)

    print(f"  BUILT {out_path.name} ({total_pages} pages)")


# ── Index page ─────────────────────────────────────────────────────────────────

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>1Z0-811 Java Foundations</title>
<style>
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
  --card-bg: #ffffff;
  --card-border: #e0e0e0;
  --accent: #e76f51;
  --accent-light: #f4a261;
  --header-bg: #1a1a2e;
  --section-bg: #f8f8f5;
}
[data-theme="dark"] {
  --bg: #1a1a2e;
  --text: #e0e0e0;
  --card-bg: #16213e;
  --card-border: #333;
  --section-bg: #0f0f23;
  --header-bg: #0f0f23;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}
.hero {
  background: var(--header-bg);
  color: #fff;
  padding: 60px 20px;
  text-align: center;
}
.hero h1 { font-size: 2.5em; margin-bottom: 10px; }
.hero p { font-size: 1.2em; opacity: 0.9; max-width: 600px; margin: 0 auto; }
.hero .subtitle { color: var(--accent-light); font-weight: 600; }
.theme-toggle {
  position: absolute;
  top: 20px;
  right: 20px;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  color: #fff;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}
.container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; }
.tier-section { margin-bottom: 50px; }
.tier-section h2 {
  font-size: 1.5em;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 3px solid var(--accent);
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
.card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 12px;
  padding: 24px;
  transition: transform 0.2s, box-shadow 0.2s;
  text-decoration: none;
  color: var(--text);
  display: block;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}
.card .day-label {
  font-size: 0.85em;
  color: var(--accent);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.card h3 { margin: 8px 0 12px; font-size: 1.15em; }
.card .tier-badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.75em;
  font-weight: 600;
}
.tier-start-here { background: #d4edda; color: #155724; }
.tier-useful-soon { background: #cce5ff; color: #004085; }
.tier-when-ready { background: #fff3cd; color: #856404; }
.tier-advanced { background: #f8d7da; color: #721c24; }
[data-theme="dark"] .tier-start-here { background: #1a3a2a; color: #7dcea0; }
[data-theme="dark"] .tier-useful-soon { background: #1a2a4a; color: #7db8f0; }
[data-theme="dark"] .tier-when-ready { background: #3a3a1a; color: #d4a847; }
[data-theme="dark"] .tier-advanced { background: #3a1a1a; color: #e07070; }
.stats {
  display: flex;
  gap: 30px;
  justify-content: center;
  margin-top: 30px;
  flex-wrap: wrap;
}
.stat { text-align: center; }
.stat .num { font-size: 2em; font-weight: 700; color: var(--accent); }
.stat .label { font-size: 0.9em; opacity: 0.7; }
.card .quiz-badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.75em;
  font-weight: 600;
  margin-left: 6px;
}
.quiz-badge.passed { background: #d4edda; color: #155724; }
.quiz-badge.failed { background: #f8d7da; color: #721c24; }
.quiz-badge.not-taken { background: #e2e3e5; color: #6c757d; }
[data-theme="dark"] .quiz-badge.passed { background: #1a3a2a; color: #7dcea0; }
[data-theme="dark"] .quiz-badge.failed { background: #3a1a1a; color: #e07070; }
[data-theme="dark"] .quiz-badge.not-taken { background: #2a2a2a; color: #888; }
.card .quiz-score-line {
  font-size: 0.8em;
  opacity: 0.6;
  margin-top: 6px;
}
footer {
  text-align: center;
  padding: 40px 20px;
  font-size: 0.85em;
  opacity: 0.6;
}
@media (max-width: 600px) {
  .hero h1 { font-size: 1.8em; }
  .card-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>
<div class="hero" style="position:relative;">
  <button class="theme-toggle" onclick="toggleTheme()">Toggle Theme</button>
  <h1>1Z0-811 Java Foundations</h1>
  <p class="subtitle">30-Day Exam Preparation Course</p>
  <p>A structured, hands-on curriculum covering every topic on the Oracle 1Z0-811 Java Foundations certification exam.</p>
  <div class="stats">
    <div class="stat"><div class="num">30</div><div class="label">Days</div></div>
    <div class="stat"><div class="num">60</div><div class="label">Assignments</div></div>
    <div class="stat"><div class="num">4</div><div class="label">Tiers</div></div>
  </div>
</div>
<div class="container">
  ${module_cards}
</div>
<footer>
  1Z0-811 Java Foundations &mdash; Built with the Course Builder Pipeline
</footer>
<script>
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  localStorage.setItem('java-foundations-theme', next);
}
(function() {
  const saved = localStorage.getItem('java-foundations-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
})();
/* Populate quiz badges from localStorage */
(function() {
  try {
    var results = JSON.parse(localStorage.getItem('java-foundations-quiz-results') || '{}');
    var cards = document.querySelectorAll('.card[data-module-slug]');
    for (var i = 0; i < cards.length; i++) {
      var slug = cards[i].getAttribute('data-module-slug');
      var badge = cards[i].querySelector('[data-quiz-badge]');
      var scoreLine = cards[i].querySelector('[data-quiz-score]');
      if (!badge) continue;
      var r = results[slug];
      if (r) {
        if (r.passed) {
          badge.className = 'quiz-badge passed';
          badge.textContent = 'Passed';
        } else {
          badge.className = 'quiz-badge failed';
          badge.textContent = 'Retry';
        }
        if (scoreLine) {
          scoreLine.textContent = r.score + '/' + r.total + ' on ' + r.date;
        }
      }
    }
  } catch(e) {}
})();
</script>
</body>
</html>"""


def build_index(all_modules: list):
    """Generate the landing page with module cards organized by tier."""
    tier_order = ["Start Here", "Useful Soon", "When You're Ready", "Advanced"]
    tier_descriptions = {
        "Start Here": "Begin your Java journey here. These modules cover the fundamentals you need before anything else.",
        "Useful Soon": "Core Java concepts you'll use constantly. Data types, operators, strings, and decision-making.",
        "When You're Ready": "Intermediate topics that build on the basics. Loops, error handling, and data structures.",
        "Advanced": "Object-oriented programming in depth. Classes, constructors, methods, and a final capstone project.",
    }

    sections_html = ""
    for tier in tier_order:
        mods = [m for m in all_modules if m.get("tier") == tier]
        if not mods:
            continue
        cards = ""
        for mod in mods:
            slug = mod["file"].replace(".md", "")
            cards += f'''<a href="html/{slug}.html" class="card" data-module-slug="{slug}">
                <div class="day-label">{mod["short"]}</div>
                <h3>{mod["title"]}</h3>
                <div>
                    <span class="tier-badge {mod.get('tier_css', '')}">{tier}</span>
                    <span class="quiz-badge not-taken" data-quiz-badge>Quiz</span>
                </div>
                <div class="quiz-score-line" data-quiz-score></div>
            </a>\n'''
        sections_html += f'''<div class="tier-section">
            <h2>{tier}</h2>
            <p style="margin-bottom:16px;opacity:0.8;">{tier_descriptions.get(tier, "")}</p>
            <div class="card-grid">{cards}</div>
        </div>\n'''

    output = Template(INDEX_TEMPLATE).safe_substitute(module_cards=sections_html)
    index_path = ROOT / "index.html"
    with open(index_path, "w") as f:
        f.write(output)
    print(f"  BUILT index.html")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build 1Z0-811 Java Foundations course")
    parser.add_argument("--module", help="Build only this module (slug without .md)")
    parser.add_argument("--no-embed", action="store_true", help="Link images instead of embedding")
    args = parser.parse_args()

    embed = not args.no_embed

    # Load template
    if not TEMPLATE_PATH.exists():
        print(f"ERROR: Template not found at {TEMPLATE_PATH}")
        sys.exit(1)

    with open(TEMPLATE_PATH) as f:
        template = f.read()

    # Create output directory
    HTML_DIR.mkdir(exist_ok=True)

    all_modules = MODULES + EXTRAS + REFERENCES

    if args.module:
        # Build single module
        target = args.module if args.module.endswith(".md") else args.module + ".md"
        for i, mod in enumerate(all_modules):
            if mod["file"] == target or mod["file"].replace(".md", "") == args.module:
                print(f"Building {mod['file']}...")
                build_module(mod, i, all_modules, template, embed)
                break
        else:
            print(f"ERROR: Module '{args.module}' not found in registry")
            sys.exit(1)
    else:
        # Build all modules
        print(f"Building {len(all_modules)} modules...")
        for i, mod in enumerate(all_modules):
            build_module(mod, i, all_modules, template, embed)

    # Build index page
    print("Building index page...")
    build_index(all_modules)

    print(f"\nDone! Open index.html or html/ directory to preview.")


if __name__ == "__main__":
    main()
