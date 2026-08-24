# Arxiv 多模态论文日报 - 2026-08-23

**统计**：收录论文 23 篇，含代码仓库 7 篇。

## VLM/MLLM 核心

### [Projector Is All You Train](https://arxiv.org/abs/2608.19726)

**作者**：Nyx Iskandar,Saathvik Selvan,Slater Victoroff | **方向**：VLM/MLLM 核心

本文探讨了仅训练 projector 而冻结 MLLM 其他组件的可行性。研究发现，projector-only training 在大幅降低计算成本的同时，可达到与端到端微调相当的性能。这一发现挑战了视觉-语言对齐必须进行全模型微调的传统认知。

### [PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment](https://arxiv.org/abs/2608.19598)

**作者**：Jiawei Feng, Jiancan Wu, Xingyu Zhu et al. | **方向**：VLM/MLLM 核心

本文提出 PEA-DPO，将视觉感知信号引入 DPO 以改善 MLLM 的对齐效果。该方法通过增强视觉内容与文本偏好之间的感知对齐，同时提升感知保真度与生成质量。实验验证了 PEA-DPO 在 MLLM 对齐任务上的有效性。

### [When Irrelevant Text Matters: Affine Margin Shifts inMultimodalLarge Language Models](https://arxiv.org/abs/2608.19208)

