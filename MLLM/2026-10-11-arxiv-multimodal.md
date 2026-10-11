# Arxiv 多模态论文日报

> 2026 年 10 月 11 日（共 45 篇相关论文）
>
> 收录论文 **45** 篇 | 含代码仓库 **22** 篇 | 覆盖方向 **8** 个

---

## VLM / MLLM 核心

### 1. [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)

**作者**: Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

小米推出 MiMo-V2.6 系列全模态模型，通过扩大 RL 计算规模实现自我提升。RL 计算沿三个维度扩展：更大批次、更多样化环境、更多评分器计算。模型在中间训练阶段使用广泛多模态语料，支持高达 1M 上下文长度的异步训练和混合任务智能体 RL。

---

### 2. [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](https://arxiv.org/abs/2610.12266)

**作者**: Jinghua Hou, Zhe Liu, Hengshuang Zhao et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

DVD 统一 2D 和 3D 感知，将边界框和掩码转化为 1D 向量序列并映射为紧凑离散 token。解码器将输出 token 还原为感知表示，大幅降低 token 开销和推理延迟，在 RefCOCO、KITTI、nuScenes 等基准上表现优异。

---

### 3. [Beyond Visual Enhancement: Adaptive Multi-Context Steering to Mitigate LVLM Hallucinations](https://arxiv.org/abs/2610.11907)

**作者**: Shuran Ma, JiaLe Li, Yuxin Dong et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 AIMS（自适应信息多源引导）框架，在解码阶段自适应协调视觉、预填充文本和生成上下文。通过构建紧凑原型并估计与当前查询的亲和力，实现逐头引导权重分配，无需额外训练即可缓解对象幻觉问题。

---

### 4. [From Suppression to Repair: Mitigating Object Hallucination in LVLMs via Localized Distribution Alignment](https://arxiv.org/abs/2610.11826)

**作者**: Chen Zhao, Xingping Dong, Jiachun Shi et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 ResOT 方法，在推理时通过局部化分布对齐修复表示。将幻觉方向投射出忠实子空间，使用高斯最优传输定义修复目标，在减少对象幻觉的同时提升字幕质量。

---

### 5. [When History Helps and Hurts: Selective History Use across Multimodal Turns](https://arxiv.org/abs/2610.11948)

**作者**: Shuoyang Sun, Kerui Gu, Hao Fang et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 ReTurn 基准，包含 7000 个基础任务，涵盖视觉和音频证据的选择性历史使用评估。在 13 个全模态、视觉语言和音频语言模型上，中位开放式准确率从直接输入的 93.7% 降至对话中的 72.3%。

---

### 6. [From What to Which: Decoding Modifier Grounding in Frozen MLLMs](https://arxiv.org/abs/2610.12305)

**作者**: Barbara Toniella Corradini, Caterina Gallegali, Ludovica Genovese et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 OTTER 方法，使用最优传输将生成的 token 与视觉区域对齐进行接地分析。结果表明修饰符 token 中可以解码实例判别信息，空间术语证据最强。基于 OT 的方法在上下文扰动和跨数据集迁移下均有效。

---

### 7. [VICO: Visual Environments Co-Evolving for Vision-Language Model Reasoning](https://arxiv.org/abs/2610.10782)

**作者**: Meng Lu, Ligeng Zhu, Olivia Xiao et al.
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 VICO 框架，让视觉环境与 VLM 推理能力协同进化。通过动态生成和迭代优化视觉环境，提升模型在复杂视觉推理任务上的表现。

---

### 8. [SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows](https://arxiv.org/abs/2610.10563)

**作者**: Albert Gao, Bing Xue, Andrea Zanette
**方向**: `VLM / MLLM` | **代码**: 暂无代码

提出 SLVR，通过类人推理流实现结构化潜在视觉推理。将视觉推理过程分解为可组合的潜在步骤，模仿人类的分步推理策略，提升复杂视觉问题的求解能力。

---

### 9. [HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration](https://arxiv.org/abs/2610.10133)

