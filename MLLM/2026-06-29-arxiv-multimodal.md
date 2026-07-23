# Arxiv 多模态论文日报 - 2026-06-29

## VLM/MLLM核心

### [ViQ: Text-Aligned Visual Quantized Representations at Any Resolution](https://arxiv.org/abs/2606.27313)
**作者:** Xumin Yu, Zuyan Liu, Zhenyu Yang et al. | **方向:** VLM/MLLM | **代码:** [Code](https://github.com/yuxumin/ViQ)

本文提出ViQ，一种文本对齐的视觉量化表示框架，通过两阶段学习（文本对齐预训练与特征离散化）在离散表示中平衡语义与细节，并支持任意原生分辨率输入。实验表明ViQ在多项多模态任务上媲美连续高维特征的最先进视觉编码器，同时可将多模态训练加速20%-70%。

---

### [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376)
**作者:** Ritesh Thawkar, Shravan Venkatraman, Omkar Thawkar et al. | **方向:** VLM/MLLM | **代码:** [Code](https://github.com/mbzuai-oryx/Ask-Solve-Generate)

本文提出一种自进化训练框架，使统一大多模态模型仅利用无标注图像，通过内部角色（提出者、求解者、生成者）及自一致性奖励同时提升视觉理解与图像生成能力。引入求解器Token熵作为连续难度信号，并在BLIP3o、BAGEL和VARGPT-v1.1三种架构上验证；BAGEL在MMMU上提升3.5%，GenEval从82%提升至85%。

---

### [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373)
**作者:** Shravan Venkatraman, Ritesh Thawkar, Omkar Thawkar et al. | **方向:** VLM/MLLM | **代码:** [Code](https://github.com/mbzuai-oryx/VISE)

针对自进化大多模态模型中解码器过度依赖语言先验而忽视视觉内容的"视觉欠条件"问题，本文提出VISE框架，通过几何不变性奖励和语义不变性奖励直接正则化模型的视觉条件策略。在18个基准上验证，Qwen3-VL-2B在COCO和TextCaps上CIDEr分别提升16.85和19.66，幻觉降低5.0 Chair-I。

---

### [RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2606.28266)
**作者:** Yelin Wang, Zijia Song, Shuo Ye et al. | **方向:** VLM/MLLM | **代码:** [Code](https://github.com/keaill/RSICCLLM)

本文提出首个面向遥感图像变化描述（RSICC）的大视觉语言模型后训练框架RSICCLLM，并发布了指令数据集RSICI与任务基准。方法包括差异感知监督微调以显式提取变化表示，以及双负例偏好优化（DNPO）通过互补负样本策略构建偏好数据集RSICP。实验表明，仅7B参数的RSICCLLM即可超越更大规模模型，在RSICC任务上取得领先性能。

---

### [Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge](https://arxiv.org/abs/2606.27527)
**作者:** Thomas Shih-Chao Liang, Zhuoran Yu, Yong Jae Lee | **方向:** VLM/MLLM | **代码:** 无

本文提出LaViD框架，通过让纯语言教师模型生成多选题来探测视觉类别间的语义差异，并将这些语义信号转化为软标签分布以指导纯视觉学生模型学习，实现跨模态细粒度概念知识迁移。该方法无需成对多模态数据，且在多个细粒度基准上优于从视觉语言模型蒸馏的MaKD等方法。在Waterbirds数据集上，LaViD显著提升了最差组准确率，增强了对虚假相关性的鲁棒性。

---

## 多模态理解与推理

### [Vision-Default, Prior-Override: Causal Mechanisms of Perception-Knowledge Conflict in Vision-Language Models](https://arxiv.org/abs/2606.28273)
**作者:** Niclas Lietzow, Danielle Bitterman, Carsten Eickhoff et al. | **方向:** 多模态理解与推理 | **代码:** [Code](https://github.com/nlietzow/vision-default-prior-override)

本文通过跨三种粒度的激活修补、组件消融与机制分析，研究了视觉语言模型中感知证据与先验知识冲突时的因果机制。研究发现视觉 grounding 默认形成，而先验 grounding 依赖于网络后半部分少量注意力头（2.5%-4.8%），消融这些头可在68%-96%的情况下将基于知识的预测转为视觉 grounded。该研究揭示了VLMs中感知-知识冲突的稀疏因果回路，包括路由头和写入头两种功能分化。

---

### [MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy](https://arxiv.org/abs/2606.27652)
**作者:** Zhiyuan Han, Beier Zhu, Wenwen Tong et al. | **方向:** 多模态理解与推理 | **代码:** 无

本文提出MER-R1，一种通过慢速-快速思维协同进行多模态情绪推理的强化学习框架，将召回与精确率解耦为双目标优化信号，并通过慢快置信度校准使最终慢思考答案与快速直觉对齐。该统一框架兼顾快速思维的召回导向直觉与慢速思维的精确导向选择性，并给出理论分析说明其可缓解优化中的方差干扰。在MER-UniBench和MME-Emotion上的实验表明，MER-R1达到最先进性能。

---

## 多模态基准与评测

### [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322)
**作者:** Yana Wei, Hongbo Peng, Yanlin Lai et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出PerceptionRubrics，一种基于评分细则的多模态评估框架，通过1,038张信息密集图像和超过12,000条实例级细则，将评估从整体语义匹配转向严格原子化审计。框架设计了"必须正确"与"容易错误"双路评分标准，并引入门控计分机制，对强制性视觉事实失败施加二进制惩罚。实验揭示了模型在密集领域中的脆弱性、开源与专有前沿模型间8%的感知差距，以及门控指标相比传统基准更对齐人类感知。

---

### [AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration](https://arxiv.org/abs/2606.28049)
**作者:** Haotian Li, Yida Wang, Leyuan Wang et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出AirGroundBench，用于评估异构无人机-无人车协作中多视角空间智能的诊断基准，包含11个高保真模拟环境、1,021对同步空地图像、约62,000条双视角选择题和115个闭环视觉语言导航片段。基准覆盖空间感知、跨视角对齐、空间变换推理和具身决策四个能力维度。对13个代表性MLLM的评估显示，模型在空间感知上表现较好，但在跨视角对齐和变换密集型推理上存在明显瓶颈。

---

### [HumanMoveVQA: Can Video MLLMs reason about human movement in videos?](https://arxiv.org/abs/2606.27999)
**作者:** Pulkit Gera, Faegheh Sardari, Asmar Nadeem et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出HumanMoveVQA，首个从自我中心视角评估人体全局轨迹与朝向推理的综合基准，通过将2D视频观测提升为世界坐标系一致的3D运动轨迹，生成超过10,000条结构化问答对。基准涵盖运动聚合、顺序排序和轨迹级推断等七类推理。实验发现当前最先进专有模型在人体运动深度理解上存在显著能力差距，但基于该监督信号微调开源模型可获得显著提升。

---

### [Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical Reasoning](https://arxiv.org/abs/2606.27828)
**作者:** Hohin Kwan, Hongyu Li, Ray Zhang et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出Video-MME-Logical，一个面向视频时序-逻辑推理的受控诊断基准，围绕状态跟踪、顺序计数、时序排序、动态空间性和结构组合五种时序逻辑操作构建，包含25个细粒度任务类别。基准通过控制对象状态、转移、时序依赖和逻辑组合实现难度可控评估，并支持中间状态诊断。实验显示最先进MLLM与人类存在显著差距，且复杂推理时差距更大。

---

### [NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning](https://arxiv.org/abs/2606.27826)
**作者:** Shiyun Zhao, Xinwei Song, Tianyu Guo et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出NormAct，一个用于评估具身规划中隐含社会规范遵守的基准，将隐藏规范嵌入日常任务，从目标达成、规范遵守和整体任务成功三个维度评估模型。实验显示当前先进MLLM在67.3%情况下完成显式目标，但仅26.4%遵守隐藏规范。为此提出的NormPerceptor能够在规划前推断场景相关规范，将任务成功率从24.2%提升至46.7%。

---

### [DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection](https://arxiv.org/abs/2606.27499)
**作者:** Yujin Tang, Chenming Shang, Ruize Xu et al. | **方向:** 多模态基准与评测 | **代码:** 无

现有智能体记忆研究多集中在文本端，缺少对多模态智能体视觉记忆的交互式评测。本文提出DMV-Bench，首个诊断长程多模态智能体视觉记忆的交互式基准，通过在产品图像中注入偶然线索并要求智能体后续回忆并导航至对应URL。基于双重编码理论提出的DualMem架构在Gemini 2.5 Flash和Qwen2.5-VL-7B上均优于现有基线。

---

### [CORTEX: A Structured Reasoning Benchmark for Trustworthy 3D Chest CT MLLMs](https://arxiv.org/abs/2606.27264)
**作者:** Hashmat Shadab Malik, Anees Ur Rehman Hashmi, Numan Saeed et al. | **方向:** 多模态基准与评测 | **代码:** 无

本文提出CORTEX，首个面向3D胸部CT MLLM的结构化推理基准，将缺失的推理过程恢复为任务理解、视觉观察、诊断推理和答案综合四阶段诊断轨迹。基于CT-RATE数据集构建76,177条经验证的推理轨迹，并提供阶段级评估协议，以训练和评估可信赖的3D胸部CT推理模型。

---

### [Unison: Benchmarking Unified Multimodal Models via Synergistic Understanding and Generation](https://arxiv.org/abs/2606.26984)
**作者:** Jinyu Liu, Xincheng Shuai, Henghui Ding et al. | **方向:** 多模态基准与评测 | **代码:** [Code](https://github.com/FudanCVL/Unison)

本文提出Unison基准，包含2,169个高质量统一任务样本，用于评估统一多模态模型中理解与生成能力的协同作用。基准涵盖内部一致性、理解引导生成、生成引导理解和相互增强四个维度，并提供统一与解耦两种评测轨道及Unison-Judge评估模型，揭示当前统一多模态系统的关键局限。

---

## Agent与具身智能

### [ProMSA: Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering](https://arxiv.org/abs/2606.27974)
**作者:** ZhengXian Wu, Hangrui Xu, Kai Shi et al. | **方向:** Agent与具身智能 | **代码:** [Code](https://github.com/DingWu1021/Promsa)

本文提出ProMSA，一种面向知识驱动视觉问答（KB-VQA）的渐进式多模态搜索智能体，能够根据图像-问题对迭代选择图像搜索、文本搜索或停止，并在工具调用预算和去重机制下避免冗余检索。训练上先通过拒绝采样SFT学习工具使用格式，再通过TN-GSPO序列级强化学习目标对生成长度和工具交互深度进行归一化优化。在E-VQA和InfoSeek上的实验表明，该方法在检索准确率和端到端准确率上均优于强RAG和智能体基线。

---

### [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://arxiv.org/abs/2606.27330)
**作者:** Tianyi Men, Zhuoran Jin, Pengfei Cao et al. | **方向:** Agent与具身智能 | **代码:** 无

本文提出PEEU方法，通过自主探索环境发现经验并利用事后经验合成高层训练数据，以增强小型开源MLLM在GUI任务规划中的跨网站泛化能力。同时提出TDHAF框架系统分析跨低、中、高三层的组合泛化行为，7B模型在真实基准上达到30.6%准确率，超越Qwen2.5-VL-32B。

---

### [PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies](https://arxiv.org/abs/2606.27146)
**作者:** Jiayu Yang, Tao Yang, Weijun Li et al. | **方向:** Agent与具身智能 | **代码:** 无

本文提出PhysReflect-VLA，一个可插拔的执行时可靠性框架，通过可行性算子评估动作状态转移的动态一致性、动作解释算子验证转移连贯性，以及基于LLM的反思模块生成纠正指导。在多阶段、接触丰富的真实机器人操作任务中，相比代表性VLA基线平均提升5.4%的任务成功率。

---

## 音频多模态

### [Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation](https://arxiv.org/abs/2606.26451)
**作者:** Neelam Saini, Sourav Ghosh | **方向:** 音频多模态 | **代码:** 无

本文提出MusicJudge框架，通过模态引导的多模态分析将歌词正确性与音高-节奏保真度相结合，实现自动演唱质量评估。该方法利用多信号匹配检测语义有意义的歌词块，并引入模态引导LoRA微调ASR以提升歌唱音频转录；实验表明其与人类专家评分具有高度一致性。

---

## 3D视觉语言

### [Depth-Semantic Alignment and Affinity-Guided Fusion for Structured Radar Point Cloud Generation](https://arxiv.org/abs/2606.26743)
**作者:** Amjad Hussain, Xin Qiu, Fuyuan Ai et al. | **方向:** 3D视觉语言 | **代码:** 无

本文提出一种基于视觉-雷达融合的多模态点云生成方法，利用图像语义信息对雷达点云施加结构约束并实现空间对齐，同时采用稀疏补全策略增强点密度并恢复缺失结构。实验表明生成点云可有效提升复杂环境下感知模型的检测精度与鲁棒性。

---

> 共收录 20 篇论文，涵盖 6 个方向
