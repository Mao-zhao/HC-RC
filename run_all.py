#!/usr/bin/env python3
"""
HC-RC 项目：一键运行全部实验和可视化。

用法：
  python run_all.py --exp all          # 运行全部实验
  python run_all.py --exp 1            # 仅实验一
  python run_all.py --exp 2            # 仅实验二
  python run_all.py --exp 3            # 仅实验三
  python run_all.py --viz              # 仅生成可视化
  python run_all.py --exp all --viz    # 全部实验 + 可视化
"""

import os
import sys
import argparse
import torch
import numpy as np

# 确保项目根目录在 sys.path
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_DIR)

from config.paths import ensure_dirs


def set_seed(seed=42):
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"


def run_experiment_1(device, seed):
    from experiments.exp1_parameter_efficiency import run_experiment_1
    return run_experiment_1(device, seed)


def run_experiment_2(device, seed):
    from experiments.exp2_topology_ablation import run_experiment_2
    return run_experiment_2(device, seed)


def run_experiment_3(device, seed):
    from experiments.exp3_heterogeneity import run_experiment_3
    return run_experiment_3(device, seed)


def run_all_visualizations():
    """运行全部可视化脚本。"""
    from visualization.visualize_dataset import fig1_dataset_3d_trajectory, fig2_sliding_window
    from visualization.visualize_topology import fig3_adjacency_heatmap, fig4_motif_distribution, fig5_spectral_distribution, fig17_hbm_flow
    from visualization.visualize_training import fig6_loss_curves, fig7_parameter_efficiency
    from visualization.visualize_results import fig8_main_results_bar, fig9_waterfall, fig10_scale_invariance
    from visualization.visualize_predictions import fig11_3d_trajectory_overlay, fig12_stepwise_error, fig13_violin, fig14_frame_by_frame
    from visualization.visualize_dynamics import fig15_activation_heatmap, fig16_readout_weights
    from visualization.visualize_summary import fig18_summary_poster

    print("\n" + "=" * 60)
    print("  生成可视化图表")
    print("=" * 60)

    print("\n[1/7] 数据集特征...")
    fig1_dataset_3d_trajectory()
    fig2_sliding_window()

    print("\n[2/7] 连接组拓扑...")
    fig3_adjacency_heatmap()
    fig4_motif_distribution()
    fig5_spectral_distribution()
    fig17_hbm_flow()

    print("\n[3/7] 训练动态...")
    fig6_loss_curves()
    fig7_parameter_efficiency()

    print("\n[4/7] 结果对比...")
    fig8_main_results_bar()
    fig9_waterfall()
    fig10_scale_invariance()

    print("\n[5/7] 预测样本...")
    fig11_3d_trajectory_overlay()
    fig12_stepwise_error()
    fig13_violin()
    fig14_frame_by_frame()

    print("\n[6/7] 储池动力学...")
    fig15_activation_heatmap()
    fig16_readout_weights()

    print("\n[7/7] 全景汇总...")
    fig18_summary_poster()

    print("\n全部可视化完成！")


def main():
    parser = argparse.ArgumentParser(
        description="HC-RC 项目：一键运行实验和可视化"
    )
    parser.add_argument("--exp", type=str, default="all",
                        choices=["1", "2", "3", "all", "none"],
                        help="运行哪个实验 (default: all)")
    parser.add_argument("--viz", action="store_true",
                        help="生成可视化图表")
    parser.add_argument("--seed", type=int, default=42,
                        help="随机种子")
    parser.add_argument("--device", type=str, default=None,
                        help="设备 (cuda/cpu)，默认自动检测")
    args = parser.parse_args()

    # 初始化
    set_seed(args.seed)
    ensure_dirs()
    device = args.device or get_device()

    print("=" * 70)
    print("  HC-RC 项目")
    print("  Structural Prior Beats Parameter Brute-Force")
    print(f"  Device: {device} | Seed: {args.seed}")
    print("=" * 70)

    all_results = {}

    # 运行实验
    if args.exp in ["1", "all"]:
        print("\n" + "=" * 70)
        print("  实验一：参数效率对比")
        print("=" * 70)
        all_results["exp1"] = run_experiment_1(device, args.seed)

    if args.exp in ["2", "all"]:
        print("\n" + "=" * 70)
        print("  实验二：N-Aligned 拓扑消融")
        print("=" * 70)
        all_results["exp2"] = run_experiment_2(device, args.seed)

    if args.exp in ["3", "all"]:
        print("\n" + "=" * 70)
        print("  实验三：异质掩码消融")
        print("=" * 70)
        all_results["exp3"] = run_experiment_3(device, args.seed)

    # 生成可视化
    if args.viz:
        run_all_visualizations()

    print("\n" + "=" * 70)
    print("  全部任务完成！")
    print("=" * 70)


if __name__ == "__main__":
    main()