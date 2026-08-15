# Arxiv 多模态论文日报 - 2026-08-15

覆盖日期：**2026-08-13 至 2026-08-14** ｜ 收录论文：**39** 篇 ｜ 含代码仓库：**13** 篇 ｜ 覆盖方向：**7** 个

## VLM / MLLM

### [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505)
**作者：**Lei Bai, Jiaqi Cao, Chiyu Chen et al. ｜ **方向标签：**VLM / MLLM、Agent ｜ **代码：**暂无代码

Intern-S2-Preview 是一系列面向科学发现的多模态智能体基础模型，通过科学多模态预训练、SFT、多任务 RL、智能体 RL 与蒸馏提升科学理解、推理与生成能力。397B 主模型结合记忆解码器在多项科学/多模态/智能体基准上取得领先，时间序列模块在 SciTS 上提升信号理解与预测。

### [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](https://arxiv.org/abs/2608.13463)
**作者：**Daniel Perkins, John Squires, Janou Milligan et al. ｜ **方向标签：**VLM / MLLM、推理 ｜ **代码：**暂无代码

ARMDIL 利用多模态大语言模型作为自适应路由器，根据输入图像动态选择最合适的视觉骨干网络，实现跨数据集图像分类的异构集成。实验表明该方法在多个视觉域上具有竞争力，并可通过提示修改快速集成新信息。

