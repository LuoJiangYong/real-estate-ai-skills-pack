"""
地产项目产策报告生成脚本
基于某品牌房企产策方法论，生成标准格式报告
支持 Markdown / HTML / Word / PPT
"""
import sys
import os
from datetime import datetime

DEFAULT_OUT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "outputs")
)


def generate_markdown(project_name, data=None) -> str:
    """生成 Markdown 格式报告"""
    d = data or {}
    today = datetime.now().strftime("%Y.%m.%d")
    return f"""# {project_name}产策定位报告

**报告日期：{today}**

---

## 一、项目概况

### 1.1 区位及配套
- 区位定位：【城市/板块/地块坐标】
- 周边配套：【商业/医疗/教育/交通】

### 1.2 四至及规划
- 四至边界：【地块四至描述】
- 轨道交通：【最近站点及步行距离】

### 1.3 不利条件
- 地质风险：【有无水坑/软土】
- 周边不利因素：【噪音/高压线等】

### 1.4 土地价值
- 外联机会：【联动积极要素】
- 内拓潜力：【通过产品可改变的属性】

---

## 二、经营策略及目标

- 战略匹配：【品牌在城市的布局目标】
- 目标成本：【成本适配策略】
- 开发节奏：【分批次开发计划】

---

## 三、客群分析及方案推导

### 3.1 三层客群定位

| 层次 | 客群描述 |
|------|---------|
| 地缘客群 | 周边原有居民、板块内换房需求 |
| 辐射客群 | 可控通勤时间内可覆盖的外区客群 |
| 溢出客群 | 主城区低供高价板块外溢客户 |

### 3.2 竞品分层

| 层级 | 代表项目 | 地价 | 主力产品 | 均价 |
|------|---------|------|---------|------|
| 上游 | - | - | - | - |
| 同级 | - | - | - | - |
| 下游 | - | - | - | - |

### 3.3 客户画像
【目标客群：职业/年龄/家庭/核心需求】

### 3.4 客户语录
【定性研究具象化，引述真实客户原话】

---

## 四、项目整体策划

### 4.1 产品规划
- 产品类型：【高层/小高/洋房/叠拼等】
- 户型配比：【面积段 × 房间数】
- 价格定位：【均价/总价段】

### 4.2 户型设计原则
【面宽取舍/关键空间尺度/特色场景】

### 4.3 产品配置
【精装标准/会所/园林风格】

### 4.4 商业设计
【商业规模/街区商业/底商】

### 4.5 社区底盘
【总图排布/归家动线/景观轴线】

---

## 五、组织及跟投（可选）

---

*本报告由 AI 基于某品牌房企产策方法论自动生成，数据请自行核实。*
"""


def generate_html(project_name, data=None) -> str:
    """生成 HTML 格式报告"""
    md = generate_markdown(project_name, data)
    # 简单 Markdown 转 HTML
    html_body = md
    html_body = html_body.replace('# ', '<h1>').replace('## ', '<h2>').replace('### ', '<h3>')
    html_body = html_body.replace('**', '<b>').replace('</b>**', '</b>')
    html_body = html_body.replace('\n\n', '</p><p>').replace('\n- ', '<li>')
    html_body = html_body.replace('| ', '<tr><td>').replace(' | ', '</td><td>').replace(' |', '</td></tr>')
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{project_name}产策定位报告</title>
<style>
body{{ font-family: 'Microsoft YaHei', Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #1a1a2e; line-height: 1.8; }}
h1{{ color: #0D1B3E; border-bottom: 3px solid #C9A855; padding-bottom: 10px; }}
h2{{ color: #0D1B3E; margin-top: 30px; }}
table{{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
td, th{{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
th{{ background: #0D1B3E; color: #fff; }}
</style>
</head>
<body>
<h1>{project_name}</h1>
<p><i>报告日期：{datetime.now().strftime('%Y.%m.%d')}</i></p>
{html_body}
</body>
</html>"""


def save_output(project_name, content, fmt, out_dir=None):
    """保存输出文件"""
    target_dir = os.path.abspath(out_dir or DEFAULT_OUT_DIR)
    os.makedirs(target_dir, exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")
    safe_name = project_name.replace(' ', '_').replace('/', '_')
    if fmt == 'html':
        fname = f"{safe_name}_{today}.html"
        fpath = os.path.join(target_dir, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
    elif fmt == 'markdown':
        fname = f"{safe_name}_{today}.md"
        fpath = os.path.join(target_dir, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
    return fpath


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_report.py [markdown|html|all] 项目名称 [--out-dir 输出目录]")
        print("  python generate_report.py markdown 项目名称")
        print("  python generate_report.py html 项目名称")
        print("  python generate_report.py all 项目名称")
        sys.exit(1)

    fmt = sys.argv[1]
    project_name = sys.argv[2] if len(sys.argv) > 2 else "未命名项目"
    out_dir = None
    if "--out-dir" in sys.argv:
        idx = sys.argv.index("--out-dir")
        if idx + 1 < len(sys.argv):
            out_dir = sys.argv[idx + 1]

    if fmt in ('markdown', 'all'):
        md = generate_markdown(project_name)
        path = save_output(project_name, md, 'markdown', out_dir)
        print(f"Markdown: {path}")

    if fmt in ('html', 'all'):
        html = generate_html(project_name)
        path = save_output(project_name, html, 'html', out_dir)
        print(f"HTML: {path}")
