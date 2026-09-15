# Arxiv 多模态论文日报 · 2026-09-15

> 收录窗口：2026-09-12 至 2026-09-13 提交的论文，共 15 篇，覆盖 7 个方向。

## VLM / MLLM 核心

### [SPARK: Representation-Level KV Memory Alignment for Safer Vision-Language Models](https://arxiv.org/abs/2609.14258)

**作者**：Mohd Azfar, Izhar Dad Khan ｜ **标签**：VLM / MLLM ｜ **代码**：暂无代码

提出两阶段 prefill 时 KV 记忆修复框架 SPARK，无需修改模型参数即可增强 VLM 安全性：先用一次性诊断适配器定位多模态键/值表示中与危害相关的方向，再通过投影加残差修复并结合图像结构先验锚定修复后的键，保留视觉定位能力。在 LLaVA-OneVision-7B、Qwen2-VL-7B 等 7B 级模型上，纯图像越狱攻击成功率降至 4.7%，MMMU 仅下降约 0.6 分，推理时无需显式危害分类器。

### [Adapting Open-Weight MLLMs to Generate Point Prompts for Electron Microscopy Segmentation](https://arxiv.org/abs/2609.14080)

**作者**：Samia Mohinta, Albert Cardona ｜ **标签**：VLM / MLLM ｜ **代码**：暂无代码

首次验证开放权重 MLLM 可作为电子显微镜分割的点提示生成器：将三个线粒体数据集的掩码转为「图像 + 指令 → 质心坐标」训练对，在冻结 MLLM 骨干与 microSAM 上仅训练 LoRA 适配器，使 Qwen3-VL 的 AP50 从 0.247 提升至 0.736。训练可跨数据集与体积迁移，对改写后的自然语言请求保持稳定，构建了可检查的语言驱动定位-掩码解码链路（ECCV 2026 BIC Workshop）。

### [StepPrune: Adaptive Sequential Visual Token Selection across Multimodal Large Language Models](https://arxiv.org/abs/2609.13804)

**作者**：Hansen Zhang, Landi He, Mingde Yao ｜ **标签**：VLM / MLLM ｜ **代码**：暂无代码

将 MLLM 视觉 token 剪枝重构为自适应序列决策过程：基于已选 token 与文本逐步构建保留集，并学习 STOP 动作让子集大小自行决定；方差保持噪声门使离散选择可训练，推理时在 prefill 前物理丢弃未选 token。在 LLaVA-1.5 上剪枝 88.9% 视觉 token 仍保留 94.6% 全前缀归一化性能，prefill 延迟从 59.95ms 降至 40.05ms（1.5 倍加速），并支持高分辨率分组选择。

### [Hyper-LLaVA: Hyperbolic Uncertainty-aware Modality-Balanced Routing for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2609.13742)

**作者**：Kunlun Xu, Yanqin Zhang, Wenwen Qiang ｜ **标签**：VLM / MLLM ｜ **代码**：[Code]（仓库已建，代码待发布）https://github.com/zhoujiahuan1991/ICML2026-Hyper-LLaVA

针对多模态持续指令调优（MCIT）中参数路由依赖任务中心点、浪费任务内多样性的问题，Hyper-LLaVA 在双曲空间中度量样本到任务分布的相似性，并量化各模态的任务匹配歧义来自适应平衡模态贡献。实验大幅超越已有 MCIT 路由方法（ICML 2026），官方仓库已建立但代码尚未上传。

### [Multimodal Foundation Models Adaptation based on Domain-Aware Relaxed Orthogonal Subspace for Remote Sensing](https://arxiv.org/abs/2609.13654)

**作者**：Han Luo, Ruoyu Yang, Yinhe Liu ｜ **标签**：VLM / MLLM ｜ **代码**：暂无代码

指出 LoRA 等 PEFT 方法的固定低秩子空间在域差大的遥感任务中存在「子空间失配」。DROS 框架将低秩适配重构为数据条件子空间学习：用下游数据的二阶激活统计初始化权重分解，再以放松正交参数化灵活调整；多模态扩展 MM-DROS 在模态特有子空间间共享变换结构以支持跨模态交互，在多个遥感基准上取得 SOTA，部分设置超过全量微调，且不增加推理开销。

