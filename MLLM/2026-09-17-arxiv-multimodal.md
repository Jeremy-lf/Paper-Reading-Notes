# Arxiv 多模态论文日报 — 2026-09-17

> 收录论文 **20** 篇 · 含代码仓库 **10** 篇 · 覆盖方向 **5** 个

---

## VLM / MLLM 核心

### 1. [Semantic-Spatial Agreement Verification for Mitigating Object Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2609.17269)

**作者:** Ziheng Ren, Qian Gao, Jun Fan et al. · `VLM/MLLM` · [Code](https://github.com/zihengren/SSAV)

提出SSAV方法，一种无需训练的MLLM输出验证方法。通过语义支持估计和空间区域验证两个模块，检测MLLM中不受视觉支持的目标声明，有效缓解目标幻觉问题。在LLaVA-1.5-7B上，CHAIRs指标从49.40%降至32.80%。

### 2. [SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2609.16601)

**作者:** 详见原文 · `VLM/MLLM` · 暂无代码

提出SAVOR训练框架，通过校准MLLM的自我评估能力来缓解幻觉。扩展输出模式以包含置信度值，使用GRPO优化目标惩罚校准误差，推理时仅在不确定时重新审视视觉证据。在POPE、HallusionBench等基准上有效降低幻觉同时保持通用能力。

### 3. [ViD: Vision-Dominant Gender Bias Mitigation for Large Vision-Language Models](https://arxiv.org/abs/2609.16647)

**作者:** 详见原文 · `VLM/MLLM` · 暂无代码

提出ViD框架，受因果分析启发，通过五个注意力配置揭示语言先验的隐含影响。利用跨模态注意力和后门调整策略抑制性别偏差，无需额外训练即可将性别偏差降低14.7%，同时保持推理能力。

### 4. [Efficient Quantization-Aware Distillation with Cross-Modal Alignment for Edge Vision-Language Models](https://arxiv.org/abs/2609.16689)

**作者:** 详见原文 · `VLM/MLLM` · 暂无代码

提出面向边缘设备的量化语义蒸馏统一框架。解决先前方法优化不一致和训练效率低下的问题，通过RGB引导的语义迁移增强非RGB模态表征，在量化条件下保持一致训练，在非RGB模态上取得一致提升。

### 5. [ReDraft: Reference-Driven Revision for Continual VLLM Post-Training](https://arxiv.org/abs/2609.16639)

**作者:** 详见原文 · `VLM/MLLM` · 暂无代码

提出ReDraft方法解决多模态模型持续后训练中能力保持与新能力获取的矛盾。让模型修订自身错误输出而非直接替换为专家答案，在目标任务上获得56.9分增益，同时将遗忘率从16.6降至1.5（降低11.3倍）。

### 6. [Sparse MLLM Anchors, Dense Adaptation: Breaking the Self-Referential Loop in Wild Test-Time Adaptation](https://arxiv.org/abs/2609.17040)

**作者:** Zhenbin Wang, Lei Zhang, Lituan Wang et al. · `VLM/MLLM` · [Code](https://github.com/wongzbb/MASA)

提出MASA框架，利用冻结MLLM生成的结构化语义描述打破野外测试时适应的"自指循环"。仅对少量可靠性排序锚点查询MLLM，编码描述并传播至邻近样本，通过在线原型记忆提供辅助适应目标。

### 7. [Hub-Spectral Activation of Latent Multimodal Knowledge](https://arxiv.org/abs/2609.17094)

**作者:** Ying Guo, Haidong Chen, Linrui Xu et al. · `VLM/MLLM` · [Code](https://github.com/Luo1Yan/HSA)

提出HSA闭式方法，恢复和激活冻结表征中的hub可读多模态知识，无需目标对监督或梯度优化。在ImageBind和LanguageBind上，将双向Recall@10从18.27%提升至31.15%，Top-1准确率从29.01%提升至52.43%。

---

## 多模态理解与推理

### 8. [Anchoring What Matters: A Dual-Level Learning Framework for Visually-Grounded Multimodal Reasoning](https://arxiv.org/abs/2609.18057)

**作者:** Xinxin Song, Siyuan Li, Tingxiong Xiao, Jinli Suo · `推理` · 暂无代码

提出PIVOT双层学习框架，通过自校准经验回放和视觉引导优势分配两个核心机制，将策略优化聚焦于有效的视觉推理线索。在多种基准上显著增强LVLM的多模态推理能力。

### 9. [What Do Hallucinations Reveal About Multimodal Reasoning? Diagnosing Visual Grounding Failures via Contrastive Decoding Probes](https://arxiv.org/abs/2609.16646)

**作者:** Zhaoyang Wei et al. · `推理` · [Code](https://github.com/zhaozhipeng1997/SAFE_public)

提出SAFE方法，利用视觉-文本系统分析自身幻觉错误。通过对比有无图像输入的输出序列差异，检测模型何时偏好语言模式而非视觉信息。揭示图像依赖随文本推进而下降、错误呈时序聚集等特征。

### 10. [Layers, Sinks, and Scaling: Adaptive Evidence Selection for Multimodal Large Language Models](https://arxiv.org/abs/2609.16795)

**作者:** 详见原文 · `推理` · [Code](https://github.com/wongzbb/AREA)

提出AREA自适应相关性引导证据分配方法，无需训练即可在推理时自适应选择证据。通过生成探测token读取视觉和文本相关性，自适应决定是否需要干预、暴露多少证据、何时刷新文本。在KB-VQA和标准多模态基准上达到无训练方法最优。

### 11. [Reasoning with Image Generation](https://arxiv.org/abs/2609.16409)

**作者:** 详见原文 · `推理` · [Code](https://github.com/multimodal-ai-lab/reimagin)

提出利用图像生成模型为多模态系统提供灵活视觉推理能力的新框架。系统接受自然语言指令执行无约束视觉修改（如清除遮挡、绘制布局），在6个空间与碰撞推理任务上超越传统方法达25%。

### 12. [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](https://arxiv.org/abs/2609.17248)

**作者:** Zhaoyang Wei, Zipeng Wang, Yushe Cao et al. · `推理` · 暂无代码

提出Video-HolmesV2基准，专注于长视频中的深度音视频耦合推理。要求模型基于精确的时空音视频证据进行推理，引入音频-文本引导的token压缩框架。即使强商用模型准确率也低于60%。

---

## 多模态基准与评测

### 13. [MechReason: Benchmarking Multi-Image Multi-Hop Reasoning in Mechanical Engineering](https://arxiv.org/abs/2609.16012)

**作者:** 详见原文 · `基准` · [Code](https://github.com/Lifelong-journey/MechReason)

提出MechReason数据集，源自工程文献，包含12K多跳QA对和21K多模态资产（微观照片、系统图等）。涵盖8种任务格式和4个推理方向（诊断、设计、预测、解释），顶级模型仅达62.89%准确率。

### 14. [SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233)

**作者:** 详见原文 · `基准` `3D` · 暂无代码

提出SceneBench，包含966个逼真3D场景和多层级语义标注（区域和单个物体），提供183K+标注元素。设置属性查询、物理推理和多层级推理三类测试任务，揭示模型在复杂结构推理上的显著不足。

### 15. [EgoPathBench: Evaluating Zero-Shot Egocentric Waypoint Decision-Making in Vision-Language Models](https://arxiv.org/abs/2609.16610)

**作者:** 详见原文 · `基准` · 暂无代码

提出EgoPathBench，评估VLM在零样本下的自我中心路径点决策能力。包含31K+训练prompt和5项任务，9个VLM最高仅达28.3分，物理avatar路由成功率仅2.9-4.0%，揭示现代系统在物理约束路径规划上的困难。

### 16. [Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model](https://arxiv.org/abs/2609.18323)

**作者:** Haoyu Zhao, Zihao Zhao, Tianyu Deng et al. · `基准` · [Code](https://github.com/gulucaptain/MiniMax-H3-Reason)

评估全模态生成模型MiniMax-H3的物理世界推理能力。提出四维评估框架，使用音频+图像/视频组合输入，517个实例中成功率41.97%。视觉任务最高(56.00%)，音频任务最低(27.40%)，证明多模态融合对最大化能力至关重要。

---

## 多模态检索与生成

### 17. [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](https://arxiv.org/abs/2609.16591)

**作者:** 详见原文 · `检索` `生成` · 暂无代码

提出FLAT预训练框架，将视觉和文本数据统一为一维连续序列，通过嵌套dropout实现灵活输出维度。单次预训练同时支持跨模态检索和生成，微调后在MS-COCO上达到83.1 GenEval（文生图）和86.8 Recall@5（图生文）。

### 18. [Efficient Text-to-Image Generation: An Adaptive Step Schedule Controller for Diffusion Models](https://arxiv.org/abs/2609.16572)

**作者:** 详见原文 · `生成` · 暂无代码

提出自适应扩散控制器，根据文本prompt复杂度动态调整去噪步数。通过组合不同步数计划并评估区间误差差异实现自适应切换，在COCO和DiffusionDB上有效缩短生成时间同时保持图像质量。

---

## Agent 与具身智能

### 19. [M²Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2609.18259)

**作者:** Chunpu Xu, Zhixuan Liang, Yuhao Zhang et al. · `Agent` · [Code](https://github.com/cpaaax/M2Tok)

提出M²Tok多头多码本动作tokenizer，解决VLA模型中现有离散tokenizer重建损失高的问题。通过多头分解和独立码本量化大幅扩展表达能力，在RoboTwin、Simpler-Env和真实机器人实验中均展现优越重建保真度和成功率。

### 20. [NeMo Data Designer: An Extensible Framework for Multimodal Synthetic Data Generation](https://arxiv.org/abs/2609.17699)

**作者:** Johnny Greco, Nabin Mulepati, Andre Manoel et al. · `Agent` · [Code](https://github.com/NVIDIA-NeMo/DataDesigner)

NVIDIA开源多模态合成数据生成框架，采用声明式配置和灵活插件系统。支持预览-修订工作流，允许构建者在小样本上测试后再全量执行，处理依赖管理和失败重试，适用于结构化、多模态和领域特定场景。

---

## 统计

| 方向 | 论文数 | 含代码 |
|------|--------|--------|
| VLM / MLLM 核心 | 7 | 3 |
| 多模态理解与推理 | 5 | 3 |
| 多模态基准与评测 | 4 | 2 |
| 多模态检索与生成 | 2 | 0 |
| Agent 与具身智能 | 2 | 2 |
| **总计** | **20** | **10** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-09-17*
