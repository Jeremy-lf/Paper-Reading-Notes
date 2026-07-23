# Arxiv 多模态论文日报 - 2026-06-21

## VLM/MLLM

### [Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2606.19565)

**作者:** Navin Ranjan, Andreas Savakis | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出 Mix-QVLA，一种面向视觉-语言-动作（VLA）模型的任务证据感知混合精度后训练量化框架。该方法通过对比全精度与量化模型在关键功能边界上的任务证据图，得到随任务阶段变化的层敏感度分数，并据此在模型大小与 BitOps 预算约束下分配混合精度位宽。在 OpenVLA 风格策略上的实验表明，Mix-QVLA 可将内存从 15.4 GB 降至 4.1 GB，同时保持 96.3% 的平均成功率，并取得 1.52 倍推理加速。

---

### [Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding](https://arxiv.org/abs/2606.19776)

**作者:** Jianing Li, Zhou Fang, Yijiang Liu et al. | **方向:** VLM/MLLM, 理解与推理, 暂无代码 | **代码:** 无

本文提出 Occ-VLM，一种仅依赖姿态 RGB 图像、使用单一 2D 视觉编码器的室内 3D 场景理解框架。该方法将 3D 占用重建作为辅助几何先验，把前景 2D 视觉 token 与 3D 空间关联后输入大语言模型，实现几何感知与视觉-语言推理的统一。实验表明 Occ-VLM 在多视图占用预测上达到 SOTA，并在 3D VQA 与 3D 稠密描述基准上媲美使用 3D 输入的 VLM。

---

### [SpatialSV: Internalizing Interpretable 3D Spatial Awareness in MLLMs via Task-Oriented Visual Supervision](https://arxiv.org/abs/2606.19915)

**作者:** Jiayu Tang, Yuchen Zhou, Chao Gou | **方向:** VLM/MLLM, 3D视觉语言, 暂无代码 | **代码:** 无

本文提出 SpatialSV，通过任务导向的视觉监督将可解释的 3D 空间意识内嵌到多模态大语言模型（MLLM）中。模型被显式约束将 2D 视觉特征提升为深度图、相机位姿和点云等 3D 表示，使空间推理过程可被可视化和诊断。在多个模型与空间推理基准上的实验表明，SpatialSV 有效增强了 MLLM 的空间智能，并在半监督场景下展现出良好的泛化能力。

---

### [CARE: Competence-Aware Reward Shaping for Adaptive Reasoning Length in Video-MLLMs](https://arxiv.org/abs/2606.19927)

**作者:** Chengwen Liu, Hao Peng, Jisheng Dang et al. | **方向:** VLM/MLLM, 理解与推理, 有代码 | **代码:** [Code](https://github.com/1Pansy/Video-CARE)

本文提出 CARE，一种面向视频多模态推理的能力感知奖励塑形框架，用于自适应地优化推理长度。该方法通过指数移动平均估计模型能力，动态地在探索导向的长推理与效率导向的短推理之间切换奖励偏好，并结合批统计归一化与后验放大器增强困难样本信号。实验表明 CARE 在多个视频推理与视频理解基准上提升了推理准确率、强化学习稳定性，并显著提高了 token 效率。

---

### [Timage: A Generative Text-in-Image Paradigm for Fine-Tuning Vision-Language Models](https://arxiv.org/abs/2606.19944)

**作者:** Yifeng Wu, Huimin Huang, Ruiluo Wu et al. | **方向:** VLM/MLLM, 多模态生成, 暂无代码 | **代码:** 无

本文提出 Timage，一种将文本查询以排版覆盖层形式渲染到图像上的生成式文本-图像对齐范式，用于增强细粒度空间推理。该方法利用约束薛定谔桥将布局合成拆分为区域搜索与外观塑造两个随机阶段，在保护显著前景的同时生成清晰可读的文本覆盖，作为显式空间注意力锚点。在 VMCBench 上，仅 7B 骨干的 Timage 即超越了更大规模的专有系统和参数微调基线。

---

### [Confidence Calibration for Multimodal LLMs: An Empirical Study through Medical VQA](https://arxiv.org/abs/2606.19950)

**作者:** Yuetian Du, Yucheng Wang, Ming Kong et al. | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文首次系统分析了医学多模态大语言模型（MLLM）在视觉问答中的准确率与置信度之间的错配问题。研究提出融合多策略询问与辅助专家 LLM 评估的校准方法，在三个医学 VQA 数据集上平均降低期望校准误差（ECE）40%。结果表明领域特定的置信度校准对提升医疗 MLLM 可靠性与辅助诊断可信度具有重要意义。

---

### [See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View](https://arxiv.org/abs/2606.20045)

**作者:** Fanfu Xue, En Yu, Yantian Shen et al. | **方向:** VLM/MLLM, Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/xuefanfu/3DG-VLN)

本文针对无人机视觉-语言导航提出目标可见阶段的 see-and-reach 任务，并构建 3DG-VLN 框架。该方法自适应处理高分辨率前视与下视观测以保留细粒度视觉-几何细节，并在闭环导航中在线更新目标相对方向，实现精确的目标定位与 3D 航点预测。在新构建的 2,717 条轨迹基准上，3DG-VLN 较竞争基线成功率提升 13.82%，并在真实无人机试验中验证了可行性。

---

### [The Hidden Evolution of Disguised Visual Context inside the VLM](https://arxiv.org/abs/2606.20077)

**作者:** Wish Suharitdamrong, Tony Alex, Muhammad Awais et al. | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文在相同训练条件下系统比较了上下文提示与逐层注入两种 VLM 视觉集成范式。研究发现视觉 token 进入大语言模型后会被逐步重塑，不同范式捕获不同的视觉频率特征，这种内部演化决定了模型能有效利用的视觉特征、视觉表征与语言空间的对齐方式以及各范式在不同任务上的表现。该工作揭示了视觉-语言对齐的内在机制，表明仅关注注意力分配不足以解释性能差异。

---

### [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092)

**作者:** Ganlin Yang, Zhangzheng Tu, Yuqiang Yang et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出 EventVLA，一种基于稀疏视觉证据记忆的长程视觉-语言-动作（VLA）策略框架。该方法通过基础视觉锚点与动态关键帧证据记忆模块，从 VLA 隐式嵌入预测未来关键帧概率，主动保存转瞬即逝的任务关键视觉证据。在 17 个需要记忆的仿真任务和 4 个真实世界双臂任务中，EventVLA 较 SOTA 记忆增强 VLA 平均成功率提升 40%。

---

### [Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs](https://arxiv.org/abs/2606.20177)

**作者:** Haochen Han, Jue Wang, Alex Jinpeng Wang et al. | **方向:** VLM/MLLM, 基准评测, 暂无代码 | **代码:** 无

本文提出 RS-Neg，首个面向遥感多模态大语言模型否定理解的基准，覆盖区域级到场景级任务。研究设计了基于 LLM 的自动化数据生成流程和动态视觉聚焦验证模块，揭示了现有遥感 MLLM 在否定查询中存在严重幻觉与性能退化。为此，本文提出测试时学习方法 NeFo，仅利用约 5% 未标注测试样本即可显著提升否定理解能力，并泛化到未见任务。

---

### [SPOT-E: Test-Time Entropy Shaping with Visual Spotlights for Frozen VLMs](https://arxiv.org/abs/2606.20244)