### [Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs](https://arxiv.org/abs/2608.12911)
**作者：**Beining Xu, Hairui Wang, Jiaxin Wang et al. ｜ **方向标签：**VLM / MLLM、检索 ｜ **代码：**[GitHub](https://github.com/xubeining/Beyond-Visual-Evidence)

该文揭示文档 MLLM 在视觉证据不足时会依赖训练数据记忆的关系推断敏感字段，导致隐私泄露。提出动态关系遗忘框架 DRUF 与 DocPrivacyBench 基准，在抑制泄露的同时保持 KIE 性能，较最强基线提升 4.8 个百分点的泄露抑制。

### [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](https://arxiv.org/abs/2608.12904)
**作者：**Yunhao Bai, Zhongwei Qiu, Guangyu Guo et al. ｜ **方向标签：**VLM / MLLM、3D ｜ **代码：**[GitHub](https://github.com/byhwhite/HounsWorld)

HounsWorld 是面向 CT 的多模态世界模型，将体积扫描与临床语言视为共享患者状态的观测，统一实现状态读取、报告重建与条件化 CT 生成。在 HounsBench 上，3B 模型在三类任务中均表现强劲，验证了临床结构化补全对 CT 理解的提升。

### [PolyPresentation: A Multimodal AI Platform for Slide-Aware Iterative Presentation Practice](https://arxiv.org/abs/2608.12857)
**作者：**Chen Chen, Jihao Li, Zhiyuan Wen et al. ｜ **方向标签：**VLM / MLLM、Agent ｜ **代码：**暂无代码

PolyPresentation 是多模态 AI 演示练习平台，围绕幻灯片组织逐页练习、完整排练、观众问答与反馈循环，利用幻灯片 grounding 证据帮助讲者诊断问题并规划下一轮练习。评估显示其反馈更具可操作性与上下文感知。

### [Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors](https://arxiv.org/abs/2608.12746)
**作者：**LingKai Bu ｜ **方向标签：**VLM / MLLM、推理 ｜ **代码：**暂无代码

DSCC 首次在微调阶段将对象级视觉锚点注入语言模型，通过感知流与认知流的双向交互约束每步生成的证据检索。实验显示其在长描述低幻觉区域达到 88.19% 对象提及精度，长度约为基线 1.9 倍，并揭示了锚点语义域的条件性。

### [A Cloud-Edge System for Multimodal Clinical Screening in Resource-Constrained Rural Settings](https://arxiv.org/abs/2608.12745)
**作者：**Hei Ting, Chan, Chenwei Wu et al. ｜ **方向标签：**VLM / MLLM、Agent ｜ **代码：**暂无代码

该云-边协同系统将边缘轻量专科模型与云端 LLM 结合，通过 LLM 编排器动态选择诊断工具，在 20 个多模态临床病例上实现 98-99% 工具召回率与 92-96% 精确率，在带宽受限环境下以 4-15 倍更低 token 成本保持与纯云方案相当或更高的临床准确率。

### [The Role of Natural Language Understanding in Multimodal Video-Based Dengue Diagnosis](https://arxiv.org/abs/2608.12677)
**作者：**Danial Sharifrazi, Saadat Behzadi, Julakha Jahan Jui et al. ｜ **方向标签：**VLM / MLLM、检索 ｜ **代码：**暂无代码

该研究提出基于 YOLO 与 CLIP 的视觉-语言框架，通过双向对比学习对齐蚊子飞行帧与生物学文本提示，用于区分未感染与登革热病毒感染蚊子。在帧级达到 98.54% 准确率与 99.91% 灵敏度，文本分支主要提供语义对齐而非直接提升视觉精度。

### [From Visual Widgets to UI Code: Efficient Tool-Grounded Generation](https://arxiv.org/abs/2608.12611)
**作者：**Houston H. Zhang, Tao Zhang, Li Gu et al. ｜ **方向标签：**VLM / MLLM、生成 ｜ **代码：**暂无代码

WidgetGen 提出轻量工具 grounding 框架，从视觉 widget 中提取可观测文本与颜色证据，进行高层布局与可选图表推理，直接生成可执行 JSX。在 1000 个 held-out widget 上优于直接提示与结构化 Widget2Code 流程，SFT 后提升 Qwen 系列模型各项指标。

### [Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Inference Overhead via Decoupled Embedding Prediction](https://arxiv.org/abs/2608.12209)
**作者：**Zhongbin Guo, Jiahao Xie, Dongling Xiao et al. ｜ **方向标签：**VLM / MLLM、生成 ｜ **代码：**暂无代码

GAS 将视觉生成重新解释为表征学习的辅助监督，在解耦的 MoT 架构中通过 Next Embedding Prediction 使生成损失增强共享视觉路径的空间精度与视觉保持力，训练后丢弃生成分支实现零推理开销。实验持续提升多模态理解，尤其在感知与空间理解任务上。

### [Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization](https://arxiv.org/abs/2608.12158)
**作者：**Byungoh Ko, Jinyoung Park, Jongha Kim et al. ｜ **方向标签：**VLM / MLLM、推理 ｜ **代码：**暂无代码

该文提出 Contextual Preference Gain 指标衡量 MLLM 在提供上下文后偏好增强的程度，发现标准 DPO 对上下文利用不足。提出的 C²-DPO 直接最大化 CPG 同时保持原始偏好顺序，在 Qwen2-VL-Instruct-2B 上相对降低 Object HalBench 幻觉率 36%。

## 多模态理解与推理

### [When Is a Task Vector Enough? An Empirical Theory of Implicit Multimodal ICL](https://arxiv.org/abs/2608.13385)
**作者：**Jiaqian Li ｜ **方向标签：**推理、VLM / MLLM ｜ **代码：**暂无代码

本文提出 Selection-Realization 假设，解释隐式多模态上下文学习中将示例压缩为任务向量的条件。通过控制任务与反事实示例对比，发现静态任务向量的有效性取决于示例诱导变化在查询间的共享程度，当存在查询特定结构时需要更复杂的干预。

### [TennisVAR: A Stroke-Evidence-Grounded Multimodal Large Language Model for Tactical Reasoning in Tennis Videos](https://arxiv.org/abs/2608.12920)
**作者：**Yifan Mei, Qingling Shi, Changli Wu et al. ｜ **方向标签：**推理、VLM / MLLM ｜ **代码：**暂无代码

TennisVAR 提出基于击球证据链的网球战术推理模型，构建 TRACE 基准包含 11189 个回合视频与 41485 个击球事件。模型通过事件解析模块与战术图引导时序推理联合建模回合进程与决策依赖，生成开放式答案、战术标签与证据链。

### [Falsehood and Impossibility Are Different Directions in an AI's Representation of Language](https://arxiv.org/abs/2608.12852)
**作者：**Yoon Pyo Lee ｜ **方向标签：**推理、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/sixticket/representing-the-impossible)

本文以多模态模型 Gemma 3 4B IT 为对象，探索模型内部对偶然假言与必然不可能的区分。激活分析显示真值方向与不可能性方向接近正交，不可能性方向更接近语义异常方向，为语言哲学中的经典区分提供了实证注脚。

## 多模态基准与评测

### [Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ](https://arxiv.org/abs/2608.13441)
**作者：**Zongyun Zhang, Jiacheng Ruan, Xian Gao et al. ｜ **方向标签：**基准、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/Solunny/Edit2TikZ)

