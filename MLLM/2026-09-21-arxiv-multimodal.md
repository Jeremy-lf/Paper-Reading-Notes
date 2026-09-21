# Arxiv 多模态论文日报 — 2026-09-21

> 收录范围：VLM/MLLM、多模态感知、理解与推理、多模态生成、基准评测、检索与信息抽取、Agent与具身智能、音频多模态、3D视觉语言等方向  
> 论文总数：**35 篇** | 开源代码：**9 篇**

---

## VLM/MLLM 理解与推理

### [DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning](https://arxiv.org/abs/2609.21675)

**作者：** Wan Xu, Yuanfan Guo, Kevin Han, LaLa Chen, Wangmeng Zuo  
**方向：** `VLM推理` | **ArXiv ID：** `2609.21675` | **[Code](https://github.com/HIT-leaderone/DRT)**

提出"密集推理轨迹"（DRT）范式，突破传统Chain-of-Thought仅依赖自然语言表达的局限。DRT通过结构化推理路径实现5.5倍的token效率提升，并在多个基准上比Qwen3-VL基线提升+1.3准确率，为多模态推理提供了更高效且可追溯的新方案。

---

### [From Retrieval to Recognition: How Vision-Language Models Become OCR Specialists](https://arxiv.org/abs/2609.21543)

**作者：** Yuanxiang Huangfu, Hanmeng Zhong, Linqing Chen, Jeffrey Tiong Jee Hui  
**方向：** `VLM分析` | **ArXiv ID：** `2609.21543`

研究通用视觉语言模型如何习得专业OCR能力。发现模型通过复用文本检索/复制头部形成新的"阅读回路"，全序列OCR本质上是密集序列式多模态"复制粘贴"过程。揭示了VLM能力涌现的内在机制。

---

### [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

**作者：** DeepSeek-AI et al.  
**方向：** `多模态MoE` | **ArXiv ID：** `2609.19969`

DeepSeek发布552B参数的多模态MoE模型，通过CSA2和FP4 KV缓存技术将全局KV缓存压缩至每token仅890字节（约为DeepSeek-V4-Flash的1/4），在保持性能的同时大幅降低推理成本，推动多模态大模型在资源受限场景下的部署。

---

### [QCPruner: Query-Conditioned Population Coverage for Visual Token Pruning](https://arxiv.org/abs/2609.19990)

**作者：** Shengli He, Yongchao Liang, Roumeng He, Junjie Zeng et al.  
**方向：** `VLM加速` | **ArXiv ID：** `2609.19990`

提出免训练的查询条件视觉token剪枝方法，在LLaVA-1.5-7B上仅保留576个token中的32个即可维持96.1%的未剪枝性能，具有(1-1/e)贪心保证的理论下界，大幅降低多模态模型推理开销。

---

### [Semantic-Spatial Agreement Verification for Mitigating Object Hallucination in MLLMs](https://arxiv.org/abs/2609.17269)

**作者：** Ziheng Ren, Qian Gao, Jun Fan, Guohui Ding et al.  
**方向：** `幻觉缓解` | **ArXiv ID：** `2609.17269`

提出免训练的SSAV方法，通过语义-空间一致性验证缓解多模态大模型的目标幻觉问题。在COCO/A-OKVQA/GQA上准确率提升1.81-3.17分，CHAIRs指标从49.40%降至32.80%，有效减少模型"凭空捏造"目标的倾向。

---

### [Anchoring What Matters: Dual-Level Learning for Visually-Grounded Multimodal Reasoning (PIVOT)](https://arxiv.org/abs/2609.18057)

**作者：** Xinxin Song, Siyuan Li, Tingxiong Xiao, Jinli Suo  
**方向：** `视觉定位推理` | **ArXiv ID：** `2609.18057`

提出PIVOT框架，结合自校准经验回放和视觉引导优势分配，在可验证奖励的强化学习中提升大型视觉语言模型的视觉定位推理能力。通过双层学习策略让模型更好地"锚定"图像中的关键区域。

---

### [Lens: Bringing the Right Semantic Perspective into Focus for Training-Free Multimodal Representation Learning](https://arxiv.org/abs/2609.20252)

**作者：** Xinran Liu, Shouqian Shi, Yixian Chen et al.  
**方向：** `多模态表征` | **ArXiv ID：** `2609.20252`

提出免训练框架Lens，在36个MMEB数据集上达到63.9的Precision@1，超越最近基线10.2分。通过动态聚焦正确的语义视角，无需额外训练即可提升多模态表征学习能力。

---

### [From Models to Systems: A Comprehensive Survey of Efficient Multimodal Learning](https://arxiv.org/abs/2609.19445)

**作者：** Pan Wang, Siwei Song, Hui Ji et al.  
**方向：** `综述` | **ArXiv ID：** `2609.19445` | **[Code](https://github.com/pwang322/Efficient-Multimodal-Learning-Survey)**

系统性综述，覆盖300+篇工作，从模型、算法、系统三个层面梳理高效多模态学习的研究进展，并以多模态大语言模型为案例深入分析。为理解该领域全貌提供了宝贵的参考框架。

---

## 多模态基准评测

### [AgentVidBench: A Multi-Hop Video Question Answering Benchmark for Evaluating MLLM Agents](https://arxiv.org/abs/2609.21386)

**作者：** Seoyeon An, Hyeonseo Jang, Minsu Kim, Chanho Lee et al.  
**方向：** `视频QA评测` | **ArXiv ID：** `2609.21386` | **[Code](https://github.com/krafton-ai/agentvidbench)**

提出多跳视频问答基准，评估MLLM Agent的空间、时间和因果推理能力。在12个MLLM上的实验表明，单轮推理性能仍然有限，揭示了当前模型在多步视频理解方面的显著差距。

---

### [MME-Safety: A Fine-grained Benchmark for Safety Evaluation of MLLMs](https://arxiv.org/abs/2609.20850)

**作者：** Yueming Lyu, Yilian Shi, Haoxiang Tan et al.  
**方向：** `安全评测` | **ArXiv ID：** `2609.20850`

面向17个最先进MLLM的安全性细粒度评测基准，采用独特的四维标注模式，通过分层框架评估响应可靠性、风险暴露和防御行为完整性，填补了多模态安全系统性评估的空白。

---

### [PolyBridgeBench: Benchmarking Multimodal LLMs for Physics-Grounded Bridge Design](https://arxiv.org/abs/2609.21493)

**作者：** Zicheng Zhao, Dongyin Chen, Rui Xu, Yinghui Xu  
**方向：** `工程评测` | **ArXiv ID：** `2609.21493`

面向物理约束桥梁设计的多模态LLM可执行基准，覆盖189个难度级别。揭示了确定性有效性与动态成功率之间的差距，以及模型在失败后恢复能力的不足。

---

### [Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction](https://arxiv.org/abs/2609.21392)

**作者：** Qi Chen, Yunfei Chu, Haolin He et al.  
**方向：** `意图理解评测` | **ArXiv ID：** `2609.21392`

面向自然音视频交互场景的基准，测试模型从复杂多模态交互中正确推断用户潜在需求的能力。随着AI助手向多模态交互演进，该基准填补了用户意图理解评估的空白。

---

### [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](https://arxiv.org/abs/2609.17248)

**作者：** Zhaoyang Wei, Zipeng Wang, Yushe Cao et al.  
**方向：** `音视频推理评测` | **ArXiv ID：** `2609.17248`

面向长视频中深度音视频耦合推理能力的基准，要求模型提供时空证据支撑的推理链。即使是最强的商业模型准确率也低于60%，凸显了音视频联合推理的巨大挑战。

---

### [A Unified Evaluation Framework for Trustworthy LLMs, Agentic AI, and Multimodal Systems](https://arxiv.org/abs/2609.19524)

**作者：** Shaina Raza, Ahmed Y. Radwan, Imran Liaquat, Kathryn Hume  
**方向：** `可信评测框架` | **ArXiv ID：** `2609.19524`

统一评估框架，连接输出级、轨迹级和跨模态评估，涵盖八个可信度维度并提供治理映射。为LLM、Agent AI和多模态系统的可信度评估提供了系统化的方法论。

---

## 多模态检索与信息抽取

### [DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering](https://arxiv.org/abs/2609.20574)

**作者：** Luca De Grandis, Silvia Cappelletti et al.  
**方向：** `文档VQA` | **ArXiv ID：** `2609.20574` | **[Code](https://github.com/aimagelab/DocAttriBench)**

引入包含237K文档和296K QA对的文档视觉问答基准，支持元素级定位标注。提出基于掩码困惑度的MAPPET归因方法，为文档理解模型的溯源能力提供了精细化评测。

---

### [AgriScope: Pixel-Grounded Multimodal Understanding for Agricultural Images](https://arxiv.org/abs/2609.20325)

**作者：** Abderrahmene Boudiaf, Mohamad Alanssari, Irfan Hussain, Sajid Javed  
**方向：** `农业多模态` | **ArXiv ID：** `2609.20325`

面向农业场景的像素级多模态理解框架，构建了AgriGround数据集（50万+图像、1100万指令跟随样本），覆盖植物病害、作物、杂草和害虫四大类别，推动精准农业的视觉智能发展。

---

### [MIRAGE: How Conversation State Shapes Historical Evidence Use in Multimodal Personal Agents](https://arxiv.org/abs/2609.19059)

**作者：** Yu Liu, Wenxiao Zhang, Cheng Hu et al.  
**方向：** `多模态Agent` | **ArXiv ID：** `2609.19059`

通过七个多模态骨干网络的受控实验，揭示对话状态如何影响多模态个人Agent对历史证据的利用。发现预压缩深度和后压缩延续形成了独特的非单调失败机制。

---

### [Scientific Image Quality Assessment via Multi-modal Retrieval-Augmented Generation](https://arxiv.org/abs/2609.19634)

**作者：** Yinuo Zhang, Bingshuo Liu et al.  
**方向：** `科学图像评估` | **ArXiv ID：** `2609.19634`

基于RAG的科学图像质量评估框架，将文本语义与细粒度视觉特征融合，在ICME 2026 SIQA挑战赛的SIQA-U赛道中获得第一名，展示了检索增强方法在科学图像理解中的巨大潜力。

---

## Agent 与具身智能

### [Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users](https://arxiv.org/abs/2609.21828)

**作者：** George Xi Wang, Xiangyu Li, Shaoyue Wen et al.  
**方向：** `辅助导航` | **ArXiv ID：** `2609.21828`

面向盲人和低视力用户的免手操作物体获取系统，结合视觉语言理解与持久空间建模，在陌生室内环境中实现100%任务成功率，远超MLLM助手的58%。展示了具身系统在辅助领域的巨大价值。

---

### [A Sim-to-Real Integration Pipeline for Training and Deployment of Chunk-Based VLA Manipulation Policies](https://arxiv.org/abs/2609.21817)

**作者：** Mathilde Kappel, Clémence Grislain, Mohamed Chetouani et al.  
**方向：** `Sim-to-Real` | **ArXiv ID：** `2609.21817` | **[Code](https://gitlab.isir.upmc.fr/kappel/sim2real_public_chunk_control)**

开源的视觉-语言-动作模型sim-to-real实验协议，通过在真实Franka FR3机器人上回放仿真轨迹来记录对齐的视觉和本体感受数据，解决了VLA训练中数据采集的瓶颈问题。

---

### [Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation (RAPID)](https://arxiv.org/abs/2609.21767)

**作者：** Lobna Joualy, Eric Demeester, Nikolaos Tsiogkas  
**方向：** `VLM奖励学习` | **ArXiv ID：** `2609.21767` | **[Code](https://github.com/rapid-vlm/rapid-vlm-rl)**

提出使用视觉语言模型替代人类标注者进行偏好奖励学习，通过并行仿真环境规模化训练机器人操作策略。RAPID方法显著降低了奖励标注成本，同时保持策略质量。

---

### [PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation](https://arxiv.org/abs/2609.21753)

**作者：** Shengbao Li, Peng Xu, Chao Tang et al.  
**方向：** `感觉运动学习` | **ArXiv ID：** `2609.21753`

定义预测性感觉运动表征（PSR）学习框架，通过分层预测表征帮助策略在接触密集操作中基于接触力进行精确动作推理，为精细操作任务提供了新的表征学习范式。

---

### [AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining](https://arxiv.org/abs/2609.21461)

**作者：** Di Wu, Dongchen Zheng, Junhe Sheng et al.  
**方向：** `具身预训练` | **ArXiv ID：** `2609.21461`

探索原子级自我中心机器人集成方案，解决具身基础模型受限于机器人演示数据规模和多样性的问题。通过更高效的预训练策略提升模型的泛化能力。

---

### [FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](https://arxiv.org/abs/2609.21358)

**作者：** Yijun Hong, Jiarun Zhu, Xiaoquan Sun et al.  
**方向：** `持续适应` | **ArXiv ID：** `2609.21358`

面向VLA模型长期真实世界部署的持续学习方案，通过前瞻性动作归一化使模型在学习新技能的同时保留已学能力，解决了灾难性遗忘的关键挑战。

---

### [DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real](https://arxiv.org/abs/2609.21045)

**作者：** Jin Wu, Lianjie Yuan, Zeyan Sun et al.  
**方向：** `灵巧操作` | **ArXiv ID：** `2609.21045`

自动化real-to-sim-to-real框架，仅需单张RGB图像即可生成可部署的灵巧操作策略。大幅降低了灵巧操作的数据采集门槛，为灵活手操作提供了实用的解决方案。

---

### [Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](https://arxiv.org/abs/2609.21022)

**作者：** Yiheng Ji, Xingru Zhou, Luis Sentis, Mingyo Seo  
**方向：** `VLA鲁棒性` | **ArXiv ID：** `2609.21022` | **[Code](https://github.com/jidaxian010/VLA-Feedback-release)**

针对VLA模型的实时反馈去噪方法，利用语义知识提升模型在噪声观测下的响应能力。解决了VLA在真实环境中因传感器噪声导致的性能退化问题，增强了部署可靠性。

---

## 多模态生成

### [Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision-Language Models](https://arxiv.org/abs/2609.21363)

**作者：** Yining Wang, Xi Li, Mi Zhang et al.  
**方向：** `隐私保护生成` | **ArXiv ID：** `2609.21363`

基于扩散模型的VLM地理定位隐私保护框架，提供有针对性的主动防御机制，防止通过随意分享的照片推断用户地理位置。在保护隐私的同时尽量保持图像的实用性。

---

### [Multimodal Conditioning of Fine-Tuned Stable Diffusion XL for Controllable Ulos Motif Generation](https://arxiv.org/abs/2609.17987)

**作者：** Humasak Simanjuntak, Tamara Yunika Sianipar et al.  
**方向：** `文化图案生成` | **ArXiv ID：** `2609.17987`

将Stable Diffusion XL与LLaMA 1.5-7B集成的多模态生成框架，专注于印尼Batak Ulos编织图案的可控生成。通过文本+图像+语义图多模态条件实现最佳FID 270，展示了多模态生成在文化遗产保护中的应用。

---

## 音频多模态

### [Samsone: A Family of Open Small Audio Language Models for On-Device Inference](https://arxiv.org/abs/2609.21666)

**作者：** Piotr Masztalski, Michał K. Grzeszczyk, Olaf Sikorski  
**方向：** `端侧音频模型` | **ArXiv ID：** `2609.21666` | **[Code](https://github.com/SamsungLabs/samsone)**

Samsung推出面向边缘计算的小型音频语言模型系列。Samsone-134M在其规模级别中实现多个基准的SOTA性能，为端侧音频理解开辟了新的可能性，支持离线场景下的智能音频处理。

---

### [The Spoken Wikipedia Presentation Corpus](https://arxiv.org/abs/2609.21676)

**作者：** Thomas Ranzenberger, Steffen Freisinger, Tobias Bocklet, Korbinian Riedhammer  
**方向：** `多模态ASR` | **ArXiv ID：** `2609.21676`

Spoken Wikipedia Corpora的扩展版本，引入LLM生成的演示幻灯片用于多模态语音识别研究。为多模态ASR提供了新的数据资源，推动语音+视觉+文本的联合理解。

---

## 多模态感知

### [Multimodal Learning for Beamforming Using Camera, LiDAR, and Radio-Frequency Pilots](https://arxiv.org/abs/2609.21193)

**作者：** Yinghan Li, Wei Yu  
**方向：** `多传感器融合` | **ArXiv ID：** `2609.21193`

融合相机图像、LiDAR点云和射频导频的多模态学习框架，用于无线通信中的波束成形。展示了视觉+LiDAR+RF三种模态协同工作在通信优化中的应用前景。

---

### [XCalib: Depth-Guided Geometric Optimization for Dense Thermal-Visible Video Registration](https://arxiv.org/abs/2609.21770)

**作者：** Aurelien Godet, Gabriel Jobert, Mauro Dalla Mura  
**方向：** `热红外配准` | **ArXiv ID：** `2609.21770`

无监督的密集热红外-可见光视频配准框架，利用深度引导的几何优化实现精确对齐，可辅助驾驶安全系统。为多传感器视频融合提供了新的技术方案。

---

### [From Stress to Affect: Multimodal Deep Learning for Physiological Emotion Recognition Across Wearable Sensor Modalities](https://arxiv.org/abs/2609.20991)

**作者：** Desta Haileselassie Hagos, Saurav Keshari Aryal, Legand L. Burge  
**方向：** `生理情感识别` | **ArXiv ID：** `2609.20991`

跨可穿戴传感器模态的多模态深度学习比较研究，用于生理情感识别。系统评估了不同时间架构在多种生理信号上的表现，为可穿戴情感计算提供了重要参考。

---

## 3D 视觉语言

### [VeriFuse: Bounded Vision-Language Arbitration and Reason-Guided Refinement for Cooperative 3D Perception](https://arxiv.org/abs/2609.21323)

**作者：** Hongyi Lin, Yiyao Liu, Qi Kang et al.  
**方向：** `协作3D感知` | **ArXiv ID：** `2609.21323`

利用视觉语言模型进行有界仲裁和原因引导精化的协作3D感知框架。VLM强大的场景理解和语义判断能力被引入多智能体3D感知，通过验证机制确保融合结果的可靠性。

---

### [A Scene Language Model for Open-Vocabulary Scene Mapping](https://arxiv.org/abs/2609.21400)

**作者：** Adam Lilja, Fabio Hübel, Siming He et al.  
**方向：** `场景语言建模` | **ArXiv ID：** `2609.21400`

构建环境物体的持久化表征，通过场景语言模型实现开放词汇的场景建图。将语言理解与3D空间映射结合，使机器人能够用自然语言描述和查询环境中的物体。

---

## 统计

| 方向分类 | 论文数量 | 有代码 |
|---------|---------|--------|
| VLM/MLLM 理解与推理 | 8 | 2 |
| 多模态基准评测 | 6 | 1 |
| 多模态检索与信息抽取 | 4 | 1 |
| Agent 与具身智能 | 8 | 3 |
| 多模态生成 | 2 | 0 |
| 音频多模态 | 2 | 1 |
| 多模态感知 | 3 | 0 |
| 3D 视觉语言 | 2 | 0 |
| **合计** | **35** | **9** |

---

*Generated on 2026-09-21 | Data source: [arXiv.org](https://arxiv.org)*
