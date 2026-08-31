# Arxiv 多模态论文日报 —— 2026-08-31

**日期**：2026 年 8 月 31 日  
**收录论文**：13 篇  
**含代码仓库**：3 篇  
**覆盖方向**：8 个

## VLM/MLLM

### [Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2608.28058)

**作者**：Kairong Yu, Zixin Zhu, Le Yu et al.  
**方向**：VLM/MLLM  

作者指出大视觉语言模型在自回归生成中存在跨模态表示随层退化、随时间漂移的推理时失效模式，进而提出无需训练的Dynamic Alignment Compensation（DAC）方法。DAC通过层间语义补偿和序列语义校正，对表示发散进行轻量化残差修正。在9个幻觉评测和通用多模态基准上的实验显示，DAC能一致降低幻觉并保持整体性能。

### [Token-Budget Distillation: Transferring Full-Token Semantics to Compressed Video Vision-Language Models](https://arxiv.org/abs/2608.28138)

**作者**：Xiaoyang Guo, Guoping Luo, Jusheng Zhang et al.  
**方向**：VLM/MLLM  

为解决视频VLM因视觉token过多导致微调与推理成本高的问题，本文提出Token-Budget Distillation（TBD）参数高效微调框架。TBD在冻结主干、仅训练LoRA的同时引入FlashVID视觉token压缩，并通过全token教师与压缩学生双路径蒸馏保持语义一致性。在LLaVA-Video、LLaVA-OneVision和Qwen3-VL等模型上，TBD在10%保留率下仍能保持或接近完整模型的性能。

### [AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2608.28312)

**作者**：Wonjun Lee, Jaehyuk Jang, Kangwook Ko et al.  
**方向**：VLM/MLLM  

针对多模态大模型在微调中记忆人物身份隐私的问题，本文提出无需保留图像即可进行身份遗忘的AIM方法。作者发现身份相关查询与视觉感知查询在隐藏状态中存在显著分离，因此用一个通用视觉提示锚定“遗忘目标”，并在Fisher约束下匹配视觉编码器。实验表明，AIM在有效擦除目标身份的同时，能较好保留非删除身份、先验知识和视觉感知能力。

### [Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs](https://arxiv.org/abs/2608.28383)

**作者**：Chenhong He, Lei Li, Shicheng Li et al.  
**方向**：VLM/MLLM  

本文发现多模态LLM中的ViT注意力头会自发分化为物体头和背景头，并据此提出Semantic Head Specialization（SHS）现象及量化指标SHS-Index。通过分析窗口交互、token序列化和局部softmax分配三个结构因素，作者设计了Ariadne Attention混合注意力机制，在22个图像和视频任务上以6.5倍更低的注意力计算接近全注意力的性能，为大规模多模态模型的高效视觉编码提供了可解释的设计原则。

## 多模态理解与推理

### [Conditional Visual Evidence Utility: State-Dependent Rank Reversals in Frozen Vision-Language Encoders](https://arxiv.org/abs/2608.28316)

**作者**：Yunxuan Fang, Xinhe Wang  
**方向**：多模态理解与推理  

本文挑战静态证据重要性排序的假设，研究在观察到部分线索后剩余证据价值发生状态依赖反转的现象。在控制组合视觉搜索中，作者发现冻结的OpenCLIP和SigLIP在候选重叠区域会出现稳健的秩反转，且仅在第一次证据获取后重新排序能带来正向决策效用。该工作提示应条件化地评估视觉语言模型的证据使用，而非依赖单一静态排序。

### [Abstract4D: A Large-Scale Dataset and Framework for Understanding the Visual Language of Abstract Art](https://arxiv.org/abs/2608.28339)

**作者**：Haowei Zhang, Yuanpei Zhao, Ji-Zhe Zhou et al.  
**方向**：多模态理解与推理  

本文推出目前规模最大的抽象画数据集Abstract4D，包含12万余张图像及描述形式、颜色、纹理与构图的多维提示，标注由人机协同VLM流程完成。作者通过大规模嵌入可视化分析抽象艺术的语义结构，并建立分类、跨模态检索与文本到图像生成等基准任务，为评估AI对抽象视觉语言的理解与再现能力提供了系统性平台。

## 多模态基准与评测

### [MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places](https://arxiv.org/abs/2608.28384)

**作者**：Jason Armitage, Ioannis Tsochantaridis, Linda Mazzone et al.  
**方向**：多模态基准与评测  

本文提出首个评估多模态AI作为真实世界无障碍规划助手的基准MAP，包含声明验证与视觉证据检索两项任务。系统需验证地点的无障碍信息是否属实，并为请求的地点与无障碍特征检索视觉证据。该benchmark支持定时刷新地面真值，结合自动评分与人工评分，适用于现实场景中动态变化的信息。