Edit2TikZ 是首个面向科学图表代码编辑的综合基准，包含 1548 个真实与合成样本，支持文本/视觉定位与多步编辑。对 14 个主流 MLLM 的评估显示当前模型在编译成功率与编辑正确性上仍不可靠，基于 TikZEditMix 的课程学习在 Qwen3.5-4B 上将编译成功率从 45.35% 提升至 83.40%。

### [EgoMonth: A Month-Level Egocentric Video Benchmark for Long-Term Spatiotemporal Memory](https://arxiv.org/abs/2608.13113)
**作者：**Weitao Chen, Hu Jiaxin, Xie Tianyidan et al. ｜ **方向标签：**基准、推理 ｜ **代码：**暂无代码

EgoMonth 是首个月级第一人称视频理解基准，包含 300 多小时、20 名参与者、20-120 天的录像与 1443 道选择题。其 14 项任务评估模式显示当前最强模型 Gemini 2.5 Pro 仅达 71.8% 准确率，显著低于人类基线 94.2%，表明现有 MLLM 仍缺乏真正的长程时空记忆。

### [Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs](https://arxiv.org/abs/2608.12781)
**作者：**Xinming Wang, Weinong Wang, Hongming Yang et al. ｜ **方向标签：**基准、推理 ｜ **代码：**暂无代码

PatternEval 是面向混合思考 MLLM 的诊断基准，关注 chain-of-thought 泄露、重复、逻辑矛盾与表演式推理等响应模式失败。实验显示非思考接口的失败率显著更高，提出的 PatternRM 与 PatternRL 可在轻微牺牲任务性能的同时缓解跨模式错位。

### [Does It Render Everywhere? A Study of Cross-Environment Compatibility in MLLM-Generated Webpages](https://arxiv.org/abs/2608.12518)
**作者：**Ziyun Guo, Jingyu Xiao, Yuqiang Sun et al. ｜ **方向标签：**基准、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/ZiyunGuo/WebCompat)

该文构建 WebCompat 数据集，系统研究 MLLM 生成网页在 9 种浏览器-设备组合下的跨环境渲染兼容性，发现 68% 网页存在兼容性问题。提出的 XCompat 离线检测器结合视觉截图与 DOM 结构，在 WebCompat-test 上取得 F1 0.903。

### [Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams](https://arxiv.org/abs/2608.12262)
**作者：**Weihao Bo, Shan Zhang, Yanpeng Sun et al. ｜ **方向标签：**基准、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/AIGrounding/Diagram-MMU)

Diagram-MMU 是面向科学图表的多模态基准，包含 3.7k 图表与 18.3k 人工验证问题，评估图转代码、图编辑与图问答三类任务。对 12 个 MLLM 的测试显示图转代码任务比图问答更具挑战，智能体设置可提升解析与编辑但可能降低问答性能。

## 多模态检索与信息抽取

### [TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](https://arxiv.org/abs/2608.13495)
**作者：**Yi-Chung Chen, Philip Jacobson, Tom Lampo et al. ｜ **方向标签：**检索、VLM / MLLM ｜ **代码：**暂无代码

TraVEL 针对驾驶视频检索中的运动感知不足问题，提出以 ego-trajectory 相似度作为 GRPO 奖励的轨迹引导视频嵌入学习方法。检索阶段仅依赖单向量视频嵌入，无需 ego 位姿或感知输出。在 nuReasoning 构建的检索基准上，纵向与横向 mAP 在 2B 模型分别提升 9.8 与 4.7 个点。

