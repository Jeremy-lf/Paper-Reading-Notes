# Arxiv 多模态论文日报 - 2026-09-23

> 收录时间范围：2026-09-21 ~ 2026-09-22

---

## VLM/MLLM 视觉语言模型

### 1. [Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611)

**Authors:** Qwen Team | **Tags:** `VLM/MLLM` `Omni-Modal` `Agent` | **Code:** [GitHub](https://github.com/QwenLM/Qwen3-Omni)

提出Qwen3.8-Omni-Flash，一个原生多模态智能体模型，面向实际多模态生产力场景。继承Qwen3.8-Next的稀疏混合专家架构，上下文窗口扩展至100万token。采用原生多模态联合训练方法，在保持强大文本能力的同时将智能体能力扩展到音频和视频领域。应用包括视频编辑、长视频翻译、音乐驱动的视频生成等。同时发布了Qwen-MM-Plugins轻量级开源插件框架和Qwen-Live-Harness实时多模态智能体框架。

### 2. [BAS-OPD: Budget-Aware Selective On-Policy Self-Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2609.25891)

**Authors:** Zihan Chen, Hengguang Zhou, Yuan Kang, Yiming Zhang, Wenhui Fang, Zenghui Ding, Yining Sun, Cho-Jui Hsieh | **Tags:** `VLM/MLLM` `多模态感知` `自蒸馏` | **Code:** 暂无

针对多模态大语言模型（MLLM）中细粒度视觉感知的挑战，提出BAS-OPD框架。在on-policy自蒸馏（OPD）基础上引入预算感知的选择性监督分配机制，在有限查询预算下选择信息量最大的样本进行教师监督。探索了随机、不确定性和基于效用的选择策略，在保持单pass全图推理的同时大幅降低教师监督成本。

### 3. [Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes](https://arxiv.org/abs/2609.25841)

**Authors:** Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong et al. | **Tags:** `VLM/MLLM` `基准评测` `空间推理` | **Code:** 暂无 (ECCV 2026)

提出Metric-Bench基准，通过上下文线索（图像中已知物理尺寸的参考物体）引导VLM进行度量空间推理，无需相机内参即可隐式学习2D到3D映射。同时提出MetricReasoner，一种使用结构化提示和可验证数值奖励的强化微调方法。实验显示该方法超越大型商业模型43.1%，在具身AI任务上也取得显著提升。已被ECCV接收。

---

## 多模态生成 Multimodal Generation

### 4. [KwaiMind Technical Report](https://arxiv.org/abs/2609.26375)

**Authors:** Junlong Wu, Zijun Li, Yuting Hu et al. (Kuaishou Group) | **Tags:** `多模态生成` `图像编辑` `电商` | **Code:** 暂无

快手推出的商业图像编辑系统KwaiMind，结合通用编辑能力与电商专业化。核心是包含约180万编辑对的"智能体数据引擎"，模型为多模态扩散Transformer，经过持续预训练、监督微调、偏好优化和在线强化学习。提出Ecom-Bench基准覆盖11个商业编辑任务。在线A/B测试中实际CTR提升约2.44%。

### 5. [VideoX-Qwen: Data-Centric Instruction-Based Video Editing](https://arxiv.org/abs/2609.26015)

**Authors:** Jiahang Li, Dingbao Shao, Xinyu Chen et al. | **Tags:** `多模态生成` `视频编辑` `指令驱动` | **Code:** 暂无

提出基于指令的视频编辑框架VideoX-Qwen，解决构建大规模配对数据集和将视频生成骨干适配编辑任务两大挑战。数据管线结合专门的生成和理解模型，产出超过120万条定向编辑记录。模型采用Qwen-Wan编辑器，配合多模态语义条件和密集源视频潜在引导，在11项指标中的9项取得最佳平均分。

### 6. [CogenPVG: Cognitive-Enhanced Reflective Multi-Agent Framework for Persuasive Video Generation](https://arxiv.org/abs/2609.25821)

**Authors:** Yuntian Xiao, Shoulong Zhang, Wenfeng Song, Yan Wang, Yi Chen, Shuai Li | **Tags:** `多模态生成` `视频生成` `多智能体` | **Code:** 暂无

提出CogenPVG多智能体框架用于说服力视频生成（PVG）。将生成过程分为论证推理、故事板规划、素材创建和后期编辑四个阶段，模拟人类视频创作者的工作流程。基于精细加工可能性模型（ELM），每个阶段配备生成器和批评器进行反思式优化。据称是首个面向"通用说服性主题"的框架。

### 7. [TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum](https://arxiv.org/abs/2609.25864)

**Authors:** Xinyue Guo, Jianxuan Yang, Daiguo Zhou et al. | **Tags:** `多模态生成` `音频处理` `文本-视觉引导` | **Code:** 暂无

提出TV-AudioRemover框架，解决视频编辑中视觉对象被移除但关联声音仍保留的问题。接收视觉编辑后的视频和自然语言指令，从原始音频混合中抑制被移除对象的声音。构建了百万级单对象音频-视觉数据集，提出任务令牌、泛化指令建模和模态特定全局引导等架构改进，以及多任务硬混合课程训练方案。

---

## 3D视觉语言 3D Vision-Language

### 8. [PartLLM: A Unified Multimodal Foundation for 3D Part Segmentation](https://arxiv.org/abs/2609.25832)

**Authors:** Zhe Zhu, Yiheng Zhang, Peng Li et al. | **Tags:** `3D视觉语言` `部件分割` `多模态基础模型` | **Code:** 暂无

将3D部件分割统一为"意图条件生成问题"，提出PartLLM多模态模型。将3D部件分割视为"自回归语义分解"，在给定形状和用户提示的条件下，生成语义部件假设作为掩码预测的查询。单一模型支持文本引导分割、交互式分割和可控粒度的全形状语义分解，在所有任务设置中一致超越特定任务基线。

---

## Agent与具身智能 Agent & Embodied AI

### 9. [MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation](https://arxiv.org/abs/2609.25756)

**Authors:** Junjie Xie, Chuxuan He, Angen Ye, Yujia Song, Dapeng Zhang | **Tags:** `Agent与具身智能` `医疗机器人` `VLA` | **Code:** 暂无

提出MedVLA分层框架，将高级多模态推理与低级功能约束执行耦合。引入可扩展的多智能体管线生成面向技能的思维链数据。在100次闭环柔性电极植入试验中达到95.0%任务成功率，大幅超越OpenVLA（8%）和π_0（15%）等代表性VLA基线，展示了结构化推理与约束功能级执行在精密医疗机器人中的实用价值。

### 10. [CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing](https://arxiv.org/abs/2609.25606)

**Authors:** Zhifei Teng, Bo Feng, Xiang Zou et al. | **Tags:** `Agent与具身智能` `VLA` `机器人操作` | **Code:** 暂无

提出CableVLA端到端多模态视觉-语言-动作框架，将仿真特权监督转化为可部署的电缆拓扑和触觉表示。TopoHead将节点级物理和电缆拓扑信息蒸馏为因果视觉上下文，TacSense从电阻阵列学习接触动力学。在345次MuJoCo评估中将成功率从62.6%提升至84.9%。

### 11. [OmniFysics-Nano-V2: Understanding the Physical World Across Modalities](https://arxiv.org/abs/2609.25738)

**Authors:** Yizhou Liu, Jinghang Han, Kaixiang Qiu et al. | **Tags:** `Agent与具身智能` `全模态` `物理推理` | **Code:** 暂无

提出OmniFysics-Nano-V2紧凑型全模态模型，面向物理世界理解。接受图像、视频、音频、语音和文本输入，输出文本和语音。构建双分支物理感知数据管线。采用两阶段GRPO课程从通用任务正确性推进到细粒度物理感知推理。在21个基准中的17个取得领先结果。

---

## 多模态感知 Multimodal Perception

### 12. [MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving](https://arxiv.org/abs/2609.25860)

**Authors:** Xiaoyu Li, Jiajia Fu, Long Shi et al. | **Tags:** `多模态感知` `自动驾驶` `LiDAR-Camera融合` | **Code:** 暂无

提出MatchFusion可学习实例匹配与融合模块，用于时空多模态自动驾驶。使用几何相似度和类别一致性初始化成对亲和力，再利用实例嵌入优化关联。在nuScenes实验中，相比先前实例中心融合方法，在提升感知精度的同时将FLOPs降低55.3%、GPU内存使用降低39.3%。

### 13. [CMT-AD: Confidence-Guided Cross-Modal Knowledge Transfer for Multimodal Anomaly Detection](https://arxiv.org/abs/2609.25856)

**Authors:** Peipeng Wang, Xiuguo Zhang, Lihua Zhang et al. | **Tags:** `多模态感知` `异常检测` `微服务` | **Code:** 暂无

针对微服务系统异常检测，提出CMT-AD方法。在单一深度聚类框架内联合建模指标和日志数据，从软聚类分布估计模态可靠性，将聚类不确定性转化为置信度分数驱动跨模态交互。引入门控中间模态和结构/语义一致性约束，在三个大规模数据集上F1-score超过0.9。

### 14. [WOOPS: When Point Clouds Outperform Pixels - Rethinking Zero-Shot Multimodal Anomaly Detection](https://arxiv.org/abs/2609.25793)

**Authors:** Chenglin Ye, Lupeng Liu, Dongbo Yu, Jun Xiao, Yunbiao Wang | **Tags:** `多模态感知` `异常检测` `零样本` | **Code:** 🔜 即将发布

挑战了零样本多模态异常检测中RGB和点云同等可靠的常见假设。使用惩罚正常区域假阳性响应的严格指标，发现点云在零样本类别迁移下显著优于RGB。提出WOOPS可靠性感知框架，包含多视图信息解耦模块和模态可靠性校准模块。

---

## 多模态检索与信息抽取 Multimodal Retrieval & Extraction

### 15. [SALI-FP: Evidence-gated Multimodal Parsing and Vectorization of Architectural Floor Plans](https://arxiv.org/abs/2609.25615)

**Authors:** Hongxuan Chen, Wenda Wang, Jiachen Lu et al. | **Tags:** `多模态检索` `建筑图纸解析` `向量化` | **Code:** 暂无

提出SALI-FP管线，将建筑图纸转化为可审查的语义图、对象、向量和关系记录。在11,534张多样化图纸上测试，为每张图纸生成结构化输出，覆盖752,510个有效多边形对象。提供面向CAD/BIM准备的工程化解释-几何工作流。

---

## 多模态轨迹预测 Multimodal Trajectory Prediction

### 16. [DSR: Destination Support Restoration for Finite-Set Multimodal Trajectory Prediction](https://arxiv.org/abs/2609.25942)

**Authors:** Fengrui Liu, Jiajun Peng, Duo Peng, Feng Liu | **Tags:** `轨迹预测` `多模态` `机器人` | **Code:** 暂无

解决机器人轨迹预测系统中固定大小候选集的模式覆盖退化问题。提出DSR因果后选择算子，在不重训主机模型或不增加假设集的情况下修复模式覆盖。在Edinburgh协议完整评估中，N=64时ADE和FDE分别降低13.36%和13.30%。

---

## 统计

| 指标 | 数值 |
|------|------|
| **论文总数** | 16 |
| **有代码** | 1 篇 (Qwen3.8-Omni) |
| **即将开源** | 1 篇 (WOOPS) |

**方向分布：**

| 方向 | 篇数 |
|------|------|
| VLM/MLLM | 3 |
| 多模态生成 | 4 |
| 3D视觉语言 | 1 |
| Agent与具身智能 | 3 |
| 多模态感知 | 3 |
| 多模态检索 | 1 |
| 轨迹预测 | 1 |