## 多模态检索与信息抽取

### [A-PAIR: A Benchmark and Identity-Consistent Grounding Framework for Air-Ground Cross-View Referring Person Detection](https://arxiv.org/abs/2608.27997)

**作者**：Zhoupeng Guo, Xinjie Yao, Yunqi Zhu et al.  
**方向**：多模态检索与信息抽取  

本文针对空地跨视角指代人检测任务，提出首个大规模基准A-PAIR及身份一致grounding框架ICRG。A-PAIR包含22,137个跨视角指代样本，并通过半自动FARA标注流程降低构建成本；ICRG通过因子化指代grounding、候选完整性与跨视角一致性校准联合选择空地配对目标，将pair F1从16.65%提升至22.28%，显示该任务需要成对检测与身份一致推理。

## Agent与具身智能

### [DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA](https://arxiv.org/abs/2608.28108)

**作者**：Kango Yanagida, Tatsuya Aoki, Yuichiro Yoshikawa et al.  
**方向**：Agent与具身智能  

本文提出DeicticVLA，将语言指令、视觉语言指令和纯视觉指令统一编码为文本提示与指示性手势掩码，使单一预训练VLA可处理三种交互模式。通过对比RGB提示、分离通道掩码与两阶段训练策略，作者发现保留第二阶段语言数据可缓解遗忘，并在真实任务中使视觉辅助模式在未见表达、外观变化和新颖物体上显著优于纯语言指令。

### [When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI](https://arxiv.org/abs/2608.28518)

**作者**：Sihan Jia, Oliver Lemon  
**方向**：Agent与具身智能  

本文首次系统研究语音识别（ASR）错误对语音控制具身AI安全性的影响。通过在SafeAgentBench和POEX上模拟ASR错误，作者发现某些错误在保持语义结构的同时增加有害歧义，另一些则会削弱模型拒答能力并导致执行不安全计划。研究表明ASR错误会给具身AI带来显著安全风险，且自动纠错并不总是可靠。

## 多模态生成

### [There and Back Again: Bidirectional Diffusion Bridges for Multimodality Translation](https://arxiv.org/abs/2608.27885)

**作者**：Gabe Guo, Elon Litman, Thanawat Sornwanee et al.  
**方向**：多模态生成 [Code](https://github.com/gabeguo/bit_diffusion)  
**代码仓库**：https://github.com/gabeguo/bit_diffusion  

本文提出BIT（Bidirectional Image-Text Diffusion Bridges），一种基于双向扩散桥的统一多模态翻译框架。与传统方法不同，BIT直接从文本出发插值到图像，既提供源感知的生成路径以支持灵活采样，又可从图像端条件化逆向生成文本。通过随机微积分推导的SDE形式具有良好的可扩展性，在视觉语言与自然科学任务上优于或持平于去噪扩散与确定性流基线。

## 音频多模态

### [Compositional Failure in Audio-Visual LLMs: Late-Layer Prior Dominance Under Cross-modal Conflict](https://arxiv.org/abs/2608.27785)

**作者**：Adarsh Sudheer, David Li, Omar Elbanna et al.  
**方向**：音频多模态 [Code](https://github.com/AdarshSudheer09/AVHBench-dmai)  
**代码仓库**：https://github.com/AdarshSudheer09/AVHBench-dmai  

本文将音视频语义冲突作为组合泛化测试，揭示音频视觉大模型在跨模态冲突下出现的“先验主导”失效模式：模型在深层过早承诺内部偏好的答案模式。机制可解释性分析显示该承诺集中在25.5±1层；即便增强时间对齐也仅改变答案偏置，无法真正解决组合冲突。该研究为诊断AV-LLM的跨模态推理提供了新视角。

## 3D视觉语言

### [ARC-CT: Anatomy-Routed Contrastive Vision-Language Learning for 3D Chest CT](https://arxiv.org/abs/2608.28455)

**作者**：Huseyin Umut Isik, Mehmet Alp Ozaydin, Sila Kurugol et al.  
**方向**：3D视觉语言 [Code](https://github.com/arc-ct/arc-ct)  
**代码仓库**：https://github.com/arc-ct/arc-ct  

本文提出ARC-CT，一种面向3D胸部CT的解剖路由对比视觉语言学习框架，仅利用大语言模型从报告中提取的标签即可训练异常分类器。通过AnatomyQFormer定位器官区域、标签Jaccard软InfoNCE减少假负样本惩罚、器官级对齐连接视觉与报告文本，ARC-CT在18种异常上达到0.86的mask-free macro AUC，并超越更大规模的Transformer模型。

---

**论文总数统计**：共收录 13 篇论文，其中 3 篇提供代码仓库，覆盖 8 个研究方向。
