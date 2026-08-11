# Arxiv 多模态论文日报 - 2026-08-09

**日期**：2026 年 8 月 9 日  
**收录论文**：57 篇  
**含代码仓库**：17 篇  
**覆盖方向**：7 个

## VLM/MLLM

### [A Paragraph is Worth a Thousand Captions: Rethinking Text Supervision for Vision-Language Retrieval](https://arxiv.org/abs/2608.05260)

**作者**：Mahyar Ghazanfari, Amin Tabrizian, Arsyi Aziz, Binshuai Wang, Peng Wei  
**方向**：VLM / MLLM  
**代码**：暂无

本文系统研究了训练文本粒度对对比式图文检索的影响，发现仅靠段落级监督即可显著提升长文本检索能力。作者基于 Qwen2-VL 与 Llama 3.2 Vision 合成 50 万张 CC3M 图像的多句段落，并在冻结视觉编码器的情况下微调 BLIP 文本编码器；实验表明，段落监督在 ShareGPT4V 上追平 Long-CLIP-L，在 DOCCI 的 image-to-text 检索上领先超过 14 分，且无需改动模型结构。

### [Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation](https://arxiv.org/abs/2608.05341)

**作者**：Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry, Vincent Jeanselme, Judy Wawira Gichoya, Sanmi Koyejo, Kathleen Capaccione, Shalmali Joshi  
**方向**：VLM / MLLM  
**代码**：暂无

针对胸部 X 光报告生成中临床报告存在的遗漏噪声，本文提出 PU-DPO 偏好优化框架，将未提及的病灶视为未标注而非真正的阴性样本。通过构造显式提及或省略特定发现的对比偏好对进行训练，PU-DPO 在多个真实胸片基准上持续提升隐藏阳性病灶的检出率，并对遗漏噪声表现出更强的鲁棒性。

### [DynaPix: Can Vision-Language Models Identify the Exact Future?](https://arxiv.org/abs/2608.05505)

**作者**：Thong Nguyen, Vinh-Hien Do, Quynh Vo, Cong-Duy Nguyen, See-Kiong Ng  
**方向**：VLM / MLLM  
**代码**：暂无

本文提出 DynaPix 基准，用于检验 VLM 是否能从物理场景视频中准确预测真实未来状态，而非仅生成看似合理的画面。该基准要求模型在高度相似的候选图库或选项中选出与精确时刻对应的真实未来帧，实验揭示了现有模型存在“时间锚定”缺陷：它们善于基于可见事件定位未来，但在仅依赖经过时间时接近随机水平。

### [TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs](https://arxiv.org/abs/2608.05616)

