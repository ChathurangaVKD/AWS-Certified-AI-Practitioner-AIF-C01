#!/usr/bin/env python3
"""Render docs/EXAM-TRAPS-EXPLAINED.md into exam-simulator/trap-guide.html.

A small purpose-built Markdown subset renderer (headings, bullets, tables,
blockquotes, numbered lists, bold, code, links). No dependencies.
Run from anywhere: python3 exam-simulator/build_guide.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "EXAM-TRAPS-EXPLAINED.md"
OUT = Path(__file__).resolve().parent / "trap-guide.html"
REPO = "https://github.com/ChathurangaVKD/AWS-Certified-AI-Practitioner-AIF-C01/blob/main/docs/"
PAGES = "https://chathurangavkd.github.io/AWS-Certified-AI-Practitioner-AIF-C01/"

FIELD_CLASS = {
    "theory": "theory", "in more detail": "detail", "the trap": "trap",
    "example": "example", "example 1": "example", "example 2": "example",
    "spot it": "spot",
}


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def fix_href(u):
    if u.startswith(PAGES):
        return u[len(PAGES):]
    if u.endswith(".md") and "/" not in u and not u.startswith("http"):
        return REPO + u
    return u


def inline(s):
    s = html.escape(s, quote=False)
    codes = []

    def keep(m):
        codes.append("<code>" + m.group(1) + "</code>")
        return "\x00%d\x00" % (len(codes) - 1)

    s = re.sub(r"`([^`]+)`", keep, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: '<a href="%s">%s</a>' % (html.escape(fix_href(html.unescape(m.group(2)))), m.group(1)),
        s,
    )
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)


def parse_list(lines, i, indent):
    """Return (items, next_i). items = [(text, children)]."""
    items = []
    pat = re.compile(r"^(\s*)(?:[-*]|\d+\.)\s+(.*)$")
    while i < len(lines):
        m = pat.match(lines[i])
        if not m or len(m.group(1)) < indent:
            break
        if len(m.group(1)) > indent:
            break
        text, i = m.group(2), i + 1
        children = []
        # continuation lines
        while i < len(lines) and lines[i].strip() and not pat.match(lines[i]) and lines[i].startswith(" " * (indent + 2)):
            text += " " + lines[i].strip()
            i += 1
        if i < len(lines):
            m2 = pat.match(lines[i])
            if m2 and len(m2.group(1)) > indent:
                children, i = parse_list(lines, i, len(m2.group(1)))
        items.append((text, children))
    return items, i


def render_list(items, ordered=False, top=False):
    tag = "ol" if ordered else "ul"
    out = ["<%s>" % tag]
    for text, children in items:
        m = re.match(r"^\*\*([^*:]+):\*\*\s*(.*)$", text) if top else None
        kids = render_list(children) if children else ""
        if m and m.group(1).strip().lower() in FIELD_CLASS:
            label = m.group(1).strip()
            cls = FIELD_CLASS[label.lower()]
            out.append('<li class="field %s"><span class="lab">%s</span><div class="body">%s%s</div></li>' % (cls, html.escape(label), inline(m.group(2)), kids))
        else:
            out.append("<li>%s%s</li>" % (inline(text), kids))
    out.append("</%s>" % tag)
    return "".join(out)


def render_table(rows):
    cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    h = "<table><thead><tr>%s</tr></thead><tbody>" % "".join("<th>%s</th>" % inline(c) for c in head)
    for r in body:
        h += "<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
    return '<div class="tw">' + h + "</tbody></table></div>"


def render_blocks(lines, field_lists=False):
    out, i, para = [], 0, []

    def flush():
        if para:
            text = " ".join(para)
            if text.startswith("**Answers:**"):
                out.append("<details class=\"ans\"><summary>Show answers</summary><p>%s</p></details>" % inline(text))
            else:
                out.append("<p>%s</p>" % inline(text))
            para.clear()

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            flush(); i += 1; continue
        if line.startswith("|"):
            flush()
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            out.append(render_table(lines[i:j])); i = j; continue
        if line.startswith(">"):
            flush()
            j, q = i, []
            while j < len(lines) and lines[j].startswith(">"):
                q.append(lines[j].lstrip("> ").strip()); j += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(q))); i = j; continue
        if line.strip() == "---":
            flush(); i += 1; continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+", line)
        if m:
            flush()
            items, j = parse_list(lines, i, len(m.group(1)))
            out.append(render_list(items, ordered=m.group(2)[0].isdigit(), top=field_lists)); i = j; continue
        para.append(line.strip()); i += 1
    flush()
    return "\n".join(out)


def build():
    text = SRC.read_text(encoding="utf-8").splitlines()
    sections, cur, topic = [], None, None
    intro = []
    for line in text:
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "lines": [], "topics": []}
            sections.append(cur); topic = None; continue
        if cur is None:
            intro.append(line); continue
        if line.startswith("### "):
            topic = {"title": line[4:].strip(), "lines": []}
            cur["topics"].append(topic); continue
        (topic["lines"] if topic else cur["lines"]).append(line)

    nav, body, total = [], [], 0
    for s in sections:
        sid = "s-" + slug(s["title"])
        nav.append('<a class="nsec" href="#%s">%s</a>' % (sid, html.escape(s["title"])))
        parts = ['<section class="sec" id="%s"><h2>%s</h2>' % (sid, inline(s["title"]))]
        if s["lines"]:
            parts.append('<div class="intro">%s</div>' % render_blocks(s["lines"]))
        for t in s["topics"]:
            tid = "t-" + slug(t["title"].split(" ")[0] + "-" + " ".join(t["title"].split(" ")[1:])[:40])
            total += 1
            nav.append('<a class="ntop" href="#%s">%s</a>' % (tid, html.escape(t["title"])))
            parts.append(
                '<article class="topic" id="%s" data-id="%s"><header><h3>%s</h3>'
                '<label class="read"><input type="checkbox"> Read</label></header>%s</article>'
                % (tid, tid, inline(t["title"]), render_blocks(t["lines"], field_lists=True))
            )
        parts.append("</section>")
        body.append("\n".join(parts))

    intro_html = render_blocks([l for l in intro if not l.startswith("**Jump to:**")])
    return TEMPLATE.replace("{{NAV}}", "\n".join(nav)).replace("{{INTRO}}", intro_html).replace("{{BODY}}", "\n".join(body)).replace("{{TOTAL}}", str(total)), total


TEMPLATE = open(Path(__file__).resolve().parent / "trap-guide.template.html", encoding="utf-8").read()

if __name__ == "__main__":
    out, total = build()
    OUT.write_text(out, encoding="utf-8")
    print("wrote %s: %d topics" % (OUT.name, total))
