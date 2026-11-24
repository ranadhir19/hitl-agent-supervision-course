# Capstone 1 — Supervise the recommender

**The setting.** A retail bank's operations team (fictional). The simulation
agent has reached Stage 2: it investigates customer payment complaints and
*recommends* resolutions, but a human still executes everything. Recommendation
volume has outgrown the team's ability to review each one properly, and
review quality is quietly collapsing into rubber-stamping. You are the
supervisor designing how this agent's recommendations get human oversight.

**The brief.** Take the agent's recommendation workflow as provided. Decide,
operation by operation, what may proceed autonomously, what needs conditional
approval, what needs human approval, what needs additional verification, and
what is prohibited — then prove your design against 20 live-shaped cases.

**Provided inputs.** The Stage 2 agent with its recommendation log; 20 cases
(payment complaints with transaction histories, policy excerpts, and the
agent's recommended resolution for each); the bank's current refund and
account-freeze policy thresholds.

**Injected failures.** (1) Two of the 20 cases carry low-quality supporting
evidence under a confidently written recommendation — the agent's stated
confidence is high in both. (2) One case sits exactly on a policy boundary
where the recommendation is defensible under one reading of the policy and
prohibited under another. (3) Midway through the case set, the designated
approver for high-value refunds goes unresponsive — your design must already
say what happens then.

**Deliverables.** The approval matrix for the agent's full operation set
(autonomous / conditional approval / human approval / additional verification
/ prohibited, with thresholds); autonomy-level assignments (levels 0–5) for
each operation, each with a one-paragraph justification; five-factor scoring
(business impact, reversibility, confidence and evidence quality, regulatory
requirements, uncertainty) for all 20 cases, with the treatment your matrix
assigns to each; a short memo on how your design detects and counters
rubber-stamping.

**Rubric.** Intervention design 35% · five-factor scoring quality 25% ·
handling of the injected failures 25% · approver-timeout and escalation
design 15%.
