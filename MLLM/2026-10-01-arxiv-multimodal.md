# Arxiv 多模态论文日报 - 2026-10-01

> 收录论文 **18** 篇 · 含代码仓库 **7** 篇 · 覆盖方向 **5** 个

---

## VLM / MLLM 核心

### [Xiaomi-OCR-0 Technical Report](https://arxiv.org/abs/2609.36136)

**作者:** Xin Chen, Anan Du, Feng Feng et al. · `VLM / MLLM` · [Code](https://github.com/SeerRay-Lab/Xiaomi-OCR-0)

提出Xiaomi-OCR-0，一个0.8B参数的紧凑型OCR专用视觉语言模型。通过构建约1.7亿样本的OCR核心语料库，结合自动化数据引擎（融合专家共识、渲染验证和定向合成）、Q-Mask文本锚定、持续预训练和混合任务强化学习（Mix-RL），在Real5-OmniDocBench上达到95.24分，在5个OCR导向VQA基准上平均83.2分，展现了小模型在文档解析领域的强大能力。

---

### [DARE to Mitigate Hallucination: Dual-path Auto-Regressive-aware Editing](https://arxiv.org/abs/2609.36440)

**作者:** Jae-Ho Lee, Jeong-Eun Lee, Gyeong-Moon Park · `VLM / MLLM` · [Code](https://github.com/KU-VGI/DARE)

针对大型视觉语言模型中的幻觉问题，提出双路径自回归感知编辑方法（DARE）。现有基于强制教师比较的非训练调整方法忽略了序列解码动态，DARE通过融合文本比较、序列感知表征位移和受控视觉差异三条路径，同时捕获序列解码动态。实验表明该方法有效减少视觉幻觉描述，同时保持感知精度和计算速度。

---

### [ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models](https://arxiv.org/abs/2609.36562)

**作者:** Ruochen Zhang, Yao Huang, Yitong Sun et al. · `VLM / MLLM` · [Code](https://github.com/FroggyChen/ThinkingGuard)

针对多模态大语言模型中隐式安全风险（由无害文本与中性图像逻辑组合引发不安全输出）的检测难题，构建了首个显式建模风险组合性的TriggerBench数据集（5,600个实例）。提出ThinkingGuard模型，采用步骤监督结构化推理训练框架，结合蒙特卡洛树搜索探索最优推理轨迹，通过双约束偏好对齐蒸馏到模型中，在标准与隐式安全基准上均取得优异表现。

---

### [How Medical VLMs Underutilize Their Vision Encoders: A Dermatology Perspective](https://arxiv.org/abs/2609.36557)

**作者:** Janet Wang, Yunbei Zhang, Xiao Wang, Jihun Hamm · `VLM / MLLM` · 暂无代码

揭示医学视觉语言模型严重低估其强大视觉编码器的问题——在皮肤科领域，MedSigLIP编码器性能超过MedGemma达10.26个百分点。通过注意力机制分析发现，"先描述后决策"的提示策略可将视觉注意力提升30-40%。提出无标签提示结合低标签编码器辅助重排序的解决方案，在保持VLM冻结的情况下改善诊断效果，并在5个VLM骨干上验证。

---

## 多模态理解与推理

### [LeRF: Learning Reference Coordinate Frames for Perspective Taking Reasoning](https://arxiv.org/abs/2609.36219)

**作者:** Bang Xiao, Wenqi Jia, Ozgur Kara et al. · `推理` · [Code](https://github.com/bangx7/LeRF)

提出LeRF框架，训练视觉语言模型构建和使用显式参考坐标系进行视角依赖推理。给定图像和查询，LeRF判断是否需要坐标系，定位参考实体并预测帧原点，通过轻量级渲染器将坐标系叠加到图像上实现后续推理，无需外部感知模型或显式3D重建。通过监督微调加空间VQA强化学习的两阶段训练，在多个视角推理基准上显著超越基线。

---

### [From Sharp Eyes to Expert Mind: Internalizing Expert Knowledge in MLLMs for Tampered Text Detection](https://arxiv.org/abs/2609.36145)

**作者:** Kaiqing Lin, Songze Li, Shen Chen et al. · `推理` · 暂无代码

将细粒度取证感知能力直接嵌入多模态大语言模型内部，用于检测篡改文本。针对两大挑战——宏观视觉特征与微小篡改区域的空间精度差距，以及语义训练与基础取证观察的感知细节脱节——提出两阶段知识迁移方法。专家模块仅在训练时需要，推理时系统速度与原始模型相同，在多种基准上超越现有专用和通用系统。

---

### [AffectReveal: Event-Grounded Emotion Recognition Beyond Visual Appearances](https://arxiv.org/abs/2609.36563)

**作者:** Yihao Qian, Runhao Zeng, Sicheng Zhao et al. · `推理` · 暂无代码

提出事件驱动的情感识别框架，认为仅凭视觉外观不足以准确识别情感——相同的生理反应在不同情境下表达不同情感。构建了涵盖多种情感和场景的大规模数据集，人类实验证明了解情境可显著提升准确率。创建了基于关键要素构建和验证替代原因的框架，在不修改后续网络权重的情况下提升了多个模型的情感识别准确率。

---

## 多模态检索与信息抽取

### [One Geometry, Different Outcomes: Readout-Dependent Effects of the Modality Gap in Vision-Language Models](https://arxiv.org/abs/2609.36101)

**作者:** Aditya Sharma, Divya Saxena · `检索` · 暂无代码

为对比视觉语言模型中的模态间隙提供统一的几何解释。发现单一主导方向捕获了图像-文本均值分离的94.4-99.9%平方范数，揭示均值分离分量近似为秩一。在零样本分类中，间隙偏移减法等价于加性类别偏置；在跨模态检索中，投影间隙方向会引入乘性排名失真；在混合模态检索中，间隙方向按模态排序候选项。该理论框架为何时及为何修改间隙提供了原则性指导。

---

## Agent 与具身智能

### [Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method](https://arxiv.org/abs/2609.35965)

**作者:** Yunzhe Xu, Zhe Liu · `Agent` · 暂无代码

首次系统性地将多智能体视觉语言导航形式化为约束协调问题。创建MAVLN基准，包含145个场景中11,724个导航片段，支持最多4个智能体团队协作。开发TRISS导航系统，耦合基于LLM的子任务调度器、共享拓扑记忆和冲突感知执行机制，为多智能体协调导航建立了全面的基线和评估框架。

---

### [StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks](https://arxiv.org/abs/2609.36352)

**作者:** Ziyi Yin, Sangmin Woo, Kang Zhou et al. · `Agent` · [Code](https://github.com/amazon-science/StructRL)

提出StructRL，一个在线强化学习框架，从可验证的子任务完成中构建结构化中间监督信号。解决现有方法仅在任务完全成功时提供奖励导致的稀疏监督问题——将每个任务分解为可验证子任务，仅在先决条件子任务完成后授予中间奖励，并根据完成进度缩放奖励。在RoboCasa365和LIBERO-Long上使用GR00T-N1.5和pi 0.5持续优于所有评估基线。

---

### [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380)

**作者:** Xirui Li, Peng Shi, Mingwen Dong et al. · `Agent` · `3D` · 暂无代码

提出LEGO-Anything，一个Image-to-Code框架，编码智能体迭代编写Blender代码来重建显式、可编辑的3D场景程序。创建LEGO-Bench（208张图像，104个场景）评估场景有效性、可见表面几何和渲染外观。发现GPT-6-astra达到最强整体结果（室内53.4%，室外39.6%），并开发LEGO-Plugin无需训练的插件将指标提升高达62.7%。

---

### [CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes](https://arxiv.org/abs/2609.36024)

**作者:** Shuzhao Xie, Lelin Wang, Guying Lin et al. · `Agent` · `3D` · 暂无代码

提出从多视角RGB图像自动重建包含刚性、关节和柔性物体的可模拟3D环境的智能体系统。全局空间提示建立比例，局部生成模型创建精确形状；关节物体分解为运动组件，柔性物体分别以曲线、曲面和体积建模。系统自动设置物理仿真并进行验证检查，展示了机器人操作柔性物体的能力（如折叠纸张）。

---

## 多模态生成

### [PreviewDiff: Multimodal Critic-Guided Search over Diffusion Latents](https://arxiv.org/abs/2609.36199)

**作者:** Vighnesh Subramaniam, Boris Katz, Brian Cheung et al. · `生成` · 暂无代码

提出PreviewDiff，一种无需训练的测试时搜索方法，将扩散采样从标量搜索转变为多模态评论家引导的中间潜在空间搜索。在选定的去噪检查点解码部分预览，由多模态评判者评分和批评，利用自然语言反馈进行语义编辑分支和局部重噪声化潜在延续。在图像和视频生成基准上持续优于预算匹配的Best-of-N选择和强标量搜索基线。

---

### [Mutually Adversarial Self-Training with Evolving Data for Unified Multimodal Models](https://arxiv.org/abs/2609.36224)

**作者:** Wentao Zhou, Weijie Gan, Jiayun Wang · `生成` · 暂无代码

提出MATE，一种统一多模态系统的后训练强化学习方法。不同于以往合作方式，图像生成和视觉理解组件相互对抗，交替担任挑战者和解决者角色。理解侧为图片生成多个文本选项，生成侧必须视觉重建，经对齐过滤后从最差尝试中学习。在Janus-Pro-1B上测试，GenEval提升2.4分，DPG-Bench提升1.7分，9项理解测试提升0.7分。

---

### [Compress to Remember: Learning Compact Memory via On-Policy Distillation for Long Video Generation](https://arxiv.org/abs/2609.36364)

**作者:** Xiaoyu Wu, Weihang Guo, Yifei Wang et al. · `生成` · 暂无代码

提出PACC方法，通过策略对齐的在策略蒸馏将历史帧压缩为紧凑记忆表示，用于长视频生成中的上下文一致性维护。仅训练压缩模块，使用不变生成器作为学生和指导者，避免核心生成引擎的修改。在MBench和VBench-Long上评估，在一致性和质量方面均优于先前方法，证明压缩上下文可增强长视频记忆而不改变核心引擎。

---

### [Reimagine Video Dynamics](https://arxiv.org/abs/2609.36496)

**作者:** Yu Yuan, Yawen Lu, Guoxian Song et al. · `生成` · [Code](https://github.com/pandayuanyu/RVD)

提出RVD框架，将紧凑、可编辑的动态token从视觉上下文中解耦，实现视频动态的直接编辑。通过自监督重建学习该token——以首帧为视觉上下文，渲染器从动态token恢复原始视频，鼓励其捕获场景演变方式而非外观。开发语言引导的动态token编辑器，配合可扩展的反事实视频对管线和两阶段训练策略，支持有效的视频动态编辑、无需训练的重定时和外观控制的重渲染。

---

### [Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531)

**作者:** Estela Monserrat Arriaga Santana, Julian Rosas Scull et al. · `生成` · `基准` · 暂无代码

引入基于事件锚定的评估协议，使用62个受控真实世界自由落体视频和124个片段（含精细释放和撞击标注），测试视频世界模型在事件边界预测物理后果的能力。评估6个现代模型发现：Runway和Veo的事件生成率超过93%但时序精度不足，Cosmos-Predict-2.5和MAGI-1频繁保持事件前状态。物理预见性被分解为三个独立挑战：启动后果、时间锚定和运动实现。

---

### [Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598)

**作者:** Ziying Zhang, Litao Li, Junchao Liao et al. · `生成` · `基准` · 暂无代码

引入VidScribe统一诊断基准，跨越4种生成机制（T2V、R2V、I2V、V2V）评估视频文本渲染和编辑能力。包含803个人工验证样本和12轴条件正交因子空间，配备11个共享指标和2个任务特定探针。基准测试11个商业和开源系统发现：视频文本能力非单一维度，内容识别与笔画级字形正确性解耦；I2V最可靠而V2V编辑是主要瓶颈；性能退化集中在少数文本结构和时间因素上。

---

## 统计

| 方向 | 论文数 | 含代码 |
|------|--------|--------|
| VLM / MLLM 核心 | 4 | 3 |
| 多模态理解与推理 | 3 | 1 |
| 多模态检索与信息抽取 | 1 | 0 |
| Agent 与具身智能 | 4 | 1 |
| 多模态生成 | 6 | 2 |
| **总计** | **18** | **7** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-10-01*
