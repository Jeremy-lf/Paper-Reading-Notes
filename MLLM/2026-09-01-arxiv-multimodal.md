# Arxiv 多模态论文日报 - 2026-09-01

**日期**：2026 年 9 月 1 日  
**收录论文**：17 篇  
**含代码仓库**：6 篇  
**覆盖方向**：6 个

---

## VLM / MLLM

### [Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs](https://arxiv.org/abs/2608.28383)

**作者**：Chenhong He, Lei Li, Shicheng Li, Hanglong Lv, Lingpeng Kong, Qi Liu, Tong Yang, Shuhuai Ren  
**方向标签**：VLM / MLLM  
**代码状态**：暂无代码

本文提出语义头 specialization（SHS）现象：多模态 LLM 中的 ViT 注意力头会自发分化为关注前景对象与关注背景的两类。作者据此设计 SHS-Index 量化该现象，并提出 Ariadne Attention 混合注意力机制，在 22 项图像与视频任务上达到与全注意力相当的性能，同时将注意力计算量降低 6.5 倍。

### [AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2608.28312)

**作者**：Wonjun Lee, Jaehyuk Jang, Kangwook Ko, Hee-Seon Kim, Changick Kim  
**方向标签**：VLM / MLLM  
**代码状态**：暂无代码

针对多模态大语言模型中的身份知识遗忘问题，本文提出 AIM 方法。该方法在保留图像不可用时，通过通用视觉提示锚定遗忘目标，并基于 Fisher 约束对齐视觉编码器，在有效移除目标身份知识的同时，保护非删除身份、先验知识与视觉感知能力。

### [Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance](https://arxiv.org/abs/2608.28218)

