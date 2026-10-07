# Arxiv 多模态论文日报 - 2026-10-07

> 收录论文 **18** 篇 | 含代码仓库 **5** 篇 | 覆盖方向 **6** 个

---

## VLM / MLLM

### [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](https://arxiv.org/abs/2610.07987)

**作者：** Yuan Feng, Qize Yang, Ruizhe Chen et al. | **方向：** `VLM/MLLM` | **代码：** 暂无

提出 VisionWeave，赋予多模态大模型"弹性视觉表征编织"能力。通过门控空间池化器和粒度路由，模型可自适应决定视觉表征的分配位置与粒度。在 Qwen3.8-27B 上，平均节省 43% token 的同时保留 98.9% 的原生性能，部署于 SGLang 后吞吐量提升 2.3 倍。

---

### [Two Vectors Replace In-Context Demos: Structured Task Adaptation via Embeddings (STAVE)](https://arxiv.org/abs/2610.07572)

**作者：** Xi Ding, Naichen Shi, Jiawei Zhang | **方向：** `VLM/MLLM` | **代码：** 暂无

提出 STAVE 方法，用两个任务特定向量替代冻结多模态模型中的 in-context 示例，消除每次查询重新编码 demo 图像的开销。一个 readout 向量更新答案生成 token，一个 context 向量更新其他结构 token。在 6 个 LMM 和 5 个 LLM 上验证，以远少于 SOTA 的任务参数达到或超越最优方法。

---

### [Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models](https://arxiv.org/abs/2610.07774)

**作者：** Ziyuan Yang, Wenxuan Ding, Shangbin Feng, Yulia Tsvetkov | **方向：** `VLM/MLLM` | **代码：** 暂无

探索利用 MoE 架构 VLM 中的路由状态作为多模态安全诊断信号，而非直接操纵模型内部状态。发现 router logits 能高度预测输入是否安全，据此提出轻量级路由器安全检测器，在 prompt 预填充阶段识别不安全请求，无需修改模型参数。在 Qwen3-VL 和 Kimi-VL 上大幅降低安全错误。

---

### [Visual-Invariance-Augmented Feature Optimal Alignment for Transferable Adversarial Attacks against Closed-Source MLLMs (IAU-FOA)](https://arxiv.org/abs/2610.06977)