**作者:** Bo Yin, Xiaobin Hu, Chengming Xu et al. | **方向:** VLM/MLLM, 有代码 | **代码:** [Code](https://github.com/YinBo0927/SPOT-E)

本文提出 SPOT-E，一种面向冻结视觉-语言模型的测试时熵塑形方法，用于提升证据密集型任务的视觉定位。该方法以答案跨度预测熵作为内部反馈信号，引入低熵锚点和熵塑形目标，通过轻量化的 GRPO 优化为每个实例生成问题条件化的视觉 spotlights。在多个基准和不同 VLM 家族上的实验表明，SPOT-E 在不重新训练的情况下带来一致的性能提升，并增强了对视觉破坏的鲁棒性。

---

### [Spectral Query-Key Product Weight Steering for Training-Free VLM Hallucination Mitigation](https://arxiv.org/abs/2606.20419)

**作者:** Karn Tiwari, Varnith Chordia, Prathosh A P | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文提出 QK Product Steering，一种无数据、无训练、零推理开销的权重编辑方法，用于抑制视觉-语言模型的物体幻觉。该方法直接编辑中间层每头 query-key 积中的主导奇异模式，并通过闭式 query-only 更新将其映射回 query 权重，同时保持共享 key 权重不变，兼容分组查询注意力。在三个基于 GQA 的 VLM 上，该方法平均相对降低 CHAIR_s 4.0%，且基本保持通用多模态能力。

---

### [Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology](https://arxiv.org/abs/2606.20477)

**作者:** Yusuf Salcan, Simon Ging, Robin Schirrmeister et al. | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文研究如何在没有人工空间标注的情况下训练面向放射学的空间可证 2D 视觉-语言模型。作者构建大规模双语（德/英）CT 与 MR 图像-文本数据集 RefRad2D，并训练出可同时完成报告生成、视觉问答与边界框/分割定位的模型 RadGrounder。实验表明，添加定位监督不会损害语言质量，且在多个外部医学 VQA 基准上取得有竞争力的性能，展示了临床数据的可迁移性。

---

### [SAFE-Cascade: Cost-Adaptive Vision-Language Routing for Chart Question Answering](https://arxiv.org/abs/2606.19646)

**作者:** Ayush Dwivedi, Qixin Wang, Ashvi Soni et al. | **方向:** VLM/MLLM, 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出 SAFE-Cascade，一种面向图表问答的成本自适应级联系统。系统先用 OCR 提取文本并由轻量语言模型生成临时答案，再通过学习得到的路由器判断是否调用 VLM，从而在保持准确率的同时降低推理成本。在 ChartQA 测试集上，该系统在匹配全 VLM 准确率的前提下将 VLM 调用率从 100% 降至 73.1%， estimated cost 降低 9.3%，并提供了透明的多模态决策界面。

---

### [StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs](https://arxiv.org/abs/2606.20527)

**作者:** Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal et al. | **方向:** VLM/MLLM, 有代码 | **代码:** [Code](https://github.com/timo-cavelius/StylisticBias)

本文提出 StylisticBias 基准，用于在属性层面控制评估多模态大语言模型中的社会偏见。研究在固定身份基础上对 500 张基础人脸生成约 2.5 万张单属性变化图像，发现年龄、体型等少数视觉线索驱动了大部分社会判断偏移，其中约 15 个属性即可解释近 80% 的总变异。该工作强调需要结合人类偏好对 MLLM 进行细粒度、公平性导向的评估。

---

### [Learning Geometric Representations from Videos for Spatial Intelligent Multimodal Large Language Models](https://arxiv.org/abs/2606.05833)

**作者:** Haibo Wang, Lifu Huang | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文提出 GeoVR，一种仅利用 2D 视频学习几何表征以增强多模态大语言模型空间智能的框架。该方法通过估计相机位姿、回归稠密深度图、预测度量尺度因子并蒸馏多尺度 3D 特征，将显式物理与几何约束注入 MLLM 的内部表征。在空间推理基准上的实验表明 GeoVR 取得 SOTA 性能，为在缺乏大规模 3D 数据的情况下赋予基础模型空间智能提供了新范式。

---

### [REVEAL++: Differentiable Phenotypic Grouping for Vision-Language Retinal Modeling of Alzheimer's Disease Risk](https://arxiv.org/abs/2606.19522)

**作者:** Ethan Elio Meidinger, Seowung Leem, Zeyun Zhao et al. | **方向:** VLM/MLLM, 暂无代码 | **代码:** 无

本文提出 REVEAL++，一种用于视觉-语言视网膜阿尔茨海默风险建模的可微分表型分组方法。该方法将离散硬分组转换为基于视网膜图像与风险档案嵌入相似度的连续软多正例关系，通过软目标对比目标端到端地学习跨模态对齐与表型结构。在 UK Biobank 数据上的实验表明，REVEAL++ 在阿尔茨海默发病预测上持续优于离散分组对比学习和标准视觉-语言基线。

---

### [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246)

**作者:** Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文揭示大规模视觉-语言-动作（VLA）模型存在严重的层间表征冗余，并提出完全免训练的深度压缩流程。该方法仅通过单次前向传递的中心核对齐识别冗余层，移除孪生层以永久压缩模型深度达 50%，然后对精简架构进行下游微调。在 LIBERO、RoboCasa、SimplerEnv 以及 10 项真实机器人任务上的实验表明，微调后的压缩模型训练时间减少 40-50%、推理加速 30%，同时达到或超越全规模基线。

---

### [RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models](https://arxiv.org/abs/2606.18950)

**作者:** San Kim, Daechul Ahn, Reokyoung Kim et al. | **方向:** VLM/MLLM, 理解与推理, 暂无代码 | **代码:** 无

本文提出 RTSGameBench，一个基于 Beyond All Reason 的实时战略游戏基准，用于评估视觉-语言模型在竞争与合作场景中的战略推理能力。该基准提供多样化对战评估、针对单一战略能力的诊断性小游戏，以及将自由文本查询转化为新小游戏的自演化生成框架。实验显示，当对局需要更紧密的多智能体协作或任务规模扩大时，多个 SOTA VLM 的性能显著下降。

---

### [Judging to Improve: A De-biased VLM-as-3D-Judge Protocol for Single-Image 3D Generation](https://arxiv.org/abs/2606.20364)

**作者:** Ali Asaria, Tony Salomone, Deep Gandhi | **方向:** VLM/MLLM, 多模态生成, 暂无代码 | **代码:** 无

本文提出一种去偏的 VLM-as-3D-Judge 协议，并将其偏好信号用于优化单图像 3D 生成器 TRELLIS。研究通过训练法官与评估法官分离、位置偏差修正以及对图像过载、几何隐藏渲染和参考无关判断等失效模式的修复，构建适合优化循环的评判流程。实验发现，在仅使用公开数据和轻量参数高效自适应的情况下，现有方法难以超越强基线，但该评判协议本身具有良好的可复用性。

---

### [EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models](https://arxiv.org/abs/2606.19784)

**作者:** Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出 EquiVLA，首个面向任意架构的端到端 SO(2) 等变视觉-语言-动作模型通用框架。该方法包含 EquiPerceptor，可从冻结 ViT 特征生成近似旋转等变视觉表征；以及 EquiActor，一种精确等变的流匹配 Diffusion Transformer 动作头。在 LIBERO、CALVIN ABCD→D 和 Mobile ALOHA 真实任务上的实验表明，EquiVLA 显著提升了旋转配置泛化能力，LIBERO 平均成功率从 78.1% 提升至 92.6%。

---

### [Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](https://arxiv.org/abs/2606.20285)

**作者:** Yandong Wang, Jiaqian Yu, Xiongfeng Peng et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出 Co-VLA，一种面向双臂视觉-语言-动作系统的协调感知结构化动作建模框架。该方法将单一动作头替换为结构化动作专家，通过共享潜变量编码任务级协调意图、残差潜变量编码单臂执行调整，并引入模块化协调感知损失。部署时的潜变量感知控制器可在关节命令级别实时调节同步强度、执行不对称性、平滑度与安全约束。实验表明 Co-VLA 在紧协调任务上成功率提升 27%，真实 OOD 场景性能提升一倍以上。

---

### [Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation](https://arxiv.org/abs/2606.20458)

**作者:** Zhenghao "Mark" Peng, Honglin He, Quanyi Li et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出一种延迟 resilient 的 VLM-Planner 接口，用于增强城市人行道导航中的轨迹评分。该方法让 VLM 从传统规划器生成的候选轨迹集合中选择最优索引，并通过几何相似度与指数衰减融合的轻量层，将存在 1–3 秒延迟的 VLM 选择实时转化为规划器评分。在约 2,000 个具有挑战性的真实场景和仿真实验中，VLM 选择使平均位移误差降低 30%，在延迟达 5 秒时仍保持 80% 以上成功率。

---

### [GroundControl: Anticipating Navigation Failures in Vision-Language Agents via Trajectory-Consistent Uncertainty Estimates](https://arxiv.org/abs/2606.20479)

**作者:** Nastaran Darabi, Divake Kumar, Sina Tayebati et al. | **方向:** VLM/MLLM, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出 GroundControl，一种通过轨迹一致性不确定性估计来预判视觉-语言导航智能体失败的算法。该方法使用常速卡尔曼滤波建模到目标距离的演化，将归一化新息与反映进度、单调性、路径效率和振荡行为的轨迹特征结合，衡量导航行为偏离目标导向动态的程度。在 EB-Navigation 多个拆分上的实验表明，GroundControl 在基于成功率与 SPL 的选择性风险评估中均取得最低的 AURC/E-AURC，显著优于熵、共形预测和启发式基线。

---

## 理解与推理

### [PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models](https://arxiv.org/abs/2606.19534)

**作者:** Yueyi Sun, Yuhao Wang, Jason Li et al. | **方向:** 理解与推理, 多模态生成, 有代码 | **代码:** [Code](https://github.com/MSALab-PKU/PerceptionDLM)

本文提出 PerceptionDLM，一种面向并行区域感知的多模态扩散语言模型。通过高效提示与结构化注意力掩码，模型可在序列和 token 两个层面同时对多个掩码区域进行感知与描述，显著提升了多区域感知任务的推理效率。为系统评估扩散语言模型的并行视觉感知能力，作者还构建了 ParaDLC-Bench 基准，实验表明 PerceptionDLM 在保持区域描述性能竞争力的同时，大幅加速了多区域感知。

---

### [ROSE: Benchmarking the Perception-to-Action Gap in Multimodal Models](https://arxiv.org/abs/2606.19965)

**作者:** Yihao Wang, Zijian He, Jie Ren et al. | **方向:** 理解与推理, 基准评测, 暂无代码 | **代码:** 无

本文提出 ROSE 基准，通过固定视觉场景并变化区域约束与符号输出，系统评测多模态大模型将共享视觉证据转换为上下文相关动作的能力。在计数与坐标动作耦合任务上，实验发现 9 个最新 MLLM 从计数任务到区域条件动作任务的性能下降最高可达 44.5 个百分点，揭示了模型在感知到动作转化过程中存在显著的、模型依赖性的瓶颈。

---

### [Vision-Reasoning-Guided Occlusion Removal from Light Fields](https://arxiv.org/abs/2606.19985)

**作者:** Mohamed Youssef, Oliver Bimber | **方向:** 理解与推理, 暂无代码 | **代码:** 无

本文提出一种视觉推理引导的光场遮挡去除框架，将光场积分（LFI）的可见性恢复能力与视觉语言模型的语义推理能力相结合。多视角观测首先经 LFI 抑制前景遮挡，随后以 VLM 作为条件语义先验恢复退化结构与细节；并通过多样本融合策略提升恢复一致性、减少幻觉伪影。在合成与真实数据集上均取得领先性能，对搜救与机器人探索导航等场景具有应用价值。

---

### [S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence](https://arxiv.org/abs/2606.20515)

**作者:** Yalun Dai, Hao Li, Shulin Tian et al. | **方向:** 理解与推理, Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/Ropedia/S-Agent/)

本文提出 S-Agent，一种空间工具使用智能体范式，将空间推理建模为时空证据累积而非孤立帧预测。S-Agent 以 VLM 作为语义规划器，配合层级空间工具与专家，将 2D 目标提升为 3D 几何证据并聚合为计数、测距、朝向和相对位置等高级空间知识；同时通过场景记忆和智能体记忆实现跨帧与跨推理步骤的证据整合。实验表明，该方法在无需训练的情况下即可持续提升开源与闭源 VLM 的空间推理能力，经 SFT 得到的 S-Agent-8B 甚至可比肩 GPT-5.4 与 Gemini 3。

---

### [TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living](https://arxiv.org/abs/2606.20561)

**作者:** Arkaprava Sinha, Dominick Reilly, Siddharth Krishnan et al. | **方向:** 理解与推理, 暂无代码 | **代码:** 无

本文提出 TimeProVe，一种面向长视频时间推理的成本高效混合框架。该框架先用轻量模块生成基于动作的答案-证据假设，再仅对关键证据调用昂贵 VLM 进行验证；核心 ACE 模块将时间定位动作转换为查询条件候选答案与支持证据窗口。作者还引入面向日常活动（ADL）真实场景的开放式基准 OpenTSUBench，实验显示 TimeProVe 在 OTB 上较最强基线提升 7.3%，同时减少 75% 的 VLM 调用和 93% 的推理成本。

---

### [MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization](https://arxiv.org/abs/2606.20164)

**作者:** Aueaphum Aueawatthanaphisut | **方向:** 理解与推理, 暂无代码 | **代码:** 无

本文提出 MedRLM，一种递归多模态健康智能框架，用于长上下文临床推理、传感器引导筛查、循证决策支持以及社区到三级医院的转诊优化。MedRLM 将患者病例视为可递归检查、分解、检索、验证与综合的外部临床环境，通过临床证据图记忆连接患者观察、循证知识、传感器生物标志物与转诊标准；并引入传感器触发的递归推理和不确定性门控精化机制，以推动医疗 AI 从静态问答向可审计、多模态、工作流感知的临床决策支持演进。

---

### [Robust Assembly State Reasoning from Action Recognition for Human-Robot Collaboration](https://arxiv.org/abs/2606.20150)

**作者:** James Fant-Male, Roel Pieters | **方向:** 理解与推理, Agent与具身智能, 暂无代码 | **代码:** 无

本文系统研究并比较了基于动作识别输入跟踪人机协作装配状态的方法，涵盖逻辑方法、隐马尔可夫模型（HMM）和神经网络（NN）等五种方法，并在两个多样化数据集以及不同噪声水平的模拟输入与真实 HAR 模型输出上进行评估。实验结果表明，不同任务的最优方法并不统一：NN 与 HMM 在变化有限的任务中表现良好，而逻辑方法在其他场景下更具鲁棒性；对包含重复动作的任务，建模预期动作时长尤为重要。

---

## 基准评测

### [WeGenBench: A Multidimensional Diagnostic Benchmark towards Text-to-Image Model Optimization](https://arxiv.org/abs/2606.20100)

**作者:** Qian Liang, Xiaomin Li, Ying Zhang et al. | **方向:** 基准评测, 多模态生成, 暂无代码 | **代码:** 无

WeGenBench 是一项面向文本到图像生成模型的多维诊断基准，包含 4000 条中英双语测试提示，并通过场景分类与多维标签细粒度定位模型在特定生成类别上的缺陷。该基准还设计了基于视觉语言模型的新型评估指标，可输出评测结果与详细推理轨迹，以更准确地衡量生成质量。

---

### [HEad and neCK TumOR (HECKTOR) 2025: Benchmark of Segmentation, Diagnosis, and Prognosis in Multimodal PET/CT](https://arxiv.org/abs/2606.20143)

**作者:** Numan Saeed, Salma Hassan, Shahad Hardan et al. | **方向:** 基准评测, 有代码 | **代码:** [Code](https://github.com/BioMedIA-MBZUAI/HECKTOR2025)

HECKTOR 2025 是一项针对头颈癌的多模态 PET/CT 基准挑战，涵盖来自全球 10 个中心的 1100 余名患者。该基准包含原发肿瘤与转移淋巴结分割、无复发生存预测以及 HPV 状态分类三项任务，并系统评估了 15 支参赛队伍的算法性能。

---

### [Evaluation of Image Matching for Art Skills Assessment](https://arxiv.org/abs/2606.20199)

**作者:** Asaad Alghamdi, Michael Poor, Trung-Nghia Le et al. | **方向:** 基准评测, 暂无代码 | **代码:** 无

该研究提出通过将手绘图像与原始模板进行匹配来评估绘画技能水平，并对比了 SIFT 特征与孪生网络两种图像相似度度量方法。实验结果表明基于 SIFT 的关键点匹配能更有效地检测绘画技能差异。

---

### [BAFIS: Dataset + Framework to assess occupational Bias and Human Preference in modern Text-to-image Models](https://arxiv.org/abs/2606.20241)

**作者:** Thomas Klassert, Adrian Ulges, Biying Fu | **方向:** 基准评测, 多模态生成, 暂无代码 | **代码:** 无

BAFIS 构建了一个包含 21140 张合成图像的多语言数据集，用于评估当前文本到图像模型在职业相关图像生成中的性别与种族偏见。研究还开发了人机对抗式评估平台，结合自动化指标与人类偏好反馈，揭示模型存在系统性偏见。

---

### [PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2606.20455)

**作者:** Haoyuan Shen, Kuihao Wang, Ruisheng Wang et al. | **方向:** 基准评测, 3D视觉语言, 暂无代码 | **代码:** 无

PCFootprint 是首个面向机载激光雷达点云建筑轮廓提取的大规模公开数据集，包含 33000 个地块瓦片及与之对齐的矢量化建筑轮廓。研究还建立了跨域测试集与综合基准，揭示了复杂地理环境下类别不平衡、噪声等挑战。

---

### [The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation](https://arxiv.org/abs/2606.20536)

**作者:** Nicolas Dufour, Alexei A. Efros, Patrick Pérez | **方向:** 基准评测, 多模态生成, 暂无代码 | **代码:** 无

该研究将 FID 视为随机变量，通过在 ImageNet 上训练数百个 SiT 网络，量化了训练种子与生成种子对 FID 的隐藏随机性。研究发现重新训练带来的 FID 波动远大于重采样，并建议采用基于多个训练种子的误差条报告新协议。

---

### [CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation](https://arxiv.org/abs/2606.20542)

**作者:** Ilona Demler, Xinran Xie, Blake Werner et al. | **方向:** 基准评测, 3D视觉语言, 暂无代码 | **代码:** 无

CalTennis 是一个大规模多视角网球视频基准，包含来自 40 名球员的超过 1100 万帧（51 小时）视频。该数据集支持单目到三维姿态估计算法的低成本无标签评估，并提出了脚步移动与稳定性等新指标。

---

### [A Controlled Benchmark of Quantum-Latent GAN Augmentation for Brain MRI](https://arxiv.org/abs/2606.18970)

**作者:** Syed Mujtaba Haider, Silvia Figini | **方向:** 基准评测, 暂无代码 | **代码:** 无

该研究构建了一个对照基准，用于分离量子生成器在脑 MRI 数据增强中的真实贡献，并与参数规模相近的经典生成器进行公平比较。实验结果表明在低数据场景下，量子与经典生成器均无显著优势，且合成分布存在模式坍塌。

---

### [A Comparative Study of Pretrained Transformer Models for Quranic ASR: Speech Representations, Label Formats, and Dataset Composition](https://arxiv.org/abs/2606.19747)

**作者:** Nabil Mosharraf Hossain, Riasat Islam, Unaizah Obaidellah | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

该研究系统比较了 Wav2Vec2.0、HuBERT 与 XLS-R 三种预训练 Transformer 模型在古兰经自动语音识别上的微调表现。在超过 870 小时的专业与用户朗诵数据上，最佳配置在 EveryAyah 子集达到 0.08 的词错误率。

---

### [PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets](https://arxiv.org/abs/2606.19597)

**作者:** Junyi Fan, Donald S. Williamson | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

PrefSQA 提出了一种无需 MOS 标签的语音质量成对偏好预测方法，通过不确定性感知 logits、损伤注意力头与非匹配参考比较模块降低标签噪声。实验表明高质量偏好数据能显著提升模型在未见数据上的泛化能力。

---

### [Cross-Dataset, Age, and Gender Generalization: A Comprehensive Analysis of Fine-Tuning Strategies for Low-Resource Children's ASR](https://arxiv.org/abs/2606.19791)

**作者:** Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo et al. | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

该文针对低资源儿童自动语音识别，系统分析了跨数据集、年龄与性别的泛化问题，并比较了不同微调策略与声学特征组合。实验在 TORGO 等数据库上表明所提方法对构音障碍语音的孤立词与句子识别均有相对提升。

---

### [Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations](https://arxiv.org/abs/2606.19951)

**作者:** Masato Takagi, Masaya Kawamura, Reo Shimizu et al. | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

该研究通过对语音施加声学退化、韵律错误与说话人特征扰动，系统分析了 MOS 预测模型与人类感知之间的差异。结果发现现有模型对声学退化敏感，但对韵律错误和说话速率变化不敏感，揭示了标量 MOS 预测的局限性。

---

### [PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors](https://arxiv.org/abs/2606.20137)

**作者:** Masaya Kawamura, Yuma Shirahata, Kentaro Mitsui et al. | **方向:** 基准评测, 音频多模态, 有代码 | **代码:** [Code](https://github.com/lycorp-jp/PASQA)

PASQA 是一种面向 pitch-accent 正确性的语音质量评估模型，通过重音可控 TTS 构建日语重音错误数据集并训练模型。实验表明传统 MOS 模型无法保持重音错误严重程度的排序，而 PASQA 与人类重音正确性判断具有更强一致性。

---

### [LaViSA: A Language and Vision Structural Ambiguity Benchmark](https://arxiv.org/abs/2606.19552)

**作者:** Lee Sangmyeong, Shun Inadumi, Koichiro Yoshino | **方向:** 基准评测, 暂无代码 | **代码:** 无

LaViSA 是一个评估视觉语言模型利用视觉场景消解结构歧义能力的基准，涵盖 7 种歧义类型。实验显示尽管近期模型在一定程度上能借助视觉线索消歧，但在处理细微语义区别时仍存在明显不足。

---

### [Light-weight Pronunciation Assessment via Discrete Speech Token Surprisal](https://arxiv.org/abs/2606.19910)

**作者:** Syeda Faiza Ahmed Sara, Shammur Absar Chowdhury | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

该研究提出一种仅使用母语者数据训练的轻量化发音评估框架，通过自监督语音编码器将学习者语音离散化，并利用 token 语言模型计算惊讶度来检测发音偏差。在 SpeechOcean762 上，结合文本引导对齐的模型 PCC 从 0.60 提升至 0.66。

---

### [CATCH-ME if you RAG: a dataset of Contextually Annotated multi-Turn Counterspeech against Hate and Misinformation Exchanges](https://arxiv.org/abs/2606.20369)

**作者:** Helena Bonaldi, Genoveffa Martone, Marco Guerini | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

CATCH-ME 是首个针对仇恨言论与错误信息交叉领域的多语言多轮反话语数据集，覆盖 5 种语言与 7 个边缘化群体。数据集基于经过核实的外部知识构建，并包含文档与片段级跨度标注，可直接用于检索增强生成系统的训练与评估。

---

### [WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League](https://arxiv.org/abs/2606.19358)

**作者:** Wenbo Ma, Daniel Swoboda, Matteo Tschesche et al. | **方向:** 基准评测, Agent与具身智能, 暂无代码 | **代码:** 无

WorkBenchMark 是一个基于 LEGO Duplo 的机器人装配基准，面向智能制造联盟，提供 400 个分难度层级的装配任务。研究还提出了一种基于拆卸的基线方案，并将在模拟环境、数据集与基线实现上开源。

---

### [ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments](https://arxiv.org/abs/2606.19675)

**作者:** Natapat Kirdwichai, Danesh Tarapore | **方向:** 基准评测, Agent与具身智能, 暂无代码 | **代码:** 无

ForEnt 是一个记录四足机器人在森林环境中被困事件的多模态数据集，采集了 8 处森林样地约 1.7 公里的 traversal 数据。数据集包含 RGB-D 图像、LiDAR、本体感受与第三视角视频，支持被困检测策略的评估。

---

### [Evaluation of Augmented Reality-based Intuitive Interface for Robot-Assisted Transesophageal Echocardiography: A User Study](https://arxiv.org/abs/2606.19971)

**作者:** Xiu Zhang, Matteo Di Mauro, Sofia Breschi et al. | **方向:** 基准评测, Agent与具身智能, 暂无代码 | **代码:** 无

该研究针对机器人辅助经食道超声心动图（TEE）提出并评估了一种基于增强现实的直观交互界面。36 名参与者的用户研究表明，3D 尖端级交互界面显著降低了定位误差与工作负荷，为下一代机器人 TEE 系统设计提供了支持。

---

### [Beyond Speaker Independence: Evaluating Cross-Lingual Acoustic-to-Articulatory Inversion Across Finnish and Russian](https://arxiv.org/abs/2606.20478)

**作者:** Ruchi Pandey, Tomi Kinnunen | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

该研究在 FROST-EMA 芬兰-俄语双语 EMA 语料库上建立了跨语言声学到发音逆映射的基线基准，评估了不同发音目标、声学前端与反转后端在跨性别与跨语言迁移下的表现。结果显示跨语言错配导致约 0.10-0.20 的 Pearson 相关下降。

---

### [PolSeT: Polish Semantics of Timbre Dataset](https://arxiv.org/abs/2606.19987)

**作者:** Jan Jasiński | **方向:** 基准评测, 音频多模态, 暂无代码 | **代码:** 无

PolSeT 是一个用于波兰语音色语义研究的数据集，通过两项实验收集了 60 名参与者的自由语言描述与 105 名参与者的语义差异评分。数据集包含原始反应、人口统计学信息、音频刺激与声学特征，填补了音色研究开放数据的空白。

---

## 检索与信息抽取

### [Vortex: Multi-Modal Fusion System for Intelligent Video Retrieval](https://arxiv.org/abs/2606.19682)

**作者:** Duc-Tho Nguyen, Hieu-Hoc Tran-Minh, Khanh-Hoa Lam et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出多模态视频检索系统Vortex，针对2025年胡志明市AI挑战赛设计。系统融合自适应关键帧提取、视觉语言与语音模型生成的多模态元数据，以及结合CLIP与SigLIP2嵌入的混合检索策略，并通过Milvus与Elasticsearch实现可扩展索引。

---

### [Exploring Multi-Modal Large Language Models and Two-Stage Fine-Tuning for Fashion Image Retrieval](https://arxiv.org/abs/2606.19684)

**作者:** Nguyen Cao Hoang, Hoang Bui Le, Nam Vo Hoang et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文针对时尚领域的组合图像检索任务，提出结合多模态大语言模型与两阶段微调的新框架。利用LLaVA生成属性感知三元组，并通过CLIP等预训练视觉语言模型扩展负样本、增强对比学习，实验表明该方法提升了细粒度时尚图像检索的组成推理能力。

---

### [QueryGaussian: Scalable and Training-Free Open-Vocabulary 3D Instance Retrieval](https://arxiv.org/abs/2606.19733)

**作者:** Xiuyuan Zhu, Ke Lu, Zijie Yang et al. | **方向:** 检索与信息抽取, 3D视觉语言, 暂无代码 | **代码:** 无

本文提出QueryGaussian，一种无需训练、可扩展的开放词汇3D实例检索框架。通过实例级查询机制将语义理解与几何表示解耦，利用预训练2D视觉模型解释提示并lift分割掩码至3D，同时引入时序融合与自适应密度聚类缓解投影歧义，实现城市级高斯场景的高效检索。

---

### [VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme Cold-Start Conditions](https://arxiv.org/abs/2606.19627)

**作者:** Katya Mirylenka, Egor Malykh, Mahdyar Ravanbakhsh et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出面向电商短视频流的Video Candidate Generation（VCG）多模态检索框架，解决极端冷启动及沉浸式feed中的位置与时长偏差问题。基于领域自适应的视觉语言模型将用户与视频映射到共享语义空间，支持零样本内容检索，在线A/B测试显示深度视频完成率提升50%。

---

### [SIMBA: ABidirectional Retrieval Forward Simulation Framework for Modeling FY-4A GIIRS Hyperspectral Infrared Radiances Toward NWP Applications](https://arxiv.org/abs/2606.19943)

**作者:** Jingdong Shen, Fu Wang, Qifeng Lu et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出SIMBA，一个面向数值天气预报应用、针对FY-4A GIIRS高光谱红外辐射的统一双向检索-正向仿真框架。该方法联合进行大气廓线反演与辐射重建，引入循环一致性约束，并采用双向Mamba状态空间模块捕获气压层上的长程依赖，在多个反演与重建任务中优于代表性深度学习基线。

---

### [ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval](https://arxiv.org/abs/2606.20280)

**作者:** Yuhan Liu, Pei Fu, Hang Li et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出ELVA，一种基于规则的强化学习框架，用于缓解通用多模态检索中的“粒度盲”问题。通过将可验证奖励强化学习扩展到检索任务，并利用规则奖励联合优化负样本排序与正负样本相似度间隔，ELVA在标准检索基准上取得最先进结果，并在多粒度基准MRBench上提升13.1%。

---

### [Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries](https://arxiv.org/abs/2606.19960)

**作者:** Yuxiang Guo, Zhonghao Hu, Yuren Mao et al. | **方向:** 检索与信息抽取, 暂无代码 | **代码:** 无

本文提出Stellar，一种面向自然语言查询的可扩展多模态文档检索框架。通过将token级文档嵌入存储在磁盘，并设计基于词汇表示过滤的稀疏编码器与磁盘支持的后期交互机制，仅加载少量候选嵌入到内存，从而在保持检索效果的同时将内存开销与查询延迟降低1-2个数量级。

---

### [Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification](https://arxiv.org/abs/2606.19598)

**作者:** Ameya Salvi, Jie Hu | **方向:** 检索与信息抽取, Agent与具身智能, 暂无代码 | **代码:** 无

本文提出Fail-RAG，一种基于检索增强生成的机器人故障识别框架。该方法将故障图像与上下文信息嵌入后检索相似故障案例，再利用视觉语言模型按照指令模板分析故障原因与细节，在仿真与真实实验中较直接使用现成VLM平均提升25个百分点的故障检测准确率。

---

## Agent与具身智能

### [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531)

**作者:** Yuyang Zhang, Wenyao Zhang, Zekun Qi et al. | **方向:** Agent与具身智能, 多模态生成, 有代码 | **代码:** [Code](https://github.com/yuyangalin/ImageWAM)

本文提出ImageWAM，一个将预训练图像编辑模型重新用于机器人动作预测的世界动作模型框架，以替代依赖视频生成的传统WAM。方法在推理时不解码目标帧，而是将图像编辑去噪产生的KV缓存作为紧凑世界动作上下文，条件化流匹配动作专家。在仿真与真实实验中，ImageWAM以1/6的FLOPs和1/4的延迟优于视频基线。

---

### [ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly Supervised Video Polyp Segmentation](https://arxiv.org/abs/2606.20161)

**作者:** Tong Wang, Siwen Wang, Yaolei Qi et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/wangtong627/ARTEMIS)

本文提出ARTEMIS框架，用于不完美监督下的视频息肉分割。系统通过辩论-评判视觉语言智能体选择可靠的时序锚点，并用SAM2双向传播以精修不可靠或未标注帧。在SUN-SEG和CVC-ClinicDB-612的涂鸦、点标注和有限标签设置下取得SOTA性能。

---

### [HilDA: Hierarchical Distillation with Diffusion for Advancing Self-Supervised LiDAR Pre-trainin](https://arxiv.org/abs/2606.20189)

**作者:** Maciej Wozniak, Jesper Ericsson, Hariprasath Govindarajan et al. | **方向:** Agent与具身智能, 多模态生成, 暂无代码 | **代码:** 无

本文提出HilDA，一个面向自动驾驶LiDAR骨干网络的自监督预训练框架。它结合分层蒸馏、全局上下文蒸馏与时间占用扩散目标，以同时捕获语义“是什么”与几何“在哪里”。预训练模型在跨模态蒸馏基准及3D检测、场景流和语义占用预测任务上达到SOTA。

---

### [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521)

**作者:** Juncheng Ma, Jianxin Bi, Yufan Deng et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/DAGroup-PKU/HumanNet/)

本文系统比较了第一人称人类视频与遥操作真实机器人轨迹作为具身基础模型预训练数据的效果。研究发现，经过精心过滤与标注的第一人称视频不仅能替代机器人数据，还能在真实机器人动作预测验证损失上降低24%，在分布内/外任务成功率上分别提升52.5%和90%。

---

### [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112)

**作者:** Jiazhao Zhang, Gengze Zhou, Hale Yin et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/QwenLM/Qwen-RobotNav)

本文提出Qwen-RobotNav，一个为agentic导航系统设计的可扩展导航模型。模型通过参数化接口支持多种任务模式与可控观察参数，并在1560万样本上与视觉语言数据联合训练，避免退化为反应式动作序列映射器。在多个导航基准上取得SOTA，并展现出从2B到8B参数的良好扩展性。

---

### [DeXposure-Claw: An Agentic System for DeFi Risk Supervision](https://arxiv.org/abs/2606.19501)

**作者:** Aijie Shu, Bowei Chen, Wenbin Wu et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/EVIEHub/DeXposure-Claw)

本文提出DeXposure-Claw，一个面向DeFi风险监管的agentic监督系统。系统通过图时间序列基础模型预测未来敞口网络，再由确定性监控与压力场景生成结构化证据，并在数据健康和置信度门控下输出可审计的监管工单。在五年真实数据上的实验支持其有效降低误干预率。

---

### [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)

**作者:** Wenli Xiao, Jia Xie, Tonghe Zhang et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出ENPIRE，一个用于真实世界机器人策略自改进的coding agent框架。它通过环境自动重置与验证、策略改进、物理机器人并行评估以及coding agent分析日志并改进代码的进化模块，形成闭环物理反馈。在整理图钉盒、紧固扎带和工具使用等灵巧操作任务上实现99%成功率。

---

### [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419)

**作者:** Junyi Zhang, Jiaxin Ge, Hanjun Yoo et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/Playful-RATs/rats)

