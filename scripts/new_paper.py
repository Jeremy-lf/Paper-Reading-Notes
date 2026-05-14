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

TEMPLATE_PATH = Path(__file__).parent.parent / "template.md"
PAPERS_DIR = Path(__file__).parent.parent / "papers"


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
    print(f"[i] 请记得在 index.md 中添加索引记录")
    return filepath


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
