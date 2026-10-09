# Arxiv 多模态论文日报 — 2026-10-09

> 收录时间范围：2026年10月7日 - 10月8日 | 共 **35** 篇论文，涵盖 **8** 个方向

---

## VLM/MLLM 视觉语言模型 (10)

### [SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces](https://arxiv.org/abs/2610.11366)
**Authors:** Rongxue Li, Meng Yang, Yiru Mao, Yongliang Tao, et al. | `Oct 8` | 方向: VLM/MLLM

空间编码Agent通过外部工具生成验证过的执行轨迹，显著提升MLLM的空间推理能力，但推理开销大。SpatialOPSD提出自蒸馏方案将外部能力内化到模型中，并设计重复感知蒸馏策略缓解数据泄露问题，以更轻量的方式实现空间智能。

### [UniData: Universal Multimodal Instruction Generation Pipeline](https://arxiv.org/abs/2610.11363)
**Authors:** Jiaqi Tang, Yi-Feng Wu, Yuting Zhang, Hao Lu, et al. | `Oct 8` | 方向: VLM/MLLM

MLLM的广泛应用面临高质量多模态指令数据稀缺的挑战。UniData提出通用多模态指令生成流水线，将用户需求转化为多轮、多模态指令，构建了包含2万条数据、覆盖9种模态的UniDataset，大幅降低数据创建成本。

### [MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making](https://arxiv.org/abs/2610.11316)
**Authors:** Jianpeng Cheng, Guangyu Sun, Aashu Singh, et al. | `Oct 8` | 方向: VLM/MLLM

System One模型输出约束决策和概率分布而非自由文本。MetaEncoder探索双编码器架构在多模态System One决策中的极限，通过自然语言接口实现高效的多模态匹配与决策。

### [Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers](https://arxiv.org/abs/2610.11315)
**Authors:** Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan | `Oct 8` | 方向: VLM/MLLM

在扩散Transformer中，低秩分支可以缓解4-bit权重-激活(W4A4)训练后量化损失。本文将每个权重分解为低比特残差和高精度低秩分量，通过Hessian矩阵降秩实现高效多模态扩散模型量化。

### [V-CoLA: Vision Token Compression with Linear Attention](https://arxiv.org/abs/2610.11251)
**Authors:** Hao Jiang, Yiru Mao, Tianpeng Bu, et al. | `Oct 8` | 方向: VLM/MLLM

VLM视觉token带来巨大计算开销。V-CoLA提出面向线性注意力的免训练压缩框架，通过独特性感知的token选择策略，在保持性能的同时大幅减少视觉token数量，加速推理。

### [Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models](https://arxiv.org/abs/2610.10990)
**Authors:** Hong Huang, Chenhongyi Yang, Junzhe Sun, et al. | `Oct 7` | 方向: VLM/MLLM

统一多模态扩散大语言模型(dLLMs)在单一架构中同时支持图像生成和多模态理解，但迭代解码需要数十到数百次前向传播。Omni-Diffusion-Distill通过少步蒸馏大幅减少推理步数，提升效率。

### [VICO: Visual Environments Co-Evolving for Vision-Language Model Reasoning](https://arxiv.org/abs/2610.10782)
**Authors:** Meng Lu, Ligeng Zhu, Olivia Xiao, et al. | `Oct 7` | 方向: VLM/MLLM

基于可验证奖励的强化学习(RLVR)已成为VLM后训练的标准方法，但通常假设静态训练环境。VICO让Actor与环境重写器共同进化，自动编辑视觉结构并重新校准任务难度，无需人工标注。

### [SAGE: Sink-Aware Guided Emphasis for Visual Grounding in VLM Decoders](https://arxiv.org/abs/2610.11469)
**Authors:** Jeonghyo Song, YoungJoon Yoo | `Oct 8` | 方向: VLM/MLLM

VLM将视觉编码器与LLM配对，但存在注意力病理抑制视觉证据的问题。SAGE利用骨干网络衍生的ROI掩码，将解码器注意力从sink token引导至查询相关区域，改善视觉定位能力。

