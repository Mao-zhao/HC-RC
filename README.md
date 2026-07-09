# HC-RC 项目

> **Structural Prior Beats Parameter Brute-Force**
> 基于异质果蝇脑连接组的物理储池轨迹预测

---

## 项目简介

本项目研究果蝇中央复合体（CX）的真实突触级连接组拓扑能否作为零梯度物理储池（Reservoir Computing），在极低参数规模下实现与深度序列模型相媲美的轨迹预测性能。

**三大核心贡献**：
1. **结构先验胜于参数暴力**：78 参数的 CX 储池以 ~1/650 参数量逼近 5 万参数深度 RNN
2. **生物拓扑不可替代**：真实物理布线优于随机/模体/非回溯拓扑
3. **细胞异质性作为计算正则化**：生理掩码将大规模混沌网络误差削减 18.3%

---

## 目录结构

```
HC-RC_项目/
├── 数学模型.md              # 全部模型的数学推导
├── 程序结构设计.md           # 模块设计、数据流、接口
├── config/                  # 路径、超参数、模型注册表
├── data/                    # 数据加载、预处理、划分
├── topology/                # 拓扑构建（Random/Motif/CX/NB/HBM）
├── models/                  # 模型定义（RC/RNN/LSTM）
├── training/                # 训练器、评估、日志
├── experiments/             # 三大实验的主脚本
├── visualization/           # 18 张图的生成脚本
├── utils/                   # 数学工具、评估指标
├── results/                 # 训练结果输出
├── figures/                 # 可视化图表输出
└── run_all.py               # 一键运行
```

---

## 快速开始

### 1. 数据预处理
```bash
python data/preprocess.py
```

### 2. 预构建拓扑
```bash
python topology/cx_direct.py
```

### 3. 运行实验
```bash
#先$env:KMP_DUPLICATE_LIB_OK = "TRUE"
#按照 --exp 1 → --exp 2 → --exp 3 的顺序

# 实验一（参数效率对比）
python run_all.py --exp 1

# 实验二（拓扑消融）
python run_all.py --exp 2

# 实验三（异质掩码消融）
python run_all.py --exp 3
```

### 4. 生成可视化
```bash
python run_all.py --viz
```

---

## 模型一览

| 模型 | N | 可训练参数 | 类型 |
|------|---|-----------|------|
| Residual-LSTM | 128 | 202,115 | 深度序列 |
| Residual-RNN | 128 | 50,819 | 深度序列 |
| Tiny Residual-RNN | 25 | 903 | 深度序列 |
| CX-Direct-RC | 25 | 78 | 储池 |
| Random-RC | 25/322/512/3422 | 78-10,269 | 储池 |
| Motif-RC | 25/322/512 | 78-1,539 | 储池 |
| CX-NB-RC | 322 | 969 | 储池 |
| CX-NB-Weighted-RC | 322 | 969 | 储池 |
| 同质 CX 储池 | 3,422 | 10,269 | 储池 |
| 异质 CX 储池 (HBM) | 3,422 | 10,269 | 储池 |

---

## 参考文献

- Burri et al. "The EuRoC micro aerial vehicle datasets." IJRR, 2016.
- 果蝇连接组：neuPrint `male-cns:v1.0`
- Jaeger, H. "The 'echo state' approach to analysing and training recurrent neural networks." GMD Report, 2001.