本文提出Playful Agentic Robot Learning范式，使具身coding agent通过自导向游戏持续学习可复用技能。RATs智能体提出可学习的探索任务，执行并验证机器人代码策略，并将成功执行蒸馏为持久代码技能库。在LIBERO-PRO和MolmoSpaces上显著优于无游戏和随机游戏基线。

---

### [Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation](https://arxiv.org/abs/2606.19632)

**作者:** Ahmad Farooq, Kamran Iqbal | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出首个通过学习多智能体通信策略的决策树蒸馏进行端到端安全验证的框架。神经策略被蒸馏为可解释决策树后，自动转换为PRISM概率模型检测器规范并验证PCTL性质。在5-7架无人机的协调任务中，18个性质满足率达88.9%，且蒙特卡洛验证确认安全性质可迁移回原网络。

---

### [VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents](https://arxiv.org/abs/2606.19729)

**作者:** Marcus Hoerger, Rishikesh Joshi, Rahul Shome et al. | **方向:** Agent与具身智能, 多模态生成, 暂无代码 | **代码:** 无

本文提出VOiLA，一个基于条件扩散模型学习POMDP转移与观测采样器、并将其蒸馏为紧凑前馈生成器以实现在线规划的框架。结合面向GPU并行的VOPP在线POMDP规划器，蒸馏策略将采样成本降低近三个数量级。在三个基准问题及真实机器人上验证了方法的有效性。