### [Generative Universal Multimodal Retrieval with Dual-role Identifiers](https://arxiv.org/abs/2608.12987)
**作者：**Kaipeng Li, Haitao Yu, Xuanchen Zhou ｜ **方向标签：**检索、VLM / MLLM ｜ **代码：**暂无代码

DrIG 提出基于双角色标识符的生成式通用多模态检索框架，单个残差量化标识符同时支持自回归解码与集合式相关性先验，缓解前缀错误与局部最优。在 M-BEIR 与文搜图任务上超越现有生成式多模态基线，并通过混合重排序逼近稠密检索效果。

### [Heterogeneous Vision-Language Ensemble with Disagreement-Aware Reranking for Text-Based Person Anomaly Retrieval](https://arxiv.org/abs/2608.12843)
**作者：**Huu-An Vu, Cam Tu Tran Thi, Thanh Toan Le Ngo et al. ｜ **方向标签：**检索、VLM / MLLM ｜ **代码：**暂无代码

该方案针对文本描述检索异常行人，提出异构视觉-语言模型集成与分歧感知 VLM 重排序。在 PAB 基准上达到 90.92% mAP 与 85.13% Recall@1，证明互补视觉-语言表示结合选择性多模态推理的有效性。

### [EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory](https://arxiv.org/abs/2608.12627)
**作者：**Le Zhang, Ke Sun ｜ **方向标签：**检索、Agent ｜ **代码：**暂无代码

EgoCITE 面向长程第一人称记忆，提出上下文增强索引 EgoScheme 与时间感知检索 EgoRetrv，将碎片化视频字幕与语音转录转为自包含原子记忆索引。在 EgoLifeQA、EgoMem 与 EgoR1-Bench 上提升 4.4-14.2% 准确率，成本仅为长上下文 LLM 智能体的 1/36。

### [Attribute-Conditioned Multimodal Slot Factorization for Controllable Fashion Retrieval](https://arxiv.org/abs/2608.12570)
**作者：**Najmeh Forouzandehmehr, Topojoy Biswas, Evren Korpeoglu et al. ｜ **方向标签：**检索、VLM / MLLM ｜ **代码：**暂无代码

MM-slotgate 将 Fashion-CLIP 文本与图像嵌入分解为四个命名属性槽，每个槽学习独立的文本-图像门控，使颜色等视觉属性更多依赖图像证据，类别等更多依赖文本。在 H&M 上 ConstraintSatisfied@10 达到 0.7566，颜色检索从 0.321 提升至 0.889，并支持可解释的量化干预。

## Agent 与具身智能

### [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560)
**作者：**Yaxin Luo, Haobin Jiang, Jialv Zou et al. ｜ **方向标签：**Agent、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/Yaxin9Luo/AutoDesign)

AutoDesign 提出面向长程智能体设计的元 harness 优化框架，通过代码智能体根据 rollout 反馈递归改进设计 harness。在学术论文转海报任务中构建 PosterBench 基准，AutoDesign 在主流指标上超越 Claude Design 7.45 分，并能以低于 3 美元成本生成接近会议海报质量的结果。

