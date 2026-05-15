#!/usr/bin/env python3
"""
export.py - 导出论文引用信息

用法:
    python scripts/export.py --format bibtex --output refs.bib
    python scripts/export.py --format csv --output papers.csv
    python scripts/export.py --format markdown --output summary.md
    python scripts/export.py --format bibtex --topic NLP  # 只导出某个领域
"""

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAPERS_DIR = ROOT / "papers"
TOPICS = ["NLP", "CV", "Multimodal", "RL", "ML", "AIGC", "Other"]


def parse_paper(filepath: Path) -> dict | None:
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    def extract(pattern, default=""):
        m = re.search(pattern, text)
        return m.group(1).strip() if m else default

    title = extract(r'\*\*标题\*\*\s*\|\s*(.+)')
    author = extract(r'\*\*作者\*\*\s*\|\s*(.+)')
    year = extract(r'\*\*发表年份\*\*\s*\|\s*(\d{4})')
    venue = extract(r'\*\*发表venue\*\*\s*\|\s*(.+)')
    arxiv = extract(r'\*\*ArXiv\*\*\s*\|\s*(.+)')
    code = extract(r'\*\*代码\*\*\s*\|\s*(.+)')
    status = extract(r'\*\*阅读状态\*\*\s*\|\s*`([^`]+)`')
    rating_m = re.search(r'\*\*评分\*\*\s*\|\s*(⭐+)', text)
    rating = len(rating_m.group(1)) if rating_m else 0
    summary_m = re.search(r'## 一句话总结\s*\n+> (.+)', text)
    summary = summary_m.group(1).strip() if summary_m else ""
    tags = re.findall(r'`(#\w+)`', text)
    bibtex_m = re.search(r'```bibtex\n(.*?)```', text, re.DOTALL)
    bibtex = bibtex_m.group(1).strip() if bibtex_m else ""

    if not title or title.startswith("<!--"):
        title = filepath.stem

    return {
        "title": title,
        "author": author,
        "year": year,
        "venue": venue,
        "arxiv": arxiv,
        "code": code,
        "status": status,
        "rating": rating,
        "summary": summary,
        "tags": tags,
        "bibtex": bibtex,
        "topic": filepath.parent.name,
        "file": str(filepath.relative_to(ROOT)),
    }


def collect_papers(topic_filter: str | None = None) -> list[dict]:
    papers = []
    topics = [topic_filter] if topic_filter else TOPICS
    for topic in topics:
        topic_dir = PAPERS_DIR / topic
        if not topic_dir.exists():
            continue
        for f in sorted(topic_dir.glob("*.md")):
            if f.name == "README.md":
                continue
            info = parse_paper(f)
            if info:
                papers.append(info)
    return papers


def export_bibtex(papers: list[dict], output: Path):
    lines = []
    for p in papers:
        if p["bibtex"] and not p["bibtex"].startswith("@article{author"):
            lines.append(p["bibtex"])
        else:
            # 生成基础 bibtex
            key = re.sub(r'\W+', '', f"{p['author'].split()[0] if p['author'] else 'Unknown'}{p['year']}{p['title'].split()[0]}")
            lines.append(f"@article{{{key},\n  title={{{p['title']}}},\n  author={{{p['author']}}},\n  year={{{p['year']}}}\n}}")
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"[✓] 已导出 BibTeX: {output} ({len(papers)} 条)")


def export_csv(papers: list[dict], output: Path):
    fields = ["title", "author", "year", "venue", "topic", "status", "rating", "summary", "arxiv", "code", "file"]
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(papers)
    print(f"[✓] 已导出 CSV: {output} ({len(papers)} 条)")


def export_markdown(papers: list[dict], output: Path):
    lines = [
        "# 论文列表摘要\n",
        "| 评分 | 年份 | 标题 | 领域 | 状态 | 一句话总结 |",
        "|------|------|------|------|------|-----------|",
    ]
    for p in papers:
        stars = "⭐" * p["rating"] if p["rating"] else "—"
        title = f"[{p['title']}]({p['file']})" if p["file"] else p["title"]
        lines.append(f"| {stars} | {p['year']} | {title} | {p['topic']} | {p['status']} | {p['summary']} |")
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"[✓] 已导出 Markdown: {output} ({len(papers)} 条)")


def main():
    parser = argparse.ArgumentParser(description="导出论文引用/列表")
    parser.add_argument("--format", choices=["bibtex", "csv", "markdown"], default="markdown")
    parser.add_argument("--output", type=Path, help="输出文件路径")
    parser.add_argument("--topic", choices=TOPICS, help="只导出某个领域")
    args = parser.parse_args()

    papers = collect_papers(args.topic)
    if not papers:
        print("[!] 未找到论文笔记")
        return 1

    ext_map = {"bibtex": "bib", "csv": "csv", "markdown": "md"}
    output = args.output or ROOT / f"exports/papers.{ext_map[args.format]}"
    output.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "bibtex":
        export_bibtex(papers, output)
    elif args.format == "csv":
        export_csv(papers, output)
    else:
        export_markdown(papers, output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
