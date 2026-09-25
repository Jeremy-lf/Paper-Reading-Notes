# Arxiv 多模态论文日报 — 2026-09-25

> 收录论文 **32** 篇 · 含代码仓库 **14** 篇 · 覆盖方向 **8** 个

---

## VLM / MLLM 核心

### [Pistis Technical Report](https://arxiv.org/abs/2609.28554)
`VLM / MLLM` · Heyun Chen, Xiaohan Lan, Jiaxi Li et al.

提出 Pistis 系列多模态大语言模型（27B/9B），采用交错蒸馏与强化学习（IDRL）的后训练策略。该方法在交错多模态数据上实现了高效训练，显著提升了模型在多图、视频理解等任务上的表现。

---

### [Hyperbolic Multimodal Continual Learning: A Closest-Admissible Solution](https://arxiv.org/abs/2609.29329)
`VLM / MLLM` · Jiahong Liu, Ming Shen, Xiaohao Liu et al.

提出 HMCL 方法，通过共享双曲等距变换和最近容许修正来保持 Lorentz 几何结构，解决多模态持续学习中的灾难性遗忘问题。在三种骨干网络上将表征漂移降低了 81.2%–95.5%。

---

### [Confidence Falls Short: Asymmetric Certainty Gains from Optimization Hinder Multimodal Classification](https://arxiv.org/abs/2609.28165)
`VLM / MLLM` · Longfei Huang, Xiangyu Wu, Yang Yang

揭示多模态学习中模态不平衡的新问题：优化过程中置信度的提升对不同模态是不对称的，反而损害分类性能。提出 MaxCR（最大置信度正则化）方法，通过最大抑制/激励机制平衡模态置信度。

---

### [VCMM: Variance-Calibrated Momentum for Multimodal Learning](https://arxiv.org/abs/2609.27577)
`VLM / MLLM` · Zhongjing Gu, Chenyang Huang, Yufa Feng et al.

提出方差校准动量法（VCMM），受卡尔曼滤波启发设计控制器，解决多模态学习中的模态不平衡问题。该方法动态校准各模态的更新动量，实现更均衡的多模态融合。

---

### [TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement](https://arxiv.org/abs/2609.29099)
`VLM / MLLM` · Haoyang Li, Yaxin Xiao, Linyan Dai et al.

提出基于自适应秩的过滤方法 TraceGuard，利用六个语料级特征之间的一致性检测并移除多模态训练数据中的投毒样本。在 19 种攻击配置下平均移除 98.4% 的投毒数据，且无需预知攻击类型。

---

### [IronViT: Toward Efficient Generalist Visual Representation Learning](https://arxiv.org/abs/2609.29252)
`VLM / MLLM` · Jiaxi Huang, Yueqi Hu, Xin Zhu et al.

提出 IronViT，一种通用视觉编码器，通过 softmax 注意力桥接整合多个专家模型能力，再蒸馏到混合 softmax-linear 编码器中。在保持高效推理的同时，达到领先视觉编码器的竞争力水平。

---

### [Multimodal Routing and Region Refinement for Language-Guided Medical Image Segmentation](https://arxiv.org/abs/2609.28860)
`VLM / MLLM` · Md Maklachur Rahman, Md Hasan Al Banna et al.

提出 MRSeg 框架，采用混合适配器架构结合 ConvNeXt 和 PubMedBERT，实现文本引导的医学图像分割。通过多模态路由和区域细化机制提升分割精度，已被 MICCAI 2026 接收。

---

### [M²PFN: End-to-End Disentangled Alignment for Generalizable Multimodal In-Context Learning in Alzheimer's Disease](https://arxiv.org/abs/2609.28836)
`VLM / MLLM` · Lujia Zhong, Shuo Huang, Jianwei Zhang et al.

将 TabPFN 扩展到多模态场景，提出 M²PFN 用于阿尔茨海默病诊断。通过解耦的图像/表格对齐机制实现可泛化的多模态上下文学习，在 ADNI 数据集上达到 82.21% 的 macro-AUC。

---

### [PhyMo: A Physical-Field Modality for Multimodal AI4Physics](https://arxiv.org/abs/2609.27554)
`VLM / MLLM` · Henan Sun, Haitao Hu, Jin Liu et al.

引入"物理场"作为新的多模态模态，提出 PhyMo 框架用于 AI4Physics。通过 PDE 关联算子处理物理场数据，拓展了多模态学习在物理科学中的应用边界。

---