### [UniTraffic-Agent: Unified Traffic Video Reasoning for AI City Challenge 2026 Track 3 with Two Out-of-Domain Evaluations](https://arxiv.org/abs/2608.13031)
**作者：**Peng Li, Qianqian Xu, Shilong Bao et al. ｜ **方向标签：**Agent、推理 ｜ **代码：**[GitHub](https://github.com/Roclp/UniTraffic-Agent)

UniTraffic-Agent 面向交通视频推理，采用 observe-reason-act-verify 流程处理异常推理、鱼眼事件与行人意图三类任务。在 AI City Challenge 2026 Track 3 的公开榜单上取得 TAR 第 16、FETV 第 2、PSI-VQA 第 4 的成绩。

### [ARIES-Mission2: A Zero-Shot Vision-Language-Action Framework for Fast Large-Scale Aerial Mission Generation](https://arxiv.org/abs/2608.12763)
**作者：**Junhao Wei, Yanxiao Li, Haochen Li et al. ｜ **方向标签：**Agent、VLM / MLLM ｜ **代码：**暂无代码

ARIES-Mission2 是面向低空无人机的零样本 VLA 框架，将视觉语义感知与物理路径优化解耦，通过 VLM 目标定位与 TSP 求解生成 GPS 航点。在 UAV-VLPA-nano-30 上较未优化 VLA 基线缩短航程 21.6%，速度约为人工规划的 3.6 倍。

### [Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence](https://arxiv.org/abs/2608.12743)
**作者：**Haokai Zhang, Yuhang Ding, Yunshu Zhou et al. ｜ **方向标签：**Agent、推理 ｜ **代码：**暂无代码

Spatial Memory Agent 提出无参数更新的 VLM 智能体自演化框架，在可验证空间环境中通过验证器引导反思提取可迁移经验，并基于 Transfer Reliability Score 进行检索。在 5 个空间基准与 4 个基础 VLM 上均取得最佳宏观平均，展示了空间智能的实际提升路径。

### [Auditable agentic AI for evidence-grounded thyroid ultrasound diagnosis and reporting](https://arxiv.org/abs/2608.12590)
**作者：**Haifan Gong, Shiyu Chen, Bodong Wang et al. ｜ **方向标签：**Agent、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/MedXAgent/ThyroidXAgent)

ThyroidXAgent 是面向甲状腺超声的临床可审计智能体系统，协调分割、分类、淋巴结转移预测与报告生成工具，在 OpenThyroidDB 与多中心测试集上取得结节分割 Dice 87.21% 与良恶性分类 AUROC 0.9466。该系统提升医生分类准确率并将报告一致性从 70.3% 提高到 86.2%。

### [Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence](https://arxiv.org/abs/2608.12290)
**作者：**Aman Tyagi, Hemanth Boinpally, Jonathan Chen et al. ｜ **方向标签：**Agent、生成 ｜ **代码：**暂无代码

本文将图生视频合成重构为闭环目标导向优化，第一阶段用多模态 LLM 迭代优化提示并通过 DSG 与 CMQ 评估语义一致性与伪影，第二阶段用贝叶斯优化联合搜索随机种子与 CFG。人类偏好研究显示该方法胜率最高达 69%，显著提升生成可控性。

### [GUIDE: Governed Unified Intelligence for Document-to-Artifact Generation in Enterprise Settings](https://arxiv.org/abs/2608.12133)
**作者：**Shivali Dalmia, Sumukha Thoppanahalli, Mohammadreza Sediqin et al. ｜ **方向标签：**Agent、VLM / MLLM ｜ **代码：**暂无代码

GUIDE 是面向企业指南文档的多智能体框架，基于共享版本规则存储与模式验证的代理间契约，通过解析、VLM 提取、一致性检查、评估、HITL 升级与工件合成六个智能体，在 120 份真实文档上实现 96% 文档成功率，将周转时间从 2-3 天缩短至 40-125 分钟。

## 多模态生成

### [Towards Physics-Faithful Generation of Scientific Diagrams](https://arxiv.org/abs/2608.13112)
**作者：**Minghui Zhang, Jinxin Shi, Yifan Chang et al. ｜ **方向标签：**生成、推理 ｜ **代码：**暂无代码

Princigram 提出结构化物理思维链 SP-CoT，将物理图表生成分解为场景识别、受力/过程分析、控制方程到合成的多步推理，并构建 430 万物理图像与 VeriphyT2IBench 评估。实验证明显式物理结构化监督显著提升生成科学图表的物理忠实度。

### [P2Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation](https://arxiv.org/abs/2608.13045)
**作者：**Yi Shi, Huichao Xie, Yuqing Wang et al. ｜ **方向标签：**生成、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/YiShi99/P2Fusion)

P2Fusion 通过可学习的动态提示将热显著性与空间质量两种图像内在先验蒸馏为红外-可见光图像融合的指导，并引入 Teach-to-Fuse 机制与 GDER 模块实现专家化解耦。在 5 个数据集 20 项指标中 14 项达到 SOTA，并在目标检测下游任务中提升 mAP。

