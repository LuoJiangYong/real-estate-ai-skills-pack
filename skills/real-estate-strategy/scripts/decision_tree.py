"""
地产产策决策树 - 根据项目特征自动推荐工作流程
"""
import sys

def run_decision_tree(project_type=None, stage=None, has_data=None):
    """
    project_type: 住宅/商业/综合体/文旅/产业（默认推断）
    stage: 投前/定位/深化/开盘（默认投前）
    has_data: 用户是否已提供数据（默认否）
    """
    print("=== 产策决策树 ===")
    print()

    if not stage:
        print("【阶段判断】请告诉我是哪个阶段：")
        print("  1 - 投前可研（拿地前）")
        print("  2 - 定位策划（拿地后）")
        print("  3 - 深化设计（方案阶段）")
        print("  4 - 开盘准备（营销阶段）")
        print()
        return

    if stage == "1" or stage == "投前":
        print("[阶段：投前可研]")
        print()
        print("【必须完成】6大风险排查（不可跳过）")
        print("  → 设计条件 / 用地风险 / 信息跟踪")
        print()
        print("【核心任务】价值挖掘")
        print("  → 奖励政策 / 成本策划 / 限价策略")
        print()
        print("【输出】《投前风险排查清单》+ 《价值挖掘建议》")
        print()
        print("【脚本】python scripts/generate_report.py risk 项目名")

    elif stage == "2" or stage == "定位":
        print("[阶段：定位策划]")
        print()
        print("【三步法】土地 → 市场 → 客户 → 产品方案")
        print()
        print("【必读参考】")
        print("  → references/产品定位方法.md（四要素）")
        print("  → references/工作机制.md（评审要点）")
        print()
        print("【输出】《产品定位报告》")
        print()
        print("【脚本】python scripts/generate_report.py competitive 项目名")

    elif stage == "3" or stage == "深化":
        print("[阶段：深化设计]")
        print()
        print("【重点】产品方案深化 + 成本适配")
        print()
        print("【参考】投前产策要点.md 中的成本策划部分")

    elif stage == "4" or stage == "开盘":
        print("[阶段：开盘准备]")
        print()
        print("【重点】客户验证 + 营销定位")
        print()
        print("【参考】工作机制.md 中的七大典型问题")

    print()
    print("=== 需要我帮你做哪一步？===")

if __name__ == "__main__":
    args = sys.argv[1:]
    kwargs = {}
    for arg in args:
        if '=' in arg:
            k, v = arg.split('=', 1)
            kwargs[k.strip()] = v.strip()
    run_decision_tree(**kwargs)
