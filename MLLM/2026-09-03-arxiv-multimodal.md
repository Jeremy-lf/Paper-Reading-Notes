# Arxiv 多模态论文日报 · 2026-09-03

**日期**：2026 年 9 月 3 日
**收录论文**：26 篇
**含代码仓库**：15 篇
**覆盖方向**：8 个

## VLM / MLLM

### [RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2609.02731)
**作者**：Canjie Liu, Jiawen Kang, Jinbo Wen, Zishao Zhong
**方向标签**：VLM/MLLM、检索 · **[代码](https://github.com/canjie-liu/RVSD)**

提出一种无需训练、即插即用的解码框架 RVSD，将语义空间视觉检索与 token 稀疏化集成到单次解码过程中。通过语义导向的 token 选择保留关键视觉信息，同时以跨模态检索按需补偿被裁减的内容，在减少 LVLM 视觉幻觉方面取得领先效果。

### [Characterizing Text Branch Sensitivity in Medical Vision-Language Segmentation via Evidence Decoupling](https://arxiv.org/abs/2609.02663)
**作者**：Ziquan Liu, Zhewei Zhu, Xuyang Shi
**方向标签**：VLM/MLLM、医学图像

系统分析临床文本对预训练视觉语言模型在医学图像分割中像素级输出的影响。提出 Evidence Decoupling Decoder (EDD)，在解码阶段将图像证据与文本调制证据解耦，发现文本主要通过全局语义调制而非独立空间定位影响预测。

### [Beauty is in the AI of the beholder: MLLMs systematically overrate facial attractiveness](https://arxiv.org/abs/2609.02512)
**作者**：Santiago Grandas, Juan Sebastian Cely-Acosta, Mohit Mendiratta, Shafee Hassan, Macken Murphy
**方向标签**：VLM/MLLM、评测

对比 2,513 名人类参与者与 Claude、Gemini、GPT、Grok 等商用 MLLM 的面部吸引力评分。发现这些模型系统性地高估人脸吸引力且评分区间更窄，虽然与人类排序相关性较强，但无法复现人类的绝对评分，不同模型对种族和性别的影响也存在差异。

### [TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models](https://arxiv.org/abs/2609.02359)
**作者**：Leqian Ding, Junning Qiu, Manwen Yang, Yu Guo, Fei Wang
**方向标签**：VLM/MLLM、视觉定位

针对流式视频中的视觉定位任务，提出 TempoGround 框架，对目标存在状态和跨帧对应关系进行建模，以减少身份漂移和不一致的定位。通过课程预测机制与针对定位、身份和一致性的强化奖励，同时预测 2D 框并提升至 3D 相机坐标框。

### [Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models](https://arxiv.org/abs/2609.02082)
**作者**：Tianqi Xiao, Shiyao Cui, Minghao Zhang, Junxiao Yang, Renmiao Chen
**方向标签**：VLM/MLLM、安全 · **[代码](https://github.com/cucu220123/safety-awareness)**

研究 MLLM 中的跨模态安全漂移问题：原本无害的文本查询在结合特定视觉图像后可能传递有害意图。提出 Safety-awareness Representation Transfer (SRT)，在保持主干冻结的同时增强模型的拒绝行为，且仅需轻量级迁移训练。

## 多模态理解与推理

### [DiscoSign: Discourse-Aware Text to Sign Language Gloss Translation](https://arxiv.org/abs/2609.02796)
**作者**：Vasileios Baltatzis, Mert Inan, Connor Gillis, Raja Kushalnagar, Lorna Quandt, Leah Findlater, Colin Lea
**方向标签**：多模态理解、手语

提出 DiscoSign，一种基于 LLM 的模块化 discourse-aware 文本到美式手语 gloss 翻译方法。处理空间指代、问答从句和概念-gloss 一致性问题，并引入新的篇章级连贯性评估指标，实验显示其在空间一致性和实体跟踪上优于句子级翻译。

### [TC-Next: Zero-Shot Multimodal Cyclone Forecasting](https://arxiv.org/abs/2609.02085)
**作者**：Zhe Wang, Sijie Chen, Yiming Luo, Daehyun Kim, Chien-Yi Chang
**方向标签**：多模态理解、气象预测

提出 TC-Next，一种多模态深度学习模型，结合 GraphCast 预报场与 GridSat 红外卫星图像，进行 6–24 小时热带气旋路径和强度预测。仅在西太平洋 GraphCast 数据上训练即可 zero-shot 迁移到 Pangu-Weather、IFS HRES 和 WeatherNext Cyclones，显著降低路径和强度误差。

## 多模态基准与评测

### [Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](https://arxiv.org/abs/2609.02864)
**作者**：Yutong Liu, Nan Huang, Xu Cao, James M. Rehg
**方向标签**：基准、生成、推理

提出 RIG-Bench，一个面向"推理驱动生成"的系统性基准，覆盖四个领域共 2,000 个样本。评估揭示了当前统一生成模型与世界仿真器存在的"推理-生成鸿沟"：模型输出往往在局部合理但全局逻辑上存在缺陷。

### [Deeply Interleaved Text-Image Contexts for Multimodal LLMs Assessment](https://arxiv.org/abs/2609.02573)
**作者**：Zihao Wang, Xi Xiang, Yuwen Sun, Yingyu Li, Yabo Zhang, Yihan Zeng, Fan Li, Wangmeng Zuo
**方向标签**：基准、VLM/MLLM · **[数据集](https://huggingface.co/datasets/pino10010/TIC-Bench)**

指出当前多模态评估过度关注多图任务，而忽视了真实应用中需要深度语义交互的"交错文本-图像场景"。提出 TIC-Bench，包含 2,280 道问题，测试模型整合图文线索并恢复真实事实的能力。

### [Blending Concepts: Benchmarking Visual Metaphor Generation in Text-to-Image Models](https://arxiv.org/abs/2609.02502)
**作者**：Chuer Chen, Zichen Wang, Yi He, Zhengxi Yu, Nan Cao
**方向标签**：基准、生成

推出 VMetaphor-Bench，首个用于评估文本到图像模型中视觉隐喻生成的基准，包含 1,500 个精心整理的隐喻和混合 MLLM-as-judge 评估。对 11 个 T2I 模型的测试表明，即使强大的闭源系统在组合结构和跨域映射方面仍面临挑战。

## 多模态检索与信息抽取

### [MARS: What Retrieval Signals Are Hidden in Multimodal Large Language Models for Text-Video Retrieval?](https://arxiv.org/abs/2609.02565)
**作者**：Uicheol Jung, Juyoung Hong, Geuntaek Lim, Yukyung Choi
**方向标签**：检索、VLM/MLLM · **[代码](https://github.com/sejong-rcv/MARS)**

提出 MARS，一种面向文本-视频检索的多层多槽嵌入框架。从解码器各层隐藏状态构建多个自适应表示槽，对匹配文本和视频槽的相似度进行聚合，并通过难负例感知的槽特化目标增强判别性线索，在四个基准上取得领先结果。

### [ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering](https://arxiv.org/abs/2609.02486)
**作者**：Adrien Mialland, Marc Plantevit, Julien Gallois, Céline Robardet
**方向标签**：检索、VLM · **[代码](https://github.com/adrienmialland/ViSAR)**

针对视觉文档问答中的 RAG 检索，提出 ViSAR，一种无需训练的自适应 k 检索方法。通过构建查询相关的页面级相似度矩阵，识别相关语义并动态决定保留页面数量，在多种编码器和 LVLM 组合上降低最多 58.7% 的 RAG 延迟，同时保持或提升准确率。

### [MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation](https://arxiv.org/abs/2609.01913)
**作者**：You-Lin Chen, Kyoungjun Park, Bin Xu, Prithviraj Sen, Pedro Herrero-Vidal
**方向标签**：检索、VLM

提出一种蒸馏方法，将大型视觉语言教师的结构化推理能力迁移到 70 亿参数学生模型，无需人工标注。教师一致同意的案例用于监督微调，冲突决策通过元裁判生成偏好对进行 DPO 训练，在多语言电商实体解析基准上显著超越人类标注和更大模型。

## Agent / 具身智能

### [LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory](https://arxiv.org/abs/2609.02350)
**作者**：Kun-Yang Yu, Yingzhe Li, Hongyu Xu, Shi-Yu Tian, Zhi Zhou, Yang Chen, Ming Yang, Sheng Wang, Qing Yu, Lan-Zhe Guo, Yu-Feng Li
**方向标签**：Agent、VLM/MLLM · **[代码](https://github.com/kunyang-YU/LookStep)**

面向视觉语言导航 (VLN)，提出 LookStep 框架，包含语言中心的未来状态建模和事件驱动的滚动记忆两个组件。前者利用语言标签生成粗粒度导航进度与未来状态；后者根据语义角色决定是否将观测写入有界滚动记忆。在 R2R-CE Val-Unseen 上取得 49.7% 成功率，同时降低数据需求和内存开销。

### [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885)
**作者**：Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig
**方向标签**：Agent、世界模型 · **[项目页](https://dhruvpendharkar.github.io/dwm/)**

提出预测状态匹配 (predicted-state matching) 训练目标，用于网页智能体的世界模型。与监督式下一状态预测不同，该目标要求预测表示能够区分真实执行结果与其他动作可能到达的状态。基于 WebArena Go-Browse 轨迹构建的分支数据集训练，在 WebPRMBench 和 WebArena-Lite 上取得提升。

### [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](https://arxiv.org/abs/2609.02459)
**作者**：Austin Tudor David Andrews, Liam Wilkinson, Jamie Heagerty, Harry Coppock, Jakob Nicolaus Foerster, Rui Ponte Costa
**方向标签**：Agent、基准 · **[代码](https://github.com/lmwilki/civ6-mcp)**

提出 CivBench，用于评估语言模型智能体在《文明 VI》长周期、工具介导环境中的能力。每次运行跨越 300+ 回合，暴露 76 个 MCP 工具，并通过文本层转换视觉游戏状态。引入主动监控率和 RAG@10 等指标，发现智能体常忽略关键战略状态查询且难以执行近期计划。

### [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](https://arxiv.org/abs/2609.02231)
**作者**：Fan Yuxuan, Huang Miaojun, Zhang Haimei, Wu Jingshen, Liu Hao
**方向标签**：Agent、多模态

提出 PhoenixNest-Video，一个用于自动化视频面试评估的多模态智能体框架。通过语义视频图、基于评分标准的检索与跨模态验证，以及强化学习评分器，为每个评分维度生成带证据的分数，在 VInterview-2025 上达到 91.50% 的等级准确率。

### [Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](https://arxiv.org/abs/2609.02309)
**作者**：Bizhe Bai, Jiakang Yuan, Hongming Wu, Xinyue Wang, Jie Ren, Siyao Chen, Yuchen Ya, Fan Bai, Pai Peng, Huafeng Qin, Tao Chen
**方向标签**：Agent、综述

从观测、上下文/记忆、动作和规划器/系统效率四个维度综述高效 GUI 智能体。强调选择性读取、可恢复记忆、验证感知控制和混合运行时等关键思路，并指出真实部署中验证器成本核算和跨基准可比性等开放问题。

## 多模态生成

### [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886)
**作者**：Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
**方向标签**：生成、世界模型 · **[代码](https://github.com/Junchao-cs/SolarWM)**

推出 SolarWM，一个面向交互式视频世界模型的开放基础。提供多源数据引擎，将 10 个数据集的 143 万片段归一化为统一格式，并支持 Wan2.2、LTX-2.5 和 MiniMax-H3 等多种视频骨干。训练 5B 到 33B 参数的因果模型，仅使用 5 秒片段即可实现长程 rollout，并开源数据、代码、配方和权重。

### [The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video Generation](https://arxiv.org/abs/2609.02367)
**作者**：Yichen Liu, Quanwei Zhang, Haozhe Wang, Donghao Zhou, Xiaojie Li, Yang Shi, Jiaming Liu, Ruihua Huang, Yingtian Zou, Daquan Zhou
**方向标签**：生成、音视频 · **[代码](https://github.com/DAGroup-PKU/Temporal-Context-Routing)**

提出 Temporal Context Routing (TCR)，将脚本驱动音视频生成中的时序对齐从视频和音频扩展到结构化脚本。通过将脚本时间映射到两种模态共享的时间轴，并将每个提示的引导路由到对应位置，显著降低镜头边界时序误差并提升对白准确率，同时保持视觉质量和音视频同步。

### [Multi-Tool Image Editing Attribution in Facial Forgery](https://arxiv.org/abs/2609.02751)
**作者**：Sheng Liu, Qiang Sheng, Danding Wang, Yu Li, Chenming Zhou, Juan Cao
**方向标签**：生成、图像编辑 · **[代码](https://github.com/ICTMCG/MIEA)**

提出 Multi-Tool Image Editing Attribution 任务，识别单张人脸肖像中应用的多种编辑工具。构建 MultiEdit 数据集，包含超过 50 万张经过 6 种工具编辑的人脸。所提模型 DPEC 从空间和频率信息中学习可定位的工具痕迹，并通过基于误差的课程学习，在多达五步编辑的图像上超越 9 个基线。

### [GDB-Reward: From Evaluation Metrics to Training Rewards for Graphic Design](https://arxiv.org/abs/2609.02813)
**作者**：Adrienne Deganutti, Purvanshi Mehta, Simon Hadfield, Andrew Gilbert
**方向标签**：生成、平面设计

提出 GDB-Reward，将多种平面设计评估指标转化为单一强化学习奖励，用于优化文本提示而无需微调图像生成器。实验表明该方法在感知质量、渲染保真度和空间准确性方面均有提升，展示了设计评估指标本身作为训练信号的可行性。

## 音频多模态

### [SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval](https://arxiv.org/abs/2609.02343)
**作者**：Zineb Lahrichi, Marc Ferras, Gaël Richard, Geoffroy Peeters
**方向标签**：音频、检索 · **[数据集](https://huggingface.co/datasets/Zineb/SonicCaps)**

发布 SonicCaps 数据集，包含约 15M 条标题与约 70 万音频片段配对，通过基于音频和文本条件的多模态大语言模型生成。每段音频平均生成约 24 条结构化标题，实验显示在该数据集上训练的 CLAP 模型在音频检索和零样本分类任务上均有提升。

### [Predictors of Loneliness in Older Adults Using Multimodal Analysis of Speech and Language](https://arxiv.org/abs/2609.02606)
**作者**：Vinmay Khandode, Sai Karthik Kosuri, Neil K. R. Sehgal, Adam Greene, Elif Alpoge, Elana Duffy, Matthew Lee Smith, Thomas K.M. Cudjoe, Sharath Chandra Guntuku
**方向标签**：音频、多模态 · **[代码](https://github.com/karthik-strikes/Audio_Analysis)**

对 310 名老年人进行半结构化电话访谈，结合语言学特征与音高、语调、响度等声学特征，分析孤独感的多模态预测因子。发现较高孤独感与否定词、负面语调和冲突相关语言有关，而较低孤独感则与社会参照、动机驱动和情感丰富性相关，多模态模型优于单模态模型。

### [A Common Measure of Communication for Speech Brain-Computer Interfaces](https://arxiv.org/abs/2609.02887)
**作者**：Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones
**方向标签**：音频、脑机接口 · **[代码](https://github.com/neural-processing-lab/OVMI)**

提出开放词汇互信息 (OVMI)，用于评估语音脑机接口与参考词分布之间的通信能力。该方法支持跨系统公平比较并辅助词汇设计，为语音 BCI 提供统一的性能度量。

## 3D 视觉语言

### [MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion](https://arxiv.org/abs/2609.02854)
**作者**：Aidan Bradshaw, Marco Giordano, David Rode, Andreas Habersack, Elif Basokur, Annika Kruse, Markus Tilp, Michele Magno, Peter Wolf, Luca Benini, Christoph Leitner
**方向标签**：3D、视频 · **[代码](https://github.com/Abradshaw1/Muybridge)**

提出 MuyBridge，一个移动端系统，通过稀疏融合紧凑 2D 姿态网络与蒸馏单目深度网络，从单部手机摄像头视频中估计运动员的度量级分段质心。利用解剖学和物理先验，无需 3D 标注或任务特定监督，适用于运动生物力学和康复分析。

---

**论文总数统计**：本次日报共收录 26 篇多模态相关论文，其中 15 篇提供代码/数据集/项目页链接，覆盖 8 个研究方向。

_自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-09-03_