### [Semantic Steering for Controllable Generation: Tuning-Free Concept Erasure in Multimodal Diffusion Transformers](https://arxiv.org/abs/2608.12829)
**作者：**Qiao Li, Xiaomeng Fu, Yuanshu Zhao et al. ｜ **方向标签：**生成、VLM / MLLM ｜ **代码：**暂无代码

针对 MM-DiT 的安全生成问题，本文发现文本条件语义表示在中间块最显著，提出从中间块提取目标概念与安全概念构建 steering vector 并注入前中层。该方法无需训练即可实现高效概念擦除，在多个 MM-DiT 模型上达到 SOTA 并抵御对抗攻击。

### [Represent, Then Generate: Multimodal-Conditioned Time-Series Generation under Irregular Missingness](https://arxiv.org/abs/2608.12592)
**作者：**Haochen Zhang, Jiaheng Guo, Yu-Chao Huang et al. ｜ **方向标签：**生成、VLM / MLLM ｜ **代码：**暂无代码

ReCoGen 提出两阶段多模态条件时间序列生成框架，先用掩码自编码器将各模态条件压缩为缺失鲁棒的 token 序列，再用流匹配生成器融合静态条件生成目标信号。在 AI-READI 血糖与 MIMIC 血压生成任务上 16 项设置全部最佳，其中 13 项达到或超过真实信号的下游效用。

## 音频多模态

### [Reasoning for Social Audio-Visual Question Answering: Where Do We Stand?](https://arxiv.org/abs/2608.13239)
**作者：**Koen P. de Vries, Xavier Alameda-Pineda, Estefanía Talavera et al. ｜ **方向标签：**音频、推理 ｜ **代码：**[GitHub](https://github.com/koenv759/IntentBench-Prime)

该文针对社交场景音频视觉问答，清理并发布 IntentBench-Prime，发现简单 Vanilla SFT 基线即可匹敌或超越现有 CoT 推理方法，且仅用文本字幕替代视频也能达到相近性能，揭示了当前 MLLM 在社交理解上的局限。

### [CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](https://arxiv.org/abs/2608.13101)
**作者：**Nhan Phan, Ilona Lähteenmäki, Anna von Zansen et al. ｜ **方向标签：**音频、VLM / MLLM ｜ **代码：**[GitHub](https://github.com/aalto-speech/CASA)

CASA 将 Whisper-medium 与 Qwen3.5-2B 结合用于自动口语评估，在 Speak & Improve Corpus 2025 上以约一半参数取得 RMSE 0.358 的 SOTA，并分离语音传达与内容贡献以提升可解释性。

### [Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences](https://arxiv.org/abs/2608.12615)
**作者：**Cosmin Dragoiu, Nooshin Nabizadeh ｜ **方向标签：**音频、生成 ｜ **代码：**暂无代码

Drive-to-Music 是面向车载场景的多模态音乐生成系统，结合行车记录仪图像与车辆遥测提取驾驶场景语义，映射为高层音乐描述并实时生成与上下文对齐的配乐。系统支持低延迟生成与平滑过渡，展示了个性化车载音频体验的可行性。

### [The SLT 2026 SmartGlasses Challenge: Benchmarking Egocentric Multi-Talker Speech Recognition and Understanding with Audio-Language Models](https://arxiv.org/abs/2608.12034)
**作者：**Dehui Gao, Zhixian Zhao, Zhennan Lin et al. ｜ **方向标签：**音频、基准 ｜ **代码：**[GitHub](https://github.com/ASLP-lab/Smart-Glass-Challenge)

SLT 2026 SmartGlasses Challenge 是面向智能眼镜的多说话人语音识别与理解的共享任务，包含 106 小时四通道第一人称语音数据，评估带时戳说话人归属 ASR 与口语语言理解。结果显示严重说话人重叠仍是 TSA-ASR 的主要难点，副语言声学理解对现有音频-语言模型仍具挑战。

---

**论文总数统计：** 本报告共收录 39 篇多模态相关论文，其中 13 篇提供公开代码仓库，覆盖 7 个研究方向。