## 多模态理解与推理

### [Talking to Me or Someone Else? Rethinking Talk-to-Me Detection in Egocentric Videos](https://arxiv.org/abs/2609.14118)

**作者**：Feiyu Du, Xi He, Jia Li ｜ **标签**：理解推理、音频 ｜ **代码**：暂无代码

将第一人称「是否对佩戴者说话」（TTM）检测从离线片段级识别重构为在线帧级预测任务，并细分对他人说话、自言自语、背景等多种非 TTM 状态。基于 Ego4D 构建含 406 个片段、约 90 万标注帧的 Online TTM 数据集，融合音频、视觉与语音语义线索的模型取得 75.5% 帧级 F1，显著优于强基线（ACM MM 2026）。

### [UniCAR-RL: Seeing Better before Thinking Deeper in Visual Mathematics](https://arxiv.org/abs/2609.13849)

**作者**：Yuzhe Li, Hao Yan, Hao Wang ｜ **标签**：理解推理 ｜ **代码**：[Code] https://github.com/yzli9/UniCAR-RL

针对 MLLM 在视觉数学中因粗糙感知导致幻觉级联的问题，提出免标注 RL 框架 UniCAR-RL，将感知与推理解耦为三分支：Caption-RL 以验证器引导提升感知，Reasoning-RL 基于黄金图像描述推理以阻断错误级联，QA-RL 保持原生端到端对齐。仅使用原始短答案数据即提升数学与视觉推理能力，并跨模型架构与规模泛化（EMNLP 2026 Findings）。

### [SyRHM: Symbolic-Language-Enhanced Reasoning with Associative Retrieval for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2609.13794)

**作者**：Hanling Wang, Chenlong Wei, Yingjuan Li ｜ **标签**：理解推理、检索 ｜ **代码**：[Code] https://github.com/Scabbards1500/SyRHM

面向有害梗图中隐晦意图（视觉-文本 incongruity 与文化刻板印象）的零样本检测，SyRHM 先将梗图解析为文本元素与描述并检索语义相关梗图提供语义基础，再把多模态输入翻译为符号中间表示，经规划器与求解器多阶段推理产出可解释的有害意图分析。在 FHM、HarM、MultiOff 上多数设置优于多模态与推理基线（EMNLP 2026）。

### [SHIFT-M3: Pre-fusion Alignment-based Consistency Screening for Multimodal ECG Record Integrity](https://arxiv.org/abs/2609.13874)

**作者**：Md Ashik Khan, Md Nahid Siddique ｜ **标签**：理解推理、检索 ｜ **代码**：[Code]（项目页占位，代码待发布）https://github.com/Anashikforu/Shift-M3

将多模态病历记录完整性筛查形式化为融合前分诊问题：用仅 57.4 万参数的轻量文本筛查器判断 LLM 心电图解读与临床报告摘要是否属于同一患者。在 78 万余条 MEETI 记录上，完整文本视图交换的 TPR@5%FPR 达 97.6%（AUROC 0.996），部分交换 90.3%，标签匹配困难负例 97.7%；主要残余误差来自同患者跨就诊对的纵向歧义（MLHC 2026）。

## 多模态基准与评测

### [AnnoSketch: Evaluating and Collecting Human Sketches for MLLM-assisted Chart Annotation](https://arxiv.org/abs/2609.14289)

**作者**：Yoonjae Oh, Seon Gyeom Kim, Jae Young Choi ｜ **标签**：基准 ｜ **代码**：暂无代码（数据集与材料见 OSF 仓库）

研究粗糙草图输入何时能提升 MLLM 生成的图表注释效果，分析草图在何种图表与标题类型下传递用户意图最有效。发布 AnnoSketch 数据集：来自草图帮助最大条件的 160 个图表-标题对上的 1600 张注释草图，标注意图、感知理解难度、表达局限及视觉标记与标题关联的结构化元数据，阐明「何时应主动引导用户提供草图输入」。

## 多模态检索与信息抽取

### [GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning](https://arxiv.org/abs/2609.14066)

**作者**：Zhongyu Wang ｜ **标签**：检索、Agent ｜ **代码**：暂无代码