**作者：** Xiaojun Jia, Simeng Qin, Yiming Li et al. | **方向：** `VLM/MLLM` | **代码：** [Code](https://github.com/jiaxiaojunQAQ/IAU-FOA)

提出 IAU-FOA，通过视觉不变性增强和自适应非平衡传输改善对闭源 MLLM 的定向迁移攻击。在全局语义对齐基础上，引入 patch 级局部模式聚类与最优传输匹配，并设计置信度自适应非平衡传输减少弱匹配簇的不可靠对齐。视觉不变性增强通过双向像素强度缩放和逐通道白平衡调整提升跨编码器迁移性。

---

## 多模态理解与推理

### [When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language Models (MOTIVE)](https://arxiv.org/abs/2610.07018)

**作者：** Ziquan Zhu, Hanruo Zhu, Si-Yuan Lu et al. | **方向：** `推理` | **代码：** 暂无

提出 MOTIVE 框架，通过多视角自验证提升 VLM 推理可靠性。系统分析验证器能力和 prompt 设计对验证性能的影响，发现更强验证器提供更可靠判断且无单一 prompt 始终最优。MOTIVE 从互补验证视角评估候选答案，学习正确性对齐的可靠性分数，控制"接受或重新思考"决策，减少不必要的推理轮次。

---

### [CueRator: Agentic Search for Symbolic Rules to Adapt Frozen Multimodal Encoders](https://arxiv.org/abs/2610.07868)

**作者：** Sunchan Park, Beomkwon Cho, Kyeongbo Kong | **方向：** `推理` | **代码：** [Code](https://github.com/cvsp-lab/cuerator)

提出 CueRator，一种智能体框架，通过搜索决策规则来适配冻结的对比式双模态系统。在开放词汇音视频事件感知任务上验证，将符号化公式与轻量策略结合，报告引导的多智能体循环离线发现公式。将已见与未见类别的性能差距从 7.1 缩小至 1.2，发现的规则在仅重训练策略后即可跨编码器竞争。

---

### [CVIF: A Criticality-Driven Visual Intervention Framework for Geometric Diagram Understanding in MLLMs](https://arxiv.org/abs/2610.06399)

**作者：** Jiahui Kang, Bifan Wei, Lingling Zhang et al. | **方向：** `推理` | **代码：** 暂无

针对 MLLM 在几何图理解中因稀疏视觉线索和符号歧义而过度依赖文本先验的问题，提出免训练的 CVIF 框架。在关键层定位后执行视觉干预，通过几何约束局部关系重建模块选择以顶点为中心的视觉证据，自适应视觉转向算子将注意力重新分配至关键 token。在 PGPS9K 和 PGDP5K 上显著提升 Overall F1。

---

### [MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks](https://arxiv.org/abs/2610.06695)

**作者：** Jiuheng Wan, Runze Li, Chen Chen et al. | **方向：** `推理` | **代码：** 暂无

针对医学多模态多智能体框架中冗余通信拓扑导致的效率问题，提出 MedPrune。将诊断过程建模为异构通信图，通过强化学习驱动的异构节点稀疏化消除与当前问题无关的专家智能体，异构边稀疏化选择性保留最具诊断价值的连接。在医学 VQA 实验中超越多智能体基线，显著提升 token 效率和对抗鲁棒性。

---

## 多模态基准与评测

### [ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications](https://arxiv.org/abs/2610.08106)

**作者：** Langxi Huang, Pingping Zhang, Lanyun Zhu et al. | **方向：** `基准` | **代码：** 暂无

提出自动化图表问答基准构建系统，将发现的模型能力缺陷转化为诊断性测试用例。主控制器管理专家智能体，在每一步要求证据与初始错误类型匹配。300 个样本测试显示模型准确率在 32.7%-84.3% 之间，86.4% 的样本成功测试了指定的错误类型，有效保持了诊断目标一致性。

---

### [PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence](https://arxiv.org/abs/2610.07127)

**作者：** Dheeraj Varghese, Anna Vettoruzzo, Walter Simoncini et al. | **方向：** `基准` | **代码：** 暂无

引入 PlaySuite，基于 5000+ 开源视频游戏的大规模交互式视觉智能基准。覆盖 Pygame、HTML5、Godot、Unity 等多种引擎，开发统一闭环交互框架和 Video-LLM-as-a-judge 评估协议。评估 14 个最新模型后发现显著的"感知-行动差距"：尽管推理能力强，当前模型在空间定位、动作执行和自我纠正方面持续失败。

---

### [DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents](https://arxiv.org/abs/2610.08102)

**作者：** Jike Zhong, Ritwick Chaudhry, Xuanbai Chen et al. | **方向：** `基准` | **代码：** 代码即将开源

针对 MLLM 智能体在专业工作流中的密集状态化视觉记忆评估，引入 DSV-Mem 基准。涵盖 5 个用户导向类别和 1000 个问题，发现最强基线得分低于 45%。关键发现：状态演变（尤其是更新次数）是主导难度因素，模型常忽略用户前提与先前状态更新的验证，增加推理努力和记忆管理方法收益有限。

---

## 多模态检索与信息抽取

### [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels (PixelTriage)](https://arxiv.org/abs/2610.07984)

**作者：** Youxing Li | **方向：** `检索` | **代码：** 暂无

提出 PixelTriage，在检索后决定哪些记忆值得加载全分辨率图像。发现像素的收益通常来自一两个检索记忆，且可在回答模型运行前预测。小型不生成文本的模型读取对话、笔记和缩略图来预测像素价值。使用 7B 回答模型时，仅使用 11-23% 的视觉 token 而不显著损失准确率，在 DMV 上回答速度提升 2.9 倍。

---

## Agent 与具身智能

### [PACE: Stage-Consistent Long-Horizon Robot Manipulation via Progress-Aligned Context for Execution](https://arxiv.org/abs/2610.07917)

**作者：** Yenan Chen, Junjie Shi, Lu Chen, Zhongxiang Zhou, Rong Xiong | **方向：** `Agent` | **代码：** 暂无

针对长时域机器人操作中的"阶段混淆"问题，提出 PACE 方法。将演示压缩为有序多模态 prompt token，通过双边缘注意力监督揭示潜在阶段结构。执行时，片段局部快权重记忆因果编码动作-观察转换并调制 prompt 交叉注意力，为统一扩散动作专家生成进度对齐上下文。在 LIBERO-Gen 和 Block Routing 任务上显著提升成功率。

---

### [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](https://arxiv.org/abs/2610.06830)

**作者：** Haozhen Zhang, Haodong Yue, Quanyu Long et al. | **方向：** `Agent` | **代码：** [Code](https://github.com/ViktorAxelsen/MemPilot)

提出 MemPilot，灵活编排按需多模态记忆整理的框架。通过强化学习优化多步 LLM 策略，迭代选择从无查询记忆检索或委托原始多模态历史的查询特定整理。策略联合控制证据量、整理指令、模型选择和视觉访问，实现运行时计算的细粒度分配。在 5 个多模态智能体记忆基准上展示优越的性能-成本-延迟权衡。

---

## 多模态生成

### [Visual Abstention in Unified Multimodal Models (VisTA)](https://arxiv.org/abs/2610.07887)

**作者：** Chufan Shi, Cheng Yang, Tiannuo Yang et al. | **方向：** `生成` | **代码：** [Code](https://github.com/visual-abstention/visual-abstention)

形式化"视觉放弃"概念：当请求的视觉变换在任务规则下不可能时，模型应识别并拒绝生成。引入 Draw-or-Decline (DoD) 基准，评估 8 个统一多模态模型发现编辑能力与放弃能力截然不同。提出 VisTA 训练方法，使模型先判断可行性再决定是否生成。训练后的 VisTA-BAGEL 拒绝 93.0% 的不可行请求，同时完成 74.3% 的可行编辑。

---

### [Learning to Read the Contextual Tokens in Diffusion Transformers](https://arxiv.org/abs/2610.06844)

**作者：** Omer Dahary, Etai Sella, Hadar Averbuch-Elor et al. | **方向：** `生成` | **代码：** 代码即将开源

研究多模态扩散 Transformer 中上下文 token 的功能。训练轻量瓶颈网络将中间上下文 token 映射到冻结 LLM 的输入空间，使 LLM 直接从隐藏表征回答关于生成图像的问题。发现上下文 token 编码丰富的全局场景语义，且在去噪早期即可访问，即使空 prompt 下也可解码。提出 Contextual Alignment 训练技术提升生成质量。

---

### [MTOR: Generalizable AI-Generated Video Detection with Multimodal Semantics and Temporal Over-Regularity](https://arxiv.org/abs/2610.06378)

**作者：** Hang Wang, Chao Shen, Lei Zhang, Zhi-Qi Cheng | **方向：** `生成` | **代码：** [Code](https://github.com/hwang-cs-ime/MTOR)

提出 MTOR 用于可泛化的 AI 生成视频检测。发现字幕衍生的文本表征为全局视觉表征提供互补判别线索，AI 生成视频表现出更强的时间持久性和更低的时间变异性（时间过度正则化）。多模态分支整合视觉和文本表征，TOR 组件在三个层级建模时间过度正则化。在 5 个基准覆盖 46 种生成器变体上达到 SOTA 性能。

---

## 音频多模态

### [AuraSE: Low-Hallucination Generative Speech Enhancement via Multimodal Flow Matching and Inference Policy Optimization](https://arxiv.org/abs/2610.06632)

**作者：** Yingda Shen, Yao Qian, Yuxuan Hu et al. | **方向：** `音频` | **代码：** 暂无

提出 AuraSE，通过多模态流匹配和推理策略优化解决生成式语音增强中的幻觉问题（改变语音内容或说话人身份）。双流到单流多模态扩散 Transformer 允许文本和声学表征交互同时保留退化输入专用通道。推理策略优化 (IPO) 在线学习最优推理配置。在 12 项指标中 11 项排名第一，部署时仅需固定 10 步 ODE 解码器。

---

## 统计

| 方向 | 论文数 | 有代码 |
|------|--------|--------|
| VLM / MLLM | 4 | 1 |
| 多模态理解与推理 | 4 | 1 |
| 多模态基准与评测 | 3 | 0 |
| 多模态检索与信息抽取 | 1 | 0 |
| Agent 与具身智能 | 2 | 1 |
| 多模态生成 | 3 | 2 |
| 音频多模态 | 1 | 0 |
| **总计** | **18** | **5** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-10-07*
