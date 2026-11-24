# Curriculum — AI Agent Supervision & Human-in-the-Loop, The Complete Course

Ten modules, thirty topics, one evolving banking-agent simulation. Every topic
is taught in four parts: (a) learning session, (b) whiteboard explanation,
(c) coding session, (d) tutorial + exercise (in `exercises/`). For operations
(Track C) learners the coding session is a configuration session — policy
files, approval matrices, dashboards — and the repo ships a no-code variant of
every coding exercise.

The course is organised around three dimensions — human-in-the-loop, agent
supervision, agent governance — and five pillars: autonomy, observability,
authority, intervention, accountability. Every topic below maps to the pillars
it is derived from.

## Module 1 — Foundations of autonomous agents

*Why do AI agents require a new model of supervision?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 1.01 | Four stages of AI: rules, predictions, generation, agency | Autonomy |
| HITL 1.02 | Anatomy of an agent | Autonomy, Observability |
| HITL 1.03 | The supervision problem | Autonomy, Accountability |

Exercises: classify 10 described systems by stage and name the first stage at
which each can cause an irreversible outcome; annotate a provided agent design
— every component and the external systems it can change; the three-scenario
supervision exercise (loan rejection recommendation; independent refund;
transaction investigation with account freeze).

## Module 2 — Agent autonomy and decision-making

*What exactly are we supervising?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 2.01 | The execution cycle | Observability |
| HITL 2.02 | Intervention points | Intervention, Observability |
| HITL 2.03 | Reading an execution trace | Observability, Intervention |

Exercises: map a provided workflow onto the six execution-cycle stages and
mark every observable stage; for six incident cards, choose the earliest stage
at which intervention prevents the outcome; audit a 15–20-step agent trace
with three hidden errors — first error, detection point, continue/stop call,
preventive intervention.

## Module 3 — Human-in-the-loop design

*When should humans become involved, and what should they actually do?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 3.01 | HITL, HOTL, HIC — three control arrangements | Authority, Intervention |
| HITL 3.02 | The autonomy scale (levels 0–5) | Autonomy, Authority |
| HITL 3.03 | When the agent asks for help — the five-factor framework | Intervention, Authority |
| HITL 3.04 | The approval matrix | Authority, Accountability |

Exercises: assign involvement patterns to eight described operations and
defend each in one line; place the simulation agent's operations on the
autonomy scale and write the evidence that would justify a promotion; score
six new situations on all five factors (business impact, reversibility,
confidence and evidence quality, regulatory requirements, uncertainty) and
assign treatments; design the full approval matrix for the banking agent,
including approver-timeout behaviour.

**Capstone 1 — Supervise the recommender** (simulation Stage 2; brief in
`capstones/`).

## Module 4 — Agent supervision architecture

*How do we technically supervise agents in a production environment?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 4.01 | The five layers | Observability, Authority |
| HITL 4.02 | Enforcement, not cosmetics | Authority, Intervention |
| HITL 4.03 | The multi-agent supervision design | Observability, Accountability |

Exercises: place 15 named components into the five layers (execution,
policy/control, supervision/observability, human supervision,
governance/audit) and find the layer missing from a broken design; wire an
approval gate so the refund tool physically cannot execute unapproved, and
demonstrate the blocked call; design the full supervisory architecture —
orchestrator, three specialised agents, policy engine, approval service,
audit service, observability platform.

## Module 5 — Risk, trust and uncertainty

*How do we decide whether an agent's output can be trusted?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 5.01 | Why confidence is not correctness | Observability, Intervention |
| HITL 5.02 | Risk-based supervision | Authority, Intervention |
| HITL 5.03 | The threat catalogue | Observability, Accountability |

Exercises: dissect three confident-but-wrong agent decisions and name which of
the four confidences failed in each (answer, evidence, authorisation,
execution); build the risk matrix for the simulation agent's operations and
flag where the simple probability-times-impact product misleads; threat-model
the simulation agent across data quality, tool reliability, prompt injection,
data leakage, distribution shift, and cascading failure.

## Module 6 — Guardrails and policy enforcement

*How do we prevent an agent from exceeding its authority?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 6.01 | Permissions and identity | Authority |
| HITL 6.02 | Limits, policy engines and shutdown | Authority, Intervention |
| HITL 6.03 | The over-permissioned agent lab | Authority, Observability |

Exercises: write the permission set for a new agent role from a job
description (identity and access management, role-based and attribute-based
access control, tool-level permissions, data access controls); implement one
preventive and one detective control for the same risk and show each firing;
the full lab — redesign an over-permissioned agent so it can retrieve account
information, calculate refunds and prepare refund requests, but cannot
independently execute high-value refunds or access unrelated customer
accounts, with the before/after permission diff as the deliverable.

