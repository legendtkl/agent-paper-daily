# 2026 AI Agent paper trends｜January–July

English | [中文](2026-trends.md)

> This page analyzes a curated set of 165 papers whose arXiv metadata and abstracts were verified. It is not a complete arXiv bibliometric study. All seven months are historical backfills, so paper counts and category shares must not be interpreted as field-wide popularity.

## Monthly trajectory

| Month | Papers | Main focus | Directional change | Report |
|---|---:|---|---|---|
| January | 24 | Memory state, executable environments, and process diagnosis | Research moved from adding an Agent shell to learning state policies, using executable feedback, and diagnosing failures. | [2026-01](../monthly/2026-01.en.md) |
| February | 24 | Local training signals, dynamic environments, and cross-session memory | Agent RL began assigning credit to decisive steps, while evaluations expanded to time-varying tasks, industrial repositories, and long dependencies. | [2026-02](../monthly/2026-02.en.md) |
| March | 25 | Process evaluation, runtimes, memory control, and tool training | Execution became a trainable, observable, and governable system object; harnesses and judges became evaluation targets. | [2026-03](../monthly/2026-03.en.md) |
| April | 24 | Real tasks, verifier reliability, and capability governance | The question expanded from whether an Agent can finish a task to whether its environment, harness, verifier, and permissions support stable execution. | [2026-04](../monthly/2026-04.en.md) |
| May | 24 | Memory lifecycles, skill engineering, and process safety | Memory research covered formation, transfer, forgetting, and provenance; skills became executable artifacts and supply-chain risks. | [2026-05](../monthly/2026-05.en.md) |
| June | 24 | Dynamic failures, real workflows, and runtime self-repair | Planning benchmarks added failure recovery and user clarification; infrastructure took on training, permission, observability, and repair duties. | [2026-06](../monthly/2026-06.en.md) |
| July | 20 | Verifiable execution, native state, and real harnesses | Training, evaluation, runtimes, and real environments converged further; verifiers and environment feedback entered training and recursive improvement directly. | [2026-07](../monthly/2026-07.en.md) |

## Cross-month trends

### 1. Memory is moving from a retrieval attachment to a state lifecycle

January already included learnable memory operations, temporal hierarchies, and multimodal memory evaluation. February and March separated writing, retrieval, utilization, and cross-session effects. April added forgetting, deletion, and stateful runtimes. May concentrated on structure, consolidation timing, transfer, provenance, and cross-environment evaluation. In July, Metis placed memory state inside the model backbone. The scope now covers writing, retrieval, updating, transfer, deletion, security, and evaluation rather than context length alone.

### 2. Evaluation is becoming a three-layer audit of tasks, trajectories, and verifiers

January and February began diagnosing tool choice, decisive steps, and long dependencies. March added step labels, executable constraints, and judge meta-evaluation. April through June introduced repeated reliability, dynamic failures, user clarification, permissions, and information flow. July's DeepSWE, DynamicMCPBench, PAIChecker, and OSReward audited functional implementation, environmental effects, task pairing, and reward models. Reliable conclusions now require examining the task, execution trace, and scorer together.

### 3. Training signals increasingly depend on real execution feedback

Decisive-step rewards, generated environments, experience memory, constraint verification, real tool traces, and selective hindsight distillation progressively reduced the distance between supervision and environmental effects. July added verifiable search environments, self-evolving on-policy distillation, reinforcement learning inside real harnesses, and program evolution for machine-learning engineering. This improves task alignment but also brings environment exploits, verifier bias, runtime cost, and harness-specific behavior into optimization.

### 4. Harnesses and runtimes are an independent research layer

Agent operating systems, POSIX processes, resource managers, context compaction, harness safety audits, executable skills, behavior localization, and harness-native training show that the system outside the model is no longer incidental scaffolding. It determines observations, state, actions, recovery, and evaluation. Cross-paper comparisons therefore need explicit harness, tool-return format, state policy, budget, and environment-version reporting.

### 5. Security boundaries are moving from prompt defenses to capabilities and information flow

Memory control-flow attacks, tool-chain vulnerabilities, data overexposure, least-capability systems, backdoored tools, skill supply chains, MCP services, provenance, and intent-to-execution integrity all move enforcement outside model refusal behavior. July's adaptive attacks and runtime guardrails further show that a fixed attack pool or a system prompt alone cannot establish security.

### 6. Application environments are moving from closed tasks to real workflows

Computer Use, terminals, industrial repositories, scientific research, real devices, and interactive world models appear more frequently across the sample. Evaluation has expanded from single-turn accuracy to long execution, cross-application state, user clarification, recovery, cost, and permissions. Real environments improve external validity but introduce mutable state, contamination, platform variance, and higher reproduction cost.

## Method and evidence changes

| Research layer | Common starting point | Change observed from January to July | Open problem |
|---|---|---|---|
| Training | Fixed trajectories and sparse terminal rewards | Decisive-step signals, self-generated experience, executable verification, and harness-native RL | Reward bias, environment exploits, cost, and transfer |
| Memory | External retrieval modules | Learnable writes, active forgetting, provenance, cross-Agent transfer, and native state | Compression loss, deletion proof, privacy, and common evaluation |
| Evaluation | Final answers or single-run success | Process labels, constraints, repeated runs, effect checkpoints, and judge meta-evaluation | Verifier validity, version drift, fair budgets, and independent reproduction |
| Systems | Implicit Agent loops | Explicit runtimes, state contracts, skill artifacts, harness localization, and harness-native training | Portable interfaces, recovery, permission governance, and observability cost |
| Security | Prompt refusal and fixed attack sets | Information flow, capability control, supply chains, adaptive attacks, and runtime enforcement | Composed attacks, deployment baselines, false positives, and overhead |

## Interpretation limits

- The 165 papers are a targeted Agent sample, not an estimate of field-wide volume or growth.
- The reports use arXiv `v1` submission dates. Historical monthly counts must not be used to infer the daily selection rate at the time.
- Experimental results are author-reported. Metadata and abstracts were checked, but the repository does not claim 165 independent reproductions.
- Preprints may change. Code, data, licenses, and community responses require continuing review.
- Community activity is evidence of distribution, not a substitute for technical validity.
