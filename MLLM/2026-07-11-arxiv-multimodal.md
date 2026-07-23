# Arxiv 多模态论文日报 - 2026-07-11

## VLM / MLLM

### [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](https://arxiv.org/abs/2607.08497)

**作者:** Feng Wang, Canmiao Fu, Zhipeng Huang et al. | **方向:** VLM / MLLM | **代码:** [Code](https://github.com/caseclose/cma-harness)

提出认知结构化的多模态智能体，将视觉信息外化为情景视觉记忆，通过感知抽象引擎、认知检索引擎和多模态执行控制器实现长程多模态对话与自主任务规划。在 20 轮会话检索任务中，8B 模型达到 91.4% 准确率，超过 32B 基线 8.2%，同时将每轮推理时间从 23.1 秒降至 12.7 秒。

---

### [DeltaV: Thinking with Visual State Updates in Unified Large Multimodal Models](https://arxiv.org/abs/2607.08434)

**作者:** Pengjie Wang, Linger Deng, Zujia Zhang et al. | **方向:** VLM / MLLM | **代码:** [Code](https://github.com/Pengjie-W/DeltaV)

提出 DeltaV，一种统一大型多模态模型 (ULMM)，用紧凑的视觉状态更新替代完整图像生成，并引入 TSIM Router 根据视觉变化幅度动态分配更新 token。在 44 个领域的 StructCoT 数据集上训练后，DeltaV-2B 在域内多模态推理上比较大尺度开源模型提升 8.4%，在外部基准上超过同规模 Qwen3-VL-2B 5.9%。

---

## 多模态基准与评测

### [VEGAS: Human-Aligned Video Caption Evaluation via Gaze](https://arxiv.org/abs/2607.08489)

**作者:** Shenghui Chen, Po-han Li, Ximeng Sun et al. | **方向:** 多模态基准与评测 | **代码:** 无

提出 VEGAS（Video caption Evaluation via GAze Score），一种无需训练的基于注视点的视频字幕评估指标，通过测试时眼动数据采样与观众注意力对齐的候选文本。在自我中心活动与教学幻灯片数据集上，VEGAS 选出的字幕与人类关注点更一致，并提升下游视频检索性能。

---

### [UniRef-UAV: A Multimodal Benchmark for Universal Referring in UAV Imagery](https://arxiv.org/abs/2607.08267)

**作者:** Haibin Tian, Huichao Xie, Xuelin Qian et al. | **方向:** 多模态基准与评测 | **代码:** 无

提出通用指代表达理解任务 Universal Referring 和 UniRef-UAV 基准，支持文本、图像及文本+图像查询，并涵盖无目标、单目标和多目标定位。该基准提供域内与跨域评估协议，检测式基线 UAV-URNet 展现出稳定的可复现性能，并降低视觉查询歧义。

---

### [AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding](https://arxiv.org/abs/2607.08745)

**作者:** Siddharth Damodharan, Radhika Gupta, Ali Alshami et al. | **方向:** 多模态基准与评测 | **代码:** 无

提出 AUTOPILOT-VQA，一个面向行车记录仪视频的安全关键事件视觉问答基准，围绕真实驾驶事件与 near-incident 设计结构化问题，覆盖天气光照、交通环境、路面状态、signage、涉及实体、事故撞击位置及可避免性推理等维度。该基准推动自动驾驶系统从对象识别迈向时间定位的安全感知推理。

---

### [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](https://arxiv.org/abs/2607.08423)

**作者:** Qian Jiang, Zhecheng Shi, Jingpu Yang et al. | **方向:** 多模态基准与评测 | **代码:** [Code](https://anonymous.4open.science/r/OmniFood-Bench-7D0B)

提出 OmniFood-Bench 基准，评估视觉语言模型在营养成分推理与个性化健康建议方面的能力，覆盖基础感知、定量推理和安全关键建议三个递进层次。实验揭示模型在菜品命名上接近人类，但在质量估算和糖尿病等高风险建议上存在显著的「语义-物理鸿沟」，频繁产生幻觉化的良性建议。

---

### [Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models](https://arxiv.org/abs/2607.08317)

**作者:** Matteo Santelmo, Xiuying Wei, Israa Fakih et al. | **方向:** 多模态基准与评测 | **代码:** 无

提出 blind-spots-bench 诊断基准，通过 235 个对人类简单但对现代 AI 困难的任务暴露多模态模型的盲区。实验显示闭源前沿模型与开源模型存在约 10% 的性能差距，且没有任何模型在所有任务类型上占主导，凸显该基准作为诊断压力测试的价值。

---

## 多模态检索与信息抽取

### [MatBind: A Shared Embedding Space for Multimodal Materials Characterization](https://arxiv.org/abs/2607.08470)

**作者:** Le Yang, Anoop K. Chandran, Jona Ostreicher et al. | **方向:** 多模态检索与信息抽取 | **代码:** 无

提出 MatBind 对比学习框架，将晶体结构、粉末 XRD、态密度 (DOS) 和文本四种材料表征模态对齐到统一嵌入空间，以晶体结构为物理锚点实现零样本跨模态检索。结果表明结合多模态查询可系统提升检索性能，嵌入空间按物理意义属性自动组织，无需显式监督。

---

## Agent 与具身智能

### [LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action](https://arxiv.org/abs/2607.08182)

**作者:** Qi Lyu, Baicheng Liu, Xudong Wang et al. | **方向:** Agent 与具身智能 | **代码:** [Code](https://github.com/LyuQi127/LEEVLA)

提出 LEEVLA，一种面向动态环境的视觉-语言-动作 (VLA) 模型，通过漂移引导动态优先级 (DGDP) 关注任务相关区域，并用结构化特征流生成 (SFFG) 建模潜在世界表示的演化。在 VLA 基准上持续优于现有方法，验证了显式任务证据引导与结构化潜在推理对可扩展 VLA 的重要性。

---

### [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/abs/2607.08716)

**作者:** Yifan Wu, Lizhu Zhang, Yuhang Zhou et al. | **方向:** Agent 与具身智能 | **代码:** [Code](https://github.com/yifannnwu/proactive-memory-agent)

提出主动记忆智能体，将记忆视为干预机制而非被动检索，通过结构化记忆库跟踪近期轨迹并决定何时向动作智能体注入记忆提醒，以缓解长程任务中的「行为状态衰减」。在 Terminal-Bench 2.0 和 tau2-Bench 上分别带来 +8.3 和 +6.8 个百分点的 pass@1 提升，选择性干预优于始终注入或通用检索等基线。

---

### [Playing ZendoWorld: Challenging AI Agents on Active Visual Concept Induction](https://arxiv.org/abs/2607.08233)

**作者:** Sophia Koehler, Antonia Wust, Inga Ibs et al. | **方向:** Agent 与具身智能 | **代码:** [Code](https://github.com/ml-research/ZendoWorld)

提出 ZendoWorld 交互环境，评估智能体在主动视觉概念归纳中联合感知复杂输入、形成隐藏模式假设并设计信息性实验的能力。研究发现高准确率不等于恢复底层规则，VLM 智能体提出的实验信息增益较低，人类数据则揭示了更复杂规则下的归纳推理差距。

---

### [Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning](https://arxiv.org/abs/2607.08647)

**作者:** Ali Larian, Qian Lin, Chang Zong Wu et al. | **方向:** Agent 与具身智能 | **代码:** [Code](https://github.com/Alilarian/multienv-reward-teaching)

研究逆强化学习 (IRL) 中的多环境、多模态机器教学问题，理论分析表明在无限数据条件下比较反馈比演示提供更强的全局约束。提出分层教学算法，先贪婪选择暴露互补奖励约束的环境，再在环境内策略性地查询低成本反馈，实验显示其在相同反馈预算下显著降低遗憾并提升对未见环境的泛化。

---

### [Open-ended Multi-agent Autocurricula via Visual Inspection of Policies with Multi-modal LLMs](https://arxiv.org/abs/2607.08193)

**作者:** Lorenzo Pante, Andrea Fanti, Roberto Capobianco | **方向:** Agent 与具身智能 | **代码:** 无

提出 Visual Inspection of Policies (VIP)，利用视频语言模型直接分析智能体行为视频以生成课程推荐，用于开放课程多智能体强化学习。在 StarCraft 多智能体挑战 (SMAC) 上的实验表明，即使使用轻量级 VideoLLaMa2-7B，VIP 也优于文本摘要和标量分数方法。

---

## 多模态生成

### [OpenCoF: Learning to Reason Through Video Generation](https://arxiv.org/abs/2607.08763)

**作者:** Xinyan Chen, Ziyu Guo, Renrui Zhang et al. | **方向:** 多模态生成 | **代码:** [Code](https://github.com/xinyan-cxy/OpenCoF)

提出 OpenCoF 框架，将视频生成作为 Chain-of-Frame (CoF) 推理路径，构建涵盖 11 个任务族的 OpenCoF-17K 推理视频数据集，并微调得到 Wan-CoF 模型。在四项视频推理基准上显著优于 Wan2.2-I2V-A14B 基线，并开源数据集、模型与代码。

---

### [Cross-Modal Generative Framework for Signal Translation from Fetal-Maternal Electrocardiograms to Fetal Doppler Waveforms](https://arxiv.org/abs/2607.08073)

**作者:** Tongli Su, Alireza Rafiei, Marly van Assen et al. | **方向:** 多模态生成 | **代码:** 无

提出跨模态生成框架，结合空洞卷积、跨模态注意力与自注意力，从胎儿-母体心电图合成胎儿多普勒包络，建模电活动与机械血流动力学之间的关系。在 39 例妊娠数据上训练，模型在功率谱密度 MSE 上比双通道基线降低 51%，跨模态注意力带来额外 39% 的误差下降。

---

## 音频多模态

### [A Reliability Assessment of LALM Audio Judges for Full-Duplex Voice Agents](https://arxiv.org/abs/2607.07985)

**作者:** A. Sayyad, J. Emmons, S. Jones et al. | **方向:** 音频多模态 | **代码:** 无

评估 Gemini 模型作为全双工语音对话音频评判员的可靠性，在 209 段立体声会话上与三位校准后的人工评分员对比 8 个生产维度。结果表明 Gemini 2.5 Flash 在多数维度上与人类评分高度一致（Spearman rho 接近人类间一致性），可作为第四位评分员部署，估计比纯人工评分降低约两个数量级的成本。

---

> 共收录 16 篇论文，涵盖 6 个方向