**Capstone 2 — Lock it down** (simulation Stage 4; brief in `capstones/`).

## Module 7 — Failure management and recovery

*What happens when an agent does something unexpected?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 7.01 | The failure catalogue | Observability |
| HITL 7.02 | The recovery process | Intervention, Accountability |
| HITL 7.03 | Recovery engineering | Intervention, Authority |

Exercises: classify 10 incident reports by failure type (wrong tool,
incomplete information, execution loop, misread rule, contradictory
instructions, double execution, lost context) and by the stage where each
became inevitable; run the recovery process end-to-end on a scripted incident
— detect, classify, contain, investigate, decide (retry, compensate, rollback,
escalate), resume or close; the duplicate-refund exercise in full, plus an
idempotency fix demonstrated in code (transaction boundaries, compensating
transactions, retry policies, circuit breakers, dead-letter queues).

## Module 8 — Agent evaluation and performance

*How do we know whether supervision is working?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 8.01 | The four measurement categories | Observability, Accountability |
| HITL 8.02 | The five supervision metrics | Observability |
| HITL 8.03 | Evaluating the humans | Accountability, Intervention |

Exercises: assign 20 candidate metrics to the four categories (agent
performance, operational reliability, supervision effectiveness, business
effectiveness) and cut the five that measure nothing actionable; compute all
five supervision metrics — intervention rate, human override rate, false
escalation rate, incident detection time, mean time to recovery — from a
provided month of simulation logs and write the honest reading, including the
ambiguous low intervention rate; audit a provided approval log for
rubber-stamp patterns and propose the countermeasure.

## Module 9 — Multi-agent supervision and governance

*How do we supervise a team of autonomous agents?*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 9.01 | The chain failure | Observability, Accountability |
| HITL 9.02 | The Agent Supervisor | Authority, Intervention |
| HITL 9.03 | Governance and accountability | Accountability, Authority |

Exercises: fault-tree the five-agent cascade (retrieval, investigation, risk
analysis, recommendation, execution) and place the cheapest control that
breaks it; implement an Agent Supervisor rule set — deterministic policy
enforcement and independent monitoring, not just another model — that catches
three injected deviations; draft the governance charter for the simulation's
agent fleet, answering who owns the agent, who approves its deployment, who
owns its business decisions, who responds to incidents, who authorises changes
to its autonomy, and what evidence must be retained.

**Capstone 3 — Run the incident** (simulation Stage 5; brief in `capstones/`).

## Module 10 — Enterprise implementation capstone

*Build and demonstrate a supervised agent system.*

| Lesson | Topic | Pillars |
|---|---|---|
| HITL 10.01 | Capstone build I — the supervised agent | All five |
| HITL 10.02 | Capstone build II — supervision, recovery, governance | All five |

**Capstone 4 — The enterprise capstone** (simulation Stage 6; brief in
`capstones/`): the supervised banking operations agent end-to-end, all eight
deliverables, defended against six injected failures.

## The simulation spine

One evolving banking-agent simulation runs through the whole course; each
stage hands you a more capable agent and new failures to supervise.

| Stage | Agent capability | Lands in |
|---|---|---|
| 1 | Agent only retrieves information | Modules 1–2 |
| 2 | Agent makes recommendations | Module 3 |
| 3 | Agent executes low-risk actions | Modules 4–5 |
| 4 | Agent operates under guardrails and handles exceptions | Modules 6–7 |
| 5 | Agent interacts with other agents | Modules 8–9 |
| 6 | Agent operates autonomously within constraints | Module 10 |

## Three tracks — one lesson set, three viewing paths

- **Track A — Business leaders and managers.** Autonomy decisions, business
  risk, accountability, governance and operating models. All learning sessions
  and whiteboards; tutorials for Modules 3, 5, 8, 9; coding sessions optional.
  Capstones 1 and 4 (design and defence portions). Outcome: can decide how an
  organisation should deploy and supervise agents.
- **Track B — AI engineers and architects.** Agent architecture, runtime
  supervision, policy enforcement, observability, approval mechanisms,
  multi-agent control. All four parts of every topic; all capstones in full.
  Outcome: can architect and implement a supervised agent platform.
- **Track C — Operations and human supervisors.** Reviewing decisions, reading
  traces, handling exceptions, approving actions, escalation, incident
  management. All learning sessions, whiteboards and tutorials; coding
  sessions as no-code configuration labs. Capstones 1–3 in full; Capstone 4 as
  the team member owning the approval matrix and recovery process. Outcome:
  can effectively supervise agents in daily business operations.

Assessment across the course: conceptual understanding 15%; risk and
intervention design 20%; technical architecture 20%; practical implementation
25%; capstone presentation 20%. Full topic briefs, exercises, and capstone
details: see the folders in this repo as production reaches them.
