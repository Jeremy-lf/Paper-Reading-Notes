# Arxiv 多模态论文日报 - 2026-08-29

**日期**：2026-08-29

**收录论文**：24 篇 | **含代码仓库**：8 篇 | **覆盖方向**：8 个

## VLM / MLLM 核心

### [Visual Information-Guided Parallel Decoding for Diffusion Multimodal Large Language Models](https://arxiv.org/abs/2608.26580)

**作者**：Insu Lee, Wooje Park, Wonseok Shin et al.

**方向标签**：VLM / MLLM

提出 Visual Information-Guided Sampler（VIG-Sampler），根据 token 对图像 token 的注意力优先解码，并惩罚与已选 token 图像注意力分布相似的候选，在 7 个图像描述和 VQA 基准上表现优于 Info-Gain Sampler。

### [Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs](https://arxiv.org/abs/2608.26581)

**作者**：Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng et al.

**方向标签**：VLM / MLLM

系统研究低比特量化在多模态大语言模型中的影响，发现激活量化是 4 比特量化性能下降的主要来源，并提出 Residual Fallback Quantization（RFQ）通过辅助量化残差路径恢复激活保真度。

### [Information-Guided Frontier Decoding: Contextual Utility-Driven Commitment in dMLLMs](https://arxiv.org/abs/2608.26641)

**作者**：Xingyou Fang, Jingxing Zhong, Xiaosong Yuan et al.

**方向标签**：VLM / MLLM

提出 Information-Guided Frontier Decoding（IGFD），一种无需训练的策略，综合考虑 token 置信度、邻域不确定性和结构承诺风险，优先解码可靠语义锚点，在多个扩散多模态大语言模型基准上超越现有策略。

### [Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models](https://arxiv.org/abs/2608.26716)

**作者**：Yiyang Huang, Zhaowen Wang, Simon Jenni et al.

**方向标签**：VLM / MLLM、推理、[Code]