### [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](https://arxiv.org/abs/2609.27395)
`VLM / MLLM` · Sanghee Park, Kee-Eung Kim · [Code](https://github.com/naver-ai/prism-vlm)

提出 PRISM-VLM，一套沿七个评估维度对紧凑型视觉语言模型进行多轴判别评测的基准。引入 PScore 综合评分指标，系统性地揭示小型 VLM 在不同能力维度上的优劣势。

---

## 多模态理解与推理

### [Is Reasoning Always Useful? Rethinking Reasoning Utility in Universal Multimodal Embeddings](https://arxiv.org/abs/2609.29560)
`推理` · Wenxiao Fan, Jingling Fu, Luohang Liu et al.

分析了通用多模态嵌入模型 UME-R1 中判别式分支与推理驱动分支的作用差异，发现推理并非在所有场景下都有益。提出 SURE 路由策略，无需重训练即可将嵌入性能提升 1.5 个百分点。

---

### [Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space](https://arxiv.org/abs/2609.29457)
`推理` · Jaron Yeh, Yen-Wei Chang, Jiang Liu, Shao-Yuan Lo · [Code](https://github.com/Yen666/Anomaly-LR)

提出 Anomaly-LR 框架，在视觉潜在空间中进行渐进式缺陷推理检测。同时构建 IAD-LR-22K 指令数据集，包含来自 4,523 张图像的 22,228 个实例，为工业异常检测提供大规模训练资源。

---

### [MoVISA: Multi-Token Reasoning for Video Object Segmentation](https://arxiv.org/abs/2609.28956)
`推理` · Ruining Zhao, Ho Kei Cheng, Alexander G Schwing

提出使用多个分割令牌（SEG0、SEG1）进行细粒度时空掩码预测的 MoVISA 方法。在 MeViS 上实现 13.2% 的 J&F 提升，在 ReVOS 上提升 8.4%，显著改善视频目标分割性能。

---

### [Exploiting Target Knowledge from MLLMs for Robust Few-Shot Segmentation](https://arxiv.org/abs/2609.28949)
`推理` · Yijun Hu, Heng Fan, Libo Zhang

提出 MK-FSS 框架，从多模态大语言模型中挖掘空间与语义知识用于少样本分割。通过双记忆辩论融合和渐进式跨模态提示生成器增强 SAM 2 的分割能力。

---

### [DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs](https://arxiv.org/abs/2609.28570)
`推理` · Yingxuan Zhuang, Miao Pan, Wangjie Gan et al.

结合熵正则化与 Renyi 预条件来对抗多模态大模型中的幻觉问题。DEEPO 方法在 VideoMMMU 等基准上提升 4.0 分，有效减少了视频理解中的幻觉现象。

---

### [BiCFlow-MER: Orchestrating Discriminative and Generative Multimodal Emotion Recognition via Conditional Transport](https://arxiv.org/abs/2609.27615)
`推理` · Yanbing Wang, Shenyue Wang, Chunyang Yu

提出条件流框架 BiCFlow-MER，协调判别式与生成式方法进行多模态情感识别。通过音频-文本集成的条件传输机制，实现更精准的多模态情感理解。

---

## 多模态基准与评测

### [SWE-PolyVision: Benchmarking Cross-Image Abductive Reasoning for Repository-Level Software Engineering](https://arxiv.org/abs/2609.29754)
`基准` · Jiajun Wu, Leixin Sun, Zihan Tan et al.

构建包含 92 个真实任务的可执行基准 SWE-PolyVision，测试编码智能体能否整合多图像证据进行验证性修复。涵盖三种访问模式，系统评估跨图像溯因推理能力。

---

### [STRAND: Benchmarking and Improving Object-Centric Spatio-Temporal Monitoring in Video Large Language Models](https://arxiv.org/abs/2609.29607)
`基准` · Thong Nguyen, Tri Cao, Khoi Le et al. · [Code](https://github.com/nguyentthong/video_hallucination)

提出 STRAND 基准，通过 Faithful Accuracy 评分评估视频大模型的中间推理能力。同时引入以对象为中心的框架，利用结构化轨迹减少幻觉，提升视频时空监控的可靠性。

---

### [RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation](https://arxiv.org/abs/2609.29028)
`基准` · Shaohua Dong, Zexuan Meng, Haiyan Sun et al. · [Code](https://github.com/ShaohuaDong2021/RGBD20K/)

发布 RGBD20K 大规模基准数据集，包含 20,000 对 RGB-D 图像，覆盖 160 个细粒度类别。提出分数净化融合（SPF）方法，在多个评测基准上达到最优性能。

---

### [MultiVENT-Raw: A Benchmark for Retrieval and Reasoning over Raw Videos](https://arxiv.org/abs/2609.28437)
`基准` · Reno Kriz, David Etter, Alexander Martin et al. · [Code](https://github.com/hltcoe/multivent-raw)

发布 MultiVENT-Raw 基准，包含约 120,000 个原始视频、130 个事件和 222 个查询，系统评估多模态模型在原始视频上的检索与报告生成任务能力。

---

### [LAYERSCOPE: A Layerwise Characterization of Video and Multimodal Learned Representations](https://arxiv.org/abs/2609.28086)
`基准` · Sandra Arcos-Holzinger, Debashish Chakraborty et al.

提出 LAYERSCOPE，一套无需标签的逐层分析框架，利用几何度量刻画视频和多模态模型的学习表征。帮助研究者理解多模态模型各层的功能分化与表征演化规律。

---

## 多模态检索与信息抽取

### [IMEX-FND: A Traceable Interaction-Aware Mixture-of-Experts Framework for Multimodal Fake News Detection](https://arxiv.org/abs/2609.29610)
`检索` · Yuchen Miao, Zijun Wang, Ke Liu et al.

提出 IMEX-FND 框架，结合自适应路由与显式交互分解（唯一性、冗余性、协同性），用于多模态假新闻检测。在 Weibo 和 Gossip 基准上达到最优性能。

---

### [Anatomy of a Decision: Uncertainty-aware Hierarchical Intent Learning via Flow Matching for Multimodal Recommendation](https://arxiv.org/abs/2609.29609)
`检索` · Yuchen Miao, Zijun Wang, Ke Liu et al.

提出 UHIFlow 框架，利用条件流匹配进行不确定性量化和层次化意图生成，动态适应用户决策粒度。为多模态推荐系统提供更精准的用户意图理解。

---

### [FoCal: Frequency-Oriented Cross-Modal Interaction and Spectral Calibration for Aerial Visible-Infrared Object Detection](https://arxiv.org/abs/2609.29125)
`检索` · Ben Liang, Chao Sui, Junqi Bai et al. · [Code](https://github.com/universeliang/FoCal)

提出面向无人机场景的频域导向跨模态框架 FoCal，包含 FADC 双域校准和 DGSM 频谱调制模块。在 DroneVehicle 上以 3.0M 参数实现 83.5% mAP50，推理速度达 113.6 FPS。

---

### [GeoNLI - A Natural Language Interpreter for Satellite Imagery](https://arxiv.org/abs/2609.28741)
`检索` · Ashutosh Gandhe, Anupam Rawat, Geet Sethi et al.

构建模块化流水线 GeoNLI，结合 SAM 变体与多模态大模型，实现对卫星图像的标题生成、视觉问答和定位功能。为遥感图像的自然语言交互提供统一接口。

---

## Agent 与具身智能

### [PolyUMI: Accessible Visual-Tactile-Audio Data Collection for Object Inference and Manipulation](https://arxiv.org/abs/2609.29760)
`Agent` · Conor W. Hayes, Rickmer Krohn, Aravind Ramaswami et al. · [Code](https://github.com/polyumi/PolyUMI-platform)

开源多模态数据采集平台 PolyUMI，支持同步的视觉-触觉-音频演示数据收集。配合 VisTA 令牌级多模态策略，实现接触感知的机器人动作执行。

---

### [C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks](https://arxiv.org/abs/2609.29735)
`Agent` · Xueshu Chen, Yan Wang, Zihao Xue et al. · [Code](https://github.com/HuzhouNLP/C3M)

提出 C3M 跨会话多模态记忆维护方法，在持久文本-图像证据上维护有界活跃索引，通过关系感知更新和预算路由实现长时程任务中的高效记忆管理。

---

### [SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support](https://arxiv.org/abs/2609.29341)
`Agent` · Muhammad Muhtasim Shahriar, Abdullah Mohammad Sayem et al.

提出 SkinAgent AI 非诊断护肤支持框架，结合视觉关注路由与可审计 LLM 编排。通过确定性安全检查和追溯机制，实现 99.84% 的路由准确率。

---

### [Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction](https://arxiv.org/abs/2609.28467)
`Agent` · Zilin Fang, Zishuo Wang, Gim Hee Lee, David Hsu

研究语言引导的机器人群组加入问题，通过谱分割和多模态能量-方向预测实现目标群组判断。使机器人能够根据自然语言指令智能选择加入合适的人群。

---

### [Multimodal Voice Activity Projection for Social Robot Mediation](https://arxiv.org/abs/2609.28317)
`Agent` · Antonio Cano, Guillermo Perez, Luis Merino, Randy Gomez · [Code](https://github.com/acano15/MM-VAP)

提出 MM-VAP 方法，从视听证据中预测未来对话轮次分配，用于社交机器人的对话调解。已被 RO-MAN 2026 接收，支持社交机器人更自然地参与多人对话。

---

### [EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks](https://arxiv.org/abs/2609.28236)
`Agent` · Lizhou Liang, Xinyu Zhong, Miao Pan et al.

发布 EmbodiedMemory-Bench，包含 2,554 个情景的具身记忆基准。同时训练 EMem-8B 策略管理场景记忆，评估发现当前模型在四项记忆挑战上仍表现不足。

---

### [Learning What to Activate: Combinatorial Capability Allocation for Long-Horizon Multimodal Agents](https://arxiv.org/abs/2609.27869)
`Agent` · Wenhao Yuan, Chenchen Lin, Jian Chen et al.

提出 CoCA 框架，研究基于阶段依赖需求激活能力子集的组合优化方法。通过动态能力分配减少长时程多模态智能体的计算开销，提升任务执行效率。

---

### [EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory](https://arxiv.org/abs/2609.27279)
`Agent` · Xuanyu Meng, Xing Fan, Xinyi Fan et al. · [Code](https://github.com/RamonMeng/EnSIMem)

提出 EnSIMem 实体结构化长期记忆架构，以对话为基础的索引条目构建智能体持久记忆。通过实体维度的组织方式实现高效记忆检索和更新。

---

## 多模态生成

### [All Modalities Are Equal, but Video Is More Equal: Closing the Cross-Attention Gap in Joint Video Generation](https://arxiv.org/abs/2609.27901)
`生成` · Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik · [Code](https://github.com/ohad204/RecCAR/)

发现联合多模态扩散 Transformer 中跨模态对应关系的不对称性，提出 RecCAR（互惠跨模态注意力正则化）方法。将音视频不同步程度从 0.804 降低至 0.752，改善联合视频生成质量。

---

### [Spot, Separate, and Enhance: Fully Generative Approach for Audio Mixing](https://arxiv.org/abs/2609.29169)
`生成` · Ilpo Viertola, Giulio Cengarle, Gouthaman KV et al.

提出 SSE 多模态生成模型，支持视频和文本引导的音频混音。构建 DegradedMix 数据集，在可控性和混音质量上超越现有基线方法。投稿 ICASSP 2027。

---

## 音频多模态

### [Speech Block Influence: Component-Specific Layer Scoring for Pruning Speech LLMs](https://arxiv.org/abs/2609.29343)
`音频` · Siyu Yao, Du Q. Huynh, Lian Xu, Mark Reynolds · [Code](https://github.com/CU-0/sbi-speechllm-pruning)

提出 SBI 层重要性评分方法，通过组件特定的 SBI-Enc 和 SBI-Dec 指标提升语音大模型剪枝的鲁棒性。在三种语音 LLM 上验证有效，避免音频令牌主导问题。

---

### [Cross-Modal Emotion Understanding: A Transformer-GAT Approach for Dialogue Emotion Recognition](https://arxiv.org/abs/2609.29556)
`音频` · Jiaqi Qiao, Yifan Lyu, Xiujuan Xu

提出混合框架，结合 Transformer 捕获全局语义与图注意力网络建模细粒度跨模态关系。在对话情感识别任务上达到 72.45% 和 77.37% 的加权 F1 分数。

---

## 3D 视觉语言

### [SARFusion: Scene-Aware Routing Fusion for Robust Camera-LiDAR 3D Object Detection](https://arxiv.org/abs/2609.29235)
`3D` · Yuting Zhao, Ziyi Zheng, Shuxiao Li

将鲁棒融合重新定义为场景感知路由问题，设计并行相机、LiDAR 和融合分支架构。通过查询级路由在 nuScenes 上达到 72.5 mAP 和 74.4 NDS。

---

### [AstraLOD3: Zero-shot Multimodal Agentic Reconstruction of LOD3 Building Models](https://arxiv.org/abs/2609.28061)
`3D` · Bryan G. Pantoja-Rosero

利用 Astra 基础模型在智能体框架中实现零样本 LOD3 建筑重建。平均 FRDS 达到 0.9647，展示了多模态基础模型在精细建筑建模中的巨大潜力。

---

### [NV-Reason-CT: 3D Visual Language Model for CT Analysis](https://arxiv.org/abs/2609.27511)
`3D` · Andriy Myronenko, Dong Yang, Yucheng Tang et al. · [Code](https://github.com/NVIDIA-Medtech/NV-Reason-CT)

提出 NV-Reason-CT，结合 3D 视觉 Transformer 与语言模型用于胸部和腹部 CT 分析。在约 550,000 个多模态指令样本上训练，实现精准的 3D 医学影像理解。

---

## 统计

| 方向 | 论文数 | 有代码 |
|------|--------|--------|
| VLM / MLLM 核心 | 10 | 1 |
| 多模态理解与推理 | 6 | 1 |
| 多模态基准与评测 | 5 | 3 |
| 多模态检索与信息抽取 | 4 | 1 |
| Agent 与具身智能 | 8 | 5 |
| 多模态生成 | 2 | 1 |
| 音频多模态 | 2 | 1 |
| 3D 视觉语言 | 3 | 1 |
| **合计** | **32** (去重后实际 31，含跨方向论文) | **14** |

---

*自动生成 · QoderWork Arxiv 多模态论文追踪 · 2026-09-25*
