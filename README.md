# 📚 论文阅读管理器

> 基于 GitHub 的轻量级论文知识管理系统 · 按主题归档 · 追踪阅读进度 · 沉淀知识洞察

[![GitHub stars](https://img.shields.io/github/stars/Jeremy-lf/Paper-Reading-Notes?style=social)](https://github.com/Jeremy-lf/Paper-Reading-Notes)
[![GitHub forks](https://img.shields.io/github/forks/Jeremy-lf/Paper-Reading-Notes?style=social)](https://github.com/Jeremy-lf/Paper-Reading-Notes)
[![Papers](https://img.shields.io/badge/Papers-0-blue)](index.md)
[![Last Update](https://img.shields.io/github/last-commit/Jeremy-lf/Paper-Reading-Notes)](https://github.com/Jeremy-lf/Paper-Reading-Notes/commits/main)

---

## 🎯 功能特性

| 功能 | 描述 |
|------|------|
| 📝 **论文记录** | 按主题分类，记录核心思想、方法、优缺点、个人见解 |
| 🏷️ **多维标签** | 主题 / 方法 / 任务 / 状态 / 质量 多维度打标 |
| ⭐ **评分系统** | 1-5 星评分 + 推荐理由，快速筛选优质论文 |
| 🔍 **智能检索** | GitHub 原生搜索，支持跨文件组合查询 |
| 📊 **统计报告** | 自动生成阅读进度报告与主题分布统计 |
| 📤 **多格式导出** | 一键导出 BibTeX / CSV / Markdown 摘要表 |
| 🔗 **引用追踪** | 记录论文间引用关系，构建知识图谱 |
| 📅 **阅读计划** | 维护待读列表，追踪阅读状态 |

---

## 📂 目录结构

```
Paper-Reading-Notes/
├── README.md                    # 本文件 · 项目入口
├── index.md                     # 📋 论文总索引（所有论文一览）
├── dashboard.md                 # 📊 阅读统计仪表盘
├── template.md                  # 📄 论文笔记模板（复制使用）
│
├── papers/                      # 📁 论文笔记（按领域分类）
│   ├── NLP/                     # 自然语言处理
│   │   └── README.md            # NLP 主题索引
│   ├── CV/                      # 计算机视觉
│   │   └── README.md
│   ├── Multimodal/              # 多模态
│   │   └── README.md
│   ├── RL/                      # 强化学习
│   │   └── README.md
│   ├── ML/                      # 机器学习（基础方法）
│   │   └── README.md
│   └── Other/                   # 其他
│       └── README.md
│
├── topics/                      # 🏷️ 按研究主题/技术方向的交叉索引
│   ├── attention-mechanism.md   # 注意力机制
│   ├── diffusion-models.md      # 扩散模型
│   ├── llm-alignment.md         # 大模型对齐
│   └── ...
│
├── reports/                     # 📊 自动生成的报告
│   └── ...
│
└── scripts/                     # 🛠️ 工具脚本
    ├── new_paper.py             # 快速创建论文笔记
    ├── export.py                # 导出 BibTeX / CSV
    └── stats.py                 # 生成统计报告
```

---

## 🚀 快速开始

### 方式一：使用脚本（推荐）

```bash
① 创建笔记
   python scripts/new_paper.py --title "xxx" --topic NLP
   → 自动在 papers/NLP/ 建文件，并在 index.md 插入占位行

② 填写笔记
   在 papers/NLP/xxx.md 里填状态、评分、标签、总结等内容

③ 同步更新
   python scripts/stats.py --update-dashboard
   → 重新扫描所有笔记，同时刷新 index.md 和 dashboard.md

```

---

## 📋 论文状态说明

| 状态标签 | 含义 |
|---------|------|
| `⬜ 待读` | 已加入阅读列表，尚未开始 |
| `🔄 在读` | 正在阅读中 |
| `✅ 已读` | 已完成阅读并记录笔记 |
| `🔁 复读` | 重要论文，值得二次精读 |
| `⏭️ 略读` | 只浏览了摘要/结论 |

---

## ⭐ 评分标准

| 评分 | 含义 |
|------|------|
| ⭐⭐⭐⭐⭐ | 领域经典，必读 |
| ⭐⭐⭐⭐ | 质量很高，强烈推荐 |
| ⭐⭐⭐ | 有价值，建议阅读 |
| ⭐⭐ | 一般，可选读 |
| ⭐ | 较弱，了解即可 |

---

## 📊 阅读统计

> 最新统计见 [dashboard.md](dashboard.md)

| 指标 | 数值 |
|------|------|
| 总论文数 | 0 |
| 已读 | 0 |
| 在读 | 0 |
| 待读 | 0 |
| 本月新增 | 0 |

---

## 🏷️ 标签体系

### 领域标签
`#NLP` `#CV` `#Multimodal` `#RL` `#ML` `#Other`

### 方法标签
`#Transformer` `#Diffusion` `#GAN` `#VAE` `#RL` `#RAG` `#RLHF` `#LoRA` `#MoE`

### 任务标签
`#TextGeneration` `#ImageGeneration` `#ObjectDetection` `#Segmentation` `#VQA` `#Translation` `#Summarization`

### 质量标签
`#MustRead` `#Influential` `#Practical` `#Theoretical` `#Survey`

---

## 🤝 使用说明

本仓库为个人论文知识库，所有笔记仅供个人学习参考。如有引用，请遵循原论文版权声明。

---

*由 [论文阅读管理器](https://github.com/Jeremy-lf/Paper-Reading-Notes) 驱动 · 持续更新中*
