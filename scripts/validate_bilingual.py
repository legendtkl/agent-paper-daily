#!/usr/bin/env python3
"""Validate Chinese–English companion coverage and stable identifiers."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ARXIV_ID = re.compile(r"\b(\d{4}\.\d{5})\b")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    _, raw, _ = text.split("---", 2)
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def main() -> None:
    errors: list[str] = []

    static_pairs = (
        (ROOT / "README.md", ROOT / "README.en.md"),
        (ROOT / "daily/README.md", ROOT / "daily/README.en.md"),
        (ROOT / "papers/README.md", ROOT / "papers/README.en.md"),
        (ROOT / "monthly/README.md", ROOT / "monthly/README.en.md"),
        (ROOT / "docs/categories.md", ROOT / "docs/categories.en.md"),
        (ROOT / "docs/2026-trends.md", ROOT / "docs/2026-trends.en.md"),
    )
    for chinese, english in static_pairs:
        if not chinese.exists() or not english.exists():
            errors.append(f"missing bilingual pair: {chinese} / {english}")

    for chinese in sorted((ROOT / "daily").glob("????-??-??.md")):
        english = chinese.with_suffix(".en.md")
        if not english.exists():
            errors.append(f"{chinese.relative_to(ROOT)}: missing {english.name}")
            continue
        chinese_ids = set(ARXIV_ID.findall(chinese.read_text(encoding="utf-8")))
        english_ids = set(ARXIV_ID.findall(english.read_text(encoding="utf-8")))
        if chinese_ids != english_ids:
            errors.append(f"{english.relative_to(ROOT)}: arXiv ID set differs")

    paper_count = 0
    for chinese in sorted(ROOT.glob("papers/????/??/*.md")):
        chinese_meta = frontmatter(chinese.read_text(encoding="utf-8"))
        arxiv_id = chinese_meta.get("arxiv_id")
        if not arxiv_id:
            continue
        paper_count += 1
        english = chinese.with_suffix(".en.md")
        if not english.exists():
            errors.append(f"{chinese.relative_to(ROOT)}: missing {english.name}")
            continue
        english_meta = frontmatter(english.read_text(encoding="utf-8"))
        if english_meta.get("source_arxiv_id") != arxiv_id:
            errors.append(
                f"{english.relative_to(ROOT)}: source_arxiv_id does not match {arxiv_id}"
            )
        if english_meta.get("arxiv_id"):
            errors.append(
                f"{english.relative_to(ROOT)}: English companion must not set arxiv_id"
            )

    if errors:
        raise SystemExit("bilingual validation failed:\n- " + "\n- ".join(errors))
    print(f"bilingual coverage: ok ({paper_count} paper pairs)")


if __name__ == "__main__":
    main()