---

### [A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems](https://arxiv.org/abs/2606.20031)

**作者:** Junzhe Xu, Zecui Zeng, Lusong Li et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出SDQN-RMFS，一个端到端神经形态框架，用于机器人移动履约系统中的高能效路径规划。通过碰撞允许策略训练ANN，再经硬标签知识蒸馏转换为SNN，解决ANN到SNN的输出分布不匹配问题。硬件实验显示相比高性能GPU基线实现高达11281倍的能耗节省和近2倍的延迟降低。

---

### [Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform](https://arxiv.org/abs/2606.20120)

**作者:** Hyeonna Choi, Jung Yup Kim, Hyuneui Lim et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出一个双智能体框架，将自然语言微孔板实验协议转换为机器人实验室平台的可执行控制命令。解析智能体将协议形式化，异构LLM验证智能体进行完整性、参数准确性和执行顺序验证，并在检测到错误时触发自校正循环。最终在Bradford实验中实现从自然语言协议到真实实验的端到端自主执行。

---

### [FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching](https://arxiv.org/abs/2606.20209)

**作者:** Francesco Argenziano, Miguel Saavedra-Ruiz, Sacha Morin et al. | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/Fra-Tsuna/flowmaps/tree/main)

本文提出FlowMaps，一个基于潜流匹配的模型，用于估计连续3D空间中动态物体未来位置的多模态分布。通过学习物体间的隐式依赖及其时间演化，FlowMaps能基于过去人类交互预测物体位置变化，并泛化到具有相似物体惯例的未见环境。在动态物体导航任务中，600多个episode上优于SOTA方法。