**作者**：Yanqi Wu, Runhe Lai, Xinhua Lu, Qichao Chen, Zhiping Zhou, Jia-Xin Zhuang, Weijiang Yu, Ruixuan Wang  
**方向**：VLM / MLLM  
**代码**：[Code](https://github.com/wyqstan/TruthLens)

本文提出 TruthLens，一种无需辅助模型和额外推理开销的 LVLM 物体幻觉自评估方法。该方法将一个特殊 token 作为参考，从 LM head 提取每个对象 token 的“真实性分数”，并通过 MSE 微调使真实对象分数趋近 1、幻觉对象趋近 0；在多个 LVLM 上取得 SOTA，Qwen2.5-VL-7B 在 MS-COCO 的 AUROC 较此前最优方法提升超过 17%。

### [SCI-CLIP: Segment-Centric Inference with Reference Memory for Training-Free Open-Vocabulary Segmentation](https://arxiv.org/abs/2608.05627)

**作者**：Mohamad Zamini, Diksha Shukla  
**方向**：VLM / MLLM  
**代码**：[Code](https://github.com/mzamini92/SCICLIP)

本文提出 SCI-CLIP，一种以区域段（segment）为中心、无需训练的开集词汇分割推理框架。它在冻结的 CLIP 视觉 token 上构建区域一致性交互图，传播重建密集特征，并通过离线参考记忆实现基于样例的检索校正；在 8 个基准上显著提升了分割的结构质量、上下文推理能力与样例校正效果。

### [Mapping Armenian Paris: Extracting and Geocoding Commercial Advertisements from the 20th-Century Diaspora Press](https://arxiv.org/abs/2608.05911)

**作者**：Chahan Vidal-Gorène, Seda Kirakosyan, Edita Matevosyan  
**方向**：VLM / MLLM  
**代码**：暂无

本文构建了面向 20 世纪法国亚美尼亚裔报刊的端到端 IIIF 流程，利用 VLM 自动定位、识别并结构化商业广告，进而进行地理编码与交互式地图展示。作者发布了 500 页、3270 条广告级标注的西亚美尼亚语语料及 Label Studio 模板，证明 VLM 驱动的数据自举策略对低资源历史语言数字化具有显著效用。

### [Respect Your Zero-Shot Uncertainty: Conservative Calibration for Test-Time-Adapted Vision-Language Models](https://arxiv.org/abs/2608.05945)

**作者**：Jingyan Jiang, Yaru Sun, Xiao Chen, Jiazhen Huang, Caiting Li, Zhijian He, Yin Chen, Pingting Hao  
**方向**：VLM / MLLM  
**代码**：暂无

本文发现测试时适应（TTA）会降低 VLM 的校准性，即使预测结果未变，置信度仍会异常升高（即“预测保持的锐化”）。为此提出 ZAEC，以 zero-shot 熵作为样本级不确定性参考，仅对熵被过度压缩的预测做最小温度缩放以恢复其 zero-shot 不确定性；在 5 种 TTA 方法和 15 个数据集上，无需标注数据和学习参数即可显著降低 ECE，同时保持分类准确率。

## 推理

### [TAU-Bench: From Anomaly Instance Tracking to Fine-Grained Video Anomaly Understanding](https://arxiv.org/abs/2608.05699)

**作者**：Kepeng Yang, Dongxuan Liu, Rongxin Gao, Zixin Su, Rui Wu, Shuzhao Xie, Chenxin Li, Panwang Pan, Yuzhi Huang, Yue Huang, Jingyan Jiang  
**方向**：推理  
**代码**：暂无

本文提出 TAU-Bench，一个面向视频异常理解（VAU）的 track-centric 基准测试，将异常实例追踪与细粒度异常理解联合评估。该基准包含 1,118 段视频、1,454 条轨迹和 20 万余个像素级掩码，并提供连接实例识别、事件理解与场景推理的分层标注。实验表明，当前 VLMs 虽能生成合理的异常描述，但在正确定位并持续追踪异常实例上仍存在显著差距，凸显了实例 grounding 评估对构建可信 VAU 系统的重要性。

### [GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?](https://arxiv.org/abs/2608.05747)

**作者**：Qifeng Zhang, Kaixiang Huang, Heng Dong, Huang Fang, Junting Chen, Junjie Zhu, Yonghang Chen, Zhiyu Zhang, Wei Li  
**方向**：推理  
**代码**：暂无

本文提出 GST-Bench，一个用于评估视频理解中全局空间智能的 VQA 基准，要求模型从输入视频中未见过的新视角进行空间推断，并将第一视角观测映射到全局俯视图像。该基准包含 6,790 分钟合成视频生成的人工校验问题，并配套 GST-Train 数据集以促进全局空间推理研究。在 22 个先进 VLM 上的评估显示，最强零样本模型得分仅 42.68，远低于人类的 79.08，揭示了模型在整合长时程观测为全局一致场景表示方面的核心瓶颈。

### [Beyond Relevance: Bayesian Evidence Acquisition for Agentic Whole-Slide Image Reasoning](https://arxiv.org/abs/2608.05757)

**作者**：Bryan Wong, Xun Xu, Huazhu Fu, Nancy F. Chen, Mun Yong Yi  
**方向**：推理  
**代码**：[Code](https://github.com/bryanwong17/BEACON)

本文提出 BEACON，一个无需训练、即插即用的 agentic 框架，将整张幻灯片图像（WSI）推理重新建模为贝叶斯证据获取问题。该方法通过维护对竞争诊断假设的概率信念，并以最大化期望信息增益（EIG）的方式顺序采 patch，从而高效降低诊断不确定性；证据控制器决定回答、继续采样或进行更高分辨率检查。在 5 个 WSI-VQA 基准的零样本实验中，BEACON 在训练自由的 agentic 方法中取得最佳整体性能，同时显著提升了证据获取效率。

### [Evidence-Driven Dynamic Visual Selector for Efficient Long Video Understanding](https://arxiv.org/abs/2608.05780)

**作者**：Bo Zhang, Wenxin Wang, Feng Chen, Zhihao Zhang, Zixuan Wang, Changsheng Li, Yinjie Lei  
**方向**：推理  
**代码**：暂无

本文提出 EviSelect，一种面向 MLLM 长视频理解的细粒度动态视觉选择框架，通过目标模型的内部注意力证据来指导查询相关的时空采样。该方法利用高度压缩的视觉输入与稀疏注意力近似目标 MLLM 的注意力图，并基于三类互补注意力分量设计轻量选择器，实现查询相关时间戳定位、局部采样率与空间分辨率的自适应调整。在 3 个长视频理解基准上，EviSelect 在降低约 50% 视觉 token 并带来 3.9 倍端到端加速的同时，取得了优于现有方法的性能。

### [Learning visual representations for compositional analysis of artworks and photographs](https://arxiv.org/abs/2608.06142)

**作者**：Fatemeh Behrad, Tinne Tuytelaars, Johan Wagemans  
**方向**：推理  
**代码**：暂无

本文对比了两种艺术/摄影作品构图分析范式：一种受感知分组启发的以人为本方法，以及基于大规模构图数据集微调基础模型的方法。前者利用以对象为中心的模型进行区域级分解，并通过图注意力网络建模元素间空间关系，在冻结编码器下保持可解释性；后者在数据充足时显著优于前者，但牺牲了可解释性与跨域泛化能力。实验涵盖构图评分/类别预测、构图图像检索与视觉 saliency 检测，系统揭示了不同范式在表征学习与泛化之间的权衡。

## 基准

### [Context Matters: Support Set Selection and Failure Detection for In-Context Medical Image Segmentation](https://arxiv.org/abs/2608.05333)

**作者**：Youssef Gehad, Emmanuel Zerefa, Krish Kabra, Guha Balakrishnan  
**方向**：基准  
**代码**：暂无

本文研究了医学图像分割中上下文学习（ICL）支持集的选择策略，提出基于查询图像视觉相似度的样本选择方法，并训练了一个基于Transformer的分类器来预测分割是否会低于指定IoU阈值。在四个基准和三种成像模态上的实验表明，相似度选择在小样本支持下始终优于随机采样，且失败预测显著高于随机水平，为临床安全部署提供了实用机制。

### [Adapting Vision Foundation Models with Cascaded Semantics](https://arxiv.org/abs/2608.05393)

**作者**：Xi Xiao, Xingjian Li, Cheng Han, Tianyang Wang, Lin Zhao, Yunbei Zhang, Guosheng Hu, Runmin Jiang, Xi Li, Xiao Wang, Min Xu  
**方向**：基准  
**代码**：[Code](https://github.com/xixiaouab/Cascaded-Semantics)

本文提出了一种面向视觉提示微调（VPT）的级联语义注入方法，通过经典算子提取颜色、纹理、形状等基础图像先验，并结合自注意力图提供实例级特征空间语义。在34个图像分类数据集上的实验表明，该方法仅微调0.74%的ViT参数即可取得优异的下游迁移性能。

### [From Sports to Safety: Benchmarking Proactive Risk Inference in MLLMs](https://arxiv.org/abs/2608.05560)

**作者**：Jiawei Qiu, Yichen Xu, Jianzhe Ma, Mingyang Yu, Wenbin Zhu, Yang Han, Pinzheng Lv, Wenxuan Wang  
**方向**：基准  
**代码**：[Code](https://github.com/DawnGavial/SPRINT)

本文提出了SPRINT基准，包含2,888段真实运动视频，用于评估多模态大语言模型（MLLMs）在物理危害发生前的主动推理能力。实验发现当前MLLMs虽能高灵敏度地发出危险信号，但在识别事故原因上表现不足，且显式危险查询会在安全视频中引发严重误报，揭示了其在动态物理环境中主动安全能力的表面性。

### [ALTER: Modeling Longitudinal Changes via Regional Differencing for 3D CT Report Generation](https://arxiv.org/abs/2608.05615)

**作者**：Dongchen Li, Jitao Liang, Wei Li  
**方向**：基准  
**代码**：[Code](https://github.com/peytonkarlie/ALTER/tree/main)

本文提出了ALTER框架，通过解剖区域级别的时序差异建模来生成3D CT随访报告，包括全局先验整合、区域代理差异和间隔变化融合三个模块。在RadGenome-ChestCT和CTRG-Chest-548K数据集上，ALTER在多数指标上达到了当前最优性能。

### [URNet: A Unified Reparameterized Network for Efficient RGB-D Semantic Segmentation](https://arxiv.org/abs/2608.05671)

**作者**：Guoan Xu, Zhengxue Wang, Yang Xiao, Ligeng Chen, Guangwei Gao, Dongchen Zhu  
**方向**：基准  
**代码**：[Code](https://github.com/Wild-Stephen/URNet)

本文提出了URNet，一种统一重参数化的RGB-D语义分割网络，在单个编码器中同时完成多模态特征提取与跨模态融合。通过线性门控注意力（LGA）模块和金字塔融合解码器（PMD），URNet在多个RGB-D分割基准上取得了state-of-the-art性能，同时保持较高的推理效率。

### [STAIL: Semantic Text-Anchored Incremental Learning for Medical Imaging via Large Language Models](https://arxiv.org/abs/2608.05808)

**作者**：Songpan Gao, Yajie Zhang, Guanxing Chen, Jiayu Qian, Zhenzhen Liu, Shijun Li, Xiaowei Zhu, Yao Hu, Kay Chen Tan, Yu-An Huang, Shiqi Wang, Zhi-An Huang  
**方向**：基准  
**代码**：[Code](https://github.com/Gao-leon/STAIL)

本文提出了STAIL框架，利用大语言模型（LLM）稳定的语义空间作为发展先验，通过文本锚定机制缓解医学影像连续学习中的灾难性遗忘。该方法引入非对称语义巩固缓冲区（SCB），以少量图像锚点和大量文本描述重建旧任务语义，在眼底、超声和X光三个数据集上显著提升了基线模型的持续性能并降低了遗忘。

### [Accurate Localization of Road Traffic Objects on the Road Plane Using Surveillance Camera Imagery](https://arxiv.org/abs/2608.05840)

**作者**：Jan Gawroński, Witold Czajewski  
**方向**：基准  
**代码**：暂无

本文提出了一种两阶段几何感知定位流程，用于从单目监控图像中将车辆足迹投影到道路平面。该方法先用YOLO26检测车辆，再用ResNet34回归网络预测投影底面的四个角点，在DAIR-V2X数据集上将平均图像空间定位误差降低了51.8%，对远距离车辆和强透视畸变场景改进尤为显著。

### [Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models](https://arxiv.org/abs/2608.05960)

**作者**：Maulik Chevli, Johannes Brandt, Rickmer Braren, Daniel Rueckert, Philip Müller  
**方向**：基准  
**代码**：[Code](https://github.com/maulikchevli/frozen-lexpert)

本文对十种冻结的3D CT基础模型在三个胸部CT队列上进行了系统基准测试，评估其诊断覆盖范围。研究发现模型性能主要由病灶与周围组织的对比度和空间尺度决定，而非架构本身；大尺度、高对比度异常较易检出，而小尺寸、低对比度病灶仍是所有编码器的共同瓶颈。

### [Universal Concept Disruption for SAM3 Image Segmentation](https://arxiv.org/abs/2608.05983)

**作者**：Hao Wang, Yuxuan Zhang, Wei Yang  
**方向**：基准  
**代码**：暂无

本文首次针对SAM3开放词汇概念分割提出了通用跨概念对抗攻击方法UCD，通过学习单一有界图像扰动同时干扰文本条件路径、共享视觉特征和presence-gated（存在门控）概念分数。在SACo-Gold、LVIS、RefCOCO、PhraseCut和OpenImages数据集上，UCD显著降低了mask AP和cgF1，且能迁移到SAM3.1和视频推理。

### [PaCoNet: Deep Data Extraction for Parallel Coordinates](https://arxiv.org/abs/2608.06030)

**作者**：Poonam Poonam, Hannah Kniesel, Pere-Pau Vázquez, Timo Ropinski  
**方向**：基准  
**代码**：[Code](https://github.com/poonam2308/PaCoNet)

本文提出了PaCoNet，首个用于从平行坐标可视化图像中提取数据的深度学习方法，不仅能提取折线坐标，还能恢复单个数据样本。作者还构建了一个大规模平行坐标数据集，实验表明PaCoNet显著优于未适配的基线方法，为复杂可视化分析与自动重设计奠定了基础。

### [HOPE: Hand-Object Pressure Estimation from Monocular Videos](https://arxiv.org/abs/2608.06192)

**作者**：Subin Jeon, Byungjun Kim, Hanbyul Joo  
**方向**：基准  
**代码**：暂无

本文提出了HOPE框架，将手部-物体压力估计建模为以手部为中心的视频预测任务，直接在手部网格顶点上预测时变法向压力和接触状态。通过将多种压力与接触标注统一到手部顶点空间，并引入顶点锚定的视频Transformer，HOPE在OpenTouch、PressureVisionDB等基准上验证了其对裸手第一人称和野外视频的泛化能力。

### [PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation](https://arxiv.org/abs/2608.06240)

**作者**：Elad Yoshai, Natan T. Shaked  
**方向**：基准  
**代码**：暂无

本文提出了PRISM，一种无GAN的流匹配框架，通过可学习的逐特征门控替代全局噪声控制，实现非配对图像翻译中内容保持与外观转换的解耦。在五个自然与生物医学基准上，PRISM在四个数据集上取得了最优的Inception FID和KID，在组织病理学图像上也能更好地保持细胞核数量比例。

### [Toward Deployable Bangla Sign Language Recognition with Expert-Validated Data and a Lightweight Attention-Based Model](https://arxiv.org/abs/2608.06252)

**作者**：Saad Ahmed, Md Khalid Syfullaha  
**方向**：基准  
**代码**：暂无

本文发布了孟加拉手语数据集RSBdSL38，包含10,874张由专家校验的38类手语图像，并提出了一种仅298,470参数的轻量注意力卷积网络。该模型从零训练在多个BdSL基准上达到与ImageNet预训练模型相近的精度，同时参数和计算量显著降低，量化后可在普通智能手机上实时运行。

## Agent

### [Text-Guided Refinement of Multi-sequence Glioma Subregion Segmentation with a Vision-Language Foundation Model](https://arxiv.org/abs/2608.05389)

**作者**：Zach Eidex, Yu-nong Lin, Mojtaba Safari, Sean Pitroda, Ralph Weichselbaum, Zhen Tian, Xiaofeng Yang  
**方向**：Agent  
**代码**：暂无

该研究基于三维视觉-语言基础模型VoxTell，提出轻量级文本引导的脑胶质瘤多亚区分割精修框架。通过将包含目标、动作、位置等信息的临床指令编码为可训练投影注入多尺度解码器，在BraTS-GLI内测及跨数据集测试上均显著提升Dice相似系数，且对正确、空白与矛盾提示表现出明显区分，展现出作为临床医生在环工具的潜力。

### [APQF: Agentic Profiling-Guided Structured Pruning and Mixed-Precision Quantization with Adaptive Fine-Tuning](https://arxiv.org/abs/2608.05499)

**作者**：Sadegh Jafari, Mohiuddin Bilwal, Fan Zhou, Brian Gelder, Ali Jannesari  
**方向**：Agent  
**代码**：暂无

本文提出APQF框架，将结构化剪枝、混合精度量化感知训练与精度恢复整合为自动化流程。分析Agent测量模型各层成本与压缩敏感度，再由LLM规划器生成逐层剪枝比例、位宽及恢复策略；在ImageNet-1k上实现13-18倍比特运算压缩且精度接近基线，验证了基于剖析的LLM决策对CNN与ViT联合压缩的有效性。

### [Overcoming Attention Drift: Homogeneity-Heterogeneity Guided Feature Aggregation for Low-Light Remote Sensing Image Enhancement](https://arxiv.org/abs/2608.05843)

**作者**：Yaozi Zhong, Xingxing Yang, Shaohui Mei, Mingyang Ma  
**方向**：Agent  
**代码**：暂无

本文提出HALO框架，将极低光照遥感图像增强建模为由基础模型先验引导的特征聚合问题。通过光照不变语义先验提供区域同质性正约束，并以伪三维拓扑先验抑制跨边界特征混淆，进而设计H2CAM模块协同融合两种先验；在8个合成与真实遥感基准上取得SOTA，显著改善边界清晰度与色彩保真度。

### [The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents](https://arxiv.org/abs/2608.06065)

**作者**：Weiwei Li, Junzhuo Liu, Tong Chu, Hengfu Yu, Wen Li  
**方向**：Agent  
**代码**：暂无

本文提出Gated Hindsight Distillation（GHD）用于训练移动GUI Agent。该方法在训练时利用后续截图作为特权 hindsight 信息，让共享参数的教师模型对学生在当前截图上的响应重新打分，并仅在学生失败且 hindsight 可恢复正确动作时进行蒸馏；在AndroidWorld与AndroidLab上显著优于GRPO，提升了Agent对延迟证据的推理能力。

### [Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal Case](https://arxiv.org/abs/2608.06075)

**作者**：Shilin Hu, Jingyi Xu, Dimitris Samaras, Hieu Le  
**方向**：Agent  
**代码**：暂无

本文针对阴影去除任务，提出基于Agent的候选选择与物理先验约束流程。通过让商业视觉-语言模型生成多个编辑候选，再由评估器依据阴影形成的物理原理筛选过滤，平衡阴影去除与场景内容保持；在ShadowRemovalRefine基准上CDD降至0.0075，较最优基线降低至少47%，表明经典低层视觉先验仍可有效约束生成模型。

### [Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training](https://arxiv.org/abs/2608.06125)

**作者**：Rui Li, Yuanzhi Liang, Ke Hao, Ziqiao Weng, Haibin Huang, Chi Zhang, XueLong Li  
**方向**：Agent  
**代码**：暂无

本文提出SURE框架，在潜在空间学习奖励分布以估计不确定性，并据此引导图像与视频扩散模型的密集后训练。SURE-LRM为每个噪声潜在预测高斯效用，SURE-REFL将其方差转化为可靠性权重，仅对局部转移加权回传；无需像素解码即可实现沿去噪轨迹的不确定性感知优化，在多个指标上达到SOTA并提升训练稳定性。

### [Depth-Guided Video Object Counting in Crowded Scenes](https://arxiv.org/abs/2608.06236)

**作者**：Yuanjing Xu, Xinyan Liu, Weidong Chen, Zixuan Zou, Linhao Zhang, Zhuangzhe Meng, Antoni B. Chan, Weigang Zhang  
**方向**：Agent  
**代码**：[Code](https://github.com/streamer-AP/DG-Net)

本文提出Depth-Guided Detector（DG-Det）与统一去重后处理框架，用于拥挤遮挡场景的视频目标计数。通过多尺度RGB-D交叉注意力融合深度线索，并显式预测遮挡关系以增强空间理解；同时发布首个RGB-D视频目标计数数据集，实验显示相比现有基线MAE降低62.01%。

## 生成

### [Innocent Panels, Hateful Stories: Evaluating and Detecting Hateful Intent in Multi-Turn Visual Story Generation](https://arxiv.org/abs/2608.05210)

**作者**：Ye Leng, Junjie Chu, Yiting Qu, Mingjie Li, Yun Shen, Yang Zhang  
**方向**：生成  
**代码**：暂无

本文聚焦多轮视觉故事生成中的群体级仇恨意图，构建 HatefulStoryPrompts 评测配置与 HatefulVisualStory 人工标注数据集，发现当前 T2I 模型能以极高比例完成仇恨叙事，而现有审核系统难以识别图像组的累积含义。论文进一步提出交互式监控与生成后联合分析两类防御机制，在召回率上显著超越现有安全模型，强调视觉叙事安全需从单图审核转向对交互与图像关系的推理。

### [In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion](https://arxiv.org/abs/2608.05237)

**作者**：Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi  
**方向**：生成  
**代码**：暂无

针对少步自回归视频扩散模型因依赖完全去噪的前序帧而泄露局部细节、导致时序语义与动态受损的问题，本文提出 In-Context Forcing 范式。该方法通过逐步降低上下文噪声等级实现自适应引导，既保证时间一致性又增强帧间动态，并支持跨帧并行去噪以加速推理，在 VBench 上同时提升视觉保真度与生成速度。

### [VideoArgus: Agentic Rubric-Grounded Unified Evaluation for Video Generation and Editing](https://arxiv.org/abs/2608.05485)

**作者**：Ziyun Zeng, Zixuan Wang, Yongsheng Yu, Hang Hua, Jiebo Luo  
**方向**：生成  
**代码**：暂无

本文提出 VideoArgus，一个面向视频生成与编辑的统一评估框架，为每个输入实例生成一次输出无关的样本级评分标准，并复用于所有候选视频。该标准指导 VLM QA 与视觉工具产生可解释、带证据的指标与诊断报告；在 VideoArgus-Bench 与人类对齐集上的实验表明，其排序与打分相关性优于各任务专用评估器。

### [Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663)

**作者**：Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
**方向**：生成  
**代码**：暂无

本文提出 Vorch-Streamer，一种面向实时长时文本到音视频（T2AV）流式生成的后训练框架。通过构建 80K 合成头像片段训练因果生成器，结合长程 Self Forcing、DMD 蒸馏与外部语言模型预测的 25Hz 语音规划 token，在 27.12 FPS 下实现联合音视频生成，满足实时播放需求并保持身份一致与音视频同步。

### [Engram-E2VID: Reference-Based Event-to-Video Reconstruction via Generative Activation of Appearance Engrams](https://arxiv.org/abs/2608.05728)

**作者**：Feiyu Ji, Xiang Li, Hao Ma, Tianxiang Huang, Qingxin Lu, Mengqi Ji, Lei Han, Xiaokang Yang, Xiaoyun Yuan  
**方向**：生成  
**代码**：暂无

本文提出 Engram-E2VID，一种基于参考帧的事件到视频重建方法，通过生成式激活外观记忆（appearance engrams）解决事件流稀疏异步、缺乏绝对外观信息的难题。该方法将参考帧编码为 token 空间外观记忆，并用事件流构建目标时刻运动结构支架，在扩散骨干中逐步激活相关外观 token，在多个基准上显著改善 PSNR 与 LPIPS。

### [Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776)

**作者**：Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
**方向**：生成  
**代码**：暂无

本文提出 Vorch-Director，一种噪声感知的残差修正策略，用于缓解自回归音视频生成中因训练使用干净历史、推理依赖生成历史而导致的误差累积。通过将注入残差与其 originating noise level 对齐，该方法生成更真实的自回归历史；在 LTX-2 基础上引入任务嵌入与混合任务训练，支持多镜头、多主体、参考引导的长时音视频生成。

### [Vorch-Omni: Multi-Task Orchestration of Sight and Sound](https://arxiv.org/abs/2608.05803)

**作者**：Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang  
**方向**：生成  
**代码**：暂无

本文提出 Vorch-Omni，一种基于任意条件到任意输出的统一多任务音视频合成框架。通过 token 级条件掩码与任务标识区分目标、源内容与参考信号，并借助 VLM 文本解读与视频 VAE 隐式编码两条互补视觉条件路径，单一 flow-matching DiT 即可支持文本/图像/参考/音频驱动、时序扩展、视频转换与音视频编辑等十余项任务。

### [Controllable Clothing: Precise Labels and Generation for Virtual Try-On with Latent Diffusion Models](https://arxiv.org/abs/2608.05834)

**作者**：Max Rehman Linder  
**方向**：生成  
**代码**：暂无

本文提出一种面向虚拟试衣（VITON）的可控服装生成方法，利用开源 AI 模型为服装图像自动标注长度、款式等精确标签，并基于这些标签与图像配对训练 adapter。用户可通过标签控制生成结果，使零售商能够生成更贴合真实穿着效果的展示图，减少误导消费者的风险。

### [MAVISEG: Manifold Propagation and Visual Prototypes for Zero-Shot Open-Vocabulary Segmentation in Diffusion Transformers](https://arxiv.org/abs/2608.05878)

**作者**：Rajatsubhra Chakraborty, Xujun Che, Ritabrata Chakraborty, Xi Niu, Depeng Xu  
**方向**：生成  
**代码**：暂无

本文提出 MAVISEG，一种无需训练的扩散 transformer 开放词汇分割精化层。通过挖掘生成轨迹的时序结构、视觉原型与图像特征几何关系，该方法对像素级分类得分场进行后处理，在六个基准上取得当前最优的训练无关方法 mIoU，且初始捕捉越差时提升越明显。

### [Wan-Animate-2: Pushing the Application Boundaries of Character Animation](https://arxiv.org/abs/2608.06009)

**作者**：Guangyuan Wang, Li Hu, Dechao Meng, Zhongyi Zhang, Peng Zhang, Mingyang Huang, Ruoshi Zhang, Ke Sun, Zhe Zhang, Xingjun Wang, Gang Cheng, Bang Zhang  
**方向**：生成  
**代码**：[Code](https://github.com/Wan-Video/Wan-Animate-2)

本文提出 Wan-Animate-2，一种端到端角色动画框架，直接在重设计的 Diffusion Transformer 中消费驱动视频，避免显式运动表示的提取误差与身份漂移。方法引入文本驱动的视角控制，并提出 Wan-Animate-2-Lite 高效变体，通过三阶段训练将推理延迟降至实时阈值，支持流式角色动画与交互式应用场景。

### [EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231)

**作者**：Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
**方向**：生成  
**代码**：暂无

本文提出 EmoWorld，在冻结的 flow-matching Video DiT 中将全局氛围、语义情感线索与时序演化解耦。通过 Visual Atmosphere Steering、Semantic Affective Steering 与 Temporal Affective Steering 三种机制，在 27 类情感上显著提升目标情感对齐度，并支持跨 Video-DiT 骨干迁移与相机条件组合。

## 3D

### [CDSeg: A Renderable Gaussian Carrier for Image-to-3D Label Transfer](https://arxiv.org/abs/2608.05482)

**作者**：Wentao Sun, Yiping Chen, Zhengsen Xu, Jonathan Li, John S. Zelek  
**方向**：3D  
**代码**：[Code](https://github.com/w27sun/CDSeg)

本文提出 CDSeg，一种无需任务专属 3D 分割训练、基于可渲染 Gaussian 原语的 2D 到 3D 标签迁移接口。该方法通过渲染可见性将 2D 掩码分配给 3D Gaussian，并利用多视角投票与局部滤波融合标签，支持 promptable、实例、语义及 LiDAR 等多种设置。在 DesktopObjects-360、NeRDS-360 和 ScanNet-v2 上分别取得了 92.35%、95.89% 和 65.77% 的 mIoU，证明 2D 图像模型的分割能力可以高效复用到点云、Gaussian 场景与新视角中。

### [Hierarchical Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2608.05557)

**作者**：Linhao Wang, Qichang Zhang, Ye Su, Hao Wang  
**方向**：3D  
**代码**：暂无

本文提出 Hierarchical Flow Matching（HFM），一种面向无条件 3D 点云生成的双层 Flow Matching 框架。模型先在紧凑隐空间中通过 Latent Flow Matching 学习全局形状流形，再基于隐编码通过 Conditional Point Flow Matching 重建局部几何细节，训练仅使用 MSE 损失。直 OT 路径使每条流仅需 15 步 Euler 采样，在 ShapeNet 和 ModelNet 上取得领先性能，且结构化隐空间可支持分类等下游任务。

### [SR-JEPA: Learning Predictive Latent State in 3D Scenes](https://arxiv.org/abs/2608.05774)

**作者**：Zihan Zhou, Qifu Wen, Xi Zeng  
**方向**：3D  
**代码**：暂无

本文提出 SR-JEPA，一种面向场景级点云的原生 3D Joint-Embedding Predictive Architecture，可在给定空间位置查询被移除物体的预测性隐状态。训练仅依赖自包含的 3D EMA 目标，无需重建、语义标签或 2D 特征；在 5,953 个 ARKitScenes 保留对象上，隐状态语义身份识别准确率显著高于强基线。实验还表明该隐状态能与锚点身份和几何信息结合，揭示出一种可查询、可组合的 3D 预测表示。

### [Curia-MAE: Multi-Modal Multi-Anatomy MAE Pre-Training for 3D Medical Image Segmentation](https://arxiv.org/abs/2608.05844)

**作者**：Théo Danielou, Antoine Saporta, Léo Alberge, Corentin Dancette  
**方向**：3D  
**代码**：暂无

本文提出 Curia-MAE，一种基于卷积 MAE 的多模态、多解剖部位 3D 医学图像预训练模型，使用 30 万张 CT 和 MRI 图像进行训练。方法在重建目标、特征正则化和局部-全局相似性目标上进行了增强，显著提升了冻结编码器在 8 个分割基准上的性能，尤其在标注稀少的病灶任务上表现优于 nnU-Net。结果表明单一冻结编码器即可跨多种分割任务复用，有助于降低临床部署成本。

### [UQ-Loc: Uncertainty-Aware LiDAR Scene Coordinate Regression](https://arxiv.org/abs/2608.06307)

**作者**：Jacek Komorowski  
**方向**：3D  
**代码**：暂无

本文提出 UQ-Loc，一种不确定性感知的 LiDAR 场景坐标回归方法，在 LightLoc 基础上增加各向异性 Gaussian 协方差头，逐体素预测 3×3 正定协方差矩阵。训练采用 NLL 损失与 kNN 空间平滑正则，推理时在改进的 SC2-PCR 求解器中引入不确定性加权评分与 Mahalanobis 距离内点检验。实验表明 UQ-Loc 在提升 6-DoF 定位精度的同时，能够输出校准良好的协方差估计。

## 检索

### [Invisible Shortcuts: Why Vision Encoders Know Your Camera](https://arxiv.org/abs/2608.05424)

**作者**：Vladan Stojnić, Ryan Ramos, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias  
**方向**：检索  
**代码**：[Code](https://github.com/ryan-caesar-ramos/visual-encoder-traces)

本文发现深度视觉编码器会利用嵌入在像素层面的不可见元数据痕迹（如图像处理与拍摄参数）作为捷径，大规模语义监督在预训练过程中会自然诱导元数据-语义相关性。研究提出了在预训练期间及之后降低模型对元数据敏感度的缓解策略，同时指出元数据敏感性也有助于解释部分编码器在生成图像检测和分布外泛化上的优势。

### [HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models](https://arxiv.org/abs/2608.05523)

**作者**：Yuanruyi, Yue Cao, Haojia Gao, Guanqiu Guo, Ziyuezhang, Shangqin, Junbo Tan, Bokui Chen, Zhuo Zou, Xueqian Wang  
**方向**：检索  
**代码**：暂无

针对潜在世界模型在遮挡场景下进行物理预测时难以利用已不可见的历史证据这一问题，本文提出 HERA 框架，通过 Register-Routed Patch Memory（RRPM）将保留的历史证据选择性路由到冻结的潜在预测器中。在 IntPhys2 上，HERA 将 V-JEPA 2-G 的成对 AvgSurprise 准确率从 52.57% 提升至 54.35%，并在固定相机连续性与不变性子集上取得显著增益。

### [EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object Removal](https://arxiv.org/abs/2608.05565)

**作者**：Feier Wu, Wanke Xia, Xu He, Zilang Zhou, Si Chen, Dongxia Liu, Liyang Chen, Qimeng Wu, Zhengbo Zhang, Wenming Yang, Zhiyong Wu  
**方向**：检索  
**代码**：[Code](https://github.com/MorleyOlsen/EffectLearner-Official)

本文提出 EffectLearner，一种结合 VLM 驱动的 Object-Effect Reasoner 与 DiT 视频擦除器的真实世界视频物体移除框架，通过结构化效应分析提示提取效应感知上下文以指导完整的目标物体及其诱导效应消除。研究还构建了 EffectWorld 数据集并设计渐进式训练课程，在 ROSE-Bench、EffectWorld-Eval 和 EffectWorld-Wild 上均优于现有基线。

### [VSMP-IMU: Video-Grounded Semantic Motion Programs for Sensor-Aware Synthetic IMU Generation](https://arxiv.org/abs/2608.05782)

**作者**：Lala Shakti Swarup Ray, Vitor Fortes Rey, Mengxi Liu, Paul Lukowicz, Bo Zhou  
**方向**：检索  
**代码**：暂无

本文提出 VSMP-IMU，一种基于语义运动程序（SMP）的视频 grounded 可控合成 IMU 生成框架，将决定活动的语义与保留标签的变化分离开来，从而缓解视频驱动方法对姿态估计的敏感性和文本驱动方法弱 grounded 的问题。在五个公开 IMU-HAR 数据集上，该方法在低资源、长尾和跨被试泛化场景下均显著优于真实数据训练及现有合成基线。

### [Energy-Guided Flow Matching](https://arxiv.org/abs/2608.05811)

**作者**：Haoyang Tong, Yu He, Fang Li, Lichen Ma, Jingling Fu, Dong Chen, Zhen Chen, Junshi Huang, Jie Cao  
**方向**：检索  
**代码**：[Code](https://github.com/ysng123/EG-FM)

本文提出 Energy-Guided Flow Matching（EG-FM），通过热核滤波动态端点替代固定干净图像端点，显式建模从低频到高频的由粗到细生成轨迹，并由图像特定能量引导调度逐步释放高频信号。该框架无需修改骨干网络与训练数据，在 ImageNet 256×256 和 512×512 条件生成以及文本到图像生成任务上均取得更低的 FID 和更优的 GenEval/DPG-Bench 分数。

### [To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generation](https://arxiv.org/abs/2608.05879)

**作者**：Xiaobin Huang, Zilong Huang, Yang Luo, Hongchao Fan, Yiping Chen, Ting Han  
**方向**：检索  
**代码**：暂无

本文提出 HoloWorld，一个统一的室内外城市世界生成框架，通过持续更新的跨尺度世界上下文，将城市级规划、建筑外观与室内场景显式关联起来，实现自回归式街区 exterior 生成和基于 3D 建筑实例的室内生成。据作者所知，这是首个在连贯 3D 城市世界中统一室内外生成的框架，在 urban exterior 生成与建筑级室内外一致性上均超越现有方法。

### [Topology-Aware Neighborhood Learning for Source-Free Cross-Scene Hyperspectral Image Classification](https://arxiv.org/abs/2608.05964)

**作者**：Qingmei Li, Juepeng Zheng, Jiarui Zhang, Jianxi Huang, Haohuan Fu  
**方向**：检索  
**代码**：暂无

本文提出一种面向无源跨场景高光谱图像分类的拓扑感知邻域学习框架，利用熵动量伪标签（EMP）精炼 k-means 分配，并通过上下文邻域拓扑（CNT）结合协同表示的全局结构与最近邻的局部相似性来编码目标域特征空间的流形几何特性。在三个典型跨场景数据集上的实验表明，该方法在无需源数据的情况下超越了现有最先进方法。

### [DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval](https://arxiv.org/abs/2608.06059)

**作者**：Xi Chen, Xu Chen, Xiangyang Jia, Wei Wang, Xu Zhang, Zhenyuan Sun  
**方向**：检索  
**代码**：暂无

本文提出 DARAD，一种面向持续遥感图像-文本检索（RS-ITR）的双适配器与排序感知蒸馏框架，通过视觉分支的空间融合适配器和文本分支的多专家语义路由来缓解尺度变化与分布漂移导致的跨模态对齐空间畸变，并利用双向排序蒸馏保持历史跨模态排序结构。多阶段持续检索协议下的实验表明，DARAD 在适应新数据的同时有效保持了历史数据检索性能。

### [CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection](https://arxiv.org/abs/2608.06205)

**作者**：Nima Hatami, Karim Faez, Saeed Sharifian, Hamidreza Amindavar  
**方向**：检索  
**代码**：[Code](https://github.com/NimaHatami99/CFGPNet)

本文提出 CFGPNet，一种面向多光谱目标检测的交叉注意力融合梯度编程网络，采用改进的 GELAN 骨干、Cross Computation Efficient Attention（CrossCEA）模块、Attention Selection and Aggregation Fusion（ASAF）网络以及可编程梯度辅助分支，以增强跨模态交互、稳定模态分布差异下的融合并降低计算开销。在 FLIR、M3FD、LLVIP、VEDAI 和 MFAD 五个基准上均取得了优异的精度-效率权衡。

---

**论文总数统计**：本次共收录 57 篇多模态相关论文，其中 17 篇提供公开代码仓库，覆盖 7 个研究方向。
