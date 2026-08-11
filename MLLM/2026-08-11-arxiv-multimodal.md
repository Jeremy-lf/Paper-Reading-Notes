# Arxiv 多模态论文日报 - 2026-08-11

**日期**：2026-08-11

本次共收录 **27** 篇多模态相关论文，其中 **13** 篇提供代码仓库，覆盖 **8** 个研究方向。

## VLM / MLLM

### [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](https://arxiv.org/abs/2608.07302)

**作者**：Zichuan Wang, Songlin Yang, Bo Peng et al. · **方向**：VLM / MLLM · [Code](https://github.com/wzczc/SADT)

该研究发现大视觉语言模型中的对象幻觉问题并非源于视觉注意力不足，而是源于模型“关注了什么”以及“为何关注”。通过 Logit Lens 解码高注意力视觉特征，真实对象区域能正确映射到目标 token，而幻觉区域则不能。研究据此提出无需训练的 Detect-Mitigate 框架，在多个基准上取得当前最优的幻觉检测与缓解效果。

### [RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs](https://arxiv.org/abs/2608.07088)

**作者**：Qiyanhui Lu, Han Wu, Rongjian Xu et al. · **方向**：VLM / MLLM · [Code](https://github.com/LukieLuu/RoRA)

针对 MLLM 视觉 token 冗长导致的预填充与缓存开销，RoRA 在固定预算下将 token 角色划分为受保护的语义核心、支撑上下文与细粒度局部细节三类，并基于注意力锚点构建区域代理以判断哪些对象区域已被表示。在 LLaVA 与 Qwen-VL 家族上，RoRA 在极高剪枝率下仍能保持接近未剪枝模型的精度，并在 H800 上实现 1.33 倍推理加速。

### [Understand Before Detect: Vision-Language Learning for Omni-Domain Infrared Small Target Detection](https://arxiv.org/abs/2608.07015)

**作者**：Haoyang Yuan, Boyang Li, Yingqian Wang et al. · **方向**：VLM / MLLM

该工作提出“先理解再检测”的思路，通过语言监督让模型先学习跨域通用的红外小目标语义理解，再迁移到精确检测。JinSight 模型中的 Latent Semantic Interaction 模块将全局语言语义与细粒度空间特征对齐，并发布了首个面向全领域红外小目标检测的大规模视觉语言数据集 OmniIRST-VL。

### [Stable Curves, Unstable Items: Item-Level Scaling Heterogeneity in Video LLMs](https://arxiv.org/abs/2608.07014)

**作者**：Wenzhang Sun, Chunfeng Wang, Xiangchen Yin et al. · **方向**：VLM / MLLM

研究指出 Video LLM 的聚合扩展曲线掩盖了个体样本层面的显著波动。通过对固定模型-样本对在受控视觉预算下的轨迹追踪，发现不存在对所有样本都最优的单一预算配置；部分样本在低预算下正确而在高预算下反而错误。研究提出针对性的采样干预与置信级联策略，在保持精度的同时降低平均共享帧成本 31.7%。

### [Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models](https://arxiv.org/abs/2608.06901)

**作者**：Minseok Kang, Hyunwoo Kim, Chanyoung Kim et al. · **方向**：VLM / MLLM · [Code](https://github.com/cau-hai-lab/PORTA)

PORTA 是一种无需重训练、任务无关的视觉语言模型剪枝框架。它基于通用校准数据上的激活变化，建立跨模态的特征级重要性度量，并通过自适应稀疏度分配机制根据输出特征可变性为各层分配剪枝比例。在 CLIP、BLIP 和 Qwen2-VL 上的实验表明，该方法在高稀疏度下仍保持有竞争力的下游性能。

### [Your VLM Already Knows When: Training-Free Temporal Grounding by Asking Yes or No](https://arxiv.org/abs/2608.08315)

**作者**：Ji Huang, Barry Devereux, Hui Wang · **方向**：VLM / MLLM

该研究提出 FV-Action，一种无需训练的视频时间定位方法，将时间戳回归转化为粗细粒度的是/否问题扫描。通过充分利用 VLM 已有的时序理解能力，该方法在多个视频基准上显著提升了动作时间定位精度，避免了对模型进行额外微调。

### [NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving MLLMs](https://arxiv.org/abs/2608.08107)

**作者**：Jiayue Jin, Jingwei Zhang, Chen Wang et al. · **方向**：VLM / MLLM

NeuPAT 在 MLLM 指令微调阶段引入神经元可塑性分配机制，根据神经元与语言能力的相关程度动态调整更新约束，从而保护语言相关神经元、缓解多模态微调带来的语言能力退化。该方法为保持 MLLM 视觉能力提升与语言能力保留之间的平衡提供了新思路。

### [ZOMP: Zeroth-Order Multi-Modal Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2608.08060)

**作者**：Sajjad Ghiasvand, Yifan Yang, Mahnoosh Alizadeh et al. · **方向**：VLM / MLLM

ZOMP 是一种零阶多模态提示微调方法，在冻结 CLIP 视觉与文本分支的同时，通过同时扰动随机逼近优化深层提示。该方法为视觉语言模型的参数高效适配提供了新的优化路径，可在不更新主干参数的情况下提升多模态下游任务表现。

## 多模态理解与推理

### [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](https://arxiv.org/abs/2608.08326)

**作者**：Yifan Li, Ruxin Sun, Tongzhou Zhao · **方向**：多模态理解与推理

StructReward 通过结构化步骤级奖励对齐，为自纠正多模态推理提供密集的强化学习信号，无需额外验证器。该方法将推理过程分解为结构化阶段，并针对不同阶段设计奖励，使模型在视觉问答等任务中能够自动检测并修正中间错误。

### [Advantage-Guided Gate: Reshaping Open-Ended Reasoning for Vision-Based Spatial Intelligence](https://arxiv.org/abs/2608.07987)

**作者**：Ling Lin, Yang Bai, Congcong Zhu et al. · **方向**：多模态理解与推理 · [Code](https://github.com/LingLin-ll/Advantage-Guided-Gate)

该研究在 MLLM 逐步推理中引入优势引导门控机制，动态评估中间步骤的价值，选择高价值前缀与最佳推理头。针对基于视觉的空间智能任务，该方法有效提升了开放式推理的准确性与效率，在多个空间推理基准上验证了优势。

### [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](https://arxiv.org/abs/2608.07959)

**作者**：Keyang Zhong, Kuo Wang, Peng Liu et al. · **方向**：多模态理解与推理

SCOUT 是一种面向超长第一人称视频推理的自检查工具思维代理，能够在多跳推理过程中识别错误状态并进行恢复感知重规划。研究还提出 UPS-GRPO 训练方法，使代理在复杂 egocentric 视频问答任务中具备更强的长程推理与错误恢复能力。

### [Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning](https://arxiv.org/abs/2608.07955)

**作者**：Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu et al. · **方向**：多模态理解与推理

NeSy-Spatial 将工具交互与几何操作抽象为原子指令，通过自进化技能库持续积累并优化工具增强的空间推理能力。该方法结合神经网络的感知能力与符号系统的可解释性，在需要精确几何推理的视觉任务中表现出色。

### [SportsGrounder: Proposal-Aided Interleaved Grounding for Dense Sports Video Reasoning](https://arxiv.org/abs/2608.07932)

**作者**：Yizhi Li, Jiawei Jiang, Guanhong Wang et al. · **方向**：多模态理解与推理

SportsGrounder 利用开放词汇视觉专家与交错定位融合机制，增强密集体育视频的细粒度推理与动作感知监督。该方法通过候选片段辅助的交错式定位，在复杂运动场景下实现了更精确的事件理解与时空推理。

## 多模态基准与评测

### [SABRE: Scalable and Automated Benchmarking of VLMs under Stress](https://arxiv.org/abs/2608.07435)

**作者**：Zixuan Lan, Luzhe Sun, Matthew R. Walter et al. · **方向**：多模态基准与评测 · [Code](https://github.com/Zesearch/vlm-SABRE)

SABRE 是一个可扩展、自动化的 VLM 压力测试构建流水线，能够将测试原语转换为结构化规范、生成或编辑图像并构造问答对。研究实例化 SABRE-Prior 来评估 VLM 是否依赖视觉证据而非世界先验，在六个 VLM 上的平均准确率仅为 22.6%，揭示了当前模型在反事实与语言诱导场景下的脆弱性。

### [Forged Peer Judgments Mislead Multimodal LLM Judge Panels: Source-Blind Anchoring and Panel-Consensus Verification](https://arxiv.org/abs/2608.07920)

**作者**：Yang Shu · **方向**：多模态基准与评测

该研究揭示了多模态 LLM 评审面板存在的来源盲锚定攻击风险：伪造的同行判断可能误导评审结果。作者提出面板共识验证机制作为防御手段，通过多评审员之间的交叉验证降低单一伪造判断的影响，为构建更可靠的多模态模型评估体系提供了参考。

## 多模态检索与信息抽取

### [DAEP: Difficulty-Aware Evidence Planning for Medical Video Corpus Temporal Answer Grounding](https://arxiv.org/abs/2608.06869)

**作者**：Tianjian He, Yujie Liu, Zhiping Huang et al. · **方向**：多模态检索与信息抽取

DAEP 针对医学视频语料库时间答案定位任务，将输入的简单/复杂标签转换为推理时的证据规划，动态调整字幕、视觉与程序上下文证据的权重以及边界阈值等参数。在 NLPCC 2026 官方评测中，BIGC 团队凭借 DAEP 在十支参赛队伍中排名第一。

## Agent 与具身智能

### [OpenVisTool: An Open Recipe for Synthesizing Instructive Visual Tool-Use Trajectories](https://arxiv.org/abs/2608.08557)

**作者**：Changhao Xiang, Shilin Zhang, Zheng Ma et al. · **方向**：Agent 与具身智能 · [Code](https://github.com/Changhao-Xiang/OpenVisTool)

OpenVisTool 构建了一套开放式的视觉工具使用轨迹合成方案，仅保留结果正确且工具观测对答案有因果贡献的轨迹，并建立了 42K 规模的数据集与基准。该工作显著提升了多模态代理在视觉工具学习与推理任务上的能力，为工具使用轨迹的自动化构建提供了可复用框架。

### [Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization](https://arxiv.org/abs/2608.08523)

**作者**：Pengfei Xu, Yong Liu, Xiaoya Nan et al. · **方向**：Agent 与具身智能 · [Code](https://github.com/EvoNexusX/2026XuQD-Plan)

该研究提出基于质量多样性优化的框架，为具身多模态智能体发现多样化的规划策略。通过离线构建经验库与在线检测停滞并切换策略，智能体能够在复杂环境中保持行为多样性，提升长程任务完成的鲁棒性与适应性。

### [Large Multimodal Agents for Intelligent Transportation Systems: Architectures, Evidence, and Deployment Challenges](https://arxiv.org/abs/2608.08184)

**作者**：Muhammad Ayub Sabir, Shaohong Zheng, Zhiyu Qu et al. · **方向**：Agent 与具身智能 · [Code](https://github.com/pangjunbiao/ITS-LMA-Review)

该综述面向智能交通系统的大型多模态代理，建立了可审计证据图以区分模型、系统与混合多模态能力，并梳理了不同架构能力等级。研究总结了该领域从架构设计到实际部署的挑战，为交通场景下的多模态代理研发提供了系统性的参考框架。

### [Multi-modal Interactive Control of Robotic Arm based on Offline Large Language Models](https://arxiv.org/abs/2608.08183)

**作者**：Hanxiao Chen · **方向**：Agent 与具身智能 · [Code](https://github.com/2000222/Socratic-Models-ChatGLM)

该研究基于离线大语言模型 Socratic Models-ChatGLM，提出了一种多模态机械臂交互控制方法。在 PyBullet 仿真环境中，系统整合文本指令与视觉观测，实现了无需联网的机械臂多模态交互操作，为资源受限场景下的具身智能应用提供了可行方案。

### [LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents](https://arxiv.org/abs/2608.06948)

**作者**：Ivan Majic, Zexian Huang, Franziska Hübl et al. · **方向**：Agent 与具身智能 · [Code](https://github.com/Geoinfo-TUGraz/COSIT2026_LMM_modality_transfer)

该研究提出模态迁移任务，让一个大型多模态模型根据网格图像生成文本描述，再由另一个模型根据文本重绘图像，以衡量空间信息在图像与文本之间的转移能力。实验发现即使是最新的 OpenAI LMM 在该任务上仍存在困难，表明自主 GIS 代理需要更强的多模态对齐能力。

## 多模态生成

### [Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation](https://arxiv.org/abs/2608.07117)

**作者**：Bruno Palau, Franziska Vogt, Daria Laslo et al. · **方向**：多模态生成 · [Code](https://gitlab.ethz.ch/BMDSlab/publications/low-back/spine-mri-report-generation)

该研究针对脊柱 MRI 放射报告生成任务，指出传统词汇与语义指标难以反映临床正确性：流畅且结构良好的报告仍可能包含临床意义上的诊断错误。为此，作者提出用半监督 U-Net++ 生成椎间盘级异常热图来增强 VLM 输入，实现更具解剖学敏感性且可解释的腰椎 MRI 报告生成。

### [Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation](https://arxiv.org/abs/2608.08469)

**作者**：Kaichen Zhang, Wei Huang, Keming Wu et al. · **方向**：多模态生成

Aero Realtime 是一个 4B 参数的双流实时多模态生成模型，通过共享时间网格对齐视频、音频与文本输出，实现低延迟增量推理。该方法为流式多模态内容生成提供了新的架构思路，能够在保持输出一致性的同时显著降低响应延迟。

## 音频多模态

### [From Speech to Interaction: Analyzing Multimodal Systems in Cocktail-Party Scenarios](https://arxiv.org/abs/2608.08510)

**作者**：Thai-Binh Nguyen, Zhaolin Li, Jan Niehues et al. · **方向**：音频多模态 · [Code](https://github.com/MCoRec/mcorec_baseline)

该研究系统分析了鸡尾酒会场景下音视频多模态系统的表现，指出目标分离、识别与大模型后处理三种策略具有互补性，挑战不仅来自语音重叠。研究为复杂声学环境下的多模态交互系统设计提供了深入分析与基准参考。

### [AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward](https://arxiv.org/abs/2608.06930)

**作者**：Mingyang Wu, Kaituo Feng, Bohao Li et al. · **方向**：音频多模态 · [Code](https://huggingface.co/collections/Apryle/avcap)

AVCap 针对详细音视频联合描述任务，发布了包含 10 万条时序对齐细粒度标注的 AVCap-100K 数据集，并提出 Detail-Aware GRPO 训练策略。该方法在开源模型中取得最先进性能，同时提出了原子级音视频描述评估基准 AVCap-Bench 与指标 AVCap-Score。

## 3D 视觉语言

### [EsaacSim: A Multimodal Event Camera Add-on for NVIDIA Isaac Sim](https://arxiv.org/abs/2608.08522)

**作者**：Ignacio Bugueno-Cordova, Malte Kuhlmann, Nicolás Navarro-Guerrero et al. · **方向**：3D 视觉语言

EsaacSim 是 NVIDIA Isaac Sim 的多模态事件相机插件，支持灰度/Bayer RGGB 事件、RGB、深度、IMU 等多种传感器的同步输出。该工具为基于事件相机的具身智能与机器人仿真研究提供了统一的数据生成环境。

### [WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN](https://arxiv.org/abs/2608.07267)

**作者**：Yuehao Huang, Yunzi Wu, Xiaotao Zhang et al. · **方向**：3D 视觉语言

WNM-3D 是一种面向连续视觉语言导航的生成式世界导航模型，通过 3D 场景条件联合预测未来视图与导航动作。该方法使用冻结的几何编码器与可训练的 3D Scene-to-Token 适配器，将几何感知特征注入世界动作 Diffusion Transformer，在 GN-Bench 上优于强 VLM 基线。

---

**论文总数统计**：本次日报共收录 27 篇论文，其中 13 篇提供代码仓库，14 篇暂无公开代码。
