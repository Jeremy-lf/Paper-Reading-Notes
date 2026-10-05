# Arxiv 多模态论文日报 — 2026-10-05

> 收录论文 **34** 篇 | 含代码仓库 **10** 篇 | 覆盖方向 **8** 个

---

## VLM / MLLM 核心（11 篇）

### [Architecture-Dependent Fusion Pathways in MLLMs](https://arxiv.org/abs/2610.03289)

`VLM/MLLM` · Hebao Zhu, Dongxia Wu · 暂无代码

深入探索多模态大语言模型（MLLM）内部视觉与文本数据的融合路径。研究发现不同架构范式（早期融合、晚期融合、交叉注意力等）在跨模态信息分布和特征空间重组方面存在显著差异，为理解MLLM内部工作机制提供了新的架构视角。

---

### [Behavior Pack Optimization for Video MLLM Post-Training](https://arxiv.org/abs/2610.03141)

`VLM/MLLM` · Zhaolu Kang, Shiyu Liu, Tailong Luo et al. · 暂无代码

针对视频MLLM过度依赖外观和语言先验而非时序证据的问题，提出Behavior Pack Optimization方法。该方法通过反事实视角评估输出，有效提升了模型在视频时序推理任务中的表现，为视频MLLM的后训练提供了新的优化范式。

---

### [Recursive Self-Improvement in Unified Multimodal Models](https://arxiv.org/abs/2610.03002)

`VLM/MLLM` · Huijuan Wang, Chufan Shi, Cheng Yang et al. · 暂无代码

提出统一多模态模型的递归跨能力自我改进框架，使文本和视觉能力能够相互提供训练数据。模型可以生成图像、识别自身不足并编写程序验证结果，实现了无需外部标注数据的持续自我进化。

---

### [Balancing Multimodal Learning via Functional Progress](https://arxiv.org/abs/2610.03035)

`VLM/MLLM` · Zhongjing Gu, Fengqiang Wan, Yiming Cui et al. · 暂无代码

针对多模态学习中常见的模态不平衡问题，提出函数空间引导的多模态优化方法（Function-Space Guided Multimodal Optimization）。该方法通过评估各模态的训练进度来协调优化过程，有效缓解了联合训练中的模态主导现象。

---

### [Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient Adaptation](https://arxiv.org/abs/2610.02123) [[Code]](https://github.com/damianomarsili/ExpertLens)

