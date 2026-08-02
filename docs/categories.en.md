# AI Agent paper taxonomy

English | [中文](categories.md)

Categories are based on the primary research problem, not a model name, benchmark, environment, or application label. Each paper has one primary category and up to three secondary categories. Primary categories drive archives and statistics; secondary categories support discovery.

## Assignment rules

- The primary category follows the paper's main contribution.
- Benchmarks, scoring methods, and evaluation reliability belong to `EV`; prevention and mitigation mechanisms belong to `SS`; runtime and system optimization belong to `SY`.
- Training that uses terminal feedback from an executable environment belongs to `AT`; post-deployment adaptation from execution experience belongs to `LT`.
- Use `CU`, `SE`, `EA`, or `RA` as the primary category only when the contribution depends on that task environment.

## Core mechanisms

These categories describe how an Agent controls work, plans, invokes capabilities, maintains state, learns, and collaborates.

| Code | Category | Scope |
|---|---|---|
| <a id="af"></a>`AF` | Agent architecture and orchestration | Control flow, module interfaces, workflow graphs, runtime abstractions, and self-modifying architectures. |
| <a id="rp"></a>`RP` | Reasoning, planning, and search | State modeling, task decomposition, candidate search, verification, and budgets. |
| <a id="tu"></a>`TU` | Tool use, actions, and protocols | Tool discovery, schemas, orchestration, protocols, transactions, and effect verification. |
| <a id="km"></a>`KM` | Memory, context, and knowledge | Writing, organizing, retrieving, updating, forgetting, and governing knowledge. |
| <a id="lt"></a>`LT` | Learning, adaptation, and self-improvement | Post-deployment adaptation based on execution experience, including reflection, memory updates, workflow or tool improvement, and reversible long-term self-modification. |
| <a id="ma"></a>`MA` | Multi-Agent collaboration and organization | Roles, artifacts, communication, topology, arbitration, and organizational governance. |

## Applications and environments

These categories describe how Agent mechanisms enter digital interfaces, software repositories, physical environments, and research tasks.

| Code | Category | Scope |
|---|---|---|
| <a id="cu"></a>`CU` | Web, GUI, and Computer Use | Web, mobile, desktop, visual grounding, and cross-application workflows. |
| <a id="se"></a>`SE` | Software engineering and Coding Agents | Repository understanding, issue resolution, testing, requirements clarification, and long-term maintenance. |
| <a id="ea"></a>`EA` | Embodied and robotics Agents | Robotic tasks, skills, VLA models, continuous control, and physical safety. |
| <a id="ra"></a>`RA` | Deep research, science, and data Agents | Deep retrieval, evidence synthesis, code experiments, scientific automation, and auditing. |

## Quality and engineering

These categories describe how Agents are evaluated, constrained, recovered, and operated efficiently.

| Code | Category | Scope |
|---|---|---|
| <a id="ev"></a>`EV` | Evaluation and benchmarks | Environments, terminal states, trajectory diagnosis, scoring reliability, and budget fairness. |
| <a id="ss"></a>`SS` | Reliability, safety, and security engineering | Injection, unauthorized actions, information flow, capability isolation, supply chains, and continuous assurance. |
| <a id="sy"></a>`SY` | Agent runtimes, systems, and efficiency | Scheduling, sandboxes, state, checkpoints, observability, and the training–execution bridge. |

## Foundations and enabling methods

These categories describe how model properties, training, and multimodal perception determine the upper bound of Agent capabilities.

| Code | Category | Scope |
|---|---|---|
| <a id="bm"></a>`BM` | Foundation-model properties and capability limits | Effective context, structured output, reasoning placement, visual token cost, cache invalidation, scale, and harness interactions. |
| <a id="pt"></a>`PT` | Model post-training | Preference, annotation, rule, or verifiable-answer rewards that do not require an executable environment. |
| <a id="at"></a>`AT` | End-to-end Agent training | Training from real terminal feedback in executable environments to optimize model weights and action policies. |
| <a id="mv"></a>`MV` | Multimodal perception and grounding | High resolution, OCR, grounding, temporal state, and action interfaces. |

## Common boundaries

| Often confused | Assignment rule |
|---|---|
| `EV` vs. `SS` | Use `EV` when the main contribution discovers, measures, or scores a problem; use `SS` when it prevents, isolates, or mitigates the risk. |
| `SY` vs. `AF` | Use `SY` for execution infrastructure, scheduling, state, or efficiency; use `AF` for changes to the Agent's control structure or module orchestration. |
| `AT` vs. `LT` | Use `AT` when executable terminal feedback optimizes model weights; use `LT` for post-deployment adaptation from execution experience. |
| `PT` vs. `AT` | Use `PT` when preference, rules, or answer rewards do not require an executable environment; use `AT` when training depends on the environment's actual terminal state. |
| `MV` vs. `CU` | Use `MV` for perception, OCR, or grounding; use `CU` when the main contribution is completing Web, desktop, or mobile tasks. |
| `RP` vs. `RA` | Use `RP` for general planning, search, and verification; use `RA` when the contribution depends on deep research, scientific, or data-analysis tasks. |