**作者**: Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu et al.
**方向**: `VLM / MLLM` | **代码**: [GitHub](https://github.com/PolyU-VCLab/HarnessIR)

HarnessIR 将修复需求、感知诊断和证据输入多模态基础模型，单次完成真实世界图像修复。处理复杂混合退化问题，利用 MFM 在一次通过中执行修复。

---

## 多模态理解与推理

### 10. [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417)

**作者**: Zheyu Fan, Yue Zhang, Mingkai Deng et al.
**方向**: `推理` | **代码**: 暂无代码

提出 WOVEN 基准，包含 36,076 个视觉转换推理样本。评估 38 个前沿 MLLM 发现其在空间、具身、物理和时间推理方面存在缺陷。在子集上训练可将 26 个外部基准中的 22 个提升最多 27.3 个百分点。

---

### 11. [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391)

**作者**: Jialu Wang, Ruichen Zhang, Xiaoou Liu et al.
**方向**: `推理` | **代码**: 暂无代码

将形式化视为可优化策略，执行推理流程、收集失败并突变表示策略。通过更好地组织几何实体和关系，将 Qwen3VL-2B 在 Geometry3K 上的准确率从 42.0% 提升至 56.0%。

---

### 12. [Look Back, Think Ahead: Visual Memory on Demand for Efficient Multimodal Reasoning](https://arxiv.org/abs/2610.12060)

**作者**: Yicheng Xue, Han Wu, Jufeng Yang et al.
**方向**: `推理` | **代码**: 暂无代码

提出 ViMoD，维护紧凑视觉上下文并可访问原始细粒度证据。DART（可变形区域 token 聚合）和 TRACE（时间路由自适应上下文证据）实现阶段特定证据访问。在 Qwen3-VL-4B 上平均归一化分数提升 39.0%。

---

### 13. [From Surface to Depth: Towards Cognitive Appraisal Reasoning in Multimodal Emotion Understanding](https://arxiv.org/abs/2610.11918)

**作者**: Jia Li, Yichao He, Yangchen Yu et al.
**方向**: `推理` | **代码**: [GitHub](https://github.com/MSA-LMC/CogEmo)

提出 CogEmo-40K 数据集、CogEmo-MoE 模型和 CogEmo-Bench，基于认知评价理论实现从感知到评价的情绪推理。引入评价证据质量分数（AEQS）解决传统情绪指标的局限性。

---

### 14. [Cognition-Oriented Emotion Tracing from Causes to Consequences in Real-World Social Scenes](https://arxiv.org/abs/2610.11410)

**作者**: Hao Li, Jinye Zhang, Bobo Li et al.
**方向**: `推理` | **代码**: [Project Page](https://cogaffc.github.io/TRACE)

提出 TRACE 框架，将情感事件形式化为条件（Condition）、情感（Affect）和效果（Effect）三个阶段。TRACE-Bench 在 646 个视频上跨五个任务评估多模态模型的认知情感追踪能力。

---

### 15. [Addressing Overcommitment in the Reasoning of Gendered Economic Memes under Multimodal Ambiguity](https://arxiv.org/abs/2610.11724)

**作者**: Kushal Kanwar, Dushyant Singh Chauhan, Kapil Rana et al.
**方向**: `推理` | **代码**: 暂无代码

提出 CGER-Net，上下文接地的多模态框架，评估输入是否为性别化经济推理提供充分证据。将性别过度承诺率降低最多 44%，解决多模态歧义下的推理过度承诺问题。

---

## 多模态基准与评测

### 16. [OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning](https://arxiv.org/abs/2610.12458)

**作者**: Zhongyu Yang, Jiale Tao, Ruitao Chen et al.
**方向**: `基准` | **代码**: [GitHub](https://github.com/Tencent/OmniCapBench)

提出 OmniCapBench，将音视频字幕评估重构为深度结构化诊断框架。预测原子可验证评估单元集合，涵盖实体引用、视觉镜头和音频事件。786 个标注视频可区分 MLLM 感知错误，包括时间接地失败、身份漂移和跨模态错位。

---

### 17. [DataVista: Diagnosing Multimodal LLMs on Data Video Understanding](https://arxiv.org/abs/2610.11993)

**作者**: Yupeng Xie, Zhenyang Wang, Jiayi Zhu et al.
**方向**: `基准` | **代码**: [GitHub](https://github.com/HKUSTDial/DataVista)

DataVista 包含 961 个真实数据视频和 6,775 个评估问题，基于三级渐进能力框架。评估 19 个 MLLM 显示最佳模型 Gemini-3.1-Pro 达到 70.0% 准确率，因果推理和叙事结构方面表现最弱。

---

### 18. [Perception Test 2026: Challenge Summary and Extension to City-scale Audio-Visual Reasoning](https://arxiv.org/abs/2610.12081)

**作者**: Fedor Kitashov, Joao Carreira, Shiry Ginosar et al.
**方向**: `基准` | **代码**: [GitHub](https://github.com/google-deepmind/perception_test)

ECCV 2026 Perception Test 研讨会包含四个赛道，新增城市级步行游览视频基准（KilometerAudio、KilometerVision）。获胜方案表明复杂空间和多模态推理可通过智能体流水线解决，但对独立模型仍然困难。

---

### 19. [Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736)

**作者**: Yawen Shao, Yubo Zhu, Ziyun Dai et al.
**方向**: `基准` | **代码**: [GitHub](https://github.com/yawen-shao/PEBench)

提出 PEBench，首个统一评估提示增强器（PE）的基准，覆盖文生视频、图生视频和参考生视频。包含 1,100 个专家验证案例和 1,005 个视觉资产。

---

### 20. [Is In-Domain Training Enough for Fine-Grained Industrial Anomaly Understanding?](https://arxiv.org/abs/2610.12310)

**作者**: Xingwu Zhang, Duanyang Du, Huiling Zhu et al.
**方向**: `基准` | **代码**: 暂无代码

提出 SiGMA，空间接地的多智能体框架，在异构 MLLM 智能体和视觉缺陷专家之间分工。在 MMAD 上达到 85.2% 平均准确率，与人类专家差距仅 1.5%，可无需重训练集成新 MLLM。

---

### 21. [GameCommBench: A Unified Benchmark and Type-Aware Evaluation for AI-Generated Game Commentary](https://arxiv.org/abs/2610.11129)

**作者**: Qirui Zheng, Zhengteng Lin, Yunyi Xiao et al.
**方向**: `基准` | **代码**: 暂无代码

提出 GameCommBench，统一的游戏解说生成评估基准，引入类型感知评估方法。系统评估 AI 生成游戏解说的质量和多样性。

---

### 22. [False Claims, Credible Images: A Red-Teaming Benchmark for Commercial Image Generators](https://arxiv.org/abs/2610.11112)

**作者**: Zeyu Ye, Yanchun Li, Sibei He et al.
**方向**: `基准` | **代码**: [GitHub](https://github.com/Ye-ze-yu/EpiReal-Bench)

提出 EpiReal-Bench，针对商业图像生成器的红队测试基准。评估生成图像中虚假声明与可信视觉效果的组合，揭示当前图像生成模型的事实准确性问题。

---

## Agent 与具身智能

### 23. [SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation](https://arxiv.org/abs/2610.12457)

**作者**: Jiayu Wang, Yue Yu, Bin Zhu et al.
**方向**: `Agent` | **代码**: [GitHub](https://github.com/emilia113/SpatialHarness)

提出 SpatialHarness，测试时具身支架，为精细机器人操作提供空间支架而无需策略微调。维护模拟场景、识别任务关键空间关系并渲染互补虚拟视图。在插头插入任务上从 26.7% 提升至 66.7%，汉诺塔任务从 0% 提升至 100%。

---

### 24. [Mental-Models for Multi-Agent Systems](https://arxiv.org/abs/2610.12453)

**作者**: Hanan Gani, Lulu Shao, Manmohan Chandraker et al.
**方向**: `Agent` | **代码**: [GitHub](https://github.com/hananshafi/Mental-Models)

提出心智模型驱动的智能体，在部分可观测下学习潜在伙伴状态表示进行多智能体决策。联合学习心智理论表示和信念条件奖励模型。在纯语言和多模态基准上提升交互质量。

---

### 25. [OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video](https://arxiv.org/abs/2610.12419)

**作者**: Hongyu Li, Manyuan Zhang, Kaituo Feng et al.
**方向**: `Agent` | **代码**: [GitHub](https://github.com/appletea233/OneSearch-VL)

提出 OneSearch-VL，以视觉接地证据图为核心的统一智能体，跨图像和视频进行深度研究。使用 SFT 和 RL 数据集及证据感知视觉接地奖励，相比 Qwen3-VL-8B 提升 20.2 和 17.6 个百分点。

---

### 26. [SuperNav: An Agentic Navigation System for Any Task in Any Scene](https://arxiv.org/abs/2610.12126)

**作者**: Jinkai Zhang, Jingyi Xu, Yuanhong Yu et al.
**方向**: `Agent` | **代码**: [GitHub](https://github.com/zju3dv/SuperNav)

SuperNav 为预训练 MLLM 配备专用智能体支架，无需导航特定微调。使用导航技能、工具和视觉点接口进行决策。在实例级、多对象和需求驱动任务上超越基线，包括真实四足机器人部署。

---

### 27. [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](https://arxiv.org/abs/2610.12090)

**作者**: Hongyu Shi, Sen Zhao, Zuyu Zhang et al.
**方向**: `Agent` | **代码**: 暂无代码

提出 FLOWMEM，将成功的潜在计算转化为可复用推理经验，动态检索和重组潜在片段。路径通过当前视觉和本体感受证据细化。在 RoboMME 和 LIBERO-Plus 上分别达到 48.0% 和 77.3% 成功率。

---

### 28. [Humanoid World Action Model With Joint State-Action Generation](https://arxiv.org/abs/2610.12026)

**作者**: Yan Yang, Jikun Rong, Minzhao Zhu et al.
**方向**: `Agent` | **代码**: 暂无代码

HWAM 联合生成参考动作和实现身体状态，通过策略、正向动力学建模和逆向动力学建模路径监督。在 LimX OLI 人形机器人上糖果拾取任务达到 70.6% 成功率，对比 Fast-WAM 的 43.3%。

---

### 29. [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](https://arxiv.org/abs/2610.12107)

**作者**: Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou et al.
**方向**: `Agent` | **代码**: 暂无代码

将 GRES 重构为闭环视觉运动过程，以可编辑轮廓作为策略状态。演化感知语义调度耦合轮廓引导采样与状态条件路由。在 gRefCOCO val/testA/testB 上 gIoU 分别提升 8.7、2.8 和 2.7 个百分点。

---

### 30. [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](https://arxiv.org/abs/2610.10409)

**作者**: Zhiqin Yang, Chenxin Li, Xiaomeng Hu et al.
**方向**: `Agent` | **代码**: 暂无代码

RobotWorld 基准评估多模态智能体在不同任务和具身形态下的机器人使用能力。提供多样化的任务场景和评估指标，系统测试 MLLM 作为机器人控制器的表现。

---

### 31. [RoboQuest: Generalist Physical Agents that Search, Inspect and Test](https://arxiv.org/abs/2610.10388)

**作者**: Liu Renhang, Navonil Majumder, Tej Deep Pala et al.
**方向**: `Agent` | **代码**: [GitHub](https://github.com/declare-lab/RoboQuest)

提出 RoboQuest，通用物理智能体具备搜索、检查和测试能力。在真实物理环境中执行复杂的多步骤任务，展示通用具身智能的潜力。

---

### 32. [AdaptEvo: Adaptive Agent Learning with Evolving Supervision](https://arxiv.org/abs/2610.11354)

**作者**: Shijun Wan, Jiancong Xie, Hang Xu et al.
**方向**: `Agent` | **代码**: 暂无代码

提出 AdaptEvo 框架，耦合置信自适应策略优化与演化决策知识。在工业多模态内容审核数据集上达到 61.9% 精确标签准确率，实现智能体学习的自适应演化。

---

## 多模态生成

### 33. [Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models](https://arxiv.org/abs/2610.10990)

**作者**: Hong Huang, Chenhongyi Yang, Junzhe Sun et al.
**方向**: `生成` | **代码**: 暂无代码

提出 Omni-Diffusion-Distill，统一多模态扩散大语言模型的少步蒸馏方法。将多步扩散过程压缩到更少步骤，保持生成质量的同时大幅提升推理效率。

---

### 34. [Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems](https://arxiv.org/abs/2610.12449)

**作者**: Anna Zimmel, Fleur Hendriks, Markus Holzleitner et al.
**方向**: `生成` | **代码**: 暂无代码

Bi-FORK 是高维分叉系统中一对多解映射的生成框架。通过潜在流匹配和排斥引导采样恢复不同分支，可扩展到多达 260,000 个离散化点，覆盖屈曲梁、超材料和相分离。

---

### 35. [Self-correction Optimization for Interleaved Multimodal Generation](https://arxiv.org/abs/2610.10400)

**作者**: Xin You, Zhiwei Ning, Zukai Chen et al.
**方向**: `生成` | **代码**: 暂无代码

提出交错多模态生成的自纠正优化方法。通过自动检测和修正在交错文本-图像生成过程中的错误，提升多模态内容生成的质量和一致性。

---

### 36. [TKCAM: Text and Keyframe to Camera Trajectory Generation](https://arxiv.org/abs/2610.11105)

**作者**: Haozhe Yang, Zhiyang Dou, Zekai Gu et al.
**方向**: `生成` | **代码**: [GitHub](https://github.com/linearalgebrayhz/TKCAM)

TKCAM 从文本和关键帧生成相机轨迹。结合语言描述和视觉关键帧信息，自动规划合理的相机运动路径，适用于视频制作和虚拟现实场景。

---

### 37. [Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers](https://arxiv.org/abs/2610.11315)

**作者**: Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan
**方向**: `生成` | **代码**: 暂无代码

提出统一框架，将低秩辅助 W4A4 PTQ 建模为耦合校准问题，配合基于优化的求解器。Rank-4 方法优于 rank-32 SVDQuant，为多模态扩散 Transformer 提供高效量化方案。

---

## 音频多模态

### 38. [Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion](https://arxiv.org/abs/2610.11846)

**作者**: Anirudh Praveen, Koteswar Rao Jerripothula, Pratik Joshi et al.
**方向**: `音频` | **代码**: 暂无代码

提出复值相似度和融合方法，通过复值神经网络（CVNN）实现音视频事件定位。四流架构配合配对虚部流在开放词汇 OV-AVEBench 上达到 66.5/59.1/54.1% Acc/Seg-F1/Event-F1，创 SOTA。

---

### 39. [EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248)

**作者**: Heeseung Kim
**方向**: `音频` | **代码**: [Project Page](https://egocentricvoice.github.io/)

EgoVoice 是从自我中心多模态流进行主动语音辅助的框架。微调全模态 LLM 优化主动干预行为，在干预时机、内容相关性和人类偏好方面均有提升。

---

### 40. [Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models](https://arxiv.org/abs/2610.11196)

**作者**: Yulin Sun, Kele Xu, Yong Dou
**方向**: `音频` | **代码**: 暂无代码

提出 ICAP-Gate，对每个模型的音频通路施加任务条件控制。在 16 个模型-条件评估中，影响率和答案翻转率均低于无门控推理，实现大型音频语言模型的选择性听觉。

---

### 41. [Event-Native Immersive Communication for 6G: From Multimodal Streams to Event Beliefs](https://arxiv.org/abs/2610.12270)

**作者**: Yiyang Zhu, Li Wei, Chau Yuen et al.
**方向**: `音频` | **代码**: 暂无代码

提出事件原生的沉浸式通信框架，物理事件定义通信对象。事件信念缺陷（EBD）评估体验质量，推导高斯事件信念在瑞利衰落上的 log-det EBD、中断概率和发射 SNR。

---

## 3D 视觉语言

### 42. [SubDGuide: A Modeler-Inspired Agentic Workflow for Mesh-to-SubD Reconstruction](https://arxiv.org/abs/2610.11721)

**作者**: Mengnan Jiang, Christian Franke, Michele Franco Adesso et al.
**方向**: `3D` | **代码**: 暂无代码

提出智能体工作流用于细分曲面笼恢复。中位 Chamfer-L1 从 0.641% 降至 0.443%，1% 容差下 F-score 从 82.00% 提升至 92.78%，实现高质量 Mesh 到 SubD 重建。

---

### 43. [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215)

**作者**: Qirui Wu, Stan Birchfield, Hesam Rabeti et al.
**方向**: `3D` | **代码**: 暂无代码

GATOR 从一张或多张图像恢复纹理对象资产和场景相对位姿。使用多模态智能体配合观察引导的编辑-渲染-审查循环，实现高质量 3D 对象重建。

---

### 44. [OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes](https://arxiv.org/abs/2610.11194)

**作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo et al.
**方向**: `3D` | **代码**: 暂无代码

构建超过 260 万个场景和 4 亿场景特定抓取真值的基准。OmniDex 模型克服抓取多模态性和最后毫米精度误差，将灵巧手抓取扩展到多样化杂乱场景。

---

### 45. [Temporal Visuo-Tactile Learning for Dexterous Grasp Stability](https://arxiv.org/abs/2610.10283)

**作者**: Ken Nakahara, Aleksei Buvailik, Prokhor Kotov et al.
**方向**: `3D` | **代码**: [Project Page](https://lasr-lab.github.io/dexterous-grasp-stability/)

提出时间视觉-触觉学习方法用于灵巧抓取稳定性。结合视觉和触觉信号的时间序列，预测和维持抓取稳定性，提升灵巧手操作的可靠性。

---

## 多模态检索与信息抽取

### 46. [Autoregressive Retriever: Improving Query Understanding from Item Feedback for Universal Multimodal Retrieval](https://arxiv.org/abs/2610.11666)

**作者**: Jianfei Zhao, Yifan Wang, Feng Zhang et al.
**方向**: `检索` | **代码**: [GitHub](https://github.com/LEOXC1571/Code-of-ARR)

提出 ARR，多模态检索模型学习选择有信息量的项目并使用其内容优化后续检索。通过监督微调和强化学习，实现从项目反馈中改进查询理解的通用多模态检索。

---

### 47. [EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval](https://arxiv.org/abs/2610.11553)

**作者**: Zifei Wang, Wei Wen, Qiang Ji et al.
**方向**: `检索` | **代码**: [GitHub](https://github.com/Tencent/EVIE)

提出 EVIE，原生视觉文档检索器家族，采用证据评判数据治理、双向师生学习和层次凝聚索引压缩。为视觉文档检索提供高效的嵌入表示方法。

---

### 48. [CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at Scale](https://arxiv.org/abs/2610.11230)

**作者**: Shixin Wan, Guoyu Hu, Yifan Wu et al.
**方向**: `检索` | **代码**: 暂无代码

CORAL 是 GPU 加速的图索引用于跨模态检索，支持层次内存管理。实现 1.6 倍吞吐量和 56% 构建时间减少，适用于大规模跨模态向量检索场景。

---

### 49. [MSGAT: Multi-Head Spiking Graph Attention with Similarity-Space Fusion for Image-Text Retrieval](https://arxiv.org/abs/2610.11526)

**作者**: Xintao Zong, Wenxuan Liu, Jianhao Ding et al.
**方向**: `检索` | **代码**: 暂无代码

提出多头脉冲图注意力网络配合 Sim-Fuse 相似度空间融合。相比 ANN 对应方法实现 55% 理论模块级能耗降低，为图文检索提供高效脉冲神经网络方案。

---

### 50. [Multimodal Graph Retrieval-Augmented Sequential Recommendation via Collaborative Filtering Paths](https://arxiv.org/abs/2610.11228)

**作者**: Jason Marcell Setiadi, Xin Cao, Lina Yao
**方向**: `检索` | **代码**: 暂无代码

MGRASRec 将协同过滤信号直接注入 MLLM 提示，通过从用户-项目交互图中检索结构化路径实现。结合多模态图检索增强序列推荐。

---

> 自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-10-11
