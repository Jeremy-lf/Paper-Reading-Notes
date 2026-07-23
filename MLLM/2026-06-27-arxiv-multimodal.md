# Arxiv 多模态论文日报 - 2026-06-27

## VLM/MLLM

### [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373)
**作者:** Shravan Venkatraman, Ritesh Thawkar, Omkar Thawakar et al. | **方向:** VLM/MLLM | **代码:** [Code](https://github.com/mbzuai-oryx/VISE)

针对自进化大型多模态模型（LMM）在生成过程中过度依赖语言先验、忽视视觉token的"视觉欠条件"问题，本文提出VISE（Visual Invariance Self-Evolution）框架。VISE通过几何不变性与语义不变性两种奖励，直接正则化模型的视觉条件策略，在无需 specialist 角色、外部奖励模型或标注的情况下，仅使用原始未标注图像进行训练。实验基于Qwen3-VL-2B在18个基准上验证，COCO和TextCaps的CIDEr分别提升16.85和19.66，并有效降低对象幻觉。

---

### [Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs](https://arxiv.org/abs/2606.26387)
**作者:** Xi Xiao, Chen Liu, Chih-Ting Liao et al. | **方向:** VLM/MLLM | **代码:** 无

多模态大语言模型（MLLMs）虽然内部编码了正确的视觉证据，却常因过度依赖语言先验而产生与视觉输入矛盾的幻觉。现有对齐方法多基于文本优化结果级奖励，加剧了语言捷径偏向。本文提出VIGIL（Visual Information Gain In aLignment），通过强化学习后训练最大化视觉输入与生成回复间的互信息，对"盲自信"样本施加惩罚。VIGIL在幻觉与推理基准上 consistently 优于近期对齐方法，并仅用25%偏好数据即可匹配全数据SOTA性能。

---

### [What We are Missing in Multimodal LLM Evaluation?](https://arxiv.org/abs/2606.26348)
**作者:** Po-han Li, Shenghui Chen, Sandeep Chinchali et al. | **方向:** VLM/MLLM | **代码:** 无

多模态大语言模型（MLLMs）能力迅速提升，但评估方法未能同步跟进。现有基准多局限于孤立任务，难以衡量模型是否真正跨模态整合信息。本文审视MLLM评估现状并梳理基准分类，指出时空一致性、物理世界理解、多模态一致性与选择性注意等关键缺口，强调填补这些缺口对衡量真实多模态智能与暴露能力边界的重要性。

---

### [Yuvion VL: A Multimodal Foundation Model for Adversarial Content and AI Safety](https://arxiv.org/abs/2606.25034)
**作者:** Shikai Qiu, Xiaowen Xu, Benlei Cui et al. | **方向:** VLM/MLLM | **代码:** 无

通用模型难以可靠识别和理解现实世界中的多模态风险，因其本质上是多模态对抗性的。本文提出Yuvion VL，一系列专为内容与AI安全构建的多模态大语言模型，包含指令微调与推理导向两种变体。Yuvion VL通过对抗感知数据合成、三阶段训练流程与Confuse-then-Contrast微调，在YVRE安全基准上取得业界领先性能，超越同规模开源与最佳闭源商业模型。

---

## 多模态理解与推理

### [ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP](https://arxiv.org/abs/2606.26794)
**作者:** Sicheng Zhang, Muzammal Naseer, Binzhu Xie et al. | **方向:** 多模态理解与推理 | **代码:** [Code](https://github.com/RISys-Lab/ReasonCLIP)

CLIP及其变体作为多模态系统的视觉骨干，预训练仍主要依赖描述性图文对齐，难以满足日益增长的视觉常识推理需求。本文提出ReasonCLIP-58M，通过两阶段持续预训练将大规模推理监督融入CLIP风格模型，并构建ReasonLite-42M、ReasonPro-16M推理数据集与RCLIP-Bench诊断基准。作为LLaVA-NeXT等MLLM的可插拔视觉编码器，ReasonCLIP在零样本检索与视觉推理任务上均取得一致提升。

---

### [Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning](https://arxiv.org/abs/2606.26631)
**作者:** Mengzhao Wang, Yanli Ji, Wangmeng Zuo et al. | **方向:** 多模态理解与推理 | **代码:** 无

交错式多模态推理通过重访视觉证据提升视觉定位，但现有方法依赖token重播导致计算开销大。直接复用历史视觉KV cache会出现位置绑定过时的关键失效模式。本文提出PRCR（Position Rebinding Cache Reuse），存储原始视觉KV cache及其空间坐标，在注入当前解码器前重新分配兼容位置并重绑定键，实现无需重播的视觉重访。实验显示PRCR在多个多模态推理基准上达到或超过重播性能，同时计算量降低数万倍。

---

### [V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning](https://arxiv.org/abs/2606.25319)
**作者:** Haoxiang Sun, Zhihang Yi, Langxuan Deng et al. | **方向:** 多模态理解与推理 | **代码:** [Code](https://github.com/eVI-group-SCU/V-Zero)

细粒度视觉推理要求MLLM识别任务相关视觉证据并基于局部图像区域进行推理，现有方法多依赖昂贵的人工标注或强化学习探索。本文提出V-Zero，一种无需答案标签的视觉推理框架，通过on-policy蒸馏结合对比证据门控，使用问题相关区域裁剪与负视觉视图评估学生采样轨迹。实验显示V-Zero在多个视觉推理基准上 consistently 提升性能，同时训练速度比SFT快5倍以上，比RL基线快10倍以上。

---

## 多模态基准与评测

### [HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal Models](https://arxiv.org/abs/2606.27187)
**作者:** Jiajun Wu, Haoyu Kang, Yining Sun et al. | **方向:** 多模态基准与评测 | **代码:** 无

现有有害视频基准多将评估简化为二分类，忽略 harmful video 的多层特征且缺乏可解释依据。本文提出HarmVideoBench，包含1,379段视频与4,137道多选题，从可观察证据、片段内含义与片段外推理三个层次诊断模型对有害视频的深层理解。同时提出BCR方法，动态预测推理边界并检索上下文，将基线模型宏观平均从61.7%提升至84.4%。

---

### [FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images](https://arxiv.org/abs/2606.25915)
**作者:** Pengwei Wang, José Morano, Virginia Mares et al. | **方向:** 多模态基准与评测 | **代码:** [Code](https://github.com/penway/FunPiQ)

彩色眼底摄影是眼科筛查最常用的成像模态，但易受退化影响，现有眼底图像质量评估数据集多为图像级标签，难以量化局部退化。本文提出FunPiQ，首个提供像素级质量标注的眼底图像质量评估基准，并提出EFIQA-CP方法，基于解剖可见性生成质量伪标签，通过非负正未标记学习训练CNN。实验表明EFIQA-CP在分类、异常检测与可解释性设计方法中表现最优。

---

### [Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets](https://arxiv.org/abs/2606.25760)
**作者:** Divake Kumar, Sina Tayebati, Devashri Naik et al. | **方向:** 多模态基准与评测 | **代码:** 无

计算机使用agent将视觉语言模型（VLM）预测转化为可执行GUI点击，因此可靠的不确定性估计对拒绝、校准与空间安全区域至关重要。本文提出Argus基准，系统评估27种后验不确定性量化方法在4个VLA agent与4个GUI grounding数据集上的表现，并研究跨模型、跨数据集与跨接口的迁移性。主要发现是UQ排名在同一模型内跨数据集稳定，但跨模型类别与可观察接口时显著下降。

---

## 多模态检索与信息抽取

### [Exact and Deterministic Patch Descriptor Retrieval via Hierarchical Normalization](https://arxiv.org/abs/2606.27280)
**作者:** Koichi Sato | **方向:** 多模态检索与信息抽取 | **代码:** 无

本文提出一种精确且确定性的patch描述符检索方法，可在仅评估少量数据库条目的前提下，保证与穷举全向量搜索完全一致的结果。核心机制为层次化归一化（HN），将特征向量划分为主要分量与次要分量，通过可证明的分支定界扫描实现精确最近邻搜索。在UBC patch数据集上的实验显示，该方法相比暴力搜索在trevi和halfdome分别达到13.7倍和12.7倍加速，且仅0.4%的条目需要完整评估。

---

### [ReaORE: Reasoning-Guided Progressive Open Relation Extraction Empowered by Large Reasoning Models](https://arxiv.org/abs/2606.26986)
**作者:** Xin Lin, Liang Zhang, Guoqi Ma et al. | **方向:** 多模态检索与信息抽取 | **代码:** 无

开放关系抽取（OpenRE）要求模型从非结构化文本中抽取未见过的新关系，现有方法或依赖聚类无法生成关系标签，或依赖LLM直接生成标签但难以区分易混淆关系。本文提出ReaORE框架，通过由粗到细的关系推理完成关系抽取：首先进行关系过滤与补充，然后通过细粒度对比推理预测目标关系。在两个广泛使用的OpenRE数据集上，ReaORE均优于现有基线。

---

### [MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation](https://arxiv.org/abs/2606.26458)
**作者:** Xiaochen Wang, Bao Hoang, Han Liu et al. | **方向:** 多模态检索与信息抽取 | **代码:** [Code](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench)

多模态知识图谱增强生成（MKG-RAG）中的检索问题尚未得到充分评估，多模态知识异质且跨模态对齐困难。本文提出MKG-RAG-Bench，一个跨域基准，涵盖通用与医疗两个多模态知识图谱，并提供精确监督的结构化查询。实验表明有效的多模态检索对端到端MKG-RAG性能至关重要，检索质量显著决定生成结果，为诊断当前系统局限提供了基础。

---

## Agent与具身智能

### [E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation](https://arxiv.org/abs/2606.27268)
**作者:** Wen Ye, Peiyan Li, Tingyu Yuan et al. | **方向:** Agent与具身智能 | **代码:** 无

针对具身任务中推理扩展机制研究不足以及历史信息利用不充分的问题，本文提出E-TTS框架。E-TTS通过历史感知的迭代细化，将推理与动作扩展统一起来，使用vision-language verifier对推理-动作联合采样进行成对评分。在4个基准、6个环境、3种具身形态和4种基础VLA模型上的实验表明，E-TTS在仿真中最高提升33.14%，真实场景中提升26.62%，且无需额外专家数据或重训练。

---

### [Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy](https://arxiv.org/abs/2606.27251)
**作者:** Junhao Shi, Zezheng Huai, Siyin Wang et al. | **方向:** Agent与具身智能 | **代码:** 无

为构建能在非结构化环境中长期自主运行的具身智能体，本文提出OmniAct框架。该框架整合多模态语义规划器、自适应层次记忆（事件边界驱动的压缩）以及异步视觉抢占引擎，实现网络-物理统一动作空间的技能路由与失败恢复。在40个真实世界长程任务上，OmniAct在两种机器人平台与四种IoT设备协同下显著提升了端到端成功率，并保持接近线性的token增长。

---

### [Ordinal Neural Collapse as a Representation Prior for Visual Navigation](https://arxiv.org/abs/2606.26839)
**作者:** E-In Son, Jung-Taak Kim, Seung-Woo Seo | **方向:** Agent与具身智能 | **代码:** 无

针对端到端模仿学习中视觉编码器因仅受间接动作监督而学习到的表征模糊、动作无关的问题，本文提出ORION（Ordinal Neural Collapse for Visual Navigation）。ORION按照导航动作的序数结构显式组织编码器表征空间，使相邻控制类别的表征在单一判别轴上顺序排列，并抑制类内离轴方差。将预训练编码器集成到扩散导航框架中，在仿真与真实世界实验中均显著提升导航成功率与目标推进。

---

### [Improving Vision-Language-Action Model Fine-Tuning with Structured Stage and Keyframe Supervision](https://arxiv.org/abs/2606.26801)
**作者:** Yuan Xu, Yixiang Chen, Kai Wang et al. | **方向:** Agent与具身智能 | **代码:** 无

VLA模型微调时动作监督均匀施加于所有时间步，缺乏对机器人操作阶段及下一个夹爪事件目标的结构化监督。本文提出StaKe插件式辅助监督框架，自动从示范夹爪状态推导操作阶段分类器与关键帧预测器两个轻量化辅助头，在不影响VLA策略架构与推理的情况下丰富训练表征。在双臂仿真与单臂Franka真实机器人任务中，StaKe分别带来14%和56%的相对成功率提升。

---

## 多模态生成

### [RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation](https://arxiv.org/abs/2606.27345)
**作者:** Minghao Yin, Jiahao Lu, Wenbo Hu et al. | **方向:** 多模态生成 | **代码:** 无

现有视频扩散Transformer通常在相机采样网格的(u,v,t)轴上使用RoPE，难以捕捉场景三维结构。本文提出RayPE，将每条光线的6D Plucker坐标以加法形式注入自注意力查询与键中，使注意力得分可分解为内容项、几何项及交叉项。该模块以零初始化方式附加到预训练视频DiT，参数量增加不到0.1%，在四数据集混合训练上提升了相机可控性、跨帧3D一致性与整体视频质量。

---

### [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147)
**作者:** Yunqi Xue, Zhijiang Li, Philip Torr et al. | **方向:** 多模态生成 | **代码:** 无

自回归统一多模态模型通过离散视觉token序列生成图像，其安全性尚未得到充分研究。本文提出迭代自改进码本方法，利用模型自身的理解与判断能力识别不安全生成，无需人工标注；通过构建有害空间更新码本表征消除有害映射，并在无害空间进行自适应微调保证图像质量。两步迭代直至收敛，可在无外部反馈的情况下持续提升模型安全性。

---

### [DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation](https://arxiv.org/abs/2606.26058)
**作者:** Nan Chen, Yiyang Cai, Rongchang Xie et al. | **方向:** 多模态生成 | **代码:** [Code](https://github.com/HKUST-C4G/DomainShuttle)

开放域主体驱动文本到视频生成需要在保留参考主体特征的同时允许跨域编辑。本文提出DomainShuttle，通过Domain-MoT解耦视频与参考特征并引入域感知AdaLN，以及Video-Reference DualRoPE将参考图像token与视频token置于独立RoPE空间，实现精确主体级空间建模。跨域一致损失则提取不受无关特征影响的内在主体特征，实验显示DomainShuttle在多种开放域场景中兼具高保真与生成灵活性。

---

### [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473)
**作者:** Kaiwen Zheng, Guande He, Min Zhao et al. | **方向:** 多模态生成 | **代码:** [Code](https://github.com/SandAI-org/MagiAttention/)

自回归视频扩散已成为实时流式视频生成与动作条件交互世界模型的重要范式。本文将rCM蒸馏框架扩展到自回归视频扩散，提出Causal-rCM，统一教师强制（teacher-forcing）与自强制（self-forcing）两种训练范式。通过自定义FlashAttention-2 JVP核实现连续时间一致性模型，收敛速度提升10倍；蒸馏后的2步因果Wan2.1-1.3B在VBench-T2V达到84.63，并可将Cosmos 3扩展为交互式世界模型。

---

### [Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation](https://arxiv.org/abs/2606.25306)
**作者:** Atin Pothiraj, Jaemin Cho, Yue Zhang et al. | **方向:** 多模态生成 | **代码:** [Code](https://github.com/atinpothiraj/pqsg)

视频生成模型虽能生成逼真视频，但仍难以遵循基本物理规律，且缺乏细粒度评估方法来定位物理违规。本文提出Physics Question Scene Graph（PQSG），一种基于层次化问题的评估流程，通过VLM生成图结构问题并检查生成视频在物体、动作与物理定律上的忠实度。基于FinePhyEval数据集，PQSG与人类判断的相关性优于现有工作，并可作为子任务基准评估VLM的问题生成与回答能力。

---

## 音频多模态

### [VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation](https://arxiv.org/abs/2606.26534)
**作者:** Tianxin Xie, Chenxing Li, Dong Yu et al. | **方向:** 音频多模态 | **代码:** 无

零样本文本转语音（TTS）虽能合成高保真语音，但在模仿相声、方言等非常见说话风格时表现不佳，且微调需要大量高质量数据。本文提出VoiceTTA，一种基于强化学习的测试时自适应方法，在流匹配模型推理阶段通过GRPO优化可学习前缀，结合F0/能量变异系数风格奖励、说话人相似度与Whisper WER可懂度奖励。实验表明VoiceTTA在非常见语音提示上显著优于现有最先进基线。

---

### [MJEPA: A Simple and Scalable Joint-Embedding Predictive Architecture for Audio-Visual Learning](https://arxiv.org/abs/2606.25225)
**作者:** Revant Teotia, Adrien Bardes, Michael Rabbat et al. | **方向:** 音频多模态 | **代码:** 无

自监督学习已在大规模视频视觉表征中占据主导，但将音频与视觉联合学习仍具挑战。本文提出MJEPA，一种面向音视觉学习的联合嵌入预测架构，使用单一统一编码器处理两种模态，并仅在单一预测目标下进行模态内与跨模态预测。实验表明跨模态预测至关重要：缺少它时共享编码器性能低于单模态基线，而加入后两种模态表征相互促进，在AudioSet-20K上超过此前最佳冻结基线6.8 mAP。

---

## 3D视觉语言

### [Pseudo-Text-Conditioned 3D Grounding DINO for Organ Localization in Abdominal CT](https://arxiv.org/abs/2606.27084)
**作者:** Siqi Chen, Han Gong, Keyi Hou et al. | **方向:** 3D视觉语言 | **代码:** [Code](https://github.com/SiqiChen9/3d-grounding-dino)

本文提出CT-3GDINO，一种轻量化的3D检测器，用于腹部CT器官定位。该方法将Grounding-DINO风格的查询架构适配到3D医学图像，使用冻结的伪文本类别token替代真实文本编码器，结合Swin3D视觉骨干、双向特征增强与跨模态解码器预测肝脏、脾脏、肾脏等器官的3D边界框。在193例RSNA/RATIC CT数据上的实验显示，多尺度模型在0.1-0.7 IoU阈值上达到0.5830 mAP， coarse localization AP高达0.9649。

---

### [Depth-Semantic Alignment and Affinity-Guided Fusion for Structured Radar Point Cloud Generation](https://arxiv.org/abs/2606.26743)
**作者:** Amjad Hussain, Xin Qiu, Fuyuan Ai et al. | **方向:** 3D视觉语言 | **代码:** 无

毫米波雷达点云通常稀疏、噪声大且结构不完整，影响下游感知任务。本文提出一种基于视觉-雷达融合的多模态点云生成方法，利用图像语义信息对雷达点云施加结构约束与空间对齐，并采用稀疏补全策略提升点密度与恢复缺失结构。实验表明，生成的点云可有效提升复杂环境下目标检测与跟踪的精度和鲁棒性。

---

### [Point Cloud Diffusion with Global and Local Reconstruction for Instance-Level 3D Anomaly Detection](https://arxiv.org/abs/2606.25740)
**作者:** Linchun Wu, Qin Zou, Jiwen Lu et al. | **方向:** 3D视觉语言 | **代码:** 无

点云3D异常检测在精密工业制造中至关重要，现有方法难以重建微弱缺陷区域且背景非缺陷区域易产生位置偏差。本文提出PCDiff，一种实例级点云扩散异常生成与检测框架：生成阶段嵌入实例级多模态注意力，以纹理梯度、图像块、文本与掩码为条件生成弱缺陷；检测阶段采用联合局部-全局重建算法保留背景正常结构并恢复前景缺陷。实验显示PCDiff在3D异常生成保真度与检测精度上均显著优于SOTA。

---

### [Disease-Centric Vision-Language Pretraining with Hybrid Visual Encoding for 3D Computed Tomography](https://arxiv.org/abs/2606.25546)
**作者:** Bowen Shi, Weiwei Cao, Ruifeng Yuan et al. | **方向:** 3D视觉语言 | **代码:** 无

视觉语言预训练（VLP）有望利用放射学报告作为监督信号构建通用医疗AI，但现有方法在3D CT上面临视觉骨干效率低与语义对齐粗粒度的问题。本文提出面向疾病的VLP框架，包含CNN-ViT混合编码器、疾病级对比学习机制以及诊断感知提示策略。在CT-RATE与Rad-ChestCT等基准上取得SOTA，并展现出良好的放射学报告生成迁移能力。

---

> 共收录 28 篇论文，涵盖 8 个方向