**作者**：Yinfeng Wang, Zhiyuan Yao, Zheren Fu et al. | **方向**：VLM/MLLM 核心 | **[Code](https://github.com/Wangyf1998/Irrelevant_Text_Matters)**

本文揭示了 MLLM 中无关文本引起的 affine margin shifts 现象。研究发现，即使文本不提供有效视觉信息，也可能系统性地影响模型在视觉 grounding 任务中的决策。该分析为提升 MLLM 抵抗文本干扰的鲁棒性提供了重要洞察。

### [Breaking the weakest link to evade vision language models](https://arxiv.org/abs/2608.18938)

**作者**：Ilan Zini,Boussad Addad,Katarzyna Kapusta | **方向**：VLM/MLLM 核心

本文研究针对 VLM 的对抗攻击，通过识别并攻击其最弱的感知或语言链路实现逃逸。研究表明，对脆弱模态施加微小扰动即可导致模型灾难性失败。该发现强调需要提升 VLM 跨模态的均衡鲁棒性。

## 多模态理解与推理

### [Rule-Compliant Visual Spatial Planning forMultimodalLarge Language Models](https://arxiv.org/abs/2608.20237)

**作者**：Yu Chen, Ting Lei, Yaoyi Li et al. | **方向**：多模态理解与推理 | **[Code](https://github.com/oceanflowlab/RuleMaze)**

本文提出 RuleMaze 基准，用于评估 MLLM 在显式规则约束下的视觉空间规划能力。该任务要求模型在视觉迷宫中规划路径，并遵守组合规则（如先访问红色物体再访问蓝色物体、避开特定区域）。实验表明，当前最先进的 MLLM 在规则组合与长程规划方面仍存在明显不足，亟需针对性的训练机制。

### [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](https://arxiv.org/abs/2608.20122)

**作者**：Linhan Cao, Siyuan Li, Jun Lan et al. | **方向**：多模态理解与推理 | **[Code](https://github.com/ant-research/ArmorOCR)**

本文提出 ArmorOCR 框架，通过 observation-transferred self-distillation 提升 LMM 对抗性视觉文本的鲁棒性。训练过程中将干净场景的观察迁移到对抗场景，从而在抵御对抗攻击的同时保持对干净输入的识别性能。实验显示，ArmorOCR 在对抗 OCR 任务上显著提升了准确率。

### [Contrastive Mixed Prompt Learning for IncompleteMultimodalSentiment Analysis with Unseen Modality Combination](https://arxiv.org/abs/2608.20019)

**作者**：Kaixin Xu, NaiJin Liu, Yulin Kang et al. | **方向**：多模态理解与推理

本文提出对比混合提示学习框架，用于处理不完全多模态情感分析中的未见模态组合问题。该方法通过 mixed prompt tokens 与对比对齐学习模态无关表示，能够适应任意缺失模态模式。实验验证了其在随机缺失及未见模态组合场景下的泛化能力。

### [Robust IncompleteMultimodalSentiment Analysis via Iterative Proxy Correction](https://arxiv.org/abs/2608.19971)

**作者**：Zhifa Geng, Subin Huang, Hao Guo et al. | **方向**：多模态理解与推理

本文提出迭代式代理修正机制，联合处理多模态情感分析中的模态缺失与标签噪声问题。通过逐步精化的伪标签，该方法在不完全监督条件下实现了更稳健的情感预测。实验表明其在真实不完美数据上具有更强的鲁棒性。

### [Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization forMultimodalSarcasm Detection](https://arxiv.org/abs/2608.19942)

**作者**：Hao Guo, Subin Huang, Junjie Chen et al. | **方向**：多模态理解与推理

本文提出动态门控跨模态融合结合讽刺感知对比正则化方法，用于多模态讽刺检测。该方法自适应地为语言、视觉和声学模态分配权重，并通过对比学习拉近讽刺样本、推远非讽刺样本。实验表明其能更好捕捉模态间的动态矛盾关系。

### [Question-Guided Evidence Acquisition forMultimodalVisual Question Answering](https://arxiv.org/abs/2608.19739)

**作者**：Alin-Ionut Popa | **方向**：多模态理解与推理

本文提出问题引导的证据获取方法，用于增强多模态视觉问答中文档理解能力。该方法根据问题主动检索并聚合文档中的视觉证据，以应对小字、表格、视觉线索和拓扑结构等复杂元素。实验表明其在结构化及视觉丰富文档上的推理能力显著提升。

### [Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions](https://arxiv.org/abs/2608.19710)

**作者**：Mohammad Arif Ul Alam | **方向**：多模态理解与推理

本文研究了水下机器人在退化视觉条件下的鲁棒跨模态基础模型感知。通过构建从清洁到极端条件的五级基准，比较了传统检测、冻结基础特征与微调多模态模型的表现。结果表明，跨模态基础模型在视觉退化环境下比单模态基线更稳健。

### [GRACE: Grounded Reasoning via Adapter Composition and Evidence-Aware Calibration for Educational Visual Question Answering](https://arxiv.org/abs/2608.19355)

**作者**：Xinjin Li, Yudi Xia, Xi Zhao et al. | **方向**：多模态理解与推理

本文提出 GRACE 框架，用于教育视觉问答中的 grounded reasoning。该方法通过 adapter composition 与 evidence-aware calibration，将推理建立在相关图像区域上，并减少对语言捷径的依赖。实验提升了教育 VQA 基准上的鲁棒性与可解释性。

### [MedUAG: Unified Understanding and Generation for MedicalMultimodalModels](https://arxiv.org/abs/2608.18937)

**作者**：Zijie Meng, Yuncheng Zhang, Hualiang Wang et al. | **方向**：多模态理解与推理

本文提出 MedUAG，面向医学多模态数据的统一理解与生成模型。该模型同时支持诊断推理以及医学图像/报告生成，以应对医疗领域对事实准确性与专业知识的高要求。研究为医学 MLLM 的 UAG 框架发展提供了新方向。

## 多模态基准与评测

### [Holtercare-Bench: AMultimodalBenchmark for Evaluating Long-Term Dynamic ECG Analysis](https://arxiv.org/abs/2608.19297)

**作者**：Yihan Xie, Hanwen Cui, Runze Ye et al. | **方向**：多模态基准与评测 | **[Code](https://github.com/ZJU4HealthCare/Holtercare-Bench)**

本文提出 Holtercare-Bench，用于评估 MLLM 在长期动态心电图分析中的能力。该基准提供标准化任务与指标，填补了对扩展时间序列临床理解评估的空白。研究为 MLLM 在动态心电监测领域的应用提供了系统评测框架。

### [Compliance, Capability, and Conflict: BenchmarkingMultimodalLLMs under System Messages](https://arxiv.org/abs/2608.19207)

**作者**：Juan Yeo,Geewook Kim | **方向**：多模态基准与评测

本文提出一个系统评估 MLLM 在 system message 下表现的基准。该基准从指令遵循、基础能力与安全冲突三个维度出发，系统暴露模型失败模式。研究旨在为 MLLM 的安全部署提供指导。

### [SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701)

**作者**：Bowen Jing, Mingxin Wang, Ruiyang Hao et al. | **方向**：多模态基准与评测 | **[Code](https://github.com/TuojingAI/SoftVTBench)**

本文提出 SoftVTBench，一个面向可形变物体操作的形变感知视触觉数据集与基准。该基准捕捉交互过程中的同步视觉与触觉信号，用于评估形变物体操作。实验表明触觉信息的引入能提升操作性能，但收益在分布内与分布外场景中有所不同。

### [Aslema at NADI 2026: Augmentation through Fewshot for SLU](https://arxiv.org/abs/2608.18689)

**作者**：Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury et al. | **方向**：多模态基准与评测 | **[Code](https://github.com/hunzed/aslema_nadi2026)**

本文介绍 Aslema 系统，参与 NADI 2026 共享任务 5 的意图识别与槽位填充。研究评估了四种 omnimodal 模型，并探索了 few-shot augmentation 在低资源阿拉伯语口语语言理解（SLU）中的应用。实验结果表明 few-shot 增强策略在该任务上具有有效性。

## 多模态检索与信息抽取

### [Time-Series Retrieval for GroundingMultimodalLanguage Models in Remaining Useful Life](https://arxiv.org/abs/2608.19218)

**作者**：Valeriu Dimidov,Raphaël Frank | **方向**：多模态检索与信息抽取

本文研究如何将多模态语言模型 grounded 于剩余使用寿命（RUL）估计任务。通过 time-series retrieval，模型能够访问历史退化模式，从而提升 RUL 预测的准确性与可解释性。实验表明基于检索的 grounding 对 PHM 任务具有实用价值。

## Agent 与具身智能

### [Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents](https://arxiv.org/abs/2608.19794)

**作者**：Fujiang Yuan, Xia Huang, Lusheng Wang et al. | **方向**：Agent 与具身智能

本文综述了通用具身智能的新兴范式，重点探讨如何整合 LLM、知识库与推理机制以构建下一代 AI agent。文章梳理了感知-动作接地、混合符号-神经网络推理、持续学习与安全人机交互等关键挑战。最后给出了发展通用具身代理的综合路线图与开放问题。

### [DentAgent: Evidence-Centric Multi-Agent Coordination forMultimodalDental Reasoning](https://arxiv.org/abs/2608.18878)

**作者**：Zijie Meng, Xiwei Dai, Yixuan Tang et al. | **方向**：Agent 与具身智能

本文提出 DentAgent，一种面向多模态牙科推理的以证据为中心的多智能体协同框架。不同专业 agent 分别处理多种影像模态并协作聚合证据，从而实现多标签诊断。实验显示该系统在多标签牙科诊断上超越了资深专家。

## 多模态生成

### [From Latent Influence to Language: Diffusion-Oriented Content Generation via Audience-Susceptible Features](https://arxiv.org/abs/2608.19809)

**作者**：Jiaying Lei, Shengqi Dang, Runqian Bai et al. | **方向**：多模态生成

本文提出面向扩散的内容生成框架，利用从潜在影响力动态中学习到的 audience-susceptible features 指导生成。通过将内容生成与这些特征条件化，模型能够生成更易于在目标受众网络中传播的多模态内容。该方法为社交媒体广告与品牌营销提供了新的生成策略。

### [Diffusion Models for High-Dimensional Clustered Data: Intrinsic-Dimension Adaptivity via Bayesian Classification](https://arxiv.org/abs/2608.19067)

**作者**：Yuga Iguchi,Paul Fearnhead | **方向**：多模态生成 | **[Code](https://github.com/YugaIgu/diffusion_models_phase_transition)**

本文研究扩散模型在高维聚类数据上的行为，通过贝叶斯分类刻画其对内在维度的自适应性。分析揭示了去噪过程中存在的相变现象，并指出如何利用低维流形结构设计更高效的模型。

## 音频多模态

### [DAVSS: Distilled Audio-Visual State Space Models](https://arxiv.org/abs/2608.19523)

**作者**：Saurabhchand Bhati, Mrudula Athi, Amit S. Chhetri et al. | **方向**：音频多模态

本文将 Transformer-SSM 知识蒸馏范式拓展到视听学习，提出 Distilled Audio-Visual State Space Models（DAVSS）。DAVSS 在保持与 Transformer 相当性能的同时，显著降低了计算开销。实验表明其在视听理解任务上兼具高效性与竞争力。

---

**论文总数**：23 篇
