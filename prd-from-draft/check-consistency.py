#!/usr/bin/env python3
"""Check that DESIGN.md only references things the skeleton actually provides.

DESIGN.md is the single source of truth for the prototype spec, and
prototype-template.html is the single source of truth for what exists. When
they drift, the doc starts promising tokens, classes or icons that a prototype
cannot use. This script catches that drift so it does not need human review.

Checked:
  1. every var(--semi-*/--brand-*) cited in DESIGN.md is defined in the skeleton
  2. every .class cited in DESIGN.md appears in the skeleton
  3. every `i-*` icon cited in DESIGN.md exists as a symbol in the skeleton
  4. the icon-count claims in DESIGN.md and SKILL.md match the skeleton

Sections marked 预留 (reserved) are skipped on purpose: they document upstream
Semi Design variables the skeleton deliberately does not ship, and say so.

Usage: python3 check-consistency.py     (exit 0 = consistent)
"""

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
DESIGN = SKILL_DIR / "DESIGN.md"
SKILL = SKILL_DIR / "SKILL.md"
SKELETON = SKILL_DIR / "prototype-template.html"


def read(path):
    return path.read_text(encoding="utf-8")


def strip_reserved_sections(md):
    """Drop '### x.y Title（预留...）' sections — they document what is NOT shipped."""
    out, skipping = [], False
    for line in md.splitlines():
        if re.match(r"^#{2,4}\s", line):
            skipping = "预留" in line
        if not skipping:
            out.append(line)
    return "\n".join(out)


def defined_tokens(skeleton):
    return set(re.findall(r"^\s*(--[\w-]+)\s*:", skeleton, re.M))


def defined_classes(skeleton):
    return set(re.findall(r"\.([a-zA-Z][\w-]*)", skeleton))


def defined_symbols(skeleton):
    return set(re.findall(r'<symbol id="([\w-]+)"', skeleton))


def check(label, cited, defined, extra_ignore=()):
    missing = sorted(c for c in cited if c not in defined and c not in extra_ignore)
    if missing:
        print("  FAIL %s — 引用了骨架里没有的 %d 项:" % (label, len(missing)))
        for m in missing:
            print("       %s" % m)
    else:
        print("  ok   %s (%d 项)" % (label, len(cited)))
    return not missing


def main():
    design_raw = read(DESIGN)
    design = strip_reserved_sections(design_raw)
    skeleton = read(SKELETON)
    skill = read(SKILL)

    symbols = defined_symbols(skeleton)
    ok = True
    print("骨架: %d 个 token / %d 个 symbol" % (len(defined_tokens(skeleton)), len(symbols)))

    # 1. tokens
    cited = set(re.findall(r"var\((--[\w-]+)\)", design))
    ok &= check("DESIGN.md → token", cited, defined_tokens(skeleton))

    # 2. classes (ignore file names like x.md / x.py and pure-numeric fragments)
    cls_src = re.sub(r"`[\w./-]+\.(md|py|html|js)`", "", design)
    cited_cls = set(re.findall(r"\.([a-zA-Z][\w-]*)", cls_src))
    ok &= check("DESIGN.md → class", cited_cls, defined_classes(skeleton))

    # 3. icons
    cited_icons = set(re.findall(r"`(i-[\w-]+)`", design))
    missing = sorted(i for i in cited_icons if i not in symbols)
    if missing:
        print("  FAIL DESIGN.md → 图标 — 骨架里没有:", ", ".join(missing))
        ok = False
    else:
        print("  ok   DESIGN.md → 图标 (%d 项)" % len(cited_icons))

    # 4. icon-count claims must match reality everywhere
    # two shapes show up: "55 个内联 SVG symbol" and "图标清单（55 个"
    COUNT_PATTERNS = (
        r"图标清单（(\d+)\s*个",
        r"(\d+)\s*个(?:内联 SVG symbol|内联 SVG 图标|图标|全部取自|都是 Arco)",
    )
    for name, text in (("DESIGN.md", design_raw), ("SKILL.md", skill)):
        nums = set()
        for pat in COUNT_PATTERNS:
            nums |= set(re.findall(pat, text))
        bad = sorted(n for n in nums if int(n) != len(symbols))
        if bad:
            print("  FAIL %s — 写着「%s 个图标」，骨架实际 %d 个"
                  % (name, "/".join(bad), len(symbols)))
            ok = False
        else:
            print("  ok   %s → 图标计数" % name)

    print("\n%s" % ("一致 ✓" if ok else "存在不一致 ✗"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
