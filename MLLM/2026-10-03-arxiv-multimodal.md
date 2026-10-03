# Arxiv 多模态论文日报 - 2026-10-03

> 收录论文 **13** 篇 | 含代码仓库 **2** 篇 | 覆盖方向 **6** 个

---

## VLM / MLLM

### [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](https://arxiv.org/abs/2610.01434)

**作者：** Xudong Wang, Hao Wu, Haozhe Hu et al. | **方向：** `VLM / MLLM` | **代码：** [GitHub](https://github.com/EIT-NLP/MWOP)

提出模态感知的逐层操作剪枝方法 MWOP，用于加速多模态大语言模型推理。发现不同模态和门控路径中存在大量冗余计算，通过跨模态剪枝策略移除冗余操作，并设计专用例程将稀疏结构转化为实际加速。实验在多种模型上实现了显著推理加速且保持精度。

---

### [SIEVE: Selective Attention-value Suppression for Vision-Language Models Unlearning](https://arxiv.org/abs/2610.01962)

**作者：** Si Qi Goh, Cap Dang Xuan Kiet, Tat-Jen Cham, Kwok-Yan Lam | **方向：** `VLM / MLLM`

针对视觉语言模型的机器遗忘问题，提出 SIEVE 方法，解决禁止遗忘与允许保留信息在视觉特征上高度重叠的挑战。通过将特定训练样本的注意力权重置零实现选择性遗忘，同时与不变基线模型对齐保护允许数据。实验证明该方法在多种设置下均优于现有遗忘技术。

---

### [HAWK: Rethinking Multimodal Drafting for Speculative Decoding](https://arxiv.org/abs/2610.00623)

**作者：** Wenhan Yang, Anirudh Rao, Ashwin Chandra | **方向：** `VLM / MLLM`

针对多模态大模型推测解码中小模型（draft model）无法充分利用视觉信息的问题，提出 HAWK 方法。通过特征相似度选择关键层并融合中间表示，使用主模型压缩后的视觉 token 替代原始像素输入，并训练 draft model 预测主模型对其猜测的反馈以提高对齐度。在 7B 模型上显著提升接受长度和加速比。

---

### [LEGO-OPD: Factorized Teacher Composition for Multimodal On-Policy Distillation](https://arxiv.org/abs/2610.00333)

**作者：** Jaeyun Shin, Hangeol Chang, Jong Chul Ye | **方向：** `VLM / MLLM` | **代码：** [匿名代码](https://anonymous.4open.science/r/LEGO_OPD-51C1)

提出分解式教师组合方法 LEGO-OPD，解决多模态蒸馏中视觉锚定与文本推理难以兼顾的问题。通过贝叶斯框架将独立训练的文本专家和视觉专家组合为统一指导信号，文本专家提供先验 token 概率，视觉专家以视觉概率更新，实现两者的独立控制。引入动态调节机制防止视觉引导过强或过弱，在 Qwen3 上超越传统单/多教师方法。

---

## 理解与推理

### [Same Reward, Different Skills: When Multimodal RL Learns to Look](https://arxiv.org/abs/2610.01908)

**作者：** Haocun Ye, Xinlong Jiang, Qile Chen et al. | **方向：** `理解与推理` `VLM / MLLM` | **代码：** [匿名代码](https://anonymous.4open.science/r/learning-without-looking-2432)

揭示多模态强化学习中的有趣现象：在无视觉输入条件下使用 RLVR 训练的多模态模型，在视觉评测中仍能获得显著性能提升（3B 模型恢复约 50% 增益，7B 恢复约 80%）。提出"视觉可解性"原则，确保图像为回答问题所必需。实验表明修改奖励函数决定了"RL 学到什么"，该能力可迁移至未训练的空间任务。

---

### [FORTE: Adaptive Scoring and Exact Keyframe Selection for Long-Video Question Answering](https://arxiv.org/abs/2610.00573)

**作者：** Haifeng Huang, Biyin Xu, Chunsheng Xin, Yang Li | **方向：** `理解与推理`

提出无需训练的长视频问答关键帧选择方法 FORTE。使用高斯过程模型快速估计帧重要性，动态分配评估预算，平衡对新时间区域的探索和对有潜力区域的利用。后续优化步骤确保选定帧子集在覆盖度和相关性上达到最优。多个基准测试上在不同评分预算和下游模型上均取得更高准确率。

---

### [Paying for Too Many Tokens? Valid and Cost-Efficient Multimodal LLM Annotation with Simple Heuristics](https://arxiv.org/abs/2610.00809)

**作者：** Zhixi Zhu, Kristina Gligoric | **方向：** `理解与推理`

系统评估多模态 LLM 视频标注中降低 token 成本的策略（帧选择、视频压缩等）。发现准确率与结论有效性之间存在脱节——最精确的设置可能产生错误结论。额外模态并不保证收益，纯文本有时效果更佳。通过场景变化检测生成单个视觉网格，即可在约 15% 的 token 成本下实现完整视频理解。

---

## 基准评测

### [Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluations](https://arxiv.org/abs/2610.01670)

**作者：** Yuan Huang, Zirui Song, Xiuying Chen | **方向：** `基准评测` | **代码：** [GitHub](https://github.com/yuan4629/EditJudgeBias)

研究多模态大模型作为图像编辑评测"裁判"时的偏差问题。核心挑战在于图像编辑可能改变图像的真实质量，影响评测客观性。构建了保证原始图像完整性不变的新评测集，测试了多个模型的评测一致性、与人类判断的对齐程度和偏好稳定性。发现无关图像属性和虚假共识会显著扭曲 AI 评分，单一指标无法全面衡量评测者可靠性。

---

## 检索与信息抽取

### [AiSearch: Interactive Multi-Modal Search with VLMs](https://arxiv.org/abs/2610.01389)

**作者：** A. Koksal, M. C. Leong, V. Sintunata, C. L. Chin, W. T. Fong | **方向：** `检索`

构建利用视觉语言模型零样本能力的交互式多模态检索框架。支持用户通过文本查询视觉媒体，并通过反馈迭代调整结果以匹配个人需求。提供不同模型的可视化比较功能，帮助用户选择最佳检索模型。作为 ECCV 2026 Demo 论文提交。

---

### [Walking the Embedding Space: Datastore Extraction from Multimodal RAG](https://arxiv.org/abs/2610.01871)

**作者：** Maria Carmen Jica, Ali Satvaty, Suzan Verberne, Fatih Turkmen | **方向：** `检索`

揭示多模态检索增强生成（MRAG）系统的数据安全漏洞。提出 ImmRAG 自适应自动数据提取攻击方法，通过将影子图像与检索图像混合，引导后续查询探索嵌入空间。创新地将恶意指令隐藏在用户输入的图像中而非文本中，在医疗、文档和通用场景中成功重建数百个文件，凸显多模态系统急需专门的安全防护机制。

---

## Agent 与具身智能

### [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204)

**作者：** Yen-Jen Wang, Haozhe Jiang, Shuying Deng et al. | **方向：** `Agent`

提出在不修改神经网络权重的前提下提升机器人智能体性能的方法。通过在虚拟环境中生成任务并回顾历史经验，利用视觉和状态信息定位错误，更新策略并生成新技能。在仿真和真实环境中均取得高成功率，为具身智能体的自我改进提供了新范式。项目主页已上线，代码即将发布。

---

## 多模态生成

### [PEARL: Personalized Image Generation with Reasoning and Reflection](https://arxiv.org/abs/2610.00737)

**作者：** Bo Ni et al. | **方向：** `生成`

提出个性化图像生成新范式 PEARL，认为用户的个人上下文远比特定示例更丰富，包含各种数字足迹。构建了首个统一基准评估个性化图像生成，涵盖电商和社交媒体两个互补任务。PEARL 结合推理模型与图像生成器，超越强基线方法 15%，展示了推理与反思在个性化创作中的价值。

---

## 音频多模态

### [PLACE: Positional Latent Adaptation via Conditioned Embeddings for Binaural Audio Generation](https://arxiv.org/abs/2610.00630)

**作者：** Tiernon Riesenmy, You Zhang, Gautam Bhattacharya, Andrea Fanelli | **方向：** `音频`

提出 PLACE 方法用于双耳空间音频生成，扩展现有音频模型以支持多模态输入。融合视觉特征并对齐文本与视觉信息建立位置提示，引入依赖输入的秩缩减调整模块，通过双耳时间差和级差目标进行学习。在多个指标上超越先前模型，用户测试在视觉到音频和新文本到音频任务中均偏好该方法。

---

## 统计

| 方向 | 论文数 | 有代码 |
|------|--------|--------|
| VLM / MLLM | 4 | 1 |
| 理解与推理 | 3 | 0 |
| 基准评测 | 1 | 1 |
| 检索与信息抽取 | 2 | 0 |
| Agent 与具身智能 | 1 | 0 |
| 多模态生成 | 1 | 0 |
| 音频多模态 | 1 | 0 |
| **合计** | **13** | **2** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-10-03*
