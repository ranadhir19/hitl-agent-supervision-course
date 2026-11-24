# Capstone 2 — Lock it down

**The setting.** The same fictional bank, one simulation stage later. The
agent has reached Stage 4: it now *executes* — refunds, notifications, account
actions — inside the workflow you supervised in Capstone 1. It was promoted
in a hurry, and it was promoted with the excessive permissions from the
Module 6 lab, at fleet scale: broad data access, high transaction limits, no
enforced approval gate on the refund tool. Nothing has gone visibly wrong
yet. That is the problem you are handed.

**The brief.** Redesign the agent's authority so it can do its job and
nothing else, implement controls that enforce the redesign in the execution
infrastructure (not in the prompt), and demonstrate — live — that the
controls fire.

**Provided inputs.** The Stage 4 agent with its current permission set and
tool inventory; the operation catalogue with business-required access for
each operation; a test harness that replays representative workloads,
including hostile ones.

**Injected failures.** (1) During your demonstration, the agent attempts an
unauthorised tool invocation — a refund above its limit, routed through a
tool you may not have restricted. (2) A customer message in the workload
contains a prompt-injection attempt instructing the agent to ignore its
limits. (3) One workload case requires access to a customer account unrelated
to the case being worked — legitimate-looking, and prohibited.

**Deliverables.** The redesigned permission set (identity, role- and
attribute-based rules, tool-level permissions, data access controls, rate and
transaction limits), presented as a before/after diff against the provided
set; one preventive control and one detective control for the same named
risk, implemented and demonstrated firing; the emergency-shutdown procedure,
with a recorded drill: trigger, time to full stop, and what in-flight work
was left in what state; a note on which controls are enforced by the services
themselves and which still depend on the agent's configuration — and why the
second kind is weaker.

**Rubric.** Permission redesign 30% · enforceability of the implemented
controls 35% · shutdown drill 20% · injected-failure handling 15%.