针对多智能体 RAG 推理深度不足、存在「状态盲」的问题，提出图记忆引导的多智能体 RAG 框架 GraMRAG：以动态多模态记忆图将推理形式化为动作-观察依赖的动态 DAG，配合视觉-文本桥接的 ReAct 式工具链支持长程跨模态推理，并提出拓扑感知策略优化（TAPO）实现关键路径识别、节点剪枝与细粒度信用分配，在长程多模态推理任务上取得 SOTA。

## Agent 与具身智能

### [VGFM: Expressive Robot Policies via Dense Value Guidance in Flow Matching](https://arxiv.org/abs/2609.14261)

**作者**：Prajwal Koirala, Mark Campbell ｜ **标签**：Agent ｜ **代码**：[Code] https://github.com/PrajwalKoirala/VGFM_Policy

提出离线 RL 方法 VGFM：将策略建模为动作空间的条件流匹配（x-prediction），使每个中间流状态都是可被现成 critic 评分的有效动作，从而无需通过时间反向传播（BPTT）即可在随机流时刻施加稠密价值引导，且推理 ODE 可重新离散化而无需重训。在 OGBench 运动与操作任务上以极少调参取得强性能，是一种简单、可扩展的长程控制方法（IROS 2026）。

## 多模态生成

### [DiVA: Enabling Interactive Digital Life Simulation via Video Models](https://arxiv.org/abs/2609.13830)

**作者**：Cheng Chen, Hao Ouyang, Qiuyu Wang ｜ **标签**：生成、Agent ｜ **代码**：暂无代码（论文承诺发表后公开）

提出深度交互式数字生活模拟器 DiVA：由 MLLM 路由器调度堆叠视频管线，生成多轮动作与音频响应；将生成拆分为等待视频、动作视频及二者过渡，Anchored Video Continuation 模块使角色回到稳定状态以抑制退化与镜头抖动，支持坐姿到站姿等大幅度动作切换，长程真实感优于长视频生成、续写与插值基线。

## 音频多模态

### [AURA: Unified Multimodal Framework for Conversational Music Editing](https://arxiv.org/abs/2609.14344)

**作者**：Quoc-Huy Trinh, Minh-Van Nguyen, Debesh Jha ｜ **标签**：音频、生成 ｜ **代码**：暂无代码

提出对话式音乐编辑框架 AURA：MLLM 读取完整对话历史及可选图像与参考音频，将迭代编辑意图压缩为紧凑概念 token，再由 concept-to-audio 模块将概念与帧对齐参考特征注入冻结的 MusicGen 主干，在精确保留未修改内容的同时执行编辑。仅调优 91M 参数（1.9B 冻结），在 Slakh2100 与 MoisesDB 上编辑正确性与内容保持优于已有指令编辑方法，域外增删操作的 FAD 降低 4-5 倍。

### [ReH-FUSE: Reliability-Aware Hierarchical Fusion of Experts for Multimodal Emotion Recognition in Conversation](https://arxiv.org/abs/2609.13857)

**作者**：Guan-Hua Wen, Hou-Chiang Tseng, Kuan-Yu Chen ｜ **标签**：音频、理解推理 ｜ **代码**：暂无代码

提出对话情感识别的可靠性感知层次化专家融合框架 ReH-FUSE：对话感知文本、音频与跨模态专家配合决策级路由器，先在文本与音频间裁决，再将单模态混合与跨模态专家权衡，解耦单模态竞争与跨模态选择。在 IEMOCAP 上取得 74.34% 加权 F1，MELD 上 68.03%，学到的路由一致优于均匀平均（投稿 ICASSP 2027）。

---

## 统计

- 收录论文总数：**15 篇**（提交日期：2026-09-12 至 2026-09-13）
- 覆盖方向：**7 个**（VLM/MLLM 5 篇、理解与推理 4 篇、基准评测 1 篇、检索与信息抽取 1 篇、Agent 与具身智能 1 篇、生成 1 篇、音频多模态 2 篇）
- 代码可用：**3 篇**（VGFM、UniCAR-RL、SyRHM）；仓库已建但代码待发布：**2 篇**（Hyper-LLaVA、SHIFT-M3）；暂无代码：**10 篇**

> 自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-09-15
