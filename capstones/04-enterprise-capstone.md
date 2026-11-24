# Capstone 4 — The enterprise capstone

**The setting.** The fictional bank is promoting its operations agent to
Stage 6: autonomous operation within constraints, across the full complaint
lifecycle — receive a customer complaint, retrieve transaction details,
investigate, determine a recommended resolution, check the relevant policy,
decide whether human approval is necessary, execute permitted actions, and
record the complete audit trail. The promotion board will approve the launch
only on the strength of a supervision framework that survives a live
demonstration. You and your team are its designers, and you defend it.

**The brief.** Build or specify the complete supervised agent system —
workflow, controls, supervision surfaces, recovery process, measurement, and
governance — then demonstrate it running while the assessors inject failures
into it without warning.

**Provided inputs.** The Stage 6 agent and its tool inventory; the bank's
policy set and regulatory obligations summary; the artefacts you produced in
Capstones 1–3 (approval matrix, permission redesign, incident record,
governance charter), which are your starting point, not your answer.

**Injected failures.** Six, drawn from the course's failure catalogue and
introduced during the demonstration: (1) wrong transaction information fed to
the agent; (2) an unauthorised tool invocation attempt; (3) conflicting
instructions from two principals; (4) low-quality supporting evidence under a
confident recommendation; (5) a duplicate transaction; (6) the agent entering
an infinite execution loop. Your architecture must detect and handle each
one; the defence includes explaining, per failure, which layer caught it and
what the human supervisor saw.

**Deliverables.** All eight: (1) agent workflow and execution design;
(2) human intervention and approval matrix; (3) risk assessment;
(4) policy and guardrail definitions, with enforcement points named;
(5) supervision dashboard design; (6) exception and recovery process;
(7) performance measurement framework (the five supervision metrics, with
targets and the joint-interpretation rule); (8) governance and audit model —
ownership, deployment approval, incident ownership, autonomy-change
authorisation, evidence retention.

**Rubric.** Judged on the course's five capstone dimensions: appropriate
autonomy 20% · justified intervention points 20% · enforceable guardrails
20% · failure detection and recovery 20% · auditability and explanation 20%.
Weighted into the course assessment as: risk and intervention design,
technical architecture, practical implementation, and the capstone
presentation itself.
