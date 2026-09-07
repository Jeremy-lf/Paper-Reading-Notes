# Arxiv 多模态论文日报 · 2026-09-07

**统计**：收录论文 28 篇，含代码仓库 7 篇，覆盖方向 7 个。

> 本报告基于 Arxiv 2026 年 9 月 3–4 日提交的多模态相关论文整理，报告生成日期：2026-09-07。

## VLM / MLLM

### [Whose record is this? Diagnosing and authorizing record use in personalized multimodal models](https://arxiv.org/abs/2609.04801)

**作者**：Xinyu Mao, Junsi Li, Chenyang Liu, Haoji Zhang, Ming Sun｜**方向**：VLM / MLLM｜**代码**：暂无

形式化视觉个性化中的记录授权问题，提出记录授权需同时满足主体存在、记录-边有效与答案支持三个条件，并将违规称为视觉记忆错绑（VMM）。构建 3,690 例诊断套件 RecordAuth-Diag，发现 Gemma-3-4B-IT 等接口存在高达 63.69% 的未授权使用，并提出生成前类型化授权将 Qwen 的卡片暴露率从 43.63% 降至 3.06%。

## 多模态理解与推理

### [SMILE: Self-Explainable Multimodal Information Bottleneck for Medical Diagnosis](https://arxiv.org/abs/2609.05174)

**作者**：Yuqing Yang, Alexander Schmatz, Zhaozhao Ma, Changkyu Choi, Robert Jenssen, Shujian Yu｜**方向**：推理｜**代码**：暂无

将自解释多模态医学诊断形式化为信息瓶颈（IB）问题，联合优化预测性能与各模态可解释性，识别对诊断决策最有信息量的模态内元素。在跨模态医学数据集上取得强劲诊断性能，其中 iCTCF 数据集准确率绝对提升 9.1 个百分点，同时提供透明、模态感知的特征相关性解释。

### [From Vision to Language: Investigating Causal Information Flow in Multimodal Decision-Making](https://arxiv.org/abs/2609.05149)

**作者**：Davide Testa, Hugh Mee Wong, Alessandro Lenci, Bernardo Magnini, Albert Gatt｜**方向**：推理｜**代码**：暂无

在视频多选推理任务中对视频-文本注意力通路进行逐层因果干预，追踪视觉信息如何影响基于语言决策。发现视觉信息主要在模型处理候选答案选项时融入，名词作为语义锚点而动词对时序关系处理更重要，并揭示 VLMs 在跨帧重建序列信息时的脆弱性。

### [Scales, Reflections, and Conversations: A Multi-Modal Approach to Emotion Annotation](https://arxiv.org/abs/2609.05046)

**作者**：Pragya Singh, Prashasti Gupta, Hitesh Bhandari, Kanishk Goel, Mohan Kumar, Pushpendra Singh｜**方向**：推理｜**代码**：暂无

提出一种以参与者为中心的多模态情绪标注应用，根据用户情绪强度与可用性动态调整标注方式。可行性研究表明多模态情绪记录能够塑造参与者体验与数据记录行为，有助于收集更丰富、更细腻的日常情绪数据。

### [MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression](https://arxiv.org/abs/2609.04947)

**作者**：Guangheng Yang, Zhenliang Ni, Zhenkai Wu, Han Shu, Juan Feng, Wenming Yang, Jie Hu｜**方向**：推理｜**代码**：暂无

提出 Modality-Contrastive Preference Optimization（MCPO），一种样本高效的两阶段多模态思维链压缩方法。通过步骤级归一化跨模态互信息剪枝去除视觉无关推理步骤，再使用非对称多模态长度受控偏好损失进行对齐，在 Qwen3-VL-Thinking 等模型上实现最高 69.5% 的 CoT 长度压缩与 3.34 倍端到端推理加速，同时保持原始准确率。

### [Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion](https://arxiv.org/abs/2609.04690)

**作者**：Xu Lin, Ke Wang, Hui Kang, Xinying Wang｜**方向**：推理｜**代码**：暂无