### [ComCLIP: Rethinking Contrastive Loss in CLIP Post-training](https://arxiv.org/abs/2610.11374)
**Authors:** Zidan Wang, Yaqian Li, Xiaokai Zhang, et al. | `Oct 8` | 方向: VLM/MLLM | [Code](https://github.com/showstarpro/ComCLIP)

CLIP作为基础VLM和下游模型的视觉编码器，其后训练至关重要。ComCLIP重新审视对比后训练，采用适当温度的InfoNCE损失和冻结文本编码器策略，显著提升CLIP的跨模态对齐效果。

### [Mid-Training Language Models on Raw Video](https://arxiv.org/abs/2610.11019)
**Authors:** Jaedong Hwang, Xiaoqian Shen, Ernie Chang, et al. | `Oct 7` | 方向: VLM/MLLM

多模态大语言模型主要从图文配对数据或标注视频中学习，原始网络视频很少用于进一步训练。本文提出通过下一视觉token预测进行原始视频中间训练，在保持文本性能的同时提升视频和图像基准表现。

---

## 多模态理解与推理 (5)

### [SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows](https://arxiv.org/abs/2610.10563)
**Authors:** Albert Gao, Bing Xue, Andrea Zanette | `Oct 7` | 方向: 理解与推理

MLLM常依赖语言先验而非视觉证据进行推理。SLVR将多模态推理组织为有类型的潜在阶段（规划、定位、证据整合），通过结构化监督避免文本思维链的开销，模拟人类推理流。

### [SPLIT-RL: Staged Perception-Language Reasoning Training](https://arxiv.org/abs/2610.10889)
**Authors:** Raja Kumar, Rajat Koner, Ritwick Chaudhry, et al. | `Oct 7` | 方向: 理解与推理

视觉语言推理需要视觉和语言推理能力。SPLIT-RL在不相交的阶段分别训练视觉推理和语言推理，配合阶段特定奖励和Claim-Level Advantage实现细粒度监督，提升VL推理性能。

### [Harness Compilation: Decisions for Small VLMs](https://arxiv.org/abs/2610.11231)
**Authors:** Minhao Fan, Yinyi Liu, Jiayu Zhao, et al. | `Oct 8` | 方向: 理解与推理

小型VLM可以阅读外部证据但难以获取。Harness Compilation借鉴编译器思想，利用教师修订来适应冻结小VLM与外部harness之间的工作分工，让小模型也能有效利用外部资源。

### [DiscoVL: Disentangled Cross-Modal Representation Learning via Orthogonal Adversarial Regularization](https://arxiv.org/abs/2610.11113)
**Authors:** Mengping Dong, Jinbao Li, Fei Li | `Oct 7` | 方向: 理解与推理

预训练VLM在感知任务上表现出色，但适配并非易事。DiscoVL将正交对抗正则化与跨模态对齐结合，解耦跨模态表示学习，提升模型在下游任务上的泛化能力。

### [Diffusion Meta-Prompting and Steering for Generalizable Foundation Model Adaptation](https://arxiv.org/abs/2610.11067)
**Authors:** Deepak Sridhar, Yi Li, Kartikeya Bhardwaj, et al. | `Oct 7` | 方向: 理解与推理

提示学习适配基础模型，但学习到的提示缺乏泛化性。DMP用扩散模型建模提示分布，并在测试时通过引导实现稳定采样和跨任务泛化，提升基础模型在新任务上的表现。

---

## 多模态检索与信息抽取 (5)

### [Autoregressive Retriever: Improving Query Understanding from Item Feedback](https://arxiv.org/abs/2610.11666)
**Authors:** Jianfei Zhao, Yifan Wang, Feng Zhang, et al. | `Oct 8` | 方向: 检索与信息抽取

通用多模态检索通常编码一次查询并按嵌入相似度排序。这种设计支持高效搜索，但即使检索项可以帮助澄清信息需求，查询表示也不变。自回归检索器利用检索反馈迭代改进查询理解。

### [EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval](https://arxiv.org/abs/2610.11553)
**Authors:** Zifei Wang, Wei Wen, Qiang Ji, et al. | `Oct 8` | 方向: 检索与信息抽取

准确且可扩展的视觉文档检索需要细粒度页面理解和高效索引。EVIE是原生视觉文档检索器，集成证据判断数据治理、双向学习和HAC压缩，同时实现精确度和效率。

### [MSGAT: Multi-Head Spiking Graph Attention with Similarity-Space Fusion for Image-Text Retrieval](https://arxiv.org/abs/2610.11526)
**Authors:** Xintao Zong, Wenxuan Liu, Jianhao Ding, et al. | `Oct 8` | 方向: 检索与信息抽取

脉冲神经网络(SNN)通过稀疏事件驱动计算提供节能计算范式。MSGAT将多头脉冲图注意力与相似性空间融合结合，用于高效图文检索，展现SNN在多模态学习中的巨大潜力。

### [CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at Scale](https://arxiv.org/abs/2610.11230)
**Authors:** Shixin Wan, Guoyu Hu, Yifan Wu, et al. | `Oct 8` | 方向: 检索与信息抽取

跨模态向量检索广泛应用于搜索引擎和向量数据库等多模态系统。CORAL通过增量图构建实现大规模跨模态向量检索，提升检索精度和效率。

### [VESSI: VLM-Enhanced Support for Surveillance and Investigations](https://arxiv.org/abs/2610.11674)
**Authors:** Saverio Cavasin, Pietro Tedeschi, Mattia Tamiazzo, et al. | `Oct 8` | 方向: 检索与信息抽取

自动化视频监控分析对情报和执法至关重要。传统系统缺乏语义感知能力，限制有意义的事件解读。VESSI提供基于VLM的框架，增强监控视频的智能分析和调查支持。

---

## Agent 与具身智能 (6)

### [AdaptEvo: Adaptive Agent Learning with Evolving Supervision](https://arxiv.org/abs/2610.11354)
**Authors:** Shijun Wan, Jiancong Xie, Hang Xu, et al. | `Oct 8` | 方向: Agent与具身智能

规则驱动的上下文决策任务要求模型将指定规则应用于具体案例。AdaptEvo提出自适应Agent学习框架，通过演化监督策略让Agent动态适应不断变化的任务规则和环境。

### [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194)
**Authors:** Naiyu Fang, Zhongjin Luo, Yuxin Mo, et al. | `Oct 7` | 方向: Agent与具身智能

灵巧抓取是具身AI的基础能力，需要大量数据训练鲁棒模型。OmniDex将灵巧手抓取扩展到多样化杂乱场景，通过大规模数据收集和训练实现复杂环境下的可靠抓取。

### [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution](https://arxiv.org/abs/2610.11508)
**Authors:** Junmyeong Lee, Dongmin Shin, Min-Gyu Park, et al. | `Oct 8` | 方向: Agent与具身智能

VLA模型性能对相机配置变化敏感。WARP-VLA使用混合专家(MoE)架构，结合视图特定特征变换的路由器，实现从腕部相机的鲁棒策略部署，解决视角变化带来的性能下降。

### [ACT3: Action-Centric Tri-Stream Transformer](https://arxiv.org/abs/2610.11416)
**Authors:** Shuang Luo, Yilun Kong, Yunpeng Qing, et al. | `Oct 8` | 方向: Agent与具身智能

VLA模型提供语义理解但缺乏物理动力学先验。ACT3将语义和动力学信息通过逐层注意力融合到控制动作中，使用三流独立Transformer架构实现更精准的机器人控制。

### [LaTraNav: Learning Language-Conditioned Traversability Representations](https://arxiv.org/abs/2610.11622)
**Authors:** Senda Chen, Changxu Cheng, Fangdi Li, et al. | `Oct 8` | 方向: Agent与具身智能

可通行性因机器人能力和偏好而异。LaTraNav将慢速VLM与基于流匹配的规划器结合，通过潜在可通行性表示实现语言条件导航，让机器人根据语言指令适应不同地形。

### [Rephrase Before You Act: Mitigating Language Sensitivity in VLAs](https://arxiv.org/abs/2610.10526)
**Authors:** Mikey Watts, Yuchen Cui | `Oct 7` | 方向: Agent与具身智能

VLA模型对指令措辞敏感，而其VLM骨干则不然。本文通过LLM蒸馏改写规则，在不重训练的情况下提升冻结策略在对抗性、VLM生成和人类措辞上的鲁棒性。

---

## 3D 视觉语言 (2)

### [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215)
**Authors:** Qirui Wu, Stan Birchfield, Hesam Rabeti, et al. | `Oct 8` | 方向: 3D视觉语言

从随意图像重建完整、场景对齐的3D物体需要整合稀疏、不确定的观测并推断被遮挡的表面。GATOR提出生成式和Agent式框架，恢复纹理化的3D物体资产。

### [TKCAM: Text and Keyframe to Camera Trajectory Generation](https://arxiv.org/abs/2610.11105)
**Authors:** Haozhe Yang, Zhiyang Dou, Zekai Gu, et al. | `Oct 7` | 方向: 3D视觉语言

生成高质量可控相机运动对AI辅助电影制作、视频合成和3D场景理解至关重要。TKCAM是文本和关键帧条件下的相机运动合成框架，实现可控的相机轨迹生成。

---

## 多模态生成 (3)

### [Learning What to Trust in Multimodal Learning under Noisy Supervision](https://arxiv.org/abs/2610.11057)
**Authors:** Jiashuo Zou, Xiaobo Xia | `Oct 7` | 方向: 多模态生成

多模态分类处理和关联来自多个模态的信息以实现更准确的预测。但在噪声监督下，模型需要学会判断该信任哪个模态。本文提出在噪声条件下学习模态信任度的方法。

### [Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics](https://arxiv.org/abs/2610.10984)
**Authors:** Hong Huang, Yuqiu Liu, Chenyu You, et al. | `Oct 7` | 方向: 多模态生成

物理感知流体-物体视频生成需要物理推理和外观合成。Fluid-Gen-Zero将运动委托给物理模拟器，同时通过Agent式规划保持预训练视频生成器的能力，实现物理合理的视频生成。

### [False Claims, Credible Images: A Red-Teaming Benchmark for Commercial Image Generators](https://arxiv.org/abs/2610.11112)
**Authors:** Zeyu Ye, Yanchun Li, Sibei He, et al. | `Oct 7` | 方向: 多模态生成

图像生成模型现在能生成包含文本、看起来自然的视觉制品，难以与真实证据区分。本文构建了商业图像生成器的红队测试基准，评估模型生成虚假但可信图像的能力。

---

## 音频多模态 (1)

### [Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models](https://arxiv.org/abs/2610.11196)
**Authors:** Yulin Sun, Kele Xu, Yong Dou | `Oct 8` | 方向: 音频多模态

大型音频语言模型(LALMs)利用多模态证据，但任务无关的音频可能改变文本推理决策。本文通过机制引导的选择性听觉，控制音频信息对推理的影响，让模型学会何时该"选择性聆听"。

---

## 基准评测 (3)

### [MedBenchAgent: Systematic Automation of Medical VLM Benchmark Construction](https://arxiv.org/abs/2610.11312)
**Authors:** Yulin Fu, Junren Wang, Guangjing Yang, et al. | `Oct 8` | 方向: 基准评测

医学VLM基准构建随着标注影像和LLM的发展变得越来越可行。MedBenchAgent将基准构建形式化为受约束的编译问题，通过多Agent框架实现自动化基准生成。

### [TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity](https://arxiv.org/abs/2610.10374)
**Authors:** Chengwei Shi, Yunnong Chen, Tingting Zhou, et al. | `Oct 7` | 方向: 基准评测

TaoD2C-Bench评估MLLM在工业UI代码生成中的表现，包含2861个设计稿。揭示了视觉还原度与实际需求满足之间的差距，超越单纯的视觉保真度评估。

### [GameCommBench: A Unified Benchmark and Type-Aware Evaluation for AI-Generated Game Commentary](https://arxiv.org/abs/2610.11129)
**Authors:** Qirui Zheng, Zhengteng Lin, Yunyi Xiao, et al. | `Oct 7` | 方向: 基准评测

游戏解说需要多模态感知、策略推理和上下文知识的开放式生成任务。GameCommBench提供统一基准和类型感知评估方法，系统评估AI游戏解说生成能力。

---

## 统计

| 方向 | 论文数 |
|------|--------|
| VLM/MLLM 视觉语言模型 | 10 |
| 多模态理解与推理 | 5 |
| 多模态检索与信息抽取 | 5 |
| Agent 与具身智能 | 6 |
| 3D 视觉语言 | 2 |
| 多模态生成 | 3 |
| 音频多模态 | 1 |
| 基准评测 | 3 |
| **总计** | **35** |

有代码仓库的论文：1 篇 (ComCLIP)

---
*Generated on 2026-10-09*
