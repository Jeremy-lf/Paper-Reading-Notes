# Arxiv 多模态论文日报 - 2026-07-31

**统计**：共收录 44 篇论文，覆盖 8 个方向，其中 9 篇提供代码仓库。

---

## VLM / MLLM 核心

### [Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2607.28341)

**作者**：Jie Ma, Zhike Qiu, Jie Gao, Jiayi Ji et al. | **标签**：VLM / MLLM | **[Code](https://github.com/JieMaMagic/Trend-aware-Pruning)**

提出一种无需训练的视觉 token 剪枝方法，通过追踪注意力分数在层间的演化趋势，挽救那些在浅层不重要但在深层变得关键的 token。在多个 MLLM 上将视觉 token 减少超过四分之三，同时保持模型性能。

### [Correcting What You Cannot See: Credit Assignment for Perception Distillation in Multimodal Reasoners](https://arxiv.org/abs/2607.28336)

**作者**：Feng Xiong, Leyan Xue, Hongyu Lin | **标签**：VLM / MLLM

提出一种感知蒸馏的信用分配方法，通过两种失败见证诊断学生模型的失败源于感知还是推理，并对感知相关失败样本加权。在多个视觉推理基准上取得平均提升。

### [Scaling Vision-Language Models Is Not Enough to Mitigate Bias](https://arxiv.org/abs/2607.28211)

**作者**：Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos | **标签**：VLM / MLLM | **[Code](https://github.com/gsarridis/vlm-spurious-robustness)**

对 194 个视觉语言模型进行大规模调研，发现单纯扩大规模能提升标准准确率，但无法改善对虚假相关性的鲁棒性；而数据筛选可将对立组准确率最高提升约四分之一。

### [MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware](https://arxiv.org/abs/2607.28006)

**作者**：Xianpeng Zhang, Jiahua Yang, Dongyu Chen, Lei Zhang et al. | **标签**：VLM / MLLM

提出多模态长文档摘要基准与模型，采用视觉对齐与关键词感知的监督微调，结合多目标奖励的 GRPO 训练。在长多模态文档上提升了摘要覆盖度与一致性。

### [LAST: The Last Query Token Guides Visual Token Pruning for Edge-Cloud Collaborative MLLM Inference](https://arxiv.org/abs/2607.27952)

**作者**：Feng Yang, Xinrui Ju, Keyang Zhang, Xiandong Meng et al. | **标签**：VLM / MLLM

提出面向边云协同 MLLM 推理的视觉 token 剪枝方法，利用边缘小模型最后一层查询 token 的注意力作为相关性信号，仅保留少量 token 即可在 11 个基准上保持准确率。

### [One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs](https://arxiv.org/abs/2607.27917)

**作者**：Enyi Shi, Fei Shen, Chuancheng Shi, Linxia Zhu et al. | **标签**：VLM / MLLM

发现视觉语言模型中存在跨语言、跨模态共享的少量安全神经元，通过仅更新这些神经元将英文安全监督迁移到多语言和多模态场景，在保持通用能力的同时提升安全性。

### [A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models](https://arxiv.org/abs/2607.27910)

**作者**：Xiangyu Yin, Tora Bodin, Rohan Menon, Chih-Hong Cheng | **标签**：VLM / MLLM

在 15 个模型-层组合上系统比较 5 种基于方向的推理时防御方法，发现不存在单一最优防御，图像条件偏移对某些架构家族有效，而基于提示的残差对另一些更有效。

### [One Patch Is Enough: Reinforcement-Optimized Visual Token Grounding for MLLM-Based Scene Text Spotting](https://arxiv.org/abs/2607.27902)

**作者**：Rui Tang, Wentao Yang, Peirong Zhang, Yongxin Shi et al. | **标签**：VLM / MLLM

提出面向场景文本检测的 MLLM 视觉 token 定位方法，通过强化学习为每个文本实例选择单一锚点 token，并结合方向解耦嵌入与全图解码进行边界精修。超越领先的闭源与 OCR 专用模型。

### [FedOGL: Combating Catastrophic Forgetting in Federated Open-World Multimodal Graph Learning](https://arxiv.org/abs/2607.27665)

**作者**：Zekai Chen, Haodong Lu, Shihao Li, Weiwei Ji et al. | **标签**：VLM / MLLM

提出联邦开放世界多模态图学习框架，通过客户端回放与蒸馏保留历史知识，服务器端原型迁移实现跨客户端知识共享。在多个基准上将灾难性遗忘降低超过 40%。

### [Regularizing modality contribution drift in multimodal continual learning](https://arxiv.org/abs/2607.27260)

**作者**：Zhen Zhang, Jielei Chu, Bin Liu, Tianrui Li | **标签**：VLM / MLLM

定义模态贡献漂移并提出正则化方法，稳定各模态在持续学习任务中的决策贡献。在类增量学习和持续视觉问答任务上验证了回放式与无回放变体的有效性。

### [Progressive Multimodal Alignment for Continual Instruction Tuning](https://arxiv.org/abs/2607.26947)

**作者**：Duzhen Zhang, Yahan Yu, Qiaoyi Su, Jiahua Dong, Tielin Zhang | **标签**：VLM / MLLM | **[Code](https://github.com/BladeDancer957/PMA)**

提出持续指令微调中的渐进式多模态对齐方法，仅在检测到分布偏移时扩展投影器专家，并将原始预训练投影器作为稳定锚点。在多模态持续学习基准上取得提升。

### [Understanding Knowledge Transfer Mechanism in Heterogeneous MLLM Fusion: A Simple Linear Approach](https://arxiv.org/abs/2607.26608)

**作者**：Yinghao Hou, Jiahe Fan, Yuanhao Pu, Zongyuan Chen, Hong Xie | **标签**：VLM / MLLM

用线性探针分析异构 MLLM 融合中的跨尺度知识迁移，发现增益主要集中在高层推理而非感知，主要来自语言模型侧，且在较小注入比例下即可显现。

### [Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution](https://arxiv.org/abs/2607.26596)

**作者**：Mingkuan Feng, Zhengqi Wen, Jianhua Tao | **标签**：VLM / MLLM

提出参数高效的多模态适配方法，将 LLM 上层解码器替换为仅处理视觉 token 的单个可训练 Transformer 块。在 LLaVA-1.5 上以远少于全量微调的可训练参数取得竞争性能。

---

## 多模态理解与推理

### [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595)

**作者**：Qixun Wang, Yang Shi, Letian Cheng, Zhuoran Zhang et al. | **标签**：推理 | **[Code](https://github.com/NOVAglow646/Beacon)**

提出视觉推理代理 Beacon，学习何时真正需要调用外部工具以及如何有效使用它们，通过必要性与能力扩展奖励进行训练。在多个基准上提升整体准确率并实现工具使用的真实增益。

### [VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy Distillation](https://arxiv.org/abs/2607.28590)

**作者**：Kangning Zhang, Yixing Li, Shuai Shao, Qingyao Li et al. | **标签**：推理 | **[Code](https://github.com/DeepExperience/VAD_Multimodal_OPD)**

提出反事实视觉证据归因方法，估计教师模型修正中有多少来自视觉证据，并构建以学生为中心的监督目标。在多个视觉基准上优于直接特权视图蒸馏。

### [HyperClaim: Fine-Grained Cross-Modal Hypergraph Reasoning for Video Misinformation Detection](https://arxiv.org/abs/2607.28375)

**作者**：Xiangbo Wang, Jiasheng Zhang, Xingtong Yu, Luoqiang Lei, Delvin Ce Zhang | **标签**：推理

提出基于超图的视频虚假声明检测器，建模查询短语、文本证据与视频帧之间的高阶交互，并聚合文本、视觉与超边状态。在三个短视频基准上取得高精度的检测效果。

### [RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning](https://arxiv.org/abs/2607.28156)

**作者**：Jingxiang Fan, Junbao Zhuo, Bochao Zou | **标签**：推理

面向长视频推理，提出反思式检索记忆方法，将历史任务中的检索经验蒸馏为多模态记忆图的查询级指导，并通过生命周期管理降低噪声与冗余。

### [OPLD: On-Policy Latent Distillation for Multimodal Reasoning](https://arxiv.org/abs/2607.28154)

**作者**：Shoutai Zhu, Tianyang Xu, Bin Sun, Mingyuan Xu et al. | **标签**：推理

提出 on-policy 隐式蒸馏框架，将特权思维链演示的推理过程迁移为连续隐状态，超越传统仅对齐压缩视觉特征的方式。在视觉推理基准上取得强表现。

### [Thinking Once Is Enough: Intermediate-Layer Evidence Routing for High-Resolution VQA](https://arxiv.org/abs/2607.27830)

**作者**：Zhongkuan Mao, Xianjie Liu, Tianyu Meng, Yidong Wang et al. | **标签**：推理

提出无需训练的单次前向高分辨率视觉问答方法，从中间层路由细粒度视觉证据，保留关键实体与背景上下文。在提升基准分数的同时降低内存与推理时间。

### [Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications](https://arxiv.org/abs/2607.27145)

**作者**：Piyush Jain, Kousik Dasgupta, Rajarshi Roy, Subarna Tripathi | **标签**：推理

提出面向关键决策应用的可解释且资源高效的空间推理框架，通过开放词汇检测器提取成对物体关系，并将其作为结构化证据注入基于深度提示的 MLLM。在 VSR 和 BLINK 上取得大幅提升，轻量版本可在 CPU 40 token 预算内运行。

### [Visual Credit Audit for Multimodal Spatial Reasoning](https://arxiv.org/abs/2607.27066)

**作者**：Feixiang Liu, Qiang Qiu, Lanbo Sun, Nan Wei, Huawei Shen, Xueqi Cheng | **标签**：推理

提出视觉信用审计方法，区分多模态空间推理中图像真正支持的决策与幸运猜测。实验显示 12.73%-26.25% 的正确回答实际上缺乏视觉证据支持。

---

## 多模态基准与评测

### [PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?](https://arxiv.org/abs/2607.28318)

**作者**：Zongyi Chen, Yu Liang, Jie Lin, Liansheng Wang | **标签**：基准

构建病理图像细粒度多尺度理解基准，包含来自 23 个公开数据集的 14 项问答任务、6.1 万张图像和 30.8 万样本。评估显示当前最先进的 MLLM 在多项任务上仍面临挑战。

### [MMHBench: A Multi-Perspective Benchmark for Mental Health Understanding in Long-Form Videos](https://arxiv.org/abs/2607.27895)

**作者**：Jinpeng Hu, Erqiang Wang, Shan Wang, Zhuo Li et al. | **标签**：基准

提出长视频心理健康理解基准，包含 260 多个视频和 2100 个问题，涵盖第三方行为评估与第一人称视角推理。22 个 MLLM 的评估表明该任务仍极具挑战性。

### [LoMeVQA: A Comprehensive Benchmark for Longitudinal Medical VQA](https://arxiv.org/abs/2607.27806)

**作者**：Zhilin Wu, Zhangkai Ni, Chengmei Yang, Longzhen Yang et al. | **标签**：基准 | **[Code](https://github.com/pepperbubble/LoMeVQA)**

提出纵向医学 VQA 基准，包含 20 多万问答对，覆盖 5 项时序图像分析任务。通用与医学 MLLM 表现均较差，专用模型创下新高。

### [MMOOC: A Comprehensive Benchmark for Out-of-Context Evaluation in Multimodal Large Language Models](https://arxiv.org/abs/2607.27637)

**作者**：Wenjie Zhu, Yabin Zhang, Wenjun Zeng, Lei Zhang | **标签**：基准 | **[Code](https://github.com/ZhuWenjie98/MMOOC)**

构建大规模 MLLM 上下文外行为基准，包含 4.1 万多图像-问题对，覆盖可回答的上下文偏移与不可回答的上下文外情况。当前模型难以平衡正确回答与适当拒绝。

### [AHA-Memes: A Fine-Grained Multimodal Benchmark for Understanding Hate in Arabic Memes](https://arxiv.org/abs/2607.27393)

**作者**：Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Abul Hasnat et al. | **标签**：基准 | **[Code](https://github.com/MohamedBayan/AHA-Memes)**

发布阿拉伯仇恨表情包细粒度多模态基准，含 5000 人工标注和 6.6 万银标样本。评估文本、图像、晚融合、少样本和视觉语言模型，揭示文化背景下的分析挑战。

### [See2Think: Do Multimodal Models Really Use Intermediate Visual States?](https://arxiv.org/abs/2607.26769)

**作者**：Siyu Yan, Zhuoran Yan, Haiying Xu, Panhao Zhou et al. | **标签**：基准

提出评估 MLLM 是否真正依赖中间视觉状态的基准与过程评估协议。发现渲染保真度是主要瓶颈，视觉反馈受损时准确率显著下降。

### [MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning](https://arxiv.org/abs/2607.26460)

**作者**：Kawai Chung, Chunkit Chan, Yauwai Yim, Yuxuan Liu et al. | **标签**：基准

构建故事驱动视觉叙事中的动机推理基准，基于心理学理论框架。测试显示当前多模态模型难以在序列上下文中保持一致的动机推理。

---

## 多模态检索与信息抽取

### [DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2607.28580)

**作者**：Jiacheng Tao, Qingyun Sun, Haonan Yuan, Ziwei Zhang, Jianxin Li | **标签**：检索

提出双层图框架分离全局文档推理与细粒度证据验证，使用图神经网络检索器与路径解码。在复杂多跳问题的检索召回与回答质量上均取得提升。

### [VIG-RL: Learning to Search and Insert for Verified Image Grounding](https://arxiv.org/abs/2607.28055)

**作者**：Qinhan Yu, Jun Guang, Chong Chen, Wentao Zhang | **标签**：检索

将图像搜索、选择与插入视为推理循环中的序列决策，通过强化学习奖励逐步工具使用与最终图文对齐。超越静态检索基线。

### [FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval](https://arxiv.org/abs/2607.27959)

**作者**：Bohan Hou, Haoqiang Lin, Xuemeng Song, Haokun Wen et al. | **标签**：检索

构建细粒度多模态五元组数据并设计两阶段 MLLM 调优策略，先教授上下文理解再优化查询-目标对齐。在 5 个数据集上实现显著零样本检索提升。

### [SciFigAlign: Scoring Scientific Figures by Fine-tuned Alignment of Visuals with Manuscript Evidence](https://arxiv.org/abs/2607.27017)

**作者**：Chuanzhi Xu, Zihan Deng, Huiqi Liang, Chengkun Yue et al. | **标签**：检索

提出科学图表质量评估数据集与多模态评分器，通过将图表内容锚定到手稿上下文来评估质量。微调 CLIP 与 SciBERT 后，错误率显著低于 LLM-as-judge 基线。

---

## Agent 与具身智能

### [FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2607.28596)

**作者**：Lifeng Zhuo, Wendi Chen, Han Xue, Shirun Tang et al. | **标签**：Agent

提出频率自适应反应式扩散操作策略，在剧集中动态选择多步低频采样或单步高频采样，并引入尊重机器人动作几何的损失。在接触丰富的操作任务中提升成功率并保留多样化预接触选项。

### [LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger](https://arxiv.org/abs/2607.28374)

**作者**：Enjun Du, Hange Zhou, Chenxu Du, Siyi Liu et al. | **标签**：Agent

提出结构化证据账本的多模态代理推理框架，将工具输出记录为可溯源条目，并通过类型化修复转换与多层 grounding 约束下游声明。提升最终准确率与轨迹忠实度。

### [FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification](https://arxiv.org/abs/2607.28225)

**作者**：Haoqing Wang, Xingrun Xing, Wei Xia, Ziheng Li, Yehui Tang | **标签**：Agent

提出多智能体框架判断视觉工具产生的中间图像是否有用，并将判断反馈到推理过程中。模型可在推理时自主评估工具调用，提升准确率与工具使用忠实度。

### [MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation](https://arxiv.org/abs/2607.27967)

**作者**：Dawei Wang, Di Zhao, Xinyuan Liu, Marci Chi Ma et al. | **标签**：Agent

将多智能体协作中的信用分配建模为基于大多模态模型成对比较的排序聚合任务，并将排名转换为贡献型奖励调整。在具身协作任务中促进有效合作。

### [RLMM-Flow: A Flow-based Mobile Manipulation Framework with Latent-Space Reinforcement Learning](https://arxiv.org/abs/2607.26452)

**作者**：Shuhang Wang, Ziming Li, Hui Cheng | **标签**：Agent

结合基于流的演示预训练策略与隐空间强化学习，实现全身移动操作。通过 critic 预热与粗到细的隐空间引导提升成功率、避障能力与轨迹质量，同时保持快速推理。

---

## 多模态生成

### [Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611)

**作者**：Chongjian Ge, Hanwen Jiang, Tianyu Wang, Jiuxiang Gu et al. | **标签**：生成

提出混合视觉生成架构 Chimera，将文本、图像与视频 token 统一处理，结合高效注意力、卷积与稀疏专家，并给出跨宽度和深度迁移超参数的缩放配方。训练了 110 亿参数模型并评估效率、视频外推与缩放规律。

### [RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation](https://arxiv.org/abs/2607.27699)

**作者**：Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan et al. | **标签**：生成 | **[Code](https://github.com/liuxiaobo66/RefineSVG)**

提出基于视觉反馈的 MLLM 图像转 SVG 生成框架，初始生成后将 SVG 渲染并与目标图像对比产生残差图，指导修正步骤。同时引入 SVG 专用语义词汇与渐进式训练流程。

---

## 音频多模态

### [Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents](https://arxiv.org/abs/2607.28165)

**作者**：Mingxiao Liu, Yitong Li, Haoren Zhao, Yaoxiang Bian et al. | **标签**：音频 | **[Code](https://github.com/Limax666/AudioAgentSecurity)**

展示可将隐藏音频指令嵌入环境声音以劫持多模态智能体，并构建多场景与攻击模式的基准。基于声源分离与跨模态一致性的防御机制可检测大部分注入攻击。

### [DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation](https://arxiv.org/abs/2607.27614)

**作者**：Hongbin Zhang, Junhao Liu, Xuefeng Bai, Youcheng Pan et al. | **标签**：音频

提出无词 Gloss 的手语翻译框架，通过两种锚定机制将多模态解码器约束到冻结 LLM 的下一 token 分布，并使用最优传输实现软视觉-文本对齐。在 PHOENIX-2014T 和 CSL-Daily 上取得强结果。

### [SKY-Piano: A Multimodal Piano Performance Dataset](https://arxiv.org/abs/2607.27296)

**作者**：Joonhyung Bae, Dawon Park, Taegyun Kwon, Yoon-Seok Choi et al. | **标签**：音频 | **[Project Page](https://joonhyungbae.github.io/skypiano/)**

发布多模态钢琴演奏数据集 SKY-Piano，包含 11 小时专业与业余演奏者的动作捕捉、多视角视频、音频、MIDI 与 MusicXML 乐谱。提供处理后的动作数据、交互式浏览器与指法标注工具。

---

## 3D 视觉语言

### [IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD](https://arxiv.org/abs/2607.28050)

**作者**：Nianchen Deng, Jiaxin Ai, Tao Hu, Shu Zou et al. | **标签**：3D

面向工业 CAD 领域，微调 270 亿参数多模态基础模型，使其能够阅读工程图纸与 3D 视图并生成参数化建模脚本与 COM 自动化代码。在 CAD 基准上超越强闭源模型且未遗忘通用能力。

### [SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM](https://arxiv.org/abs/2607.26595)

**作者**：Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao | **标签**：3D

提出基于 MLLM 的 3D Gaussian Splatting 场景质量评估框架 SpatialQ，从多视图图像、深度与点云学习 3D 感知质量特征，并使用 Qwen-based MLLM 进行可解释的质量推理。

---

**论文总数统计**：本报告共收录 44 篇论文，其中 VLM / MLLM 核心 13 篇、多模态理解与推理 8 篇、多模态基准与评测 7 篇、多模态检索与信息抽取 4 篇、Agent 与具身智能 5 篇、多模态生成 2 篇、音频多模态 3 篇、3D 视觉语言 2 篇。含代码仓库 9 篇。
