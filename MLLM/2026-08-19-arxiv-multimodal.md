# Arxiv 多模态论文日报 · 2026-08-19

**日期**：2026 年 8 月 19 日  
**收录论文**：29 篇  
**含代码仓库**：11 篇  
**覆盖方向**：8 个

---

## VLM / MLLM

### [Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study](https://arxiv.org/abs/2608.17583)

**作者**：Hamidreza Saffari, Francesco Pierri  |  **方向**：VLM / MLLM  |  **代码**：暂无代码

本文以法国、意大利和瑞典的 TikTok 为对象，使用代表 13、16、19、40 岁四种年龄身份的虚拟账号，通过被动浏览与主动关键词搜索收集了 36,971 条视频，并利用多模态大模型进行规模化标注。研究发现，关键词搜索使有害内容占比升至 35%–56%，在 12 个国家-年龄组合中的 10 个里达到滚动基线的 1.5–7.5 倍，但这种激增是暂时的，并削弱了法国和瑞典原本的年龄差异。

[arXiv](https://arxiv.org/abs/2608.17583)

### [Code as Representation: A Compilable Parsing Paradigm for Academic Documents](https://arxiv.org/abs/2608.17550)

**作者**：Rihui Jin, Jun Wang, chengyuan zhu et al.  |  **方向**：VLM / MLLM  |  **代码**：[Code](https://github.com/AriKing11/CADP-Bench)

本文提出可编译学术文档解析范式 CADP，将完整学术页面重建为上下文 LaTeX 与可执行 Python，以保留表格、公式、图表、伪代码等结构化学术元素及其可执行图表表示。作者还构建了专家验证的 CADP-Bench，并通过重新注入编译协议评估，发现即便是前沿模型也难以生成高保真可执行重建。

[arXiv](https://arxiv.org/abs/2608.17550) / [GitHub](https://github.com/AriKing11/CADP-Bench)

### [SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment](https://arxiv.org/abs/2608.17514)

**作者**：Bishwash Khanal, Anlan Zhang, Sasu Tarkoma et al.  |  **方向**：VLM / MLLM  |  **代码**：暂无代码

本文提出 SE-MoLoRA，一种面向特定领域摄影评估的模块化参数高效适配框架，通过始终激活的共享 LoRA 专家与针对构图、光照、技术质量的路由适配器分离通用摄影知识与专家残差判断。在保留外样本评论生成任务上，SE-MoLoRA 的 BERTScore-F1 从 0.2317 提升至 0.4215，且在 84.6% 的成对比较中更受偏好，同时激活参数量少于独立专家模型。

[arXiv](https://arxiv.org/abs/2608.17514)

### [MS-MFAD : Multimodal large language models for Face Anti-spoofing Detection](https://arxiv.org/abs/2608.17328)

**作者**：Xiaoyong Yu, Rongzhen Li, Shuming Shi et al.  |  **方向**：VLM / MLLM  |  **代码**：暂无代码

本文提出面向统一人脸活体检测（UFAD）的多模态大语言模型 MFAD，通过细粒度像素-语义锚定机制激活 MLLM 的内在推理能力，并配套语义级标注基准。在 Qwen-VL 上的监督微调表明，仅使用有限高质量样本即可使域内 ACER 相对降低 40%–50%，并将跨域性能退化控制在 11.62%/5.23% 以内，显著优于现有框架。

[arXiv](https://arxiv.org/abs/2608.17328)

### [COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models](https://arxiv.org/abs/2608.17234)

**作者**：Md Abdullahil Oaphy, Anhao Xiang, Zongxing Xie et al.  |  **方向**：VLM / MLLM  |  **代码**：[Code](https://anonymous.4open.science/r/COMIC-E15D/)

本文识别了多模态大语言模型中依赖引用（reference-dependent）的安全失效模式：提示或图像单独无害，但模型将某项操作绑定到局部视觉目标时会产生不安全行为。为此提出 COMIC 预生成安全门控机制，通过推断操作与引用类型、构建候选目标并显式评估操作-目标对的安全性，在保持良性效用与效率的同时显著提升鲁棒性。

[arXiv](https://arxiv.org/abs/2608.17234) / [GitHub](https://anonymous.4open.science/r/COMIC-E15D/)

### [Which Source Wins? Task-Dependent Reliance in Vision-Language Models](https://arxiv.org/abs/2608.17205)

**作者**：Rodela Ghosh, Aviral Gupta, Guangjing Wang  |  **方向**：VLM / MLLM  |  **代码**：[Code](https://github.com/Ro-netizen004/multimodal-arbitration-artifact)

本文通过控制图像或文本的可读性退化，研究视觉语言模型在模态冲突时的依赖再分配行为，并基于 GSM8K、SVAMP 构建冲突样本，同时发布 229 条人工校验的 ChartQA-Conflict 基准。实验发现模态依赖并非固定，而是随任务、证据结构、模型与评估设置变化：在 GSM8K/SVAMP 上模型更倾向于远离退化的文本，而在 ChartQA-Conflict 上则呈现相反趋势。

[arXiv](https://arxiv.org/abs/2608.17205) / [GitHub](https://github.com/Ro-netizen004/multimodal-arbitration-artifact)

### [Uncertainty-Aware Decision Making in Multimodal Large Language Models](https://arxiv.org/abs/2608.17084)

**作者**：Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed  |  **方向**：VLM / MLLM  |  **代码**：暂无代码

本文围绕以决策为中心的框架综述了多模态大语言模型中的不确定性意识研究，涵盖不确定性来源、可观测信号、校准与风险控制，以及选择性回答、弃权、澄清、检索、自查与升级等系统动作。文章系统梳理了 token/logit 不确定性、语义分歧、扰动稳定性、 grounding、口头化置信度、验证器评分、共形预测等方法，并指出来源感知分解、动作感知基准、分布偏移下校准等开放问题。

[arXiv](https://arxiv.org/abs/2608.17084)

### [Clinical Pathways Matter for Multimodal Deep Learning in Early Alzheimers Disease Detection](https://arxiv.org/abs/2608.16962)

**作者**：Yao Lu, Solveig Kristina Hammonds, Alvaro Fernandez-Quilez  |  **方向**：VLM / MLLM  |  **代码**：暂无代码

本文提出基于 SigLIP 的零样本多模态框架，将结构 MRI 嵌入与常规收集的临床变量文本嵌入相结合，用于早期阿尔茨海默病风险分层。在 ADNI 416 名受试者上的评估显示，单次就诊时结合 MRI 与 MMSE、年龄、性别的 AUC 达 0.91，优于基于 CSF Aβ42 和仅基于 MMSE 的模型；两次就诊设置下性能保持稳定或进一步提升。

[arXiv](https://arxiv.org/abs/2608.16962)

## 多模态理解与推理

### [REChart: Reasoning-Efficient Chart Editing with Large Reasoning Models](https://arxiv.org/abs/2608.17414)

**作者**：Yuanbang Liu, Chenxi Ruan, Yihan Hou et al.  |  **方向**：多模态理解与推理  |  **代码**：暂无代码

本文提出 REChart，一个针对图表编辑的两阶段训练框架，通过为中间推理步骤提供过程级监督来提升编辑保真度与推理效率。首先利用 Reason-Score-Refine 智能体工作流合成 20 万条高质量推理轨迹进行监督微调，然后通过结合保真度奖励与随机推理预算截断的效率奖励进行强化学习；在 ChartEdit 与 ChartMIMIC 上达到同类规模开源模型的最优性能，同时平均推理 token 减少 79.0%。

[arXiv](https://arxiv.org/abs/2608.17414)

### [Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL](https://arxiv.org/abs/2608.17253)

**作者**：Yunhao Yang, Yuexin Bian, Yunjie Tian et al.  |  **方向**：多模态理解与推理  |  **代码**：[Code](https://github.com/DrStranded/Co-RL)

本文提出 Co-RL 框架，通过多智能体强化学习让多个参数解耦的模型基于同伴反馈的奖励同时优化，并利用异构模型家族、规模与重述样本提升队列多样性，从而在无真值监督的情况下涌现无监督推理能力。在文本与多模态任务上，Co-RL 不仅超越基线与先前无标签方法，还能匹配或超过监督方法。

[arXiv](https://arxiv.org/abs/2608.17253) / [GitHub](https://github.com/DrStranded/Co-RL)

### [Expressivity In Multimodal Contrastive Learning](https://arxiv.org/abs/2608.17203)

**作者**：Andrew Stuart, Florian Wolf  |  **方向**：多模态理解与推理  |  **代码**：暂无代码

本文从总体密度估计视角研究多模态对比学习的表达能力，证明双塔 CLIP 在两种模态下具有通用逼近性，而基于成对相似度求和的自然推广在三模态及以上无法表示任意联合分布。为此提出 Hadamard-CLIP，仅在现有编码器上增加一个可学习权重向量即可恢复任意模态数下的联合分布通用逼近能力，并保持 CLIP 快速预计算嵌入检索的优势。

[arXiv](https://arxiv.org/abs/2608.17203)

### [HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target Identification in Harmful Memes](https://arxiv.org/abs/2608.16622)

**作者**：Yujia Li, Yiqun Zhang, Zihan Cheng et al.  |  **方向**：多模态理解与推理  |  **代码**：[Code](https://github.com/llly1234/HarmTrace-for-Harmful-Memes)

HarmTrace 将有害模因检测从单一有害性分类拓展到细粒度目标识别，回答攻击目标类型、对象与位置。作者整合多个公开数据集构建 Meme3W，并提供人工校验的细粒度标注；同时提出严格的联合记录准确率（JRA）指标，要求有害性标签与所有目标识别字段同时正确。HarmTrace 采用锚点校准解耦优化框架增强目标实体监督，并通过条件目标识别策略优化（CTPO）解耦有害性与目标识别优势。实验表明其在多个主干上同时提升 JRA 与有害性准确率，其中 Qwen3-VL-8B 的 JRA 从 17.58% 提升至 52.51%。

[arXiv](https://arxiv.org/abs/2608.16622) / [GitHub](https://github.com/llly1234/HarmTrace-for-Harmful-Memes)

## 多模态基准与评测

### [BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models](https://arxiv.org/abs/2608.17895)

**作者**：Liubov Chubarova, Alexandra Kuleshova, Daniil Volkov et al.  |  **方向**：多模态基准与评测  |  **代码**：暂无代码

本文提出 BEAR-Bench，一个包含 1000 道人工标注问题的英俄双语基准，用于评估多模态大模型在文本密集的商业与学术专业文档上的推理能力，且不依赖外部领域知识。作者在 16 个闭源与开源 MLLM 上进行了评测，发现即便是最强模型仍存在明显提升空间，并进一步利用模型输出比较了现有幻觉检测方法的有效性。

[arXiv](https://arxiv.org/abs/2608.17895)

### [TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation](https://arxiv.org/abs/2608.16765)

**作者**：Haoran Wang, Chaofan Ma, Ran Yi et al.  |  **方向**：多模态基准与评测  |  **代码**：[Code](https://github.com/Amuseum-WHR/TraceBench)

TRACE-Bench 从能力视角出发，为多参考图像生成形式化定义了锚定、解耦、应用与组合四类算子，并据此构建了约 1,600 个评测用例。基于公式结构实现了与算子对齐的评分协议和递归诊断树，可定位失败根因。对 9 个领先模型的评估表明，瓶颈在于解耦与属性绑定，而非场景级组合；即便最佳模型在属性保真度上也仅得 0.74。

[arXiv](https://arxiv.org/abs/2608.16765) / [GitHub](https://github.com/Amuseum-WHR/TraceBench)

### [PersonaShot: Benchmarking Person-Centric Narrative Continuity in Multi-Shot Video Generation](https://arxiv.org/abs/2608.16717)

**作者**：Yuji Wang, Yuheng Chen, Teng Hu et al.  |  **方向**：多模态基准与评测  |  **代码**：暂无代码

PersonaShot 是首个面向多镜头视频生成中以人物为中心的叙事连续性评测基准，包含约 1,000 个多镜头片段与覆盖物理连续性、情感动态和电影语法三个维度的 16 项指标。作者将大型多模态教师的推理能力蒸馏为多个轻量级、面向具体指标的评测器，使其依据视觉、时序或关系证据进行判断，并与专家人工标注对齐。评测显示，各前沿模型在不同维度能力差异明显，感知质量与跨镜头叙事连续性之间存在显著差距。

[arXiv](https://arxiv.org/abs/2608.16717)

### [AnchorScore: A CLIP-Based Diagnostic of MLLM Annotation Difficulty](https://arxiv.org/abs/2608.16690)

**作者**：Yan Ma, Lizhuo Zhang  |  **方向**：多模态基准与评测  |  **代码**：暂无代码

AnchorScore 是一种基于 CLIP 的先验诊断指标，用于预判多模态大语言模型在自动标注中哪些类别更容易出错。在课堂行为数据上，AnchorScore 与逐类 MLLM 准确率显著相关（Spearman rho=0.769），在 Stanford40 Actions 独立复现中亦得到接近效应（rho=0.817）。该指标可支撑三项应用：可部署的 CLIP/MLLM 混合路由策略（在节省约 44% MLLM 成本的同时提升 23 个百分点）、难类提示消歧，以及人工复核优先级预测。

[arXiv](https://arxiv.org/abs/2608.16690)

## 多模态检索与信息抽取

### [LAVA: Logic-Aware Validation and Augmentation Framework for Large-Scale Financial Document Auditing](https://arxiv.org/abs/2608.16763)

**作者**：Ruoqi Shu, Xuhui Wang, Isaac Wang et al.  |  **方向**：多模态检索与信息抽取  |  **代码**：暂无代码

LAVA 是一个模块化、主干无关的金融文档逻辑感知验证与增强框架，基于多模态大语言模型实现文档规则检索、版式保持信息抽取、辅助元数据增强和可审计的符号/算术验证四阶段流程。该框架支持规则接地、细粒度错误归因和一致的端到端可追踪执行。在包含多种金融文档与数十条专家规则的大规模真实基准上，LAVA 在抑制幻觉和处理边界案例方面优于基线，同时保持较高的 token 效率。

[arXiv](https://arxiv.org/abs/2608.16763)

### [Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement](https://arxiv.org/abs/2608.16628)

**作者**：Shenao Chen, Yidan Xu, Xiangmin Han et al.  |  **方向**：多模态检索与信息抽取  |  **代码**：[Code](https://github.com/ShenAoChen2001/MMHRAG)

Hyper-M2RAG 提出基于高阶超图表示学习的多模态检索增强生成框架，利用超边作为统一语义容器来编码文本、图像与表格之间的多元关联，以克服传统简单图二值连接范式的局限。针对物理分页导致的语义碎片化问题，作者提出锚点驱动的增量细化机制，通过识别跨页锚点并利用其一阶邻域重建局部超图拓扑。在多个多模态基准上的实验表明，该方法在检索精度与生成连贯性上均显著优于现有最优方法。

[arXiv](https://arxiv.org/abs/2608.16628) / [GitHub](https://github.com/ShenAoChen2001/MMHRAG)

## Agent 与具身智能

### [Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies](https://arxiv.org/abs/2608.17484)

**作者**：Yuhwan Jeong, Kuk-Jin Yoon  |  **方向**：Agent 与具身智能  |  **代码**：暂无代码

本文定义了可恢复余量与检索互补性两个概念，用于刻画冻结 VLA 策略在测试时可通过采样自身行为恢复多少性能，以及外部动作先验能填补多大缺口。实验表明，基于回合的重试选择器在 LIBERO 的多种 VLA 主干上稳定恢复大量潜在能力，最高提升 21.0 个成功率点，且可迁移到不同机器人与模拟器；检索则在动作先验缺口最大的策略上带来额外增益。

[arXiv](https://arxiv.org/abs/2608.17484)

### [DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation](https://arxiv.org/abs/2608.17282)

**作者**：Xing Wei, Changmeng Zheng, XiaoYong Wei et al.  |  **方向**：Agent 与具身智能  |  **代码**：暂无代码

本文提出 DeAR（去中心化智能体推理）框架，通过去中心化能力定位、思维图导航和拓扑更新三种机制，使多个智能体能够自主进行点对点协作，从而替代集中式路由与固定角色分配。在 9 个多模态推理与文本问答基准上的实验表明，DeAR 持续优于近期基线方法。

[arXiv](https://arxiv.org/abs/2608.17282)

### [Teach and Grow: An Agent-Centered Architecture for General Robot Learning](https://arxiv.org/abs/2608.17209)

**作者**：Chang Nie, Zhe Liu, Hesheng Wang  |  **方向**：Agent 与具身智能  |  **代码**：暂无代码

本文提出 Teach-and-Grow Learning（TGL）这一以智能体为中心的通用机器人学习架构，将少量成功演示转化为可复用的 Skill Blocks，并在新场景中完成 grounding、组合、工具选择与执行反馈后的路径修正。在 LIBERO 基准上取得最优性能，并通过控制实验验证了技能归纳、持续复用与智能体自主适应能力。

[arXiv](https://arxiv.org/abs/2608.17209)

### [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885)

**作者**：Xiaowei Cai, Yunuo Cai, Bingao Chen et al.  |  **方向**：Agent 与具身智能  |  **代码**：[Code](https://github.com/sii-research/tau-0-vla)

τ₀-VLA 是一种面向长程机器人操作的分层式基础模型，将高层子任务生成建模为可扩展推理问题，并在执行记忆中通过世界模型引导的测试时搜索来权衡多种备选子任务后再决策。底层策略负责将生成子任务在多种机器人本体上闭环执行。模型在 40,115 小时异构真实数据上多模态协同训练，额外推理计算显著提升了下一子任务预测精度，并转化为长程任务成功率的提升。

[arXiv](https://arxiv.org/abs/2608.16885) / [GitHub](https://github.com/sii-research/tau-0-vla)

### [Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation](https://arxiv.org/abs/2608.16843)

**作者**：Jiawei Liu, Jiacheng Guo, Tian Zhang et al.  |  **方向**：Agent 与具身智能  |  **代码**：暂无代码

本文从信任边界视角系统综述了基础模型赋能的具身智能体安全，依据“首个被攻破的信任边界”原则将攻击面与攻击机制解耦，并划分为 5 层 12 个攻击面。基于截至 2026 年 8 月的 58 条攻击记录与 61 条防御记录，作者分析了典型攻击、跨层传播、防御部署与评估实践。最后指出了状态溯源、组合防御、长程攻击传播、物理可实现性、拜占庭多机器人行为与统一闭环评估等开放挑战。

[arXiv](https://arxiv.org/abs/2608.16843)

## 多模态生成

### [Where a New Concept Must Enter: Entry Point Gates Cross-Task Usability in Unified Multimodal Models](https://arxiv.org/abs/2608.17564)

**作者**：Zongyang Qiu, Yihan Wu, Kaixuan Fan et al.  |  **方向**：多模态生成  |  **代码**：[Code](https://github.com/Zane-ZYQiu/entry-point-umm)

本文通过构造只在单一任务方向上绑定新视觉概念（渲染 3D 资产与伪词）的实验，分离统一多模态模型中的理解与生成目标。研究发现概念迁移的双向通道真实存在，但生成训练使模型只能做候选匹配，而理解训练使其能够主动生成；进一步提出中间层对齐目标，可在仅牺牲 0.1% 文本到图像能力的情况下获得新概念，远低于标准生成路径的 41%。

[arXiv](https://arxiv.org/abs/2608.17564) / [GitHub](https://github.com/Zane-ZYQiu/entry-point-umm)

### [SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version](https://arxiv.org/abs/2608.17164)

**作者**：Tuan-Binh Tran, Dat Nguyen Cong, Duc-Trong Le et al.  |  **方向**：多模态生成  |  **代码**：[Code](https://anonymous.4open.science/r/ScenarioDiff_ICDM-2C4C)

本文提出 SCENARIODIFF，一种面向含噪且弱对齐文档的多模态时间序列预测分层上下文推理框架，通过历史上下文、场景与锚点引导三个层级组织文本信息，并用其约束多模态扩散 Transformer，同时以 Anchor Blended Sampling 在无需重训练的情况下局部优化生成轨迹。Time-MMD 实验表明该方法在事件驱动领域尤为有效。

[arXiv](https://arxiv.org/abs/2608.17164) / [GitHub](https://anonymous.4open.science/r/ScenarioDiff_ICDM-2C4C)

## 音频多模态

### [UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource Music Understanding](https://arxiv.org/abs/2608.17852)

**作者**：Ziya Zhou, Shangda Wu, Shenyang Xu et al.  |  **方向**：音频多模态  |  **代码**：[Code](https://github.com/SylviaZiyaZhou/UniVerse)

本文提出 UniVerse 框架，包含覆盖 38 个以上文化与语言实体的 5042 个问答对基准 UniVerseBench，以及自动化生成的多轮对话训练集 UniVerseSet，用于低资源音乐理解。实验表明，结合自动化数据整理与不平衡感知训练可在稠密和 MoE 架构上带来非平凡提升，但模型仍难以捕捉细粒度声学特征。

[arXiv](https://arxiv.org/abs/2608.17852) / [GitHub](https://github.com/SylviaZiyaZhou/UniVerse)

### [Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](https://arxiv.org/abs/2608.17102)

**作者**：Xiutian Zhao, Luqi Sun, Björn Schuller et al.  |  **方向**：音频多模态  |  **代码**：暂无代码

本文在多模态基础模型中探究情绪敏感神经元（ESNs），发现视觉 ESN 具有因果意义：抑制其激活会选择性损害对应面部情绪识别，而引导其激活可增强识别；听觉与视觉 ESN 在情绪匹配上存在重叠且层间分布相似，跨模态干预还呈现双向因果迁移。结果表明多模态基础模型对语音与面部情绪的识别至少部分共享情感功能单元。

[arXiv](https://arxiv.org/abs/2608.17102)

### [Closing the Affective Loop: Multimodal Speaker-Listener Emotion-Dynamics-Aware Empathetic Social Robots](https://arxiv.org/abs/2608.16686)

**作者**：Zi Haur Pang, Casey Kennington, Tatsuya Kawahara  |  **方向**：音频多模态  |  **代码**：暂无代码

AffectLoop 是一个部署于 Misty II 社交机器人的多模态说话人-倾听者情感动态感知对话系统。系统同时追踪说话人的言语与面部情感动态，并估计机器人倾听者自身的言语与行为情感状态，进而将两者共同作为条件输入大语言模型生成共情回复。机器人据此输出简短口语回应并配合情感一致的具身行为，形成闭合的情感反馈环路；初步用户研究显示其在整体印象、共情回应与用户满意度方面获得更高评分。

[arXiv](https://arxiv.org/abs/2608.16686)

## 3D 视觉语言

### [NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting](https://arxiv.org/abs/2608.17447)

**作者**：Hao Qin, Yukai Sun, Luyuan Chen et al.  |  **方向**：3D 视觉语言  |  **代码**：暂无代码

本文提出 NGS-Marker，一种面向 3D Gaussian Splatting 的原生水印框架，通过联合训练的水印注入器与消息解码器，并采用基于梯度的渐进式注入策略实现全场景覆盖。该方法还支持混合保护（原生与间接水印结合）以及多模态水印，为 3DGS 原始高斯原体的版权保护提供了新方案。

[arXiv](https://arxiv.org/abs/2608.17447)

---

**统计**：本次共收录 2026-08-19 前后 2 天内（2026-08-17 至 2026-08-18）提交的 29 篇多模态相关论文，其中 11 篇提供了代码或项目链接。