提出新的多模态情绪识别框架，对音频提取 Wav2Vec2 语义嵌入、MFCC 与统计声学描述子并通过 BiLSTM 融合，对视频使用 ResNet50-BiLSTM 提取面部时空特征。进一步引入基于多头注意力的特征级融合机制，在 MELD 与 IEMOCAP 数据集上显著优于基线，并提升非平衡数据下的性能。

### [Latent-Aligned Reasoning for Multimodal Recommendation](https://arxiv.org/abs/2609.04645)

**作者**：Jiarui Jin, Anyang Ji｜**方向**：推理｜**代码**：暂无

提出 LARK（Latent-Aligned Reasoning frameworK）两阶段潜在推理框架，解决推荐中视觉与文本信号在多步推理中逐渐衰减的跨模态稀释问题。第一阶段用可学习潜在 token 与冻结视觉编码器对齐作为视觉检查点，第二阶段通过桥接 MLP 与项目间对比学习保持推理语义，在三个公开基准与一个工业数据集上达到最优。

### [Explainable Multimodal Deep Learning Integrating Imaging and Clinical Data for Oral Potentially Malignant Disorder Detection](https://arxiv.org/abs/2609.04512)

**作者**：Ruilin You, Yihan Wang, Jiabin Chen, Cherie Wink, Petra Wilder-Smith, Rongguang Liang, Bofan Song｜**方向**：推理｜**代码**：暂无

开发 M2-OPMDNet，一种可解释的多模态深度学习框架，将配准的白光与自体荧光口腔图像与结构化临床信息融合，用于口腔潜在恶性疾病（OPMD）检测。通过 SHAP 量化特征与模态级贡献，AUC 达到 0.952，优于单模态方法，并对视觉不明显的病灶表现出提升性能。

### [BioSync: Transformer-Based Cross-Modal Fusion for a Multimodal Physiological Digital Biomarker](https://arxiv.org/abs/2609.04504)

**作者**：Seyed Mahmoud Sajjadi Mohammadabadi｜**方向**：推理｜**代码**：暂无

提出 BioSync，将心脏、神经、行为与语音信号通过跨模态注意力融合为连续复合生理数字生物标志物 BioSync Index（BSI）。在认知衰退与代谢-自主神经两个合成队列上验证，宽深混合架构在模态缺失等损坏设置下表现优于拼接、早融合与晚融合基线。

### [Corporate Language Model (CLM): Transforming Tacit and Fragmented Enterprise Knowledge into a Sovereign, Auditable, and Executable Corporate Intelligence Layer](https://arxiv.org/abs/2609.04377)

**作者**：Fabricio C. Avini, Guilherme Trez｜**方向**：推理｜**代码**：暂无

提出 Corporate Language Model（CLM）框架，将企业结构化、非结构化、多模态与隐性知识转化为本体锚定的企业智能层。通过神经符号网格、技能图、数字孪生与深层安全层的四维架构，支持可解释、可审计且可执行的推理与治理，并在巴西一家 JCI 认证医院中实例化部分成熟度阶段。

### [Cross-modal triage network: a multimodal deep learning framework for severity-based triage and visual explainability in chest radiographs](https://arxiv.org/abs/2609.04357)

**作者**：Zinah Ghulam, Richa Mittal, Eranga Ukwatta｜**方向**：推理｜**代码**：暂无

提出 Cross-Modal Triage Network（CMTN），通过门控交叉注意力融合 Swin Transformer V2 视觉编码器与 PubMedBERT 文本编码器，实现胸部 X 光片严重程度分诊、病理检测与原生可视化解释。在 MIMIC-CXR-JPG 上取得 QWK 0.9341 与 14 种病理宏观 AUROC 0.9970，但临床审计显示与真实放射科医生判断仍有显著差距。

### [Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding](https://arxiv.org/abs/2609.04131)

**作者**：Hongyu Qu, Guangming Yao, Ling Xing, Xiaobin Hu, Rongxing Ding, Guibin Zhang, Fan Zhang, Yi Yuan, Xiangbo Shu, Shuicheng Yan｜**方向**：推理｜**代码**：暂无

