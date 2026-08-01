#!/usr/bin/env python3
"""Rebuild the generated overview block in README.md."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- BEGIN AUTO:OVERVIEW -->"
END = "<!-- END AUTO:OVERVIEW -->"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
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


def relative_link(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_overview() -> str:
    paper_rows = []
    for path in ROOT.glob("papers/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        meta = parse_frontmatter(path)
        if not meta.get("arxiv_id"):
            continue
        paper_rows.append((meta.get("date", ""), meta, path))
    paper_rows.sort(key=lambda item: (item[0], item[1].get("arxiv_id", "")), reverse=True)

    daily_files = sorted(
        (p for p in (ROOT / "daily").glob("????-??-??.md")), reverse=True
    )
    monthly_files = sorted(
        (p for p in (ROOT / "monthly").glob("????-??.md")), reverse=True
    )

    categories: dict[str, int] = {}
    for _, meta, _ in paper_rows:
        category = meta.get("primary_category", "未分类")
        categories[category] = categories.get(category, 0) + 1

    lines = [
        f"- 已收录论文：**{len(paper_rows)}** 篇",
        f"- 每日记录：**{len(daily_files)}** 期",
        f"- 月度归档：**{len(monthly_files)}** 期",
    ]
    if categories:
        dist = "、".join(
            f"[{key}](docs/categories.md#{key.lower()}) {value}"
            for key, value in sorted(categories.items())
        )
        lines.append(f"- 主分类分布：{dist}")

    lines.extend(["", "### 最近每日更新", ""])
    if daily_files:
        lines.extend(
            f"- [{path.stem}]({relative_link(path)})" for path in daily_files[:10]
        )
    else:
        lines.append("暂无每日记录。")

    lines.extend(["", "### 最近收录论文", "", "| 日期 | 主分类 | 论文 | arXiv |", "|---|---|---|---|"])
    if paper_rows:
        for date, meta, path in paper_rows[:20]:
            title = meta.get("title", meta["arxiv_id"])
            category = meta.get("primary_category", "—")
            arxiv_id = meta["arxiv_id"]
            lines.append(
                f"| {date} | [{category}](docs/categories.md#{category.lower()}) | [{title}]({relative_link(path)}) | "
                f"[{arxiv_id}](https://arxiv.org/abs/{arxiv_id}) |"
            )
    else:
        lines.append("| — | — | 暂无论文 | — |")

    lines.extend(["", "### 月度归档", ""])
    if monthly_files:
        lines.extend(
            f"- [{path.stem}]({relative_link(path)})" for path in monthly_files[:12]
        )
    else:
        lines.append("暂无月度归档。")

    return "\n".join(lines)


def replace_block(path: Path, start: str, end: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    replacement = f"{start}\n{body}\n{end}"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    updated, count = pattern.subn(replacement, text)
    if count != 1:
        raise SystemExit(f"generated markers are missing or duplicated: {path}")
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    papers = []
    for path in ROOT.glob("papers/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        meta = parse_frontmatter(path)
        if meta.get("arxiv_id"):
            papers.append((meta.get("date", ""), meta, path))
    papers.sort(key=lambda item: (item[0], item[1].get("arxiv_id", "")), reverse=True)

    daily_files = sorted((ROOT / "daily").glob("????-??-??.md"), reverse=True)
    monthly_files = sorted((ROOT / "monthly").glob("????-??.md"), reverse=True)

    daily_body = "\n".join(f"- [{p.stem}]({p.name})" for p in daily_files) or "暂无每日记录。"
    monthly_body = "\n".join(f"- [{p.stem}]({p.name})" for p in monthly_files) or "暂无月度归档。"

    paper_lines = ["| 日期 | 主分类 | 论文 | arXiv |", "|---|---|---|---|"]
    for date, meta, path in papers:
        title = meta.get("title", meta["arxiv_id"])
        arxiv_id = meta["arxiv_id"]
        relative = path.relative_to(ROOT / "papers").as_posix()
        category = meta.get("primary_category", "—")
        category_cell = (
            f"[{category}](../docs/categories.md#{category.lower()})"
            if category != "—"
            else category
        )
        paper_lines.append(
            f"| {date} | {category_cell} | [{title}]({relative}) | "
            f"[{arxiv_id}](https://arxiv.org/abs/{arxiv_id}) |"
        )
    if not papers:
        paper_lines.append("| — | — | 暂无论文 | — |")

    replace_block(ROOT / "README.md", START, END, build_overview())
    replace_block(
        ROOT / "daily" / "README.md",
        "<!-- BEGIN AUTO:DAILY -->",
        "<!-- END AUTO:DAILY -->",
        daily_body,
    )
    replace_block(
        ROOT / "papers" / "README.md",
        "<!-- BEGIN AUTO:PAPERS -->",
        "<!-- END AUTO:PAPERS -->",
        "\n".join(paper_lines),
    )
    replace_block(
        ROOT / "monthly" / "README.md",
        "<!-- BEGIN AUTO:MONTHLY -->",
        "<!-- END AUTO:MONTHLY -->",
        monthly_body,
    )


if __name__ == "__main__":
    main()