**代码仓库**：[GitHub](https://github.com/hukcc/Beyond-Atomic-Layouts)

提出组合式布局理解任务和 CoDeLayout 数据集，识别语义漂移和结构歧义两大挑战，并提出 MASON 后训练范式，结合多模态对齐和结构感知，显著提升视觉语言模型表现。

### [UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization](https://arxiv.org/abs/2608.26722)

**作者**：Jiahao Wen, Hang Yu, Zhedong Zheng

**方向标签**：VLM / MLLM、检索

提出 UniGeo 多模态大语言模型用于文本引导的无人机跨视角地理定位，支持地理语义理解、跨视角语义生成和候选级验证，在 GeoText-1652 上显著提升 R@10 和 mAP。

### [Emotion Understanding in Streaming Video with Trajectory-Aware Reliability](https://arxiv.org/abs/2608.26786)

**作者**：Qingsong Wang, Qigong Lei, Zitong Wang et al.

**方向标签**：VLM / MLLM、音频、[Code]

**代码仓库**：[GitHub](https://github.com/APTX574/Trace)

提出 TRACE 轨迹感知可靠性框架，将流式视频情绪理解视为不断演化的信念决策过程，对稳定样本使用低延迟在线路径，对不确定样本调用更强的多模态上下文推理。

### [LLaVAFlow: Preserving Latent Alignment Flow for Parameter-Efficient Multimodal Fine-Tuning](https://arxiv.org/abs/2608.26820)

**作者**：Muyao Yuan, Muyan Jiao, Jiangyong Ying et al.

**方向标签**：VLM / MLLM

提出信息论蒸馏框架 LLaVAFlow，通过互信息压缩和最大化预训练与微调 MLLM 之间的对齐流，保持跨模态对齐，缓解视觉指令微调中的灾难性遗忘。

### [SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting](https://arxiv.org/abs/2608.26829)

**作者**：Haizhao Fan, Xinyi Le

**方向标签**：VLM / MLLM、检索

提出基于 CLIP 的端到端框架 SAGE，通过变量级描述和统计描述增强时间序列预测，在不需要推理时 LLM 的情况下，在八个长期预测基准和 M4 上取得最先进精度。

### [Mitigating Strong-Modality Collapse in Multimodal Learning via Inverted Asymmetric Fusion](https://arxiv.org/abs/2608.26879)

**作者**：Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat

**方向标签**：VLM / MLLM

发现多模态融合可能降低主导模态性能，称为强模态坍塌。提出 Inverted Asymmetric Fusion（IAF），保留主导模态路径，让较弱模态以其为上下文锚点，并通过模态感知知识蒸馏增强弱模态。

### [Omni-Interactive Universal Embedder](https://arxiv.org/abs/2608.27044)

**作者**：Wei-Yao Wang, Kazuya Tateishi, Shuyang Cui et al.

**方向标签**：VLM / MLLM、检索、音频

提出首个 Omni-Interactive Universal Embedder（OmniUE），学习文本、视频、音频的统一嵌入空间，并支持文本、视觉兴趣区域和音频跨度等全方位交互查询。同时引入 OmniCHOIR 组合式音频检索基准。

## 多模态理解与推理

### [Self-Reflective Multi-modal Reasoning for Short-Video Fake News Detection](https://arxiv.org/abs/2608.26787)

**作者**：Pinjie Xu, Yuzhou Yang, Zhikai Tan et al.

**方向标签**：推理、VLM / MLLM

提出 SRM-FND 自反思多模态推理框架，用于短视频假新闻检测，通过对比审议、迭代根因诊断和纠正提示改进推理质量，并结合跨样本验证，在 FakeSV 和 FakeTT 上超越基线。

### [Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning](https://arxiv.org/abs/2608.26993)

**作者**：Hengyuan Xu, Wei Cheng, Yumeng Ji et al.

**方向标签**：推理、VLM / MLLM

提出 Aphanta 自动任务发现和闭环诊断框架，用于评估 MLLM → 图像编辑器 → MLLM 流程中视觉中间表示的效用。发现视觉中间件的收益高度依赖任务类型，在视觉线索注入、grounding 和反事实状态实现上有效。

## 多模态基准与评测

### [AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability](https://arxiv.org/abs/2608.26713)

**作者**：Xuanwei Hu, Haoyu Dong, Kejun Wu et al.

**方向标签**：基准

发布 AesCanvas 套件，包含 CritiqueCanvas 长形式美学评论数据集和 ContextCanvas 情境适宜性评估，发现美学评论生成与情境敏感判断之间存在明显差距。

### [DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?](https://arxiv.org/abs/2608.26757)

**作者**：Jiahui tang, Kuicai Dong, Dexun Li et al.

**方向标签**：基准、[Code]

**代码仓库**：[GitHub](https://github.com/tangdouer1005/DeepChart)

提出 DEEPCHART 基准，包含 1,482 个真实科学论文、财务报告和生态系统报告中的图表生成实例，分阶段评估数据提取、推理和渲染。发现视觉上合理的图表常隐藏数据级幻觉。

### [Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning](https://arxiv.org/abs/2608.26866)

**作者**：Haihan Li, Haihao Li, Zhenfei Xu et al.

**方向标签**：基准、推理

提出中文多格表情包基准 CMPM，覆盖五种结构类型和顺序依赖，评估大型视觉语言模型对结构化梗图布局的顺序感知推理能力。结果显示打乱面板顺序会导致准确率显著下降。

## 多模态检索与信息抽取

### [CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object Detection](https://arxiv.org/abs/2608.27214)

**作者**：Hao Xu, Zhaoning Shi, Hehe Jin et al.

**方向标签**：检索

针对开放世界目标检测中多模态基础模型的语义歧义和未知对象过度抑制问题，提出推理时框架 CODE，包含跨模态联合置信度校准、不确定性引导的通用对象性增强和基于置信度边界的动态离群抑制。

## Agent 与具身智能

### [RegulAR: Graph-Grounded Error Recognition and Assistance for Procedural Tasks in AR](https://arxiv.org/abs/2608.26715)

**作者**：Yi-Lin Ye, Jindu Wang, Hiu Tung Wong et al.

**方向标签**：Agent

提出 AR 任务助手 RegulAR，将任务指令建模为层次依赖图并结合多模态大语言模型解释自我中心视角观察，以跟踪进度、识别偏差类型并估计对后续步骤的影响，提供恢复指导。

### [GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory](https://arxiv.org/abs/2608.26983)

**作者**：Geng Li, Yuhao Wang, Dong Li et al.

**方向标签**：Agent、[Code]

**代码仓库**：[GitHub](https://github.com/ligeng0197/graphmemix)

提出 GraphMemix，将多模态智能体的长期记忆组织建模为查询感知的证据森林，通过候选图构建、证据效用与激活成本、森林优化三个组件，在四个长期记忆基准上取得更好的准确率-生命周期成本权衡。

## 多模态生成

### [From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation](https://arxiv.org/abs/2608.26856)

**作者**：Haowen Gu, Gensheng Pei, Junzhu Mao et al.

**方向标签**：生成、VLM / MLLM、[Code]

**代码仓库**：[GitHub](https://github.com/NUST-Machine-Intelligence-Laboratory/MedREAL)

提出 MedREAL 医学推理驱动回答与定位框架，将语言推理与像素级分割 grounding 对齐，并构建 MedRAVS-13K 数据集覆盖四种医学影像模态，在医学 VQA 和分割任务上超越现有方法。

### [How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space](https://arxiv.org/abs/2608.27121)

**作者**：Corey D. C. Heath

**方向标签**：生成、VLM / MLLM、音频

提出自监督框架，将文本、音频、图像和视频投影到共享 256 维嵌入空间，并通过迭代聚类发现美学结构，讨论 AI 聚类结果与人类情感标签之间的差异。

### [TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation](https://arxiv.org/abs/2608.27127)

**作者**：Jingyi Zheng, Yule Liu, Zifan Peng et al.

**方向标签**：生成、Agent、[Code]

**代码仓库**：[GitHub](https://github.com/Jingyi62/TransMeme)

提出多智能体框架 TransMeme，用于中英双向跨文化表情包再创作，通过文化适配、目标文本重写、修订和条件视觉调整解决文化知识理解、意图语气保持和多模态一致性三大挑战。

## 音频多模态

### [Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs](https://arxiv.org/abs/2608.26684)

**作者**：Ji Soo Lee, Jinyoung Park, Seohyun Lee et al.

**方向标签**：音频、VLM / MLLM

提出 Echo-GRPO 框架，将教师策略的推理轨迹改写为学生策略的习语（idiolect）同时保留语义，用于视频推理蒸馏，在三个多模态 LLM 骨干和五个基准上取得一致提升。

### [Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models](https://arxiv.org/abs/2608.27135)

**作者**：Basel Mousi, Fahim Dalvi, Shammur Chowdhury et al.

**方向标签**：音频、VLM / MLLM、基准、[Code]

**代码仓库**：[GitHub](https://github.com/baselmousi/cfhr-ci)

构建覆盖 18 个中东和北非国家 10,150 张文化 grounding 图像的语音增强视觉对比三元组基准，评估多模态模型在文本/语音、英语/阿拉伯语下的 triplet 级一致性。发现模态和语言切换会导致显著的片段化推理失败。

## 3D 视觉语言

### [UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City](https://arxiv.org/abs/2608.27456)

**作者**：Tianjie Ju, Zheng Wu, Yueqing Sun et al.

**方向标签**：3D、Agent、[Code]

**代码仓库**：[GitHub](https://github.com/UrbanGround/UrbanGround)

提出 UrbanGround，一个基于香港全境 3D 地理数据构建的真实比例城市沙盒，用于测试多模态大语言模型（MLLMs）能否将局部街景感知转化为持续可靠的导航与行动。研究发现当前智能体在视觉识别和短程空间推理上有用，但方向感和行人感知移动仍不可靠，长期探索中错误会累积。

---

**论文总数统计**：本次共收录 24 篇最近 2 天内提交的多模态相关论文，其中 8 篇提供或即将提供代码仓库，覆盖 8 个研究方向。