提出 LatentStream，一种将流式视频理解记忆从“存储-检索”转变为“检索-内化”的渐进潜在工作记忆框架。通过查询无关的分层流式记忆、分层潜在记忆演化与渐进置信度引导的潜在记忆优化，在现有在线与离线视频基准上取得新的最优结果。

## 多模态基准与评测

### [SciDocBench: A Workflow-Centered Benchmark and Data Pipeline for Scientific Document Understanding](https://arxiv.org/abs/2609.05141)

**作者**：Shenxi Wu, Yuhong Liu, Haosong Zhang, Tongjin Zou, Yanxun Zhang, Gaochang Chen, Dun Liang, Jiaqi Wang, Zhecan James Wang, Yuhang Zang, Dahua Lin｜**方向**：基准｜**代码**：[Code](https://github.com/InternLM/SciDocBench)

推出 SciDocBench，一个以工作流为中心的科学文档理解基准，包含 124 道专家编写、难度筛选的问题，覆盖七个研究助手能力组与 19 个子任务。同时提出类型化证据图表示 SciDocIR 与约 15K SFT、8K RL 样本的 SciDocDataset，形成从评测到训练的科学文档助手改进框架。

### [MM-IFEval-Pro: A Multilingual and Attack-Resistant Benchmark for Instruction-Following in Vision-Language Models](https://arxiv.org/abs/2609.04859)

**作者**：Changming Xiao, Zhenliang Ni, Jinhui He, Han Shu, Jie Hu｜**方向**：基准｜**代码**：暂无

提出 MM-IFEval-Pro，一个覆盖中英文与多种指令劫持场景的多模态指令遵循基准，包含 4 大任务类别、24 子类别、8 种指令类型与 52 子类别。构建的强化学习训练集显著提升了模型在 MM-IFEval-Pro 及其他主流多模态基准上的表现，展现出强的跨任务与跨语言泛化能力。

### [MMTClinic: Multimodal, Multilingual Time Series Question Answering and Reasoning Benchmark for Clinical Domain](https://arxiv.org/abs/2609.04842)

**作者**：Sourav Malakar, Harshit Nigam, Akash Ghosh, Sriparna Saha, Amlan Chakrabarti, Saptarsi Goswami, Priti Singh｜**方向**：基准｜**代码**：[Code](https://github.com/rakhujoy/MMTClinic)

推出 MMTClinic，首个面向临床领域的多模态、多语言时间序列问答与推理基准，融合文本、医学影像与多变量生理信号。包含 30,000 个 QA 对，覆盖英语、印地语、孟加拉语、马拉地语与泰米尔语，评估 13 个 SOTA LLM 在死亡率预测、心率预测与 SOFA 评分估计等任务上的表现。

### [PetQA: Benchmarking Veterinary Knowledge and Clinical Reasoning](https://arxiv.org/abs/2609.04598)

**作者**：Taegyun Kim, Youngwook Ham, Jungwook Rhim, Ju-Hyun An, Sungkyu Park, Kunwoo Park｜**方向**：基准｜**代码**：[Code](https://github.com/ssu-humane/PetQA)

推出 PetQA，一个韩语长式问答基准，用于评估大语言模型与大视觉语言模型在兽医知识与临床推理方面的能力。包含 10,076 个纯文本与 8,751 个多模态 QA 对，来自真实猫狗临床问题，并在零样本、RAG 与 SFT 设置下对 18 个模型进行全面评测。

### [VISTA: Dense Multi-Label Classroom Coding with Vision-Language Models](https://arxiv.org/abs/2609.04550)

**作者**：Andrew Franck, Brendan Ng, Ben Fitzgerald, Zane Derrod, Chris Cianci, Chris Craney｜**方向**：基准｜**代码**：[Code](https://github.com/ajfranck/VISTA)

将具有十年可靠性文献的课堂观察协议 COPUS 重新设计为多模态基础模型的视频基准，提供每 2 分钟 24 维二进制标签的密集结构化标注。提出 VISTA 基线，在 MiniCPM-V-4.5 上通过轻量 MLP 头精炼滑动窗口输出，在三段化学讲座上达到 80.1% 的限制宏准确率。

### [ICM-Bench: Person-Level Identity Reasoning in Multimodal Agents with Long-Term Memory](https://arxiv.org/abs/2609.04438)

**作者**：Shidu Ren, Yunze Liu, Xing Liu, Chi-Hao Wu, Enmin Zhou, Junxiao Shen｜**方向**：基准｜**代码**：[Code](https://github.com/Shidu-Ren/ICM-Bench)

推出 ICM-Bench，首个针对长视频记忆中身份中心推理的多模态智能体基准。包含 839 个合成片段、141 分钟视频与 1,217 个开放性问题，围绕六个反复出现的成年人构建一年生活相册。实验显示 Gemini 3.1 Pro 总体准确率达 74.0%，但依赖长期身份档案的问题得分降至 60.3%。

## 多模态检索与信息抽取

### [Beyond Maintenance Manual Multimodal RAG: Suggesting What Tool](https://arxiv.org/abs/2609.05116)

**作者**：Seongjun Ha, Md Rashedul Islam｜**方向**：检索｜**代码**：暂无

将多模态检索增强生成（MRAG）扩展到飞机维修场景，提出 MRAG-SWAT，在检索维修程序与配图的同时返回所需的手动工具与特殊工具。在 Lycoming IO-360-N1A 发动机上针对八个查询进行演示，有望减少往返工具库次数并防止因工具选择不当造成的飞机损伤。

### [SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for E-commerce](https://arxiv.org/abs/2609.04961)

**作者**：Hui Zhou, Jian Hui Ji, Lei Ma, Rong Xiao, Xiaoyi Zeng｜**方向**：检索｜**代码**：暂无

提出 SAM-D2Q，面向电商搜索的业务对齐多模态文档扩展框架，通过任务适配的多模态 SFT、多模态数据增强与基于 RL 的搜索业务目标偏好对齐，生成更符合用户意图与商业价值的伪查询。在 AliExpress 生产搜索系统部署后，GMV 提升 3.38%，支付笔数提升 2.27%。

### [MURAL: Multimodal Uncertainty-aware Recommendation via Adaptive edge Learning](https://arxiv.org/abs/2609.04574)

**作者**：Ahmad Mousavi, Majid Alikhani, Yeon-Chang Lee, Roberto Corizzo, Yeganeh Abdollahinejad｜**方向**：检索｜**代码**：暂无

提出 MURAL，将多模态推荐从固定结构增强转向动态拓扑发现。自适应边学习器结合可微检索与近似最近邻搜索发现潜在项目-项目关联，不确定性感知融合模块建模异构模态的偶然不确定性，在 TikTok 与 Amazon 等大型基准上显著优于结构与生成式 SOTA。

## Agent 与具身智能

### [Temporal Tactile Encoding and Compliance for Intent-Aware Robot-to-Human Bimanual Handover](https://arxiv.org/abs/2609.05282)

**作者**：Pasquale Marra, Stefano Berti, Gabriele Mario Caddeo, Lorenzo Natale｜**方向**：Agent｜**代码**：暂无

将人机交接视为本质上的多模态任务，把 VLA 模型与顺应控制器相结合，利用 RGB 观测、时序编码的触觉反馈和本体感觉对人体演示进行微调。在人类受试研究中验证了触觉时序编码与顺应控制互补，能显著提升交接的可靠性与舒适度。

### [First Things First: Teaching LLM-Based Agents to Prioritize Must-Haves before Nice-to-Haves](https://arxiv.org/abs/2609.05224)

**作者**：Tianjie Ju, Xinyue Xu, Wanxuan Sun, Lingxiao Diao, Gongshen Liu, Zhuosheng Zhang, Cheng Yang｜**方向**：Agent｜**代码**：[Code](https://github.com/claire62/FTF-RL)

针对多模态智能体在满足复杂结构化需求时的灾难性失败，提出 FTF-rl（First Things First Reinforcement Learning），显式优化对多优先级用户需求的推理。在 3,649 个电商、预订、地图/打车等场景问题上显著提高了任务成功率，并泛化到 LogicVista、MathVision 等推理基准。

### [MIVAIS: A Study Environment for Multi-Agent Mixed-Initiative Visual Analytics Applications](https://arxiv.org/abs/2609.04983)

**作者**：Tobias Stähle, Simon Schneider, Rita Sevastjanova, Mennatallah El-Assady｜**方向**：Agent｜**代码**：暂无

提出 MIVAIS 双层研究平台，下层基础设施标准化人与软件智能体之间的交互、状态同步与通信，上层声明式研究环境自动记录应用状态、屏幕、音频等多模态遥测数据。通过复现三个前沿系统并开展专家案例研究，证明其能降低混合主动可视化系统的原型与评估门槛。

### [Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges](https://arxiv.org/abs/2609.04778)

**作者**：Chenqi Li, Minghui Min, Dusit Niyato, Wei Ni｜**方向**：Agent｜**代码**：暂无

综述扩散语言模型（DLM）在移动边缘智能体中的应用潜力，分析其在延迟、内存、能耗、带宽、隐私与可靠性约束下的适用性。涵盖资源高效架构、训练与推理加速、边云部署、物联网/无线应用及评估方法，并讨论长上下文状态管理、可信执行与多模态接地等开放问题。

### [Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI](https://arxiv.org/abs/2609.04552)

**作者**：Amarjot Singh, Tanmay R. Pancholi, Jainam Kothari, Shrirang Mahajan, Ketan Bansal, Zackory Erickson, Giuseppe Loianno, Alexandre M. Bayen, Jeff Schneider, Vince Nakayama｜**方向**：Agent｜**代码**：暂无

提出 Continual Field-Adaptive Models（CFAM），通过互补学习架构实现少量样本实验室内学习与部署后无梯度、设备端持续学习。在机械臂、四足、人形、四旋翼和越野车五种形态上验证，仅用 40% 数据即可达到标准策略性能，并在验证的近 OOD 案例上提升动作成功率 13.9 个百分点。

## 多模态生成

### [WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing](https://arxiv.org/abs/2609.05171)

**作者**：Hui Zhang, Zongkai Liu, Liqiang Niu, Juntao Liu, Han Li, Zhen Cao, Wenchao Chen, Chengduo Zhao, Fandong Meng｜**方向**：生成｜**代码**：暂无

提出 WeAgent-MMGenEdit 全栈方案，包括多模态运行环境 WeAgent-Harness、可扩展数据构建流程、双语基准 WeBench-MMGenEdit 以及针对智能体策略与图像后端的 SFT 与 RL 后训练。通过持久化证据管理与专用验证/整合工具组织检索到的多模态证据，使 30B 总参数/3B 活跃参数的策略逼近 1T 参数智能体性能。

## 3D 视觉语言

### [Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States](https://arxiv.org/abs/2609.04196)

**作者**：Kang Liao, Yihang Luo, Xiao-Ming Wu, Linyi Jin, Size Wu, Chunyu Lin, Yao Zhao, Fei Wang, Wei Li, Chen Change Loy｜**方向**：3D｜**代码**：[Code](https://github.com/KangLiao929/Puffin)

提出 Puffin-World，一种统一多模态架构，原生整合物理理解、空间模拟与 3D 世界生成/重建。通过联合建模物理（重力场、纬度）、几何（深度）与外观（图像）三种世界状态，并引入 Omni-Camera 统一表示与物理动力学传播策略，构建 Puffin-16M 数据集，已发布代码、模型与数据。

---

**论文总数**：28 篇｜**含代码**：7 篇｜**覆盖方向**：7 个

*生成于 2026-09-07 · QoderWork Arxiv 多模态论文追踪*