`VLM/MLLM` · Damiano Marsili, Raphi Kang, Aditya Mehta et al. · **[Code](https://github.com/damianomarsili/ExpertLens)**

探索多模态混合专家模型中稀疏性如何驱动语义特化。提出ExpertLens方法，仅识别和微调与目标任务相关的专家模块，以最小参数更新实现高效适配，揭示了MoE架构中专家分工的内在机制。

---

### [Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation](https://arxiv.org/abs/2610.02148)

`VLM/MLLM` · Mohammed Irfan Kurpath, Jaseel Muhammad Kaithakkodan et al. · 有代码

提出仅0.9B参数的紧凑架构，将文本、语音、声音、图像、视频和文档格式投射到统一嵌入空间，同时保持文本权重完全不变。核心发现是指令信号无需独立系统，通过最小投影层和分阶段适配即可实现多模态同步，在跨模态检索中达到与专有系统相当的性能。

---

### [MoLE: Mixture of Latent Experts for Complementary Visual Reasoning](https://arxiv.org/abs/2610.01917)

`VLM/MLLM` · Yingcheng Liu, Tianyi Jiang, Yujuan Ding et al. · 暂无代码

提出MoE式潜在专家混合框架，控制每个潜在视觉专家观察什么视觉证据以及如何转换。通过隔离证据提取阶段并使用专用摘要专家聚合互补表示，在五个视觉推理基准上平均得分78.6，超越SFT 4.9个百分点。

---

### [Same Reward, Different Skills: When Multimodal RL Learns to Look](https://arxiv.org/abs/2610.01908)

`VLM/MLLM` `推理` · Haocun Ye, Xinlong Jiang, Qile Chen et al. · 暂无代码

揭示了一个重要现象：使用可验证奖励的强化学习即使没有视觉训练数据也能提升视觉语言基准分数。但研究强调，视觉证据必须对任务是必要的，模型才能学到真正的视觉定位技能，而非仅依赖语言捷径。

---

### [VETO: Video Efficient Token Optimization for Vision Language Models](https://arxiv.org/abs/2610.01785)

`VLM/MLLM` · Gueter Josmy Faure, Hao Ping Wang, Min-Hung Chen et al. · 暂无代码

提出VETO，一种训练可选的即插即用框架，通过双轴压缩解决长视频推理的token开销问题：帧内压缩器合并语义相似token，帧间压缩器识别并合并时序冗余帧。在LLaVA-OneVision-7B上实现45%推理加速，极端token限制下准确率达55.7%。

---

### [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](https://arxiv.org/abs/2610.01434) [[Code]](https://github.com/EIT-NLP/MWOP)

`VLM/MLLM` · Xudong Wang, Hao Wu, Haozhe Hu et al. · **[Code](https://github.com/EIT-NLP/MWOP)**

提出模态感知的宽度方向操作剪枝方法，对视觉和文本输入独立剪枝注意力路径并选择FFN通道。该方法在保持多模态基准高性能的同时实现了显著的预填充加速，为MLLM高效部署提供了实用方案。

---

### [SpikeMoE: Brain-Inspired Competitive Routing for Flexible Spiking Mixture-of-Experts](https://arxiv.org/abs/2610.01418)

`VLM/MLLM` · Xiaoli Liu, Yujie Liang, Jialin Li et al. · 暂无代码

将脉冲神经网络与混合专家模型结合，采用生物启发的竞争性路由机制。该方法有效处理多模态任务中的模态缺失问题，在保持高能效的同时达到SOTA性能，为神经形态计算在多模态AI中的应用开辟新方向。

---

## 多模态理解与推理（6 篇）

### [Revealing Epistemic Uncertainty in MLLMs via Causal-Invariant Masking](https://arxiv.org/abs/2610.02887)

`推理` · Haoyang Luo, Linwei Tao, Jie Gui et al. · 暂无代码

针对MLLM幻觉问题提出因果不变掩码方法来量化认知不确定性。通过测量语义偏移引入Semantic Divergence指标，捕捉模型在知识边界处的局限性，为理解和缓解多模态幻觉提供了新的理论工具。

---

### [Seeing, Saying, but Not Using: From Reportable Spatial Facts to Usable States in MLLMs](https://arxiv.org/abs/2610.02876) [[Code]](https://github.com/changcv2021/Seeing-Saying-but-Not-Using-From-Reportable-Spatial-Facts-to-Usable-States-in-Multimodal-Models)

`推理` · Jinchang Zhang, Guoyu Lu · **[Code](https://github.com/changcv2021/Seeing-Saying-but-Not-Using-From-Reportable-Spatial-Facts-to-Usable-States-in-Multimodal-Models)**

发现MLLM能正确报告空间事实却无法在后续推理中使用它们。引入SpaceConflict基准研究这一区别，提出操作状态监督方法来对齐共享事实与可用状态，揭示了当前模型在空间推理中的深层缺陷。

---

### [How Robust Is Multimodal Claim Verification to LLM Rewriting?](https://arxiv.org/abs/2610.02841)

`推理` · Yun-Ang Wu, Xanh Ho, Andre Greiner-Petter et al. · 暂无代码

研究LLM改写带来的风格变化如何影响多模态事实验证。评估多个模型发现，虽然准确率保持稳健，但在对冲导向条件下概率输出会发生一致性偏移，揭示了模型对文本风格的隐式敏感性。

---

### [Architectural Sampling: Test-Time Scaling via Computational Diversity in Frozen VLMs](https://arxiv.org/abs/2610.01687) [[Code]](https://github.com/Akshit21112002/Architectural-Sampling)

`推理` · Akshit Singh, Shyam Marit, Wei Lin et al. · **[Code](https://github.com/Akshit21112002/Architectural-Sampling)**

提出无需训练的测试时扩展方法，通过复用解码器层的选定块生成多样化候选，引入计算多样性。该方法在不更新模型权重的情况下，比标准温度采样显著提升准确率和候选覆盖率。

---

### [SIEVE: Selective Attention-Value Suppression for Vision-Language Models Unlearning](https://arxiv.org/abs/2610.01962)

`推理` · Si Qi Goh, Cap Dang Xuan Kiet, Tat-Jen Cham et al. · 暂无代码

提出使视觉语言模型选择性遗忘个人身份信息同时保留允许知识的框架。通过抑制遗忘样本的注意力值实现SOTA的机器遗忘性能，为VLM隐私保护提供了新思路。

---

### [Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluation with Verified Quality Preservation](https://arxiv.org/abs/2610.01670)

`推理` `基准` · Yuan Huang, Zirui Song, Xiuying Chen · 暂无代码

引入反事实基准来审计多模态模型作为图像编辑评判者时的偏见。实验发现保持质量的线索和无关视觉元素会显著偏移模型判断，揭示了MLLM评判的系统性偏差。

---

## 多模态基准与评测（5 篇）

### [Beyond Single Videos: Benchmarking and Active Evidence Seeking for E-Commerce Cross-Video Reasoning](https://arxiv.org/abs/2610.03099)

`基准` `Agent` · Jinghan Zhao, Yiman Hu, Liang Wu et al. · 暂无代码

引入AdsCVR电商跨视频推理基准，并提出AdSeek智能体框架进行主动证据获取。该方法动态选择视觉和音频工具来整合多个视频中的细节，推动了电商场景下多视频联合推理的研究。

---

### [VisAudit: Evaluating Multimodal Agents for Visual Diagnosis and Repair](https://arxiv.org/abs/2610.02399)

`基准` `Agent` · Shicheng Liu, Adam Kahirov, Qi Zhang et al. · 暂无代码

提出VisAudit基准，评估多模态智能体在数据可视化场景中自主审查、诊断和修复缺陷图表的能力。测试表明即使是最先进的模型也难以可靠地执行自主修复，揭示了当前Agent在视觉诊断方面的不足。

---

### [TasteBench: Multimodal Benchmark for Sensory Prediction, from Molecules to Sustainable Foods](https://arxiv.org/abs/2610.02599) [[Code]](https://github.com/Food-Intelligence-Lab/tastebench)

`基准` · Anna T. Thomas, Sohum Patnaik, Caroline Cotto et al. · **[Code](https://github.com/Food-Intelligence-Lab/tastebench)**

提出TasteBench多模态感官预测基准和竞赛，覆盖从分子级分类到食品级排序的多层次评估。为解决新型食品是否接近其动物源目标口味的评估难题提供了标准化测试框架。

---

### [Structural-Functional Brain Connectivity Generation via Multimodal Hypergraph-based Flow Matching](https://arxiv.org/abs/2610.02722)

`基准` `生成` · Chyong Yi Poh, Hwa Hui Tew, Junn Yong Loo et al. · 暂无代码

提出多模态超图流匹配框架，用于联合生成结构-功能脑连接数据和跨模态转换。利用超图神经网络建模高阶关系，为脑科学中配对数据稀缺问题提供了生成式解决方案。

---

### [No-Free-Graph: Learning When Multimodal Data Should Be Graphified](https://arxiv.org/abs/2610.02768)

`基准` `检索` · Zekai Chen, Kai Hu, YuXin Zeng et al. · 暂无代码

提出MAG-SCOUT框架，在生成完整拓扑之前估计图结构的预期效用。研究表明多模态图学习并非总是有益，"何时图化"是一个被忽视的关键问题，为多模态图学习的合理应用提供了理论指导。

---

## 多模态检索与信息抽取（3 篇）

### [AMBER: Multi-View Adaptive Budget Allocation for Listwise Vision-Language Reranking](https://arxiv.org/abs/2610.02831) [[Code]](https://github.com/wnlfc/AMBER)

`检索` · Wenteng Chen, Jiachen Zhu, Rong Shan et al. · **[Code](https://github.com/wnlfc/AMBER)**

针对视觉语言重排序的高推理成本问题，提出自适应多视角预算Elo重排序框架。该在线框架动态优化全局资源分配以最大化期望信息增益，在保持重排序质量的同时大幅降低计算开销。

---

### [Walking the Embedding Space: Datastore Extraction from Multimodal RAG](https://arxiv.org/abs/2610.01871)

`检索` · Maria Carmen Jica, Ali Satvaty, Suzan Verberne et al. · 暂无代码

提出针对图像返回型多模态RAG系统的自动数据提取攻击方法。通过将阴影图像与恢复图像混合，高效重建私有数据存储项，揭示了多模态RAG系统的安全隐患。

---

### [AiSearch: Interactive Multi-Modal Search with VLMs](https://arxiv.org/abs/2610.01389)

`检索` · Ali Koksal, Mei Chee Leong, Vicky Sintunata et al. · 暂无代码

利用视觉语言模型的零样本能力实现基于自然语言的图像和视频搜索。支持通过用户反馈进行交互式精化，将搜索结果与特定意图对齐，为多模态检索提供了灵活的人机协作范式。

---

## Agent 与具身智能（6 篇）

### [WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents](https://arxiv.org/abs/2610.03036)

`Agent` · Jiangang Han · 暂无代码

提出WebFovea视觉Web智能体，在实时网站界面上操作并返回可验证答案。研究发现失败往往发生在模型与页面之间的交互层而非推理本身，揭示了Web Agent实际部署中的关键瓶颈。

---

### [A Simulation-Grounded Agentic VLM Framework for Wildfire Monitoring and Reporting](https://arxiv.org/abs/2610.02451)

`Agent` · Duowen Chen, Yuchen Sun, Zhiqi Li et al. · 暂无代码

提出仿真驱动的VLM智能体框架用于野火监控。将2D野火仿真转换为标注视频片段，创建多模态记忆使VLM无需训练即可生成结构化报告，为灾害监控提供了低成本的数据增强方案。

---

### [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204)

`Agent` · Yen-Jen Wang, Haozhe Jiang, Shuying Deng et al. · 暂无代码

提出RPG框架，使机器人在不更新模型权重的情况下自主提升执行系统。通过仿真练习和执行反馈精化技能，显著提高了物理世界中的任务成功率，为具身智能的自主进化提供了新路径。

---

### [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200)

`Agent` `推理` · Qiushi Han, Keya Hu, Linlu Qiu et al. · 暂无代码

证明多模态模型具有强大的推理能力，只需适当的视觉工具即可释放。VISTA提供长视野视觉和无损视觉记忆，使模型能主动检索过去的观察，在复杂视觉推理基准上达到满分。

---

### [Token Communication-Assisted Collaborative Embodied Artificial Intelligence](https://arxiv.org/abs/2610.01826)

`Agent` · Peng Yi, Ying-Chang Liang · 暂无代码

探索token通信作为协作具身AI的原生智能接口。提出token作为紧凑语义载体的框架，在保持任务效率的同时大幅降低通信负载，为多机器人协作提供了高效的通信范式。

---

### [Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents](https://arxiv.org/abs/2610.01892)

`Agent` `推理` · Feiyu Gavin Zhu, Xiaoyu Zhu, Jiqi Yang et al. · 暂无代码

将推理重新表述为从预指定候选中选择的任务，大幅降低推理延迟。该方法在多模态搜索基准中保持了有竞争力的成功率，同时显著减少推理开销，为高效Agent设计提供了新思路。

---

## 多模态生成（2 篇）

### [Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521) [[Code]](https://github.com/xbyym/SMI)

`生成` · Ying Yang, Guiyu Zhang, Lianghua Huang et al. · **[Code](https://github.com/xbyym/SMI)**

提出Spatial Memory Intelligence框架解决长视频生成和世界模型中的长程空间上下文管理难题。采用理解模型进行空间记忆管理，使用协调原子操作实现高效的长期记忆存储与检索。

---

### [Form and Void: Entangled Composition through an Autonomous AI Agent](https://arxiv.org/abs/2610.02045)

`生成` `Agent` · Shiwen Wang, Jian Yang, Xu Wang et al. · 暂无代码

提出一种利用正空间和负空间生成图像的自主AI Agent。采用渐进式工作流分析形状并生成构图指令，同时考虑实体与虚空的关系，显著提升了生成图像的视觉连贯性和艺术性。

---

## 音频多模态（3 篇）

### [GAANet: Global-guided Asymmetric Attention Network for Audio-Visual Speech Separation](https://arxiv.org/abs/2610.02752) [[Code]](https://github.com/redizzy/GAANet)

`音频` · Zhiyuan Zhang, Jingyuan Xu, Yiming Tang et al. · **[Code](https://github.com/redizzy/GAANet)**

提出全局引导的非对称注意力网络用于音视频语音分离。通过非对称多尺度融合和全局引导注意力机制解决多尺度信息建模难题，在语音分离任务中达到SOTA性能。

---

### [Teaching LLMs to Hear Who Spoke What: Metadata-Supervised Pretraining for Encoder-Free Speech-LLMs](https://arxiv.org/abs/2610.01695)

`音频` `VLM/MLLM` · Mohan Shi, Ruchao Fan, Sunit Sivasankaran et al. · 暂无代码

提出元数据监督预训练方法，在无编码器的语音语言模型中发展说话人区分能力。使模型能从低级声学特征中学习，在说话人识别任务上与基于编码器的模型竞争，为端到端语音LLM开辟新路径。

---

### [AVSD-Scenes: A Dataset for Audio-Visual Description of Urban Scenes](https://arxiv.org/abs/2610.01861) [[Code]](https://github.com/dhanunjaya-varma/AVSD-Scenes)

`音频` `基准` · Dhanunjaya Varma Devalraju, Arshdeep Singh, Mark D. Plumbley · **[Code](https://github.com/dhanunjaya-varma/AVSD-Scenes)**

构建城市环境的配对音视频场景描述数据集，使用LLM生成描述。基准测试表明结合音频和视觉描述可提升语义对齐和场景分类准确率，为多模态场景理解提供了新的数据资源。

---

## 3D 视觉语言（3 篇）

### [Kinematics-Induced Multimodal 3D Human Pose Estimation with Subject-Level Privacy](https://arxiv.org/abs/2610.02943)

`3D` · Kaushik Bhargav Sivangi, Fani Deligianni · 暂无代码

提出统一框架将运动学诱导的传感器融合与受试者级隐私审计相结合。在融合多传感器信息进行3D人体姿态估计的同时，通过差分隐私等技术保护个体隐私，平衡了性能与安全。

---

### [Octrees as an Explicit 3D Language](https://arxiv.org/abs/2610.02388) [[Code]](https://github.com/octree-nn/octllm)

`3D` `VLM/MLLM` · Ran Dan, Si-Tong Wei, Pengfei Xiong et al. · **[Code](https://github.com/octree-nn/octllm)**

提出OctLLM，将八叉树占用token作为显式3D序列引入语言模型，通过独立分支添加3D能力而不覆盖通用语言技能。避免了将形状压缩到隐式码本的妥协，在3D理解任务中达到SOTA。

---

### [TouchTherm: Building Multimodal Digital Twins of Objects for Tactile and Thermal Rendering](https://arxiv.org/abs/2610.01943)

`3D` `生成` · Yitao Zhang, Hong Ying, Haoran Guo et al. · 暂无代码

构建捕获视觉、触觉和热学属性的仿真就绪数字孪生框架。结合结构光扫描与红外视频恢复微高度场和动态热数据，为机器人触觉感知和虚拟现实提供了多模态物理仿真资产。

---

## 统计

| 方向 | 论文数 | 含代码 |
|------|--------|--------|
| VLM / MLLM 核心 | 11 | 3 |
| 多模态理解与推理 | 6 | 2 |
| 多模态基准与评测 | 5 | 1 |
| 多模态检索与信息抽取 | 3 | 1 |
| Agent 与具身智能 | 6 | 0 |
| 多模态生成 | 2 | 1 |
| 音频多模态 | 3 | 2 |
| 3D 视觉语言 | 3 | 1 |
| **总计** | **34** | **10** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-10-05*
