#!/usr/bin/env python3
"""
new_paper.py - 快速创建新论文笔记

用法:
    python scripts/new_paper.py --title "Attention Is All You Need" --topic NLP
    python scripts/new_paper.py --title "DDPM" --topic ML --year 2020 --author "Ho"
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

TOPICS = ["NLP", "CV", "Multimodal", "RL", "ML", "Other"]

ROOT = Path(__file__).parent.parent
TEMPLATE_PATH = ROOT / "template.md"
PAPERS_DIR = ROOT / "papers"
INDEX_PATH = ROOT / "index.md"

# index.md 中全量列表的定位锚点
INDEX_TABLE_ANCHOR = "<!-- 新增论文时在下方添加一行 -->"


def slugify(text: str) -> str:
    """将标题转换为适合文件名的格式"""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '_', text.strip())
    return text[:50]


def create_paper_note(title: str, topic: str, year: int, author: str) -> Path:
    topic_dir = PAPERS_DIR / topic
    topic_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(title)
    filename = f"{year}_{author}_{slug}.md"
    filepath = topic_dir / filename

    if filepath.exists():
        print(f"[!] 文件已存在: {filepath}")
        return filepath

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    # 替换模板中的占位符
    today = date.today().isoformat()
    content = template.replace("<!-- 论文完整标题 -->", title)
    content = content.replace("<!-- YYYY -->", str(year))
    content = content.replace("<!-- YYYY-MM-DD -->", today)
    content = content.replace(
        "*笔记创建时间: <!-- YYYY-MM-DD --> · 最后更新: <!-- YYYY-MM-DD -->*",
        f"*笔记创建时间: {today} · 最后更新: {today}*"
    )

    filepath.write_text(content, encoding="utf-8")
    print(f"[✓] 已创建论文笔记: {filepath}")

    # 自动更新 index.md
    update_index(title, topic, year, filepath)
    return filepath


def update_index(title: str, topic: str, year: int, filepath: Path):
    """在 index.md 的全量列表中插入一行新记录"""
    index_text = INDEX_PATH.read_text(encoding="utf-8")

    rel_path = filepath.relative_to(ROOT)
    new_row = f"| ⬜ 待读 | — | {year} | [{title}]({rel_path}) | {topic} | — | — |"

    if str(rel_path) in index_text:
        print(f"[i] index.md 中已存在该论文记录，跳过")
        return

    # 在表头行之后插入新行（紧接表头的下一行）
    separator = "|------|------|------|------|------|------|-----------|"
    insert_after = separator + "\n"

    if insert_after in index_text:
        index_text = index_text.replace(
            insert_after,
            insert_after + new_row + "\n",
            1,
        )
        INDEX_PATH.write_text(index_text, encoding="utf-8")
        print(f"[✓] 已自动更新 index.md")


def main():
    parser = argparse.ArgumentParser(description="快速创建论文笔记")
    parser.add_argument("--title", required=True, help="论文标题")
    parser.add_argument("--topic", required=True, choices=TOPICS, help=f"领域分类: {TOPICS}")
    parser.add_argument("--year", type=int, default=date.today().year, help="发表年份")
    parser.add_argument("--author", default="Unknown", help="第一作者姓氏")
    args = parser.parse_args()

    filepath = create_paper_note(args.title, args.topic, args.year, args.author)
    return 0


if __name__ == "__main__":
    sys.exit(main())