---

### [Efficient and Sound Probabilistic Verification for AI Agents](https://arxiv.org/abs/2606.20510)

**作者:** Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu et al. | **方向:** Agent与具身智能, 音频多模态, 暂无代码 | **代码:** 无

本文提出一个基于分布鲁棒优化的AI agent概率验证框架，用于在谓词间可能存在相关性的情况下计算策略违反概率的可靠上界。相比现有确定性策略监控方法，该框架支持概率性谓词和状态转移。在终端和工具调用agent标准基准上改善了安全-效用权衡。

---

### [DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning](https://arxiv.org/abs/2606.19656)

**作者:** Calvin Luo, Chen Sun, Shuran Song | **方向:** Agent与具身智能, 多模态生成, 有代码 | **代码:** [Code](https://github.com/calvinluo/df-expense)

本文提出DF-ExpEnse，一种利用预训练生成式控制策略的多模态建模能力改进在线经验收集的探索技术。方法构建表达性强且可评估的候选动作集，并通过critic ensemble选择质量与探索兴趣最佳平衡的动作。在多种操作与运动任务上验证了样本效率提升。

---

### [Deep-Unfolded Coordination](https://arxiv.org/abs/2606.19920)

**作者:** Hunter Kuperman, Minchan Jung, Rahul V. Ghosh et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出Deep Coordinator，一个深度展开框架，用于在求解时动态调整ADMM-DDP分布式求解器的超参数。通过将固定次数的ADMM-DDP迭代展开为神经网络并学习层间超参数映射函数，方法在汽车和四旋翼机队轨迹优化任务上比传统求解器快6.18-9.44倍，并能在比训练大8倍的系统上保持性能。

---

### [Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents](https://arxiv.org/abs/2606.16682)

**作者:** Zewen Liu | **方向:** Agent与具身智能, 有代码 | **代码:** [Code](https://github.com/aidless/mm-epc)

本文研究了多模态设置下的评估器偏好坍塌现象。发现多模态自我评估中单一策略会吸收48.4%的权重，并提出了跨模态传染现象，即在一个模态上习得的评估偏好会转移并破坏另一模态的策略选择。通过四阶段隔离训练范式量化了传染系数，并发布MM-EPC框架。

---

### [DiffusionVS: A Generative Framework for Robust Visual Servoing Based on Diffusion Policy](https://arxiv.org/abs/2606.19397)

**作者:** Hongkang Cui, Rui He, Haoyao Chen | **方向:** Agent与具身智能, 多模态生成, 暂无代码 | **代码:** 无

本文提出DiffusionVS，一个基于扩散策略的鲁棒视觉伺服框架。方法以观测标签角点的归一化图像坐标为输入，通过条件去噪生成相机速度，并采用在线训练范式持续扩展训练数据多样性。在仿真和真实实验中分别实现近100%和93%的成功率，且该扩散模块可增强现有视觉伺服网络。

---

### [One-to-Two Acting: A Novel Framework for Single-arm Agent Action Expansion to Dual Arms](https://arxiv.org/abs/2606.19897)

**作者:** Youbin Yao, Nieqin Cao, Mingyan Li et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出ExS2D，一个从单臂监督实现双臂操作的分层动作扩展框架。方法首先根据文本指令生成结构化子任务并捕获时间优先级，然后通过子任务引导的动作映射在观察中落地为可执行动作，最后由MLLM协调器选择无碰撞的双臂执行。在仿真中将平均执行步数减少54.4%，并在真实机器人上验证。

---

### [Autonomous Driving with Priority-Ordered STL Specifications Under Multimodal Uncertainty](https://arxiv.org/abs/2606.20336)

**作者:** Taha Bouzid, Shuhao Qi, Mircea Lazar et al. | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出一种不确定性感知的轨迹规划框架，用于在无法满足所有要求的安全关键场景下，按预定义的STL规范字典序优先级进行规划。方法显式考虑周围交通参与者轨迹预测的多模态不确定性，并通过MPPI控制实现。在仿真场景中验证了处理冲突目标的有效性。

---

### [An Infrastructure-less, Control-Independent Solution to Relative Localisation of a Team of Mobile Robots using Ranging Measurements](https://arxiv.org/abs/2606.20365)

**作者:** Paolo Golinelli, Tommaso Faraci, Daniele Fontanelli | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出一种去中心化协同定位算法，用于无基础设施、无锚点的移动机器人群。方法不依赖控制运动来保证可观测性，仅使用局部里程计、稀疏智能体间测距和短程通信。它采用多假设贝叶斯框架维护全部可行解，并在部分连接条件下通过信息共享使每个智能体受益于群体估计。

---

### [Agentic AutoResearch forSpace Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems](https://arxiv.org/abs/2606.20394)

**作者:** Amit Jain, Richard Linares | **方向:** Agent与具身智能, 暂无代码 | **代码:** 无

本文提出AutoResearch，一个由大语言模型自主驱动的航空航天控制问题研究代理框架。系统读取自然语言问题描述和运行历史，提出训练脚本修改并执行，同时通过可信度层对结果进行种子噪声校准。在相对交会与避撞对接两个基准上，代理生成的策略均显著超过测量到的种子噪声。

---

### [DIFF-IPPO: Diffusion-Based Informative Path Planning with Open-Vocabulary Belief Maps](https://arxiv.org/abs/2606.16780)

**作者:** Sausar Karaf, Oleg Sautenkov, Mikhail Martynov et al. | **方向:** Agent与具身智能, 多模态生成, 暂无代码 | **代码:** 无

本文提出DIFF-IPPO，一个将开放词汇信念图生成器与基于扩散的规划器相结合的告知性路径规划流程。方法直接在高信念区域上生成全局轨迹，使传感器覆盖集中于目标区域。在搜索救援仿真中，五架无人机团队使用批量化信念图条件轨迹生成，可在3.5分钟内完成首次检测。

---

### [Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow](https://arxiv.org/abs/2606.20001)

**作者:** Wen Zhang, Wenbin Jiang, Yang Zhang et al. | **方向:** Agent与具身智能, 多模态生成, 暂无代码 | **代码:** 无

本文提出Autonomous Rectified Flow框架，挑战生成式语音增强中显式时间步条件化的必要性。通过线性插值路径，方法证明目标向量场本质上是时间不变的，并引入时间无条件网络仅根据当前状态与噪声观测的空间关系推断去噪方向。该设计显著提升了生成质量、鲁棒性和推理效率。

---

## 多模态生成

### [Learning When to Denoise: Optimizing Asynchronous Schedules for Latent Diffusion](https://arxiv.org/abs/2606.19662)

**作者:** Bingshuo Qian, Xiang Cheng | **方向:** 多模态生成, 有代码 | **代码:** [Code](https://github.com/bsq532087/LWD)

本文提出了一种学习多表示扩散模型异步去噪 schedule 的方法。通过将异步流匹配建模为参数化的凸单调 schedule 类，并使用 schedule 校正目标保持局部加噪时间权重不变，作者以不足 1% 的额外训练开销学习该 schedule。在 ImageNet 256×256 上，600 epoch 模型达到 FID 1.02，超越了 1B 参数的 SFD-XXL 结果，同时显著减少训练量。

---

### [One-Shot Novel View and Pose Human Image Synthesis via 3D Prior Guided Diffusion Model](https://arxiv.org/abs/2606.19718)

**作者:** Shenjian Gong, Kangkan Wang, Shanshan Zhang et al. | **方向:** 多模态生成, 3D视觉语言, 有代码 | **代码:** [Code](https://github.com/Yankeegsj/3DPGDM)

本文提出了一种基于条件去噪扩散模型的人体新视角与新姿态合成方法。通过引入 3D 人体先验（3D normal map 和 color prompt）作为几何与颜色条件，模型能够在复杂姿态下生成包含遮挡区域的高质量人体图像。在多个公开数据集上的实验表明，该方法显著优于现有方法，并具有更好的跨数据集泛化能力。

---

### [DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation](https://arxiv.org/abs/2606.19939)

**作者:** Wei Pan, Xuhan Zheng, Yilin Shi et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 DiffMath，一种符号与图感知的潜在扩散框架，用于手写数学表达式生成。该方法设计了关系抽象语法树（RelAST）将 MathML 结构蒸馏为紧凑的三元组序列，并引入 MathVAE 和 MathDiT 在结构保持的潜在空间中进行条件去噪。实验表明，DiffMath 生成的手写表达式结构一致性强，并能通过合成数据增强提升下游 OCR 模型的准确率。

---

### [Addressing Detail Bottlenecks in Latent Diffusion for RGB-to-SWIR Image Translation](https://arxiv.org/abs/2606.19961)

**作者:** Kaili Wang, Martin Dimitrievski, Jose Maria Salvador et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文针对潜在扩散模型在 RGB 到 SWIR 图像翻译中丢失细粒度空间细节的问题，识别了自编码器和条件路径两个瓶颈。作者提出了源条件自编码器（SCAE）和可学习引导编码器（LGE），以轻量且骨干无关的方式注入高分辨率源特征并替代朴素的下采样。在驾驶场景实验中，该方法将检测 mAP 提升最多 2 倍，并达到了最先进的 FID。

---

### [Variable-Length Tokenization via Learnable Global Merging for Diffusion Transformers](https://arxiv.org/abs/2606.20076)

**作者:** Dong Hoon Lee, Seunghoon Hong | **方向:** 多模态生成, 有代码 | **代码:** [Code](https://github.com/movinghoon/lgm)

本文提出了一种基于可学习全局合并的可变长度 Tokenizer，用于扩散 Transformer。与通过截断有序 token 序列来调节长度的传统方法不同，该方法通过合并相似 token 来实现跨长度的表示对齐，并确保合并模式在生成时可用。在 ImageNet 256×256 生成任务上，该方法取得了更优的 gFID-计算权衡。

---

### [MakeupMirror: Improving Facial Attribute Preservation in Diffusion Models for Makeup Transfer](https://arxiv.org/abs/2606.20094)

**作者:** Nefeli Andreou, Angel Martínez-González, Sabine Sternig et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 MakeupMirror，一种基于扩散模型的 makeup transfer 方法，重点解决身份和肤色保持问题。方法集成了面部几何条件、区域特定 makeup 控制、肤色感知调制以及 Levenberg-Marquardt Langevin 采样器，以在保持生成质量的同时加速推理。实验表明，MakeupMirror 在面部识别相似度和肤色差异指标上显著优于 Stable-Makeup。

---

### [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)

**作者:** Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 FrozenDrive，一种零样本文本引导的驾驶场景生成与数据增强框架。通过保留预训练扩散模型的知识并引入知识保留的时空注意力机制，模型在无需针对天气或场景特定微调的情况下，生成全局一致的多视角驾驶场景，尤其在夜间和雨天等恶劣天气与罕见条件下表现优异。在 nuScenes 上的实验表明，FrozenDrive 增强的数据能显著提升自动驾驶模型的鲁棒性。

---

### [Pixel-Level Residual Diffusion Transformer: Scalable 3D CT Volume Generation](https://arxiv.org/abs/2606.20112)

**作者:** Zhenkai Zhang, Markus Hiller, Krista A. Ehinger et al. | **方向:** 多模态生成, 3D视觉语言, 有代码 | **代码:** [Code](https://github.com/Fredy-Zhang/PRDiT)

本文提出了 Pixel-Level Residual Diffusion Transformer（PRDiT），一种直接在体素级别生成高分辨率 3D CT 体积的生成框架。该方法采用两阶段架构，包括基于 MLP 的局部去噪器和全局残差扩散 Transformer，分别处理低频结构和高频残差。在 LIDC-IDRI 和 RAD-ChestCT 数据集上的实验表明，PRDiT 在 3D FID、MMD 和 Wasserstein 距离等指标上持续优于现有方法。

---

### [NAMESAKES: Probing Identity Memorization in Text-to-Image Models](https://arxiv.org/abs/2606.20155)

**作者:** Morris Alper, Vasudha Varadarajan, Moran Yanuka et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 NAMESAKES，一个用于探测文本到图像模型中身份记忆问题的黑盒行为探测方法及数据集。该数据集包含超过一千个涵盖不同知名度公众人物的名字与面孔，以及扰动后的低知名度名字。实验表明，该探测方法能够有效预测身份记忆，并区分记忆化与未识别的名字。

---

### [Cinematic Compositing Using Character-Environment-Harmonized Video Generation Models](https://arxiv.org/abs/2606.20233)

**作者:** Tianyi Xiang, Mingming He, Li Ma et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了一种端到端的视频扩散框架，用于电影级人物-环境和谐化合成。方法联合建模了人物到环境（C2E）的物理交互和环境到人物（E2C）的光照和谐化，并通过 tri-mask 引导的 RGB-D 联合去噪架构确保人物、道具与环境之间的物理一致性。实验表明，该框架在电影级动态视频合成方面显著优于现有方法。

---

### [Through the PRISM: Preference Representation in Intermediate States of Video Diffusion Models](https://arxiv.org/abs/2606.20310)

**作者:** Haoxuan Wu, Lai Man Po, Mengyang Liu et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 PRISM（Preference Representation in Intermediate States of Video Diffusion Models），用于从视频扩散模型的噪声潜在表示中直接解码偏好信号。通过轻量级的基于查询的聚合头，PRISM 在偏好预测准确率上达到 SOTA，并展现出强噪声鲁棒性，支持在降噪早期进行 Best-of-N 采样，从而显著降低计算开销并提升视频质量。

---

### [On the Redundancy of Timestep Embeddings in Diffusion Models](https://arxiv.org/abs/2606.20416)

**作者:** José A. Chávez | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文挑战了扩散模型中显式 timestep embedding 的必要性。作者从理论上证明，在某些条件下，扩散训练目标的全局最小值可以在没有显式时间条件的情况下达到，并在 CelebA 和 CIFAR-10 上进行了大量消融实验。结果表明，去除 timestep embedding 的时间无关模型能够保持高结构保真度，甚至在 FID、precision 和 recall 等指标上超过有条件模型。

---

### [SSD: Spatially Speculative Decoding Accelerates Autoregressive Image Generation](https://arxiv.org/abs/2606.20543)

**作者:** Shilong Xiang, Zirui Zhang, Lijun Yu et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 Spatially Speculative Decoding（SSD），一种利用图像二维空间相关性加速自回归图像生成的方法。方法同时预测相邻的水平和垂直 token，而非仅预测一维序列中的下一个 token，从而克服视觉推理中的内存墙。在 DPG-Bench 和 GenEval 上，SSD 在保持高保真度的同时将自回归图像生成加速最多 13.3 倍。

---

### [PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation](https://arxiv.org/abs/2606.19935)

**作者:** Zhangzhao Liang, Xiaofen Xing, Mingyue Yang et al. | **方向:** 多模态生成, 音频多模态, 暂无代码 | **代码:** 无

本文提出了 PhysDrift，一种具身感知的人体协同语音动作生成框架，用于解决从人体表示 retarget 到人形机器人时的具身差距问题。方法首先通过 IK-EER 框架在 retargeting 阶段保持韵律与运动时间对齐，然后直接在机器人关节轨迹空间进行生成，并引入物理正则化稳定运动动力学。真实世界人形机器人部署实验表明，该方法在语音-运动对齐、物理合理性和实时交互能力上均有显著提升。

---

### [Hybrid Diffusion Transformer for Instruction-Guided Audio Editing via Rectified Flow](https://arxiv.org/abs/2606.20101)

**作者:** Liting Gao, Yonggang Zhu, Yaru Chen et al. | **方向:** 多模态生成, 音频多模态, 暂无代码 | **代码:** 无

本文提出了一种基于 Rectified Flow 的混合两阶段扩散 Transformer 架构，用于指令引导的音频编辑。方法在低分辨率阶段对音频和文本 token 进行联合注意力以实现粗略语义对齐，在高分辨率阶段交替使用联合注意力和交叉注意力来精细化编辑细节。实验表明，该框架在重叠音频事件和复杂指令的编辑任务上取得了显著性能提升，同时大幅提高了编辑效率。

---

### [Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation](https://arxiv.org/abs/2606.20457)

**作者:** Rostislav Makarov, Timo Gerkmann | **方向:** 多模态生成, 音频多模态, 暂无代码 | **代码:** 无

本文研究了将预训练语音分类器重新用于引导扩散语音生成的方法。通过在冻结的噪声条件分类器上附加一个轻量子网络并在去噪分数匹配目标下进行训练，方法实现了在单一骨干模型内完成条件生成，减少了内存占用和计算成本。实验表明，该方法在保持高语音质量的同时提供了一种判别式建模与条件语音合成之间的有效桥梁。

---

### [STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training](https://arxiv.org/abs/2606.17979)

**作者:** Jinjie Shen, Wei Deng, Xian Hu et al. | **方向:** 多模态生成, 暂无代码 | **代码:** 无

本文提出了 STAR（SpatioTemporal Adaptive Reward Allocation），一种用于文本到图像扩散和流模型 RL 后训练的空间-时间自适应奖励分配方法。方法利用生成模型内部的文本-图像注意力构建随去噪步骤和 rollout 动态变化的空间分配图，将更强的策略更新应用于与奖励更相关的潜在区域。在 Stable Diffusion 3.5 Medium 上的实验表明，STAR 在 GenEval、OCR 文本渲染和 PickScore 任务上均取得了提升。

---

### [Performance Analysis and Optimization of 3D Generative Diffusion Models across GPU Architectures](https://arxiv.org/abs/2606.19365)

**作者:** Jeeho Ryoo, Yongchan Jung, Muhammad Ali Khaliq et al. | **方向:** 多模态生成, 3D视觉语言, 暂无代码 | **代码:** 无

本文对 3D 医学扩散模型 Med-DDPM 在多种 NVIDIA GPU 架构上进行了全面的性能分析与优化。研究揭示了训练主要由 cuDNN 卷积和隐式 GEMM 核主导，并受限于内存访问模式和 Tensor Core 利用率不足。作者评估了 TF32 Tensor Core 激活和 3D channels-last 布局等优化，在 A100 上将 Tensor Core 利用率从 1.45 提升至 9.98 倍，且不降低合成质量。

---

### [LLM-Based Synthetic Ground Truth Generation for Audio-Based Emotion Classification via In-Context Learning](https://arxiv.org/abs/2606.14784)

**作者:** Qing Huang, Pooja Pol, Jianing Zhang | **方向:** 多模态生成, 音频多模态, 暂无代码 | **代码:** 无

本文提出了一种基于大语言模型的智能推理流程，用于从多用户 VR 环境中的流式语音数据自动生成与情绪相关的合成 ground truth。方法利用上下文学习（ICL）结合声学特征空间中的检索式样本选择，动态构建信息丰富的 in-context 提示。该流程旨在解决动态团队过程中情绪标注困难的问题，支持低成本、可扩展的多模态情感分析数据生成。

---

### [Joycent: Diffusion-based Accent TTS without Accented Phone Prediction](https://arxiv.org/abs/2606.16417)

**作者:** Xintong Wang, Ye Wang | **方向:** 多模态生成, 音频多模态, 有代码 | **代码:** [Code](https://github.com/oshindow/Joycent-code)

本文提出了 Joycent，一种无需预测口音音素的基于扩散的口音文本转语音（TTS）模型。方法通过条件层归一化（CLN）在文本编码器中整合口音和说话人表示，并引入 WhisAID 口音识别模型提取口音特征。实验表明，Joycent 在保持说话人身份的同时提升了口音相似度。

---

## 音频多模态

### [How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech](https://arxiv.org/abs/2606.20532)

**作者:** Nityanand Mathur, Hamees Sayed, Wasim Madha et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究首次将DAAM交叉注意力归因方法引入语音扩散模型，用于解析风格字幕中每个词对CapSpeech-TTS声学输出的影响。通过提取跨层和ODE步的逐词热力图，分析了3600组风格-文本组合，发现风格词呈现全局调控特性，与基频和能量相关，并在早期去噪步与深层网络中作用最强。注意力熵在第17层达到最小，对应风格重要性峰值，揭示了网络选择性最强的风格关键阶段。

---

### [Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech](https://arxiv.org/abs/2606.19381)

**作者:** Yue Heng Yeo, Haoyang Li, Yizhou Peng et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

本文提出一种基于代码混合指数（CMI）的偏好学习框架，引导合成语音生成更忠实的语码转换语音，以扩充语码转换ASR训练数据。在SEAME普通话-英语对话语料上的实验表明，该方法显著提升了合成数据对Whisper Large微调的效用，DevMAN和DevSGE集的混合错误率分别从12.1%/17.8%降至8.9%/14.2%。

---

### [FlowFake: Liquid Networks for Audio Deepfake Detection](https://arxiv.org/abs/2606.19579)

**作者:** Shivaay Dhondiyal, Divyansh Sharma, Dinesh Kumar Vishwakarma | **方向:** 音频多模态, 有代码 | **代码:** [Code](https://github.com/GhostRider2023/FlowFake)

FlowFake采用液态时间常数（LTC）网络，通过可学习的常微分方程隐藏状态和自适应时间常数同时捕捉频谱与韵律层面的伪造痕迹。该模型仅34K参数，在ASVspoof2019-LA、FakeOrReal、InTheWild和MLAAD的跨域评测中超越了RawGAT-ST和Whisper-DF，并以Wav2vec2万分之一的参数量达到与之相当的性能。

---

### [Systematic Study of Dysarthric Speech Recognition: Spectral Features and Acoustic Models](https://arxiv.org/abs/2606.19793)

**作者:** Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该文系统研究了针对构音障碍语音的不同声学特征与F-TDNN声学模型组合，发现加入基频特征对句子识别任务尤为有益。在TORGO数据库上的实验相较于前人工作，孤立词识别和句子识别分别取得了4.65%和4.63%的相对提升，验证了特征选择对补偿语音变异性的作用。

---

### [Improving End-to-End Speech Recognition for Dysarthric Speech through In-Domain Data Augmentation](https://arxiv.org/abs/2606.19797)

**作者:** Paban Sapkota, Hemant Kumar Kathania, Sudarsana Reddy Kadiri et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究针对构音障碍语音数据稀缺问题，通过语速、基频、共振峰和声道长度扰动等数据增强方法，对Wav2Vec2进行按严重度分级的微调。实验显示，低、中、高严重度分别采用SRM和PM增强时WER最低，相对提升分别为30.02%、16.64%和15.47%，显著改善了端到端构音障碍语音识别。

---

### [QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement](https://arxiv.org/abs/2606.18611)

**作者:** Shogo Yamauchi, Hideaki Tamori, Makoto Sakai et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

QC-GAN将四元数Conformer生成器与MetricGAN判别器结合，利用Hamilton乘积在减少参数量的同时保持幅度与相位间的依赖关系。在VoiceBank+DEMAND数据集上，0.89M参数模型取得PESQ 3.48，35K参数变体达到PESQ 3.23，实现了以更少参数逼近最先进语音增强性能。

---

### [Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning](https://arxiv.org/abs/2606.19823)

**作者:** Satwinder Singh, Qianli Wang, Zihan Zhong et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究探索利用Higgs Audio V2进行零样本语音克隆，为构音障碍ASR提供低负担的数据增强方案。在TORGO数据上的Whisper-medium微调实验表明，克隆数据微调后的WER降至26.00%，接近真实或混合数据微调效果，并在SAP-1102跨语料测试中取得最佳表现。

---

### [ReNikud: Audio-Supervised Hebrew Grapheme-to-Phoneme Conversion](https://arxiv.org/abs/2606.20179)

**作者:** Maxim Melichov, Yakov Kolani, Morris Alper | **方向:** 音频多模态, 暂无代码 | **代码:** 无

ReNikud通过数千小时无标注希伯来语音频的ASR伪标签获取弱音频监督，并采用伪元音化架构在每个字符位置预测IPA音素。该方法在现有希伯来G2P基准和新的MILIM口语基准上均超越了现有最优方法，并将发布代码与训练模型。

---

### [Segment-Level Mandarin Chinese Speech-Based Cognitive Impairment Detection via an Autoencoder with Contrastive Learning](https://arxiv.org/abs/2606.19996)

**作者:** Yongqi Shao, Hong Huo, Flavio Bertini et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究提出基于片段级语音表示的认知障碍检测框架，将语音切分为短时片段并转换为频谱图，结合自编码器与对比学习学习判别性隐层表示。在四个独立普通话数据集上的实验表明，该方法在二分类和三分类任务中均表现稳定，尤其在更具挑战性的三分类设置中提升明显。

---

### [Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs](https://arxiv.org/abs/2606.05846)

**作者:** Gio Paik, Hyunseo Shin, Soungmin Lee | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该工作研究了通过模型融合与域泛化方法，将语码转换ASR从已见语言对泛化到未见语言对的能力。实验结果表明，合并后的双语模型对未见语言对仅有适度的泛化能力，提示双语语码转换能力在不同语言对之间的可迁移性有限。

---

### [A Survey of Full-Duplex Spoken Dialogue Systems: Architectural Hierarchy, Interaction Ontology, and Decision State Machine](https://arxiv.org/abs/2606.19453)

**作者:** Jingyu Lu, Yuhan Wang, Jianming Luo et al. | **方向:** 音频多模态, 有代码 | **代码:** [Code](https://github.com/DuplexLM/DuplexSurvey)

本文首次系统梳理了全双工口语对话系统，提出L0-L3架构层次、T×I×R交互本体以及IDLE/LISTEN/SPEAK/WAIT/DUAL决策状态机三种互补框架。作者指出当前系统在架构能力与实际交互行为之间存在实现鸿沟，公共训练数据覆盖不足与L3表征级建模是未来研究的关键前沿。

---

### [Analyzing Language and Geographical Variation in Speech Representations Across 60 Indic Languages](https://arxiv.org/abs/2606.19940)

**作者:** Pavan Kumar J, Agneedh Basu, Pranav Bhat et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究对60种印度语言、386个语言-地区类别的语音表征进行分析，比较了仅语言监督与联合语言-地区监督对Whisper和Wav2Vec2.0表征的影响。结果发现，联合监督在保持语言可分性的同时增强了地理变异区分能力，embedding空间呈现出按语言聚类、内部按地区子聚类的结构。

---

### [Interpreting Content and Speaker Characteristics in Factorised Self-Supervised Subspaces](https://arxiv.org/abs/2606.19974)

**作者:** Kyle Janse van Rensburg, Herman Kamper | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究对WavLM经SVD分解后的内容与说话人子空间进行可解释性分析，揭示各维度与音高、强度、发声等语音特征的关联。实验发现内容空间的主导维度主要编码强度、高阶共振峰和发声信息，而说话人空间的主导维度与音高和性别强相关，干预这些维度可实现对语音特征的精细控制。

---

### [Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification](https://arxiv.org/abs/2606.20106)

**作者:** Ming-Hsiang Hu, Kuan-Tang Huang, Chien-Chun Wang et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

ZP-KWS通过融合音素监督音频编码器与GE2E说话人编码器，并采用乘法晚期融合机制，实现了对未见关键词和未见说话人的双重零样本关键词唤醒。在LibriPhrase、Google Speech Commands和Qualcomm数据集上，该1.55M参数模型在1%误接受率下将目标误拒绝率相对降低最多60%，同时保持良好的关键词检测性能。

---

### [Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning](https://arxiv.org/abs/2606.20266)

**作者:** SooHwan Eom, Hee Suk Yoon, Eunseop Yoon et al. | **方向:** 音频多模态, 暂无代码 | **代码:** 无

RTFree-F5在F5-TTS流匹配文本转语音框架中，用连续自监督语音表征替代参考文本，通过轻量适配器将其映射到文本条件空间。在构音障碍语音上的实验将WER从24.6%降至10.4%，甚至超过使用真实转录文本的基线，同时在标准基准上保持竞争力。

---

### [Stuttering Classification and Segmentation with Attention-Based Multiple Instance Learning](https://arxiv.org/abs/2606.20338)

**作者:** Petar Sušac, Sebastian P. Bayerl, Hrvoje Džapo | **方向:** 音频多模态, 暂无代码 | **代码:** 无

该研究提出基于注意力多示例学习（MIL）的口吃分类与分割框架，利用微调后的wav2vec 2.0、WavLM和Whisper编码器学习片段级标签下的帧级预测。实验在帧级F1上提升23%，片段级F1提升2%-9%，展示了利用粗粒度标注数据进行细粒度口吃事件定位的有效性。

---

### [S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning](https://arxiv.org/abs/2606.19398)

**作者:** Georgios Ioannides, Adrian Kieback, Judah Goldfeder et al. | **方向:** 音频多模态, 有代码 | **代码:** [Code](https://github.com/gioannides/s-jepa)

S-JEPA提出用高斯混合模型的软后验分布替代离散聚类标签，通过KL散度训练JEPA风格的语音编码器-预测器网络。该方法省去了离线重聚类步骤，在SUPERB评测中取得了90M参数以下自监督模型的最低WER，并在参数量约为HuBERT-Base一半时达到相当的情绪识别性能。

---

### [Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding](https://arxiv.org/abs/2606.19688)

**作者:** Yunsik Kim, Yoonyoung Chung | **方向:** 音频多模态, 暂无代码 | **代码:** 无

LaCo-SENet通过非对称时序填充与双缓冲流式机制，将过去与未来上下文按可配置延迟进行分配，实现单一模型在不同延迟设置下的流式语音增强。在VoiceBank+DEMAND上，1.37M参数骨干可生成12.5ms至75ms的模型族，PESQ从3.35提升至3.43，其中12.5ms全因果模型已优于先前因果最优方法。

---

## 3D视觉语言

### [3D-PLOT-LLM: Part-Level Object Tokens for 3D Large Language Models](https://arxiv.org/abs/2606.19828)

**作者:** Jintang Xue, Xinyu Wang, Yixing Wu et al. | **方向:** 3D视觉语言, 暂无代码 | **代码:** 无

3D-PLOT-LLM 提出了一种无需分割解码器或边界框头的部件级 3D 大语言模型方法：它将冻结点编码器的 patch 划分为 K 个局部连贯区域，并在每个区域前插入可学习的区域标记和保留词表 token &lt;part_k&gt;，使模型输出能直接引用和推理物体部件。在 3DCoMPaT-GrIn 部件感知描述基准上，该方法在多个文本指标上超越了 PointLLM 等现有模型，且仅增加不到 100 万可训练参数。

---

### [Alzheimer's Disease Diagnosis using a Multimodal Approach with 3D MRI and PET](https://arxiv.org/abs/2606.20037)

**作者:** Loukas Ilias, Anthi-Maria Vozinaki, Christos Ntanos et al. | **方向:** 3D视觉语言, 暂无代码 | **代码:** 无

该研究提出了一种结合 3D MRI 与 PET 的多模态阿尔茨海默病诊断框架，采用 3D 卷积特征提取器，并比较了拼接、门控多模态单元（GMU）和门控自注意力三种融合策略，配合稀疏门控混合专家（MoE）分类器实现输入自适应路由。实验显示 GMU 在 NC vs MCI 和 NC vs AD 任务上分别达到 80.46% 和 95.47% 的准确率，消融实验表明去除 MoE 会降低各任务性能。

---

> 共收录 124 篇论文，涵盖 8 个方向
