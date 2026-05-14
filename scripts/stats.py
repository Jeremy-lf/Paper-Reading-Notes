#!/usr/bin/env python3
"""
stats.py - 扫描所有论文笔记，生成统计报告，可选更新 dashboard.md

用法:
    python scripts/stats.py              # 打印统计报告到终端
    python scripts/stats.py --update-dashboard  # 同时更新 dashboard.md
"""

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAPERS_DIR = ROOT / "papers"
DASHBOARD_PATH = ROOT / "dashboard.md"
INDEX_PATH = ROOT / "index.md"

STATUS_EMOJI = {
    "已读": "✅",
    "在读": "🔄",
    "待读": "⬜",
    "复读": "🔁",
    "略读": "⏭️",
}

TOPICS = ["NLP", "CV", "Multimodal", "RL", "ML", "Other"]


def parse_paper(filepath: Path) -> dict | None:
    """从论文笔记文件中解析元信息"""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    def extract(pattern, default=""):
        m = re.search(pattern, text)
        return m.group(1).strip() if m else default

    title_m = re.search(r'^# 📄 (.*)', text, re.MULTILINE)
    if not title_m:
        # 使用文件名作为备用标题
        title = filepath.stem
    else:
        title = title_m.group(1).strip()

    status_raw = extract(r'\*\*阅读状态\*\*\s*\|\s*`([^`]+)`')
    status = ""
    for key in STATUS_EMOJI:
        if key in status_raw:
            status = key
            break

    rating_m = re.search(r'\*\*评分\*\*\s*\|\s*(⭐+)', text)
    rating = len(rating_m.group(1)) if rating_m else 0

    read_date = extract(r'\*\*阅读日期\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})')

    # 提取所有标签
    tags = re.findall(r'`(#\w+)`', text)

    # 从路径推断领域
    topic = filepath.parent.name

    return {
        "title": title,
        "file": filepath.relative_to(ROOT),
        "topic": topic,
        "status": status,
        "rating": rating,
        "read_date": read_date,
        "tags": tags,
    }


def collect_papers() -> list[dict]:
    papers = []
    for topic in TOPICS:
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


def compute_stats(papers: list[dict]) -> dict:
    total = len(papers)
    status_counts = Counter(p["status"] for p in papers)
    topic_counts = Counter(p["topic"] for p in papers)
    rating_counts = Counter(p["rating"] for p in papers)
    tag_counts = Counter(tag for p in papers for tag in p["tags"])

    by_topic_status = defaultdict(lambda: Counter())
    for p in papers:
        by_topic_status[p["topic"]][p["status"]] += 1

    return {
        "total": total,
        "status": status_counts,
        "topics": topic_counts,
        "ratings": rating_counts,
        "tags": tag_counts,
        "by_topic_status": dict(by_topic_status),
    }


def render_progress_bar(done: int, total: int, width: int = 20) -> str:
    if total == 0:
        filled = 0
    else:
        filled = int(done / total * width)
    bar = "█" * filled + "░" * (width - filled)
    pct = f"{done/total*100:.0f}%" if total > 0 else "0%"
    return f"[{bar}] {pct}"


def print_stats(stats: dict):
    print("\n" + "=" * 50)
    print("📊 论文阅读统计")
    print("=" * 50)
    print(f"总论文数: {stats['total']}")
    for key, emoji in STATUS_EMOJI.items():
        count = stats["status"].get(key, 0)
        print(f"  {emoji} {key}: {count}")

    print("\n🗂️  领域分布:")
    for topic in TOPICS:
        count = stats["topics"].get(topic, 0)
        print(f"  {topic}: {count}")

    print("\n⭐ 评分分布:")
    for stars in range(5, 0, -1):
        count = stats["ratings"].get(stars, 0)
        print(f"  {'⭐'*stars}: {count}")

    print("\n🏷️  热门标签 Top 10:")
    for tag, count in stats["tags"].most_common(10):
        print(f"  {tag}: {count}")
    print("=" * 50 + "\n")


def update_dashboard(stats: dict, papers: list[dict]):
    today = date.today().isoformat()
    total = stats["total"]
    done = stats["status"].get("已读", 0)
    reading = stats["status"].get("在读", 0)
    pending = stats["status"].get("待读", 0)
    skim = stats["status"].get("略读", 0)

    bar = render_progress_bar(done, total)

    topic_rows = "\n".join(
        f"| {t} | {stats['topics'].get(t, 0)} | "
        f"{'%.0f' % (stats['topics'].get(t,0)/total*100 if total else 0)}% |"
        for t in TOPICS
    )

    rating_rows = "\n".join(
        f"| {'⭐'*s} | {stats['ratings'].get(s, 0)} |"
        for s in range(5, 0, -1)
    )

    tag_top10 = "\n".join(
        f"| `{tag}` | {count} |"
        for tag, count in stats["tags"].most_common(10)
    ) or "| — | — |"

    content = f"""# 📊 阅读统计仪表盘

> 由 `scripts/stats.py` 自动生成 · 最后更新：{today}

---

## 📈 总体进度

```
总论文数:  {total:<4} {render_progress_bar(total, max(total, 1))}
已  读:   {done:<4} {render_progress_bar(done, max(total,1))}
在  读:   {reading}
待  读:   {pending}
略  读:   {skim}
```

---

## 🗂️ 领域分布

| 领域 | 数量 | 占比 |
|------|------|------|
{topic_rows}

---

## ⭐ 评分分布

| 评分 | 数量 |
|------|------|
{rating_rows}

---

## 🏷️ 热门标签 Top 10

| 标签 | 论文数 |
|------|--------|
{tag_top10}

---

## 📅 月度阅读记录

| 月份 | 新增论文数 | 累计总数 |
|------|-----------|---------|
| {today[:7]} | — | {total} |

---

## 📚 年度阅读目标

### {today[:4]} 年目标

- [ ] 阅读论文总数：**50 篇**
- [ ] 精读（4-5星）：**20 篇**

**当前进度：{done} / 50 ({done/50*100:.0f}%)**

---

*返回 [主页](README.md) · 查看 [论文总索引](index.md)*

*最后更新：{today}*
"""

    DASHBOARD_PATH.write_text(content, encoding="utf-8")
    print(f"[✓] 已更新 dashboard.md")


def main():
    parser = argparse.ArgumentParser(description="生成论文阅读统计")
    parser.add_argument("--update-dashboard", action="store_true", help="同时更新 dashboard.md")
    args = parser.parse_args()

    papers = collect_papers()
    stats = compute_stats(papers)
    print_stats(stats)

    if args.update_dashboard:
        update_dashboard(stats, papers)

    return 0


if __name__ == "__main__":
    sys.exit(main())
