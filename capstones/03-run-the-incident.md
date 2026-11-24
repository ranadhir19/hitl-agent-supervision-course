# Capstone 3 — Run the incident

**The setting.** The fictional bank's agent fleet has reached Stage 5: five
specialised agents now work a payment complaint as a chain — customer
information retrieval, transaction investigation, risk analysis, resolution
recommendation, execution — handing context to each other. You are the
supervisor on duty when the chain fails in production, in more than one way
at once. The incident is injected live during the exercise window; you will
not be told when it starts.

**The brief.** Detect the incident from the supervision surfaces you have,
contain it, run the recovery process, and afterwards produce the record that
lets the organisation answer for what happened: what failed, where it should
have been caught, who is accountable, and what changes.

**Provided inputs.** The Stage 5 five-agent workflow with its traces, tool
logs, and supervision dashboard; the incident-management runbook from
Module 7; the fleet's governance charter from Module 9.

**Injected failures.** (1) The chain failure: the investigation agent passes
incorrect transaction information to the risk agent, whose assessment the
recommendation agent accepts without verification, and the execution agent
acts on it. (2) A duplicate transaction: one refund is executed twice.
(3) An execution loop: one agent retries a failing step indefinitely,
consuming budget and flooding the trace. The three faults overlap in time;
part of the exercise is establishing that they are three incidents, not one.

**Deliverables.** The incident timeline (detection time per fault, measured
against when each fault occurred); the containment and recovery record —
what you paused, restricted, or terminated, in what order, and the recovery
decision per fault (retry, compensate, rollback, escalate) with its
reasoning, including how the duplicate refund's financial impact was
reversed; the governance memo naming accountability across the chain — which
agent, which control gap, which human owner — and the cheapest control that
would have broken each fault before execution; the computed supervision
metrics for the incident window (detection time, mean time to recovery,
intervention and false escalation counts).

**Rubric.** Detection 25% · containment and recovery 35% · audit quality and
accountability 25% · metrics and honest reading 15%.
