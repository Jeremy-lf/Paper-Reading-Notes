# Arxiv 多模态论文日报

**日期**：2026 年 8 月 5 日  
**收录论文**：37 篇　|　**含代码仓库**：8 篇　|　**覆盖方向**：8 个

---

## VLM / MLLM

### [UEmbed: Unified Sparse and Dense Multimodal Embeddings](https://arxiv.org/abs/2608.02583)

**作者**：Tingyu Song, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Zhijie Nie, Yilun Zhao, Shu Wu　|　**方向**：VLM / MLLM | [Code](https://github.com/Alibaba-NLP/UEmbed)

UEmbed 是一个解码器统一的多模态嵌入模型，可在单次因果前向传播中同时输出稀疏词项表示与稠密向量。通过可学习特殊 token 与分区词表生成稀疏向量，2B/4B/9B 模型在 MMEB-v2 和 BEIR 上取得了有竞争力的结果。

### [Douyin Multimodal Embedding Model Technical Report](https://arxiv.org/abs/2608.02148)

**作者**：Haonan Chen, Chu Li, Zhicheng Wang, Yuanwei Liu, Yuanjiang Wang, Shaohua Jiang, Zhicheng Dou　|　**方向**：VLM / MLLM

抖音多模态嵌入模型通过大规模对比预训练、隐式推理与跨条件重建，在提升细粒度判别能力的同时保持高效，在 MMEB-v2 和抖音业务场景均取得显著收益。

### [Two Sides of the Same Coin: Co-Evolving Search for Cross-Task Attacks on Vision-Language Models](https://arxiv.org/abs/2608.02137)

**作者**：Xuanhui Lin, Junhao Dong, Mingrong Gong, Yucheng Chen, Xinghua Qu, Yew-Soon Ong　|　**方向**：VLM / MLLM

该工作提出协同演化框架，同时搜索文本与视觉对抗空间：文本侧演化语义负嵌入，视觉侧演化局部图像扰动，从而提升对统一 VLM 的跨任务攻击迁移性。

### [Messages, Not Tokens: Grounded Coresets for Faithful VLM Compression](https://arxiv.org/abs/2608.02134)

**作者**：Long Qian, Jiaqi Wei, Bingke Zhu, Yingying Chen, Jinqiao Wang　|　**方向**：VLM / MLLM

Grounded Message Coreset Pruning 将视觉 token 剪枝建模为解码器消息的紧凑核心集构造，联合选择查询相关、外观与坐标感知证据的代表，显著减少 token 数量并保留能力。

### [ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs](https://arxiv.org/abs/2608.01979)

**作者**：Zizhong Ding, Junxian Li, Kai Liu, Shaoqiu Zhang, Xiao Xiao, Linghe Kong, Yulun Zhang　|　**方向**：VLM / MLLM | [Code](https://github.com/Labyrinth0419/ET-Prune)

ET-Prune 将视觉 token 剪枝视为面向问题的证据分配，保护文本样区域并根据证据不确定度与密度设定样本级 token 预算，在约一半 token 下提升 OCR 与通用基准表现。

### [Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models](https://arxiv.org/abs/2608.01849)

**作者**：Junxiang You, Junkai Chen, Yuhao He, Ruiqi Liu, Zhetao Guo, Shu Wu　|　**方向**：VLM / MLLM

该研究揭示已遗忘 MLLM 中存在“知识空洞”——与遗忘集相似的良性输入出现意外退化，并提出基于锚定正则化的选择性保护方法，在保持遗忘效果的同时保护通用模式。

### [Decoupling semantics from vision: A framework for faithful visual-text compression evaluation](https://arxiv.org/abs/2608.01848)

**作者**：Yonghan Gao, Zehong Chen, Lijian Xu, Jingzhi Chen, Jingwei Guan, Xingyu Zeng　|　**方向**：VLM / MLLM

作者指出下游任务准确率会因 MLLM 依赖语言先验而高估视觉-文本压缩质量，提出解耦评估框架与 ZeroSense Benchmark，以隔离压缩保真度与推理能力。

### [Illuminating Visual Identity in Universal Multimodal Embeddings](https://arxiv.org/abs/2608.01794)

**作者**：Jiawei Cao, Junyi Feng, Jiashen Hua, Ziheng Huang, Bing Deng, Kaijie Wu, Chaochen Gu, Jieping Ye　|　**方向**：VLM / MLLM

该工作指出视觉身份判别是通用多模态嵌入中尚未充分探索的能力，提出 MVEB 基准与身份感知采样框架，联合优化通用多模态表征与身份表征。

### [Allocation Before Ranking: Decoupled Token Compression for OmniLLMs](https://arxiv.org/abs/2608.01665)

**作者**：Zhenghui Guo, Yilin Yang, Yuanbin Man, Miao Yin, Weidong Shi, Rabimba Karanjai, Omprakash Gnawali, Chengming Zhang　|　**方向**：VLM / MLLM

该研究认为全模态大模型的 token 压缩应将模态间预算与模态内排序解耦，提出无需训练的压缩器，先为音频和视频分配显式预算，再在各模态内部排序 token。

### [Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning](https://arxiv.org/abs/2608.01635)

**作者**：Qianlong Yang, Bowen Ye, Xianda Guo, Yanlun Peng, Wenke Huang, Hongyuan Zhang, Yulei Jia　|　**方向**：VLM / MLLM

针对 MLLM 指令微调后的视觉感知退化，该工作在训练中注入吸收外部视觉基础模型知识的视觉锚点提示，并加入空间与频域对齐损失，已被 ACM MM 2026 接收。

### [Slot2Text: Object-Centric Visual Tokenization for Efficient and Spatially Traceable Surgical MLLMs](https://arxiv.org/abs/2608.01473)

**作者**：Guiqiu Liao, Matjaz Jogan, Daniel A. Hashimoto　|　**方向**：VLM / MLLM

Slot2Text 将手术 MLLM 的图像表示为紧凑的 slot 隐变量而非稠密 token，提供快速模式与可关联空间区域的 grounded 推理模式。

### [PixVL: Self-Supervised Training of Pixel-Level MLLMs via a Unified Mask--Text Consistency Cycle](https://arxiv.org/abs/2608.01354)

**作者**：Yicheng Xiao, Haoxuan Ma, Caorui Li, Yucheng Wu, Weijie Wang, Haoxiao Wang, Shuang Chen, Fan Yang, Haiyun Guo, Jinqiao Wang　|　**方向**：VLM / MLLM | [Code](https://github.com/StuHude/PixVL)

PixVL 提出面向像素级 MLLM 的自监督后训练框架，通过掩码-文本一致性循环、混淆感知语义验证与跨视角验证，提升区域理解与分割能力。

### [GeoArbiter: Verifiability-Guided Grounding for Remote-Sensing Multimodal LLMs](https://arxiv.org/abs/2608.00877)

**作者**：Xuechen Li　|　**方向**：VLM / MLLM

GeoArbiter 对注入遥感 MLLM 的地理记录进行跨模态可验证性过滤，保留图像无法验证的事实，提升准确率并减少与视觉证据冲突的幻觉。

### [Through the LENS: Local Geometric Decomposition of Vision-Language Model Representations](https://arxiv.org/abs/2608.00561)

**作者**：Shalom Kachko, Raz Lapid, Margarita Vald, Almog Dubin, Moshe Sipper　|　**方向**：VLM / MLLM

LENS 使用因子分析混合模型将 VLM 激活分解为局部低秩高斯邻域，揭示层间依赖的融合模式，并实现跨模态因果引导。

## 推理

### [AdaThinkV: Adaptive Thinking for Token-Efficient Video Reasoning](https://arxiv.org/abs/2608.01980)

**作者**：Jingqi Tian, Haoji Zhang, Lin Chen, Hongbo Jin, Haonan Xu, Tianrui Zhu, Xingming Shui, Shilin Ma, Wenjing Yang, Yansong Tang　|　**方向**：推理

AdaThinkV 让视频 MLLM 自适应选择显式推理或直接回答，通过匹配 rollout 采样与 Variance Recovery Policy Optimization 从困难样本中学习，在提升准确率的同时减少输出 token。

### [TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory](https://arxiv.org/abs/2608.01922)

**作者**：Kang Liu, Zijing Wang, Yongkang Liu, Mengjie Zhao, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang　|　**方向**：推理

TRAM 是一种无需训练的多模态推理增强方法，从模型自身推理轨迹构建辅助潜记忆通路，通过快慢循环流更新并压缩历史推理，再注入解码层提升数学、科学与通用视觉推理。

### [Remember-R1: Mitigating Long-Context Visual Forgetting through Reinforcement Learning](https://arxiv.org/abs/2608.01314)

**作者**：Jianmin Chen, Jiaqi Tang, Wei Wei, Xiaogang Xu, Jiafei Wu, Zhe Liu, Qianzhou Wang, Yingying Yan, Botong Geng, Yuyang Xia, Lei Zhang, Qifeng Chen　|　**方向**：推理 | [Code](https://github.com/Ch921-cell/Remember-R1)

Remember-R1 通过过程级强化学习缓解 MLLM 在长思维链中的视觉遗忘，奖励视觉关键词覆盖、持续视觉依赖与对关键图像区域的关注，已被 ACM Multimedia 2026 接收。

### [LUT: Latent Utility Training for Visual Reasoning](https://arxiv.org/abs/2608.00743)

**作者**：Jiaxuan Kang, Siyu Chen, Mingda Li, Mingjie Liu, Tianyue Wang, Zhaoyang Wei, Yongheng Zhang, Yanchao Hao, Zheng Wei　|　**方向**：推理

LUT 仅使用标准 VQA 监督训练潜在视觉推理，通过效用感知蒸馏选择可靠潜在轨迹，并在强化学习中通过答案到潜在的归因细化每个推理步骤。

## Agent

### [MoRAL: Sensor-Grounded BEV Reasoning for Compact VLMs toward Edge-Oriented Autonomous Driving](https://arxiv.org/abs/2608.02449)

**作者**：Ambarish Govindarajulu Kaliamurthi, Kaikai Liu　|　**方向**：Agent

MoRAL 将 Cosmos-Reason2-2B 微调为可读取物理编码 BEV 表征并进行驾驶决策推理的紧凑 VLM，可在 8GB GPU 上部署。在多数 nuScenes 问题类型上，该小模型超越了零样本 8B 基线。

### [Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation](https://arxiv.org/abs/2608.02257)

**作者**：Donglin Yang, Haoran Chen, Xingyu Chen, Lixing Liu, Manyi Li, Changhe Tu, Ke Xu, Xiaojian Ma, Si Liu　|　**方向**：Agent

该研究通过全身遥操作采集轮式双臂机器人的多模态演示数据，提出 PanoVLA 策略，通过全景编码与融合模块引入全景空间上下文，提升了真实场景移动操作性能。

### [VC-Tooler: Learning Compositional and Adaptive Visual Tool Use](https://arxiv.org/abs/2608.02217)

**作者**：Yizheng Wu, Jiashen Hua, Bing Deng, Jieping Ye　|　**方向**：Agent

VC-Tooler 构建覆盖单工具定位、多工具组合与多样化情境的视觉工具使用轨迹库，采用监督学习与强化学习两阶段训练，在通用基准与 Agent 基准上达到先进水平。

### [DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal Agents](https://arxiv.org/abs/2608.01827)

**作者**：Huanyao Zhang, Jiepeng Zhou, Runhao Zhao, Yanzhe Shan, Jiaoyang Chen, Bowen Zhou, Bo Li, Fang Wang, Jialong Wu, Zhengwei Tao, Lang Mei, Xiaohan Yu, Liyan Liu, Chong Chen, Wentao Zhang　|　**方向**：Agent

DeepVoyager-VL 是一个长程多模态深度搜索框架，视觉证据驱动中间检索；通过构建多模态事件图进行数据合成，并设计主动视觉获取智能体。

### [Long-Horizon Embodied Decision-Making via Multimodal Memory Compression](https://arxiv.org/abs/2608.01456)

**作者**：Bingxuan Li, Rui Yang, Cheng Qian, Jiateng Liu, Jeonghwan Kim, Zhenhailong Wang, Manling Li, Tong Zhang, Heng Ji　|　**方向**：Agent

该研究提出一个基于人类偏好的长程具身决策基准，以及一个多模态记忆压缩器，在大幅提升智能体准确率的同时显著降低记忆开销。

### [PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents](https://arxiv.org/abs/2608.00962)

**作者**：Jingyu Sun, Yan Lin, Yuyang Xue, Yifan Wang, Zhengtao Yao, Rui Qian, Zefeng Xu, Jiachen Li, Xianyang Liu, Jiancheng Pan, Jingyuan Sun, Syed Murtuza Baker, Hongpeng Zhou　|　**方向**：Agent

PMMC 为长期 LVLM Agent 设计前瞻性多模态记忆编译机制，将部分推理工作从查询时前移到整合时：预测可能问题、构建多模态证据程序、验证并结构化存储以加速检索。

### [Models as Tools: An Agentic Coordination Framework for Unified Multimodal Visual Tracking](https://arxiv.org/abs/2608.00847)

**作者**：Wenrui Cai, Yuzhe Li, Qingjie Liu, Yunhong Wang　|　**方向**：Agent

ACTrack 将专用模型作为事件触发工具用于统一多模态视觉跟踪，协调实例匹配、SAM3 运动感知模块与 VLM 重提示工具，以更少可训练参数实现强劲性能。

### [DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable](https://arxiv.org/abs/2608.00548)

**作者**：Pu Cao, Qingye Kong, Xuedan Yin, Xuekun Zhao, Rupeng Yan, Qing Song, Yao Zhang, Lu Yang　|　**方向**：Agent

DrawAI 提供将光栅图像转换为可编辑结构化图形的基准与 Agentic 工作流，解析器规划重建，重建智能体迭代生成图形代码。

### [DiffuseAgent-MI: Distributionally-Grounded, Tool-Integrated Self-Evolving Agents for Faithful Visual Reasoning](https://arxiv.org/abs/2608.00540)

**作者**：An Lanji, Dawei Liu, Jin Li, Haoran Xu, Mei Chen, Yu Tian　|　**方向**：Agent

DiffuseAgent-MI 通过 KL 极小能量模型与轨迹级奖励提升工具集成视觉语言推理的忠实度，并对标记为不忠实的步骤进行修复重条件化。

## 基准

### [CAPEval: A Decoupled Caption Evaluation across Understanding and Generation](https://arxiv.org/abs/2608.02589)

**作者**：Zhipeng Liu, Haochen Wang, Zhaoxiang Zhang　|　**方向**：基准

CAPEval 将图像描述质量解耦为 Coverage（覆盖度）和 Precision（精确度）两个指标，分别衡量描述对视觉事实的覆盖程度与陈述的正确率。实验发现 Coverage 更能预测下游理解任务表现，而 Precision 对文本到图像生成任务的预测力更强。

### [MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing](https://arxiv.org/abs/2608.02059)

**作者**：Zitong Xu, Huiyu Duan, Xinyun Zhang, Weifei Xiong, Tianyi Zheng, Xiongkuo Min, Qiang Hu, Zhengxue Cheng, Bo Li, Guangtao Zhai　|　**方向**：基准 | [Code](https://github.com/IntMeGroup/MIEScore)

MIE-Bench 是一个大规模多源图像编辑基准，含人工标注与 12 个模型的输出；MIEScore 是基于 MLLM 的评估器，通过技能优化与监督微调对齐人类偏好。

### [SVGEval: A Vision-Grounded Framework for Perceptual-Quality Benchmarking and Evaluation in Text-to-SVG Generation](https://arxiv.org/abs/2608.01977)

**作者**：Yiming Wang, Ye Chen, Hanqi Chen, Bingbing Ni　|　**方向**：基准

SVGEval 是一个面向文本到 SVG 生成的感知质量基准，利用渲染图像与专家精炼的人工标注训练可解释的 SVG 质量评分器，输出多维度分数与理由。

### [LongChart VQA: A Comprehensive Benchmark for MLLMs with Complex Multi-Chart Reasoning](https://arxiv.org/abs/2608.01328)

**作者**：Ziyan Xiao, Yinghao Zhu, Wenting Zhang, Heaju Kim, Lequan Yu　|　**方向**：基准

LongChart VQA 是一个面向复杂多图表视觉问答的综合基准，评估模型在推理模式、工具使用以及对图像扰动的鲁棒性等方面的表现。

## 生成

### [PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diversity with Editable Print-Ready Outputs](https://arxiv.org/abs/2608.02218)

**作者**：Haojie Hu, Chenhao Dang, Yaojia Liu, Hengrui Kang, Conghui He, Weijia Li　|　**方向**：生成 | [Code](https://github.com/Shannon4Science/PosterMELD)

PosterMELD 是一个基于模板的多智能体论文转海报生成框架，可将多模态论文压缩为可编辑海报并导出 PPTX/PNG，实现了高印刷就绪率与低成本。

### [CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942)

**作者**：Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu　|　**方向**：生成

CultureVidBench 包含覆盖 12 个国家、多个文化维度的 1000 个提示，用于评估文本到视频模型的文化理解能力，强调仪式、社交互动以及文化适配的文本与音频等多模态动态表达。

### [EchoChange: A Diffusion Language Model with Dual Pass Remasking for Factual Remote Sensing Disaster Change Captioning](https://arxiv.org/abs/2608.01856)

**作者**：Dongwei Sun, Bowen Yao, Yujie Zhang, Pei Liu, Jing Yao, Xiangyong Cao　|　**方向**：生成 | [Code](https://github.com/sundongwei/EchoChange_Project)

EchoChange 将遥感灾害变化描述生成形式化为迭代掩码 token 去噪，而非自左向右生成，从而能够修正不确定内容与中间错误预测，提升双时相遥感灾害图像的描述事实性。

## 检索

### [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](https://arxiv.org/abs/2608.01543)

**作者**：Dingyi Kang, Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li　|　**方向**：检索 | [Code](https://github.com/Dingyi-Kang/V-Mem)

V-Mem 是一种面向长期多模态 Agent 记忆的模态路由检索系统，按查询与证据模态组织对话轮次，并利用 LLM 生成的锚点弥合模态与相关性鸿沟。

## 音频

### [Hear, Invoke, and Understand: A Skill-Calling Multimodal Agent for Large Audio Language Models](https://arxiv.org/abs/2608.01881)

**作者**：Yuwen Wang, Tian-Hao Zhang, Minghao Cai, Yilin Ren, Ziyang Jiang, Xin Wang, Zhichao Wang, Pan Zhou, Kun Zhan, Xinyuan Qian　|　**方向**：音频

SpeechAgent-R 是一个能够调用工具进行交互式音频推理的音频智能体，基于 HIU-Corpus 训练并在 HIU-Bench 上验证了分布内与分布外任务的强劲表现。

## 3D

### [Multimodal Embeddings for 3D Similarity Search in Semantic Web-of-Things Digital-Twin Platforms](https://arxiv.org/abs/2608.01852)

**作者**：Oussama Zaid, Romaric Gaudel, Hassan Thomas, Maria Massri, Philippe Raipin-Parvédy　|　**方向**：3D

该框架为语义 Web of Things 平台扩展多模态嵌入层，将 3D 点云、时序属性与语义标签编码为潜在向量，在 Thing'in 平台上实现混合本体-向量查询。

---

**论文总数统计**：本报告共收录 37 篇多模态相关论文，其中 8 篇提供 GitHub 代码仓库，涵盖 8 个研究方向。

*自动生成于 2026-08-05 · QoderWork Arxiv 多模态论文追踪*