**作者**：Jiazhao Liang, Hao Huang, Shuaihang Yuan, Congcong Wen, Geeta Chandra Raju Bethala, Giles Hamilton-Fletcher, Yu Hao, John-Ross Rizzo, Mengyu Wang, Anthony Tzes, Yi Fang  
**方向标签**：VLM / MLLM  
**代码状态**：[Code](https://github.com/topo-focus/Topofocus)

本文面向低视力辅助场景，提出基于显著性的视觉语言模型 Salience-LLaVA，能够按重要性排序生成描述内容。作者构建了三个显著性感知数据集，并提出 SCMI 指标评估描述顺序，最终在辅助眼镜上完成部署验证。

### [Token-Budget Distillation: Transferring Full-Token Semantics to Compressed Video Vision-Language Models](https://arxiv.org/abs/2608.28138)

**作者**：Xiaoyang Guo, Guoping Luo, Jusheng Zhang, Keze Wang, Wenhao Wang  
**方向标签**：VLM / MLLM  
**代码状态**：暂无代码

本文提出 Token-Budget Distillation（TBD），通过双路师生框架将完整 token 的视觉语义迁移到压缩后的视频视觉语言模型。该方法仅训练 LoRA 适配器，在三种视频 VLM 骨干和四个基准上验证，可在显著压缩 token 的同时保持接近全 token 的准确率。

### [Visual Token Coding for Video Multimodal Large Language Models](https://arxiv.org/abs/2608.28008)

**作者**：Chenxin Fang, Tao Chen, JunChao You, Jun Peng, Yiyi Zhou, Rongrong Ji  
**方向标签**：VLM / MLLM  
**代码状态**：[Code](https://github.com/Msr233/VTC)

本文提出 Visual Token Coding（VTC），借鉴视频编码思想对视频 MLLM 的视觉 token 进行压缩。通过预测 I/P 帧与帧间残差来估计 token 冗余，VTC_Dy 版本在 Qwen3-VL 上于 50% token 预算时保持 100.1% 平均性能，25% 预算时保持 97.8%，且无需微调模型。

---

## 多模态理解与推理

### [Post-Training VLMs for Video Mistake Detection](https://arxiv.org/abs/2608.28406)

**作者**：Federico Spurio, Olga Zatsarynna, Lars Doorenbos, Emad Bahrami, Gianpiero Francesca, Juergen Gall  
**方向标签**：推理  
**代码状态**：[Code](https://github.com/FedeSpu/mstk)

本文针对教学视频中步骤执行错误的检测问题，提出 MD-VQA 基准与视频语言模型的后训练方法。通过自定义奖励强化指令与视频之间的不匹配信号，使模型学习更泛化的错误概念而非记忆具体步骤，在未见过的新流程上表现更优。

### [Conditional Visual Evidence Utility: State-Dependent Rank Reversals in Frozen Vision-Language Encoders](https://arxiv.org/abs/2608.28316)

**作者**：Yunxuan Fang, Xinhe Wang  
**方向标签**：推理  
**代码状态**：暂无代码

本文研究视觉证据的价值如何随已观察信息动态变化。在结构化的搜索任务中，作者发现冻结的 OpenCLIP 与 SigLIP 编码器会出现可靠的条件性排序反转，表明证据价值应被动态评估，而非使用固定排序。

### [Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2608.28058)

**作者**：Kairong Yu, Zixin Zhu, Le Yu, Hongwei Wang  
**方向标签**：推理  
**代码状态**：暂无代码

本文提出 Dynamic Alignment Compensation（DAC），一种无需训练的推理时幻觉缓解方法。DAC 检测跨模态表示在解码层与生成步之间的漂移，并通过层级语义补偿与序列语义修正进行轻量级残差补偿，在九个基准上有效降低幻觉且不损害整体性能。

---

## 多模态基准与评测

### [SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions](https://arxiv.org/abs/2608.29607)

**作者**：Zirong Chen, Fuda Ye, Kuan Zhang, Enjun Du, Junfu Pu, Xinlei Wang, Xinyu Zuo, Lisheng Duan, Jin Ma, Yongqi Zhang  
**方向标签**：基准  
**代码状态**：暂无代码

本文提出首个面向移动端"拍照即问"场景的多模态检索鲁棒性基准 SnapBench，包含 1145 条查询与在 53 种受控扰动下的 9085 个图库样本。实验发现图像损坏会显著降低检索质量，而文本噪声主要影响纯文本搜索；仅使用清晰图像往往优于图文融合，揭示了粗粒度文本拖累与跨模态回退缺失问题。作者进一步提出自适应融合方法 MOOR。

### [MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places](https://arxiv.org/abs/2608.28384)

**作者**：Jason Armitage, Ioannis Tsochantaridis, Linda Mazzone, Chuqiao Yan, Srini Narayanan, Sarah Ebling  
**方向标签**：基准  
**代码状态**：暂无代码

MAP 是首个评估多模态 AI 系统作为无障碍出行助手的基准，包含两项任务：验证地点的无障碍声明是否属实，并为指定需求检索对应的视觉证据。该基准支持随真实世界数据变化定期刷新，并结合自动评分与人工评价。

---

## Agent 与具身智能

### [𝒩₀-Foundation: Towards the Age of Tactile Intelligence](https://arxiv.org/abs/2608.29601)

**作者**：NeoteAI Team, Fudan TEAI Team  
**方向标签**：Agent  
**代码状态**：[Code](https://github.com/neoteai/N0-Foundation)

本文提出触觉驱动的机器人操作范式 𝒩₀-Foundation，构建覆盖超过 3 万小时视觉-触觉演示的 NeoData 数据集，并提供 5000 小时公开子集 OpenNeoData。学习得到的跨传感器触觉表示模型 NeoForce 与真实/仿真测试套件 NeoReal、NeoSim 共同验证：策略受益于物理接触状态而非触觉信号的特定设备外观。

### [AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction](https://arxiv.org/abs/2608.28491)

**作者**：Yafei Zhang, Nan Wu  
**方向标签**：Agent  
**代码状态**：暂无代码

本文提出轻量化的文本辅助机器人视频动作模型，将未来预测解耦为以对象为中心的运动与稠密外观。通过冻结的 SAM3-DLP 编码器将上下文帧转换为语义粒子，再用 0.28M 参数的时空 Transformer 预测粒子未来状态，最终解码生成未来帧，在 VRS 基准上相比 persistence 基线降低轨迹误差 21.0%。

### [RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents](https://arxiv.org/abs/2608.28399)

**作者**：Yupeng Zhang, Liuyuan Jiang, Hongyi Huang, Bingheng Li, Lisha Chen  
**方向标签**：Agent  
**代码状态**：暂无代码

本文研究多模态 LLM 交易代理的序列决策是否存在可被市场参与者利用的方向性结构。RetailAgent 让 LLM 基于日内股价历史与状态反复选择持仓或空仓，暴露匹配后的收益显示存在持续负向择时；自生成记忆会增强策略持续性并加剧该现象。

### [WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents](https://arxiv.org/abs/2608.28062)

**作者**：Zongkai Liu, Hui Zhang, Liqiang Niu, Zhen Cao, Han Li, Juntao Liu, Wenchao Chen, Chengduo Zhao, Chao Yu, Fandong Meng  
**方向标签**：Agent，检索  
**代码状态**：暂无代码

本文提出 WeAgent-Harness 多模态代理框架，支持原生文本-视觉交互与运行时恢复；并构建 WeAgent-MMSearch 系统，涵盖数据构建、代理后训练与多模态 rollout。检索到的图像以持久化磁盘引用形式保留，便于模型在轨迹中反复查看与引用。在 VisTarget-Bench 等基准上，代理后训练平均提升 19.22 分。

---

## 3D 视觉语言

### [InstructMesh: Selective Refinement of Generative 3D Models for Fabrication](https://arxiv.org/abs/2608.28534)

**作者**：Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller  
**方向标签**：3D  
**代码状态**：暂无代码

InstructMesh 是一款交互式工具，支持通过区域选择与文本提示对生成式 3D 模型进行选择性修复，包括开孔/封口、调整局部厚度等制造相关缺陷。方法直接在中间隐表示上施加修正，无需专业建模技能，用户研究显示新手可完成相关修复并偏好滑块与语言混合界面。

### [ARC-CT: Anatomy-Routed Contrastive Vision-Language Learning for 3D Chest CT](https://arxiv.org/abs/2608.28455)

**作者**：Huseyin Umut Isik, Mehmet Alp Ozaydin, Sila Kurugol, Şeyda Ertekin  
**方向标签**：3D  
**代码状态**：[Code](https://github.com/arc-ct/arc-ct)

本文提出面向 3D 胸部 CT 与放射学报告的解剖学路由对比学习框架 ARC-CT。通过解剖学约束查询定位视觉证据，采用软标签 Jaccard InfoNCE 损失降低共享病灶间的假阴性惩罚，并将器官级图像特征与器官特异性报告文本对齐，在 18 种异常分类上达到 0.86 的无需掩码宏观 AUC。

---

## 视觉语言模型（其他）

### [Dual-Stream Semantic Guidance with Prototype Anchor Calibration for Source-Fully-Free Adaptation of Vision-Language Models](https://arxiv.org/abs/2608.28145)

**作者**：Weiwei Xiang, Shun Peng, Guangyi Xiao, Hao Chen, Lei Yang  
**方向标签**：VLM  
**代码状态**：[Code](https://github.com/mrmenand/DSSG)

本文研究视觉语言模型的无源域自适应问题，指出固定类别嵌入导致的静态漂移与生成标题导致的动态漂移共同加剧了稳定性-可塑性困境。提出的 DSSG 框架融合标题流与类别锚点流，并扩展为 DSSG-PAC 以降低计算开销，在保持性能的同时将总适应时间减少 18.9%。

---

## 统计

- **总论文数**：17 篇
- **有代码仓库**：6 篇
  - [N0-Foundation](https://github.com/neoteai/N0-Foundation)
  - [ARC-CT](https://github.com/arc-ct/arc-ct)
  - [Post-Training VLMs for Video Mistake Detection](https://github.com/FedeSpu/mstk)
  - [Focus Where It Counts](https://github.com/topo-focus/Topofocus)
  - [DSSG](https://github.com/mrmenand/DSSG)
  - [Visual Token Coding](https://github.com/Msr233/VTC)
- **无代码仓库**：11 篇
- **方向覆盖**：VLM / MLLM、多模态理解与推理、多模态基准与评测、Agent 与具身智能、3D 视觉语言

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-09-01*
