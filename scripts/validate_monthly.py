#!/usr/bin/env python3
"""Validate monthly reports for coverage, structure, and duplicate arXiv IDs."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ARXIV_ID = re.compile(r"\b(\d{4}\.\d{5})\b")
REQUIRED_HEADINGS = (
    "## 月度主题",
    "## 论文总览",
    "## 趋势分析",
    "## 社区与开源观察",
    "## 证据与复现限制",
    "## 后续观察",
)
REQUIRED_HEADINGS_EN = (
    "## Monthly theme",
    "## Paper overview",
    "## Trend analysis",
    "## Community and open-source observations",
    "## Evidence and reproducibility limits",
    "## Follow-up",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict-counts",
        action="store_true",
        help="Fail when a monthly report contains fewer than 20 papers.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    ownership: dict[str, list[str]] = defaultdict(list)

    paths = sorted((ROOT / "monthly").glob("????-??.md"))
    if not paths:
        raise SystemExit("no monthly reports found")

    for path in paths:
        text = path.read_text(encoding="utf-8")
        ids = sorted(set(ARXIV_ID.findall(text)))
        if len(ids) < 20:
            message = f"{path.name}: {len(ids)} papers, below the 20-paper target"
            (errors if args.strict_counts else warnings).append(message)
        if len(ids) > 35:
            errors.append(f"{path.name}: {len(ids)} papers, above the 35-paper limit")

        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.name}: missing heading {heading!r}")

        english_path = path.with_suffix(".en.md")
        if not english_path.exists():
            errors.append(f"{path.name}: missing English companion {english_path.name}")
        else:
            english_text = english_path.read_text(encoding="utf-8")
            english_ids = set(ARXIV_ID.findall(english_text))
            if english_ids != set(ids):
                errors.append(
                    f"{english_path.name}: arXiv ID set differs from {path.name}"
                )
            for heading in REQUIRED_HEADINGS_EN:
                if heading not in english_text:
                    errors.append(
                        f"{english_path.name}: missing heading {heading!r}"
                    )

        for arxiv_id in ids:
            ownership[arxiv_id].append(path.name)

        print(f"{path.stem}: {len(ids)} papers")

    for arxiv_id, months in ownership.items():
        if len(months) > 1:
            errors.append(f"{arxiv_id}: duplicated across {', '.join(months)}")

    for warning in warnings:
        print(f"warning: {warning}")
    if errors:
        raise SystemExit("monthly validation failed:\n- " + "\n- ".join(errors))


if __name__ == "__main__":
    main()
