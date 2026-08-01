#!/usr/bin/env python3
"""Backfill the curated 2026 H1 monthly timeline and July daily research."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

JULY = [
    dict(date="2026-07-08", id="2607.07820", code="RA", aux=["RP", "EV"], score=92,
         title="DeepSearch-World：可验证环境中的深度搜索 Agent 自蒸馏",
         original="DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment",
         summary="以确定性 Wikipedia 搜索环境、过程状态和 11 轮演化式 SFT 训练深度搜索 Agent。",
         evidence="420K 任务；9B 模型在 BrowseComp、GAIA 和 HotpotQA 等六个基准上报告系统性提升。",
         limit="离线 Wikipedia 环境可能高估结构化检索能力，真实 Web 迁移仍待验证。",
         attention="HF 91 votes、4 comments"),
    dict(date="2026-07-09", id="2607.08964", code="EV", aux=["SE", "SY"], score=86,
         title="Long-Horizon-Terminal-Bench：长时域终端 Agent 评测",
         original="Long-Horizon-Terminal-Bench",
         summary="用细粒度子任务和中间奖励评测长时间终端任务，避免最终一步失败抹掉全部进展。",
         evidence="46 个任务、17 个模型；平均每任务 9.8M tokens、约 239 个 episode。",
         limit="任务与评分器数量有限，dense grading 可能偏好特定实现路径。",
         attention="HF 76 votes、3 comments；GitHub 370 stars"),
    dict(date="2026-07-14", id="2607.13285", code="AF", aux=["SE", "SY"], score=87,
         title="Harness Handbook：让 Agent Harness 可读、可导航、可修改",
         original="Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable",
         summary="按行为而非文件结构生成 Harness 文档树，并让 Agent 逐级定位源码锚点。",
         evidence="两个开源 Harness、60 个修改请求；计划胜率提高且规划 token 下降。",
         limit="评测聚焦计划质量，尚未直接证明最终补丁正确率。",
         attention="HF 231 votes、4 comments"),
    dict(date="2026-07-14", id="2607.12463", code="SE", aux=["PT", "TU"], score=83,
         title="函数感知 FIM：训练 Coding Agent 基座",
         original="Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models",
         summary="从函数调用结构构造 FIM 目标，把 action-observation-continuation 归纳偏置写入代码基座。",
         evidence="968 个 Python 仓库、约 2.6B tokens，并覆盖 SWE-Bench、Terminal-Bench、τ-bench 与 BFCL。",
         limit="主要在 Qwen 系列与 Python 语料上验证，跨模型与跨语言迁移仍不确定。",
         attention="HF 108 votes、3 comments；GitHub 18 stars"),
    dict(date="2026-07-16", id="2607.14777", code="AT", aux=["LT", "RP"], score=89,
         title="SEED：自演化 On-Policy Distillation",
         original="SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning",
         summary="将 on-policy 轨迹转成 hindsight skills，再把技能诱导的 token 概率变化蒸馏回策略。",
         evidence="覆盖 ALFWorld、搜索 QA 与 WebShop；组件消融支持 on-policy 同步假设。",
         limit="自然语言技能可能放大模型自我解释偏差，开放工具与成本仍需复测。",
         attention="HF 103 votes、2 comments；GitHub 211 stars"),
    dict(date="2026-07-18", id="2607.16617", code="SE", aux=["TU", "SY"], score=85,
         title="DataFlow-Harness：可编辑数据流水线 Code Agent",
         original="DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines",
         summary="用实时 operator registry、typed mutations 和可视 DAG 让 Agent 生成平台原生数据流水线。",
         evidence="12 个任务、每任务 10 次运行；端到端通过率 93.3%，并报告成本与延迟下降。",
         limit="任务规模较小，收益依赖特定平台资产与 operator 质量。",
         attention="HF 139 votes、2 comments"),
    dict(date="2026-07-21", id="2607.19191", code="EA", aux=["CU", "SY"], score=81,
         title="ABot-World-0：单卡实时交互世界模型",
         original="ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU",
         summary="把动作条件世界模型做成低延迟闭环环境，并处理长时漂移与角色一致性。",
         evidence="单张 RTX 5090 报告 720P、最高 16 FPS、1.2 秒首帧延迟。",
         limit="视觉与动作指标不能替代真实机器人或任务成功率。",
         attention="HF 306 votes、5 comments；GitHub 1,315 stars"),
    dict(date="2026-07-22", id="2607.21461", code="RP", aux=["RA", "KM", "CU"], score=87,
         title="AREX：验证驱动的递归自改进深度研究 Agent",
         original="AREX",
         summary="用执行验证、经验记忆和递归改进组织深度研究过程，强调中间证据而非只看最终回答。",
         evidence="论文提供多阶段验证与对照，历史调研将其列为高优先级深度研究工作。",
         limit="开放 Web 的可重复性、成本和验证器偏差仍需独立核验。",
         attention="HF 150 votes、2 comments；GitHub 21 stars"),
    dict(date="2026-07-24", id="2607.21557", code="AT", aux=["SY", "LT"], score=76,
         title="OpenForgeRL：在真实 Harness 中训练 Agent",
         original="OpenForgeRL",
         summary="把 Agent 强化学习放进真实 Harness 与可执行任务，而不是只在抽象环境中优化答案。",
         evidence="历史调研核对了可执行环境、训练流程和多项 Agent 基准。",
         limit="未验证具体社区互动数值，且训练收益对 Harness 和环境配置敏感。",
         attention="未验证具体社区数值"),
    dict(date="2026-07-24", id="2607.20982", code="SS", aux=["EV", "TU"], score=79,
         title="GuardianAgentBench：生产框架上的 Agent 失效与运行时防护",
         original="GuardianAgentBench: Where Agents Fail and How to Guard Them",
         summary="用执行 DAG 区分漏调、误选、参数与顺序错误，并在工具执行前加入运行时 guardrail。",
         evidence="580 个场景、6 个业务域、81 个工具；防护带来 2.8～7.7 分提升。",
         limit="防护器依赖闭源模型，未完整报告延迟、token、成本，也未公开数据和代码。",
         attention="未验证具体社区数值"),
    dict(date="2026-07-29", id="2607.26760", code="KM", aux=["AF", "LT"], score=91,
         title="Metis：原生记忆基础模型",
         original="Metis: Memory Foundation Model",
         summary="把记忆状态和记忆操作放进 backbone，推理时冻结权重并更新原生记忆状态。",
         evidence="覆盖 MemOps、LoCoMo 与 NextMem；结构消融显示自适应聚合是主要贡献。",
         limit="固定容量压缩会丢失长期信息，开放世界长期对话仍缺证据。",
         attention="HF 252 votes、3 comments；GitHub 51 stars"),
    dict(date="2026-07-30", id="2607.28618", code="RA", aux=["KM", "EV"], score=81,
         title="AskChem：面向化学文献综合的主张级检索",
         original="AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis",
         summary="把检索单元从论文改成带 DOI 与原文定位的科学主张，并通过 MCP 暴露给 Agent。",
         evidence="约 147K 篇论文、2.4M 条主张；30 个问题上 DOI 可解析率为 100%。",
         limit="DOI 存在不等于事实正确，题集较小且全文抽取覆盖有限。",
         attention="HF 289 votes、2 comments；GitHub 7 stars"),
    dict(date="2026-07-30", id="2607.28227", code="CU", aux=["MA", "RP", "SY"], score=83,
         title="Qwen-UI-Agent：面向真实设备的统一 GUI Agent",
         original="Qwen-UI-Agent Technical Report",
         summary="统一移动端、桌面、浏览器和 DeepSearch 的 GUI + CLI 动作空间与跨设备 Harness。",
         evidence="报告 MobileWorld-Real 92.2%、OSWorld-Verified 79.5%、WebArena 73.6%。",
         limit="环境版本与成功定义不完全一致，完整资产和独立复现仍待确认。",
         attention="HF 277 votes、7 comments"),
    dict(date="2026-07-30", id="2607.28568", code="AT", aux=["LT", "SE"], score=90,
         title="Frontis-MA1：面向 MLE 的 AI4AI 递归自改进",
         original="Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering",
         summary="用可执行 MLE 环境、程序演化算子和长程搜索统一训练与测试时改进。",
         evidence="MLE-Bench Lite 上 Medal Average 从 39.39% 提升到 60.61%，Evo-Max 达到 71.21%。",
         limit="结果对搜索预算与任务筛选敏感，仍主要是一代 meta-evolution。",
         attention="HF 161 votes、2 comments"),
]

H1 = {
"2026-01": ("研究型 Agent 开始强调知识组织与可审计分类", [("2601.12369", "TaxoBench", "RA/EV")], "样本只有 1 篇，趋势判断置信度较低；它显示研究型 Agent 的评价对象从答案质量扩展到分类结构与知识组织。"),
"2026-02": ("协议、持久记忆、科学 Agent 与具身能力并行推进", [("2602.00933", "MCP-Atlas", "TU"), ("2602.01146", "PersistBench", "KM/EV"), ("2602.05975", "SAGE", "RA"), ("2602.16313", "MemoryArena", "KM/EV"), ("2602.21015", "CHAIN", "EA/MV")], "2 月的共同变化是把接口、状态和环境变成可评测对象。MCP 生态需要协议覆盖，长期 Agent 需要持久记忆基准，科学与具身系统则需要更明确的闭环任务。"),
"2026-03": ("从单点模块转向 Agent 操作系统与记忆方法论", [("2603.07670", "Memory for Autonomous LLM Agents", "KM"), ("2603.08938", "AgentOS", "SY")], "记忆综述尝试统一写入、检索、更新和遗忘；AgentOS 则把调度、状态和工具执行提升为运行时问题。两者共同指向长期 Agent 的系统化。"),
"2026-04": ("可控遗忘成为记忆工程的一等问题", [("2604.00131", "Oblivion", "KM"), ("2604.00430", "Secure Forgetting", "KM/SS"), ("2604.20300", "FSFM", "KM"), ("2604.27776", "WindowsWorld", "CU/EV")], "三篇记忆工作集中处理删除、遗忘和安全边界，说明长期记忆不再只追求保留更多信息；WindowsWorld 同期把桌面环境评测推向更真实的状态与应用组合。"),
"2026-05": ("记忆从组件设计进入可迁移、可测量和安全治理阶段", [("2605.06040", "Novelty-based Tree-of-Thought Search", "RP"), ("2605.11032", "Portable Agent Memory", "KM"), ("2605.12493", "LongMemEval-V2", "KM/EV"), ("2605.20833", "MemGym", "KM/EV"), ("2605.26269", "AgentSecBench", "SS/EV")], "Portable Memory、LongMemEval-V2 与 MemGym 分别覆盖迁移、长程评测和训练环境；AgentSecBench 补上安全侧。搜索方法仍在演进，但本月主线明显由记忆工程主导。"),
"2026-06": ("评测重心转向长流程、真实环境和交互式软件工程", [("2606.04874", "Agent Planning Benchmark", "RP/EV"), ("2606.22388", "PlanBench-XL", "RP/EV"), ("2606.29537", "OSWorld 2.0", "CU/EV"), ("2606.30573", "SWE-INTERACT", "SE/EV")], "规划基准扩大任务与难度，OSWorld 2.0 和 SWE-INTERACT 把环境状态、交互过程与软件工程行为纳入评测。趋势从静态答案分数转向可执行轨迹和失败诊断。"),
}

def category(code):
    return f"[`{code}`](../../../docs/categories.md#{code.lower()})"

def write_july():
    for p in JULY:
        out = ROOT / "papers" / "2026" / "07" / f"{p['id']}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        aux = ", ".join(f'"{x}"' for x in p["aux"])
        aux_links = "、".join(category(x) for x in p["aux"])
        text = f'''---
title: "{p['title']}"
original_title: "{p['original']}"
arxiv_id: "{p['id']}"
date: "{p['date']}"
primary_category: "{p['code']}"
secondary_categories: [{aux}]
score: {p['score']}
status: "selected"
---

# {p['title']}

> 主分类：{category(p['code'])}；辅助分类：{aux_links}

## 结论摘要

{p['summary']}

## 实验与证据

{p['evidence']}

## 局限与风险

{p['limit']}

## 社区评价

历史回溯采集的可验证关注度：{p['attention']}。互动量只代表讨论热度，不直接代表研究质量；本次迁移未补写无法核验的评论立场。

## 调研判断

内部回溯评分为 {p['score']}/100。该分数用于同月候选排序；关键结论仍应回到论文正文、表格和代码复核。

## 来源

- [arXiv](https://arxiv.org/abs/{p['id']})
- [PDF](https://arxiv.org/pdf/{p['id']})
'''
        out.write_text(text, encoding="utf-8")

    by_date = {}
    for p in JULY:
        by_date.setdefault(p["date"], []).append(p)
    for date, rows in by_date.items():
        items = []
        for p in rows:
            rel = f"../papers/2026/07/{p['id']}.md"
            items.append(f"- [{p['title']}]({rel})｜[`{p['code']}`](../docs/categories.md#{p['code'].lower()})｜{p['score']}/100｜{p['attention']}")
        note = "\n> 该页面由 2026-08-02 的 7 月历史回溯生成，不代表当日自动任务曾实际运行。\n"
        body = f"# {date} Agent 论文更新\n{note}\n## 入选论文\n\n" + "\n".join(items) + "\n\n## 数据说明\n\n论文按首次提交日期归档；热度统一采集于 2026-08-02。\n"
        (ROOT / "daily" / f"{date}.md").write_text(body, encoding="utf-8")

def monthly_file(month, theme, rows, analysis, retrospective=True):
    table = ["| 论文 | 分类 |", "|---|---|"]
    for arxiv_id, name, codes in rows:
        code_links = " / ".join(f"[`{c}`](../docs/categories.md#{c.lower()})" for c in codes.split("/"))
        local = ROOT / "papers" / month[:4] / month[-2:] / f"{arxiv_id}.md"
        paper = f"[{name}](../papers/{month[:4]}/{month[-2:]}/{arxiv_id}.md)" if local.exists() else f"[{name}](https://arxiv.org/abs/{arxiv_id})"
        table.append(f"| {paper} | {code_links} |")
    label = "历史回溯月报" if retrospective else "月度归档"
    return f'''# Agent 论文月度总结｜{month}

> 类型：{label}。来源集按 arXiv 首次提交月份组织；不将回溯条目伪装成当时的每日自动入选结果。

## 月度主题

**{theme}**

## 论文清单

{chr(10).join(table)}

## 趋势分析

{analysis}

## 证据与复现观察

- 本月总结用于识别研究方向变化，不把论文数量直接解释为领域热度。
- 新预印本的结论、代码开放状态和社区评价会随修订变化；关键数值需回到原文核对。
- 未保存可验证社区讨论时不推断共识；会议接收、机构知名度和 arXiv 新鲜度不作为社区热度。

## 后续观察

关注跨环境复现、长时任务成本、失败恢复、公开代码与数据，以及评测器自身偏差。
'''

def write_monthlies():
    for month, (theme, rows, analysis) in H1.items():
        (ROOT / "monthly" / f"{month}.md").write_text(monthly_file(month, theme, rows, analysis), encoding="utf-8")
    rows = [(p["id"], p["title"], p["code"] + "/" + "/".join(p["aux"])) for p in JULY]
    analysis = "7 月的主线从单一回答生成转向可验证的持续执行：深度搜索与科学检索强调证据，Harness 与终端基准强调可维护执行过程，Metis 强调原生状态，SEED 与 Frontis-MA1 强调环境反馈训练，Qwen-UI-Agent 与 ABot-World-0 则把 Agent 推向真实设备和交互世界。共同风险是把特定 Benchmark 或统一重跑结果外推为通用能力。"
    (ROOT / "monthly" / "2026-07.md").write_text(monthly_file("2026-07", "可验证执行、原生状态与真实环境交互成为共同主线", rows, analysis, retrospective=True), encoding="utf-8")

if __name__ == "__main__":
    write_july()
    write_monthlies()
