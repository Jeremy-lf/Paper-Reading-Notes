# Arxiv 多模态论文日报 - 2026-06-18

## VLM/MLLM

### [Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation (ViGOS)](https://arxiv.org/abs/2606.19120)

**作者:** Shengyuan Ding, Xilin Wei, Xinyu Fang et al. | **方向:** VLM, 推理, 暂无代码 | **代码:** 无

提出 ViGOS，一个视觉接地的 On-Policy Self-Distillation (OPSD) 框架，用于 MLLM 后训练。发现直接扩展 OPSD 到多模态大语言模型会产生"捷径"问题——模型依赖文本先验而非视觉证据。ViGOS 通过解耦感知与推理，先训练视觉感知再训练推理，显著提升模型在视觉推理任务上的鲁棒性。

---

### [Visual-OPSD: Cross-Modal On-Policy Self-Distillation for Efficient Unified Multimodal Reasoning](https://arxiv.org/abs/2606.18974)

**作者:** Pengyu Li, Zhitao Gao, Lingling Zhang et al. | **方向:** VLM, 推理, 有代码 | **代码:** [Code](https://github.com/TiezMind/Visual-OPSD)

针对统一多模态模型 (UMMs) 中"视觉思维" (Visual Thoughts) 生成带来的推理效率问题，提出 Visual-OPSD 方法。发现交错式视觉推理对空间任务的直接收益有限，通过跨模态 On-Policy 自蒸馏实现高效统一多模态推理，在保持性能的同时显著降低推理开销。

---

### [AMALIA-VL: A Native European Portuguese Open-Source Vision and Language Model](https://arxiv.org/abs/2606.19100)

**作者:** Diogo Glória-Silva, João Cardeira, Manuel Letras da Luz et al. | **方向:** VLM, 暂无代码 | **代码:** 无

推出 AMALIA-VL，首个为欧洲葡萄牙语 (pt-PT) 原生构建的开源指令微调大型视觉语言模型。针对当前 LVLM 主要服务英语和巴西葡萄牙语而系统性忽略欧洲葡萄牙语的问题，在多个视觉-语言基准上展现了有竞争力的性能。模型权重和数据集将公开发布。

---

### [Image Prompt Reconstruction Attacks on Distributed MLLM Inference Frameworks](https://arxiv.org/abs/2606.18710)

**作者:** Xinjian Luo, Hongyan Chang, Jianxin Wei et al. | **方向:** MLLM, 安全, 暂无代码 | **代码:** 无

揭示分布式 MLLM 推理框架中的图像提示重建攻击风险。随着 LLM 演变为 MLLM，中间嵌入的隐私敏感性从纯文本扩展到图像领域——图像提示包含丰富的视觉和语义信息，使得中间嵌入更具隐私敏感性。提出针对分布式推理场景的新型攻击范式。

---

## 理解与推理

### [Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games (RNG-Bench)](https://arxiv.org/abs/2606.19338)

**作者:** Shengyuan Ding, Xilin Wei, Xinyu Fang et al. | **方向:** 基准, 推理, 暂无代码 | **代码:** 无

引入 RNG-Bench (Reconstructive Non-Markov Games)，一套用于评估多模态基础模型在闭环策略中重建过往观察能力的基准。部署多模态基础模型作为闭环策略需要基于不再可见的观察来条件化动作，该基准隔离了模型对历史观察的重建能力。

---

### [Reasoning as Intersection: Consensus-Frame Alignment for Visual Focus in Video-MLLMs (VideoCFR)](https://arxiv.org/abs/2606.18441)

**作者:** Chengwen Liu, Zhe Huang, Jisheng Dang et al. | **方向:** Video-MLLM, 推理, 有代码 | **代码:** [Code](https://github.com/1Pansy/VideoCFR)

将强化学习应用于视频多模态大语言模型 (Video-MLLMs)，提出"推理即交集"的理念——通过共识帧对齐引导视觉焦点。发现仅用结果奖励对 Video-MLLMs 提供有限的视觉证据指导，提出 VideoCFR 框架，在推理质量和视觉 grounding 上均有显著提升。

---

### [ThinkDeception: A Progressive Reinforcement Learning Framework for Interpretable Multimodal Deception Detection](https://arxiv.org/abs/2606.18988)

**作者:** Jinhao Song, Shan Liang, Yiqun Yue et al. | **方向:** 推理, 暂无代码 | **代码:** 无

提出 ThinkDeception，首个可解释的多模态欺骗检测框架。首次将 MLLM 引入欺骗检测领域，将传统二分类任务转化为显式认知推理过程。提出 Visual-Audio Consistency GRPO (VAC-GRPO) 配合渐进式训练策略（由易到难的课程学习），在主流基准上达到新 SOTA。

---

### [Learning Robust Pair Confidence for Multimodal Emotion-Cause Pair Extraction (RPCL)](https://arxiv.org/abs/2606.18893)

**作者:** Zhuangzhuang Pan, Ning Dong, Yingna Su et al. | **方向:** 推理, 暂无代码 | **代码:** 无

研究多模态情感-原因对抽取 (MECPE) 中的配对置信度脆弱性问题。提出 RPCL (Robust Pair Confidence Learning)，通过学习鲁棒的配对置信度来提升候选对的可靠性，解决现有方法在面对对抗性扰动时配对置信度不稳定的问题。

---

## 基准评测

### [Benchmarking Large Vision-Language Models on Fine-Grained Image Tasks: From Evaluation to Diagnosis (FG-BMK)](https://arxiv.org/abs/2606.19053)

**作者:** Hong-Tao Yu, Chen-Wei Xie, Yuxin Peng et al. | **方向:** 基准, VLM, 有代码 | **代码:** [Code](https://github.com/SEU-VIPGroup/FG-BMK)

尽管 LVLM 在多模态感知和推理上表现出色，但在细粒度图像任务上的能力仍缺乏充分理解。提出 FG-BMK 基准，从评估到诊断系统性地分析 LVLM 在细粒度视觉任务上的表现，为改进模型提供明确的方向指引。

---

### [A Multi-Domain Benchmark for Detecting AI-Generated Text-Rich Images from GPT-Image-2](https://arxiv.org/abs/2606.19259)

**作者:** Yijin Wang, Shuyi Wang, Wenhan Zhang et al. | **方向:** 基准, 暂无代码 | **代码:** 无

针对 GPT-Image-2 等模型生成的文字丰富图像，提出跨域检测基准。发现现有检测方法在面对文字布局和文本内容时表现不佳，强调需要文本感知和布局感知的检测方法以应对新一代 AI 生成图像。

---

## 检索与信息抽取

### [DREAM: Extending Vision-Language Models with Dual-Objective Encoding for Cross-Modal Retrieval](https://arxiv.org/abs/2606.19062)

**作者:** Kaleem Ullah, Altaf Hussain, Muhammad Munsif et al. | **方向:** 检索, VLM, 暂无代码 | **代码:** 无

提出 DREAM (Dual-path Representation Enhancement and Alignment Model)，通过双目标编码扩展视觉语言模型用于跨模态检索。在视频内容通过自然语言查询检索的场景中，双路径表示增强与对齐显著提升了检索精度。

---

### [SAMA: Semantic Anchor-aligned Augmentation for Unified Low-Resource Multimodal Information Extraction](https://arxiv.org/abs/2606.18780)

**作者:** Quanjiang Guo, Chong Mu, Jiazhou Pan et al. | **方向:** 信息抽取, 有代码 | **代码:** [Code](https://github.com/UESTC-GQJ/SAMA)

多模态信息抽取 (MIE) 涵盖命名实体识别 (MNER)、关系抽取 (MRE) 和事件抽取 (MEE)，但严重受限于数据稀缺。提出 SAMA，通过语义锚点对齐增强实现统一的低资源多模态信息抽取，在多个 MIE 任务上展示了显著的数据效率提升。

---

## Agent与具身智能

### [VISUALSKILL: Multimodal Skills for Computer-Use Agents](https://arxiv.org/abs/2606.18448)

**作者:** Ziyan Jiang, Li An, Yujian Liu et al. | **方向:** Agent, 有代码 | **代码:** [Code](https://github.com/XMHZZ2018/VisualSkills)

计算机使用智能体 (CUAs) 在标准化基准上接近人类水平，但在长期任务和未见软件上仍然困难。提出 VISUALSKILL：层次化多模态技能框架，为每个目标应用定制技能模块，在长程任务中展示了显著的性能提升。

---

### [LandslideAgent with Multimodal LandslideBench: A Domain-Rule-Augmented Agent for Autonomous Landslide Identification and Analysis](https://arxiv.org/abs/2606.18661)

**作者:** Chengfu Liu, Dongyang Hou, Junwu Xiang et al. | **方向:** Agent, 有代码 | **代码:** [Code](https://github.com/GeoRSAI/LandslideAgent)

智能滑坡灾害解读受限于当前范式难以同时提取视觉特征和高层地球科学语义。提出指令驱动的 Agent 框架 LandslideAgent，配合多模态 LandslideBench 基准，结合领域规则增强实现自主滑坡识别与分析。

---

## 多模态生成

### [Bridging Creative Intent and Visual Quality: Creator-Driven Recurrent Video Generation with Agentic Feedback Loops (CHIEF)](https://arxiv.org/abs/2606.18591)

**作者:** Denis Savytski, Aiden Lei, Heding Liu et al. | **方向:** 生成, Agent, 暂无代码 | **代码:** 无

生成式 AI 使内容创建日益普及，但许多 AI 生成视频缺乏叙事连贯性和创意方向。提出 CHIEF，人机协同创作的视频生成框架，通过创作者驱动的循环视频生成和 Agent 反馈循环，桥接创意意图与视觉质量。

---

## 音频多模态

### [Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs](https://arxiv.org/abs/2606.18924)

**作者:** Hyebin Cho, Suho Yoo, Jaehyuk Jang et al. | **方向:** 音频, LLM, 暂无代码 | **代码:** 无

虽然 Audio LLM 在多模态理解上表现出色，但存在"文本主导"偏差——模型盲目偏好文本而非声学证据。通过机制可解释性方法深入分析这一偏差的内在机制，揭示了音频与文本模态冲突时的决策过程。

---

## 3D视觉语言

### [Domain Generalizable Adaptation of 3D Vision-Language Models via Regularized Fine-Tuning (ReFine3D)](https://arxiv.org/abs/2606.18472)

**作者:** Sneha Paul, Zachary Patterson, Nizar Bouguila | **方向:** 3D, VLM, 暂无代码 | **代码:** 无

域适应仍是 3D 视觉的核心挑战，尤其是对齐 3D 点云与视觉和文本数据的多模态基础模型。提出 ReFine3D，一种正则化微调框架，用于 3D 大型多模态模型的域泛化调优，在跨域 3D 理解任务上展示了良好的泛化能力。

---

## VQA与遥感

### [A Unified Framework for Efficient Remote Sensing Visual Question Answering](https://arxiv.org/abs/2606.19277)

**作者:** Timothy Agboada, Shikha Chandel, Yadav Raj Ghimire et al. | **方向:** VQA, 暂无代码 | **代码:** 无

适配 Dual、Hybrid 和 Encoder-Decoder 架构用于高效遥感视觉问答。发现 Hybrid FLAVA 架构在多模态推理和检索能力上优于单模态对应方案，为资源受限场景下的遥感 VQA 建立了新基线。

---

> 共收录 18 篇论文，涵盖 9 个方向
