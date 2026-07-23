# Arxiv 多模态论文日报 - 2026-07-09

## VLM / MLLM

### [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](https://arxiv.org/abs/2607.07673)

**作者:** Hyunjae Kim, Dain Kim, Pan Xiao et al. | **方向:** VLM / MLLM | **代码:** [Code](https://github.com/Yale-BIDS-Chen-Lab/MedPMC)

提出 MedPMC，一个可自动更新、将开放获取医学文献转化为高质量多模态训练数据的框架；从 610 万篇 PMC 文章中整理出 1100 万医学图文对，显著提升医学基础模型零样本 AUC。

---

### [On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces](https://arxiv.org/abs/2607.07375)

**作者:** Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht et al. | **方向:** VLM / MLLM | **代码:** 无

从中间线性变换谱结构的新视角分析 VLMs 的对抗脆弱性，提出白盒谱子空间引导攻击 SSGRA，将中间表示与右奇异向量底部子空间对齐；实验显示攻击效果优于现有基线，并为提升模型鲁棒性提供可解释性洞察。

---

## 多模态理解与推理

### [HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](https://arxiv.org/abs/2607.07507)

**作者:** Feng He, Zhenting Wang, Qifan Wang et al. | **方向:** 多模态理解与推理 | **代码:** [Code](https://github.com/hefengcs/HIVE)

提出后幻觉推理（PHR）任务，研究 VLMs 在生成幻觉内容后是否仍能进行忠实推理；构建 HIVE 评测基础设施，在忠实与幻觉标题之间进行可控对比，揭示视觉证据模糊性对幻觉行为的影响机制。

---

### [BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning](https://arxiv.org/abs/2607.07361)

**作者:** Jiacheng Yang, Tongying Xiao, Yunkai Dang et al. | **方向:** 多模态理解与推理 | **代码:** 无

受神经科学反向预测机制启发，提出 BUS 无监督自反思训练框架，无需标注数据即可增强视觉语言模型在复杂图像分析中的细粒度推理能力，在 8 个基准上验证有效。

---

### [When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs](https://arxiv.org/abs/2607.07395)

**作者:** Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe et al. | **方向:** 多模态理解与推理 | **代码:** 无

针对提示微调导致 VLM 校准过自信的难题，提出 ArgTca 方法，将（类别，属性）对建模为符号属性图节点，并用图注意力网络学习属性间依赖关系，生成结构化的置信度估计。

---

## 多模态基准与评测

### [Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language Models](https://arxiv.org/abs/2607.07251)

**作者:** Kaito Watanabe, Taisei Yamamoto, Tomoki Doi et al. | **方向:** 多模态基准与评测 | **代码:** [Code](https://github.com/ynklab/multilingual-demonstratives-eval)

构建覆盖四种语言的空间指示词使用能力基准，评估 VLM 在语言-视觉联合推理中的上下文依赖指称能力；实验发现现有模型在选择指示词时与人类存在系统性差异，尤其在基于距离的指称判断上。

---

## Agent 与具身智能

### [MMAgent-R²: Learning to Rerank and Reject for Agentic mRAG](https://arxiv.org/abs/2607.07383)

**作者:** Tao Zhang, Ziqi Zhang, Zongyang Ma et al. | **方向:** Agent 与具身智能 | **代码:** 无

针对知识库视觉问答中视觉相似实体难以区分的挑战，提出 MMAgent-R² 智能体 mRAG 框架，集成视觉重排序与主动拒绝机制，并采用 GRPO 进行步骤级验证奖励训练，在 InfoSeek、E-VQA 和 MMhops 上取得最佳性能。

---

## 多模态生成

### [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)

**作者:** Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. | **方向:** 多模态生成 | **代码:** [Code](https://github.com/robbyant/lingbot-world-v2)

提出 LingBot-World 2.0，一个支持无限交互时长、720p@60fps 快速响应和多样交互元素的开放世界生成框架，配套 14B 主模型与可单卡部署的 1.3B 小模型，服务于多模态智能体训练与交互。

---

### [Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning](https://arxiv.org/abs/2607.07117)

**作者:** Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee | **方向:** 多模态生成 | **代码:** [Code](https://github.com/Pandastep/ToT-T2I-ICL)

针对文本到图像上下文学习（T2I-ICL）中潜在组合模式推断难题，提出 Tree-of-Thoughts（ToT）推理框架，通过多阶段推理与选择机制提升少样本图像生成的质量与可控性。

---

## 3D 视觉语言

### [EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning](https://arxiv.org/abs/2607.07187)

**作者:** Youtan Yin, Yanning Zhou, Jiacheng Wei et al. | **方向:** 3D 视觉语言 | **代码:** 无

针对 3D 物体局部编辑在粗粒度引导下难以保持质量的瓶颈，提出 EditVerse3D 区域感知学习框架，实现高质量、可控的 3D 对象局部编辑。项目页面已公开，代码标注为即将发布。

---

### [PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170)

**作者:** Yi Yang, Myrna Castillo, Bodo Rosenhahn et al. | **方向:** 3D 视觉语言 | **代码:** [Code](https://github.com/yyyyangyi/PUF)

针对在线 3D 场景图生成中观测、2D 模型和 3D 表示三类不确定性，提出 PUF 即插即用框架，将节点关联建模为语义与空间因素上的概率似然，提升场景图融合的鲁棒性与一致性。

---

### [Ego-Human Motion Prediction with 3D-Aware LLM](https://arxiv.org/abs/2607.07001)

**作者:** Yujin Bae, Jaewoo Jeong, Hyeonseong Kim et al. | **方向:** 3D 视觉语言 | **代码:** [Code](https://github.com/jinyubae/Ego3DLM)

提出 Ego3DLM，一个 3D 感知大语言模型，用于第一视角人体运动预测；通过单次自回归同时解码过去与未来姿态及相应叙述，为 AR/VR、人机协作与具身智能应用提供支持。

---

> 共收录 12 篇论文，涵盖 6 个方向
