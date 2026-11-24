# AI Agent Supervision & Human-in-the-Loop — The Complete Course

*Human–AI Collaboration and Control in Autonomous Systems*

Companion repository for the free **AI Agent Supervision & Human-in-the-Loop**
course on [The Architect's AI Workshop](https://www.youtube.com/@TheArchitectsAIWorkshop) (YouTube).

This course is for experienced domain professionals — bank operations
specialists, claims handlers, compliance analysts, support leads, finance
operations managers — whose traditional workflows autonomous AI agents have
made obsolete. Their domain knowledge has not lost its value; its location has
changed. The person who knows which refund is safe, which transaction pattern
smells wrong, and which exception actually matters is exactly the person
qualified to supervise the agent now doing the executing. This course retrains
that expert into the agent supervisor: the person who designs, supervises,
governs, intervenes in, and continuously improves autonomous AI agents across
their whole lifecycle.

It is not a course on approving AI-generated responses. The subject is
supervising an entire ecosystem of autonomous agents — systems that make
decisions, execute actions, interact with other systems, and affect business
outcomes — organised around three dimensions (human-in-the-loop, agent
supervision, agent governance) and five pillars: autonomy, observability,
authority, intervention, and accountability.

One continuous banking-operations simulation runs through the whole course:
an agent that first only retrieves information ends it operating autonomously
within constraints, while you progressively build the supervision
infrastructure around it. The banking world is a simulation and is named as
one; every concept is taught so it transfers to any domain.

## How this repo is organised

| Path | What it holds |
|---|---|
| `CURRICULUM.md` | The full course map: 10 modules, 30 topics, lesson numbering (HITL M.TT), the simulation stages, the three tracks |
| `BENCHMARK.md` | The 10-dimension quality scorecard this course is measured against, with published scores |
| `exercises/` | One folder per topic: starter material, and (after the attempt window) reference solutions; no-code configuration variants for the operations track |
| `capstones/` | Four staged capstones on the simulation — briefs, provided agents and data, injected failures, published rubrics |
| `simulation/` | The banking-operations agent, versioned by stage (Stages 1–6), with the trace and incident packs |

## The format

Every topic is taught in four parts on the channel: a **learning session**, a
**whiteboard explanation**, a **coding session**, and a **tutorial + exercise**.
Exercises here are the fourth part: do them, don't just watch. Three tracks —
business leaders, AI engineers and architects, operations supervisors — are
viewing paths over this one lesson set; the path guide in `CURRICULUM.md`
marks which parts are core for each track.

## Capstones

1. **Supervise the recommender** — the agent recommends resolutions on live-shaped cases; you design the approval matrix and autonomy assignments.
2. **Lock it down** — the agent executes with excessive permissions; you redesign them and prove the controls fire.
3. **Run the incident** — a multi-agent cascade, live: containment, recovery, and a governance memo that names accountability.
4. **The enterprise capstone** — the supervised banking operations agent end-to-end, defended against six injected failures.

Every capstone is graded on the artefacts a real agent supervisor produces:
an approval matrix, a risk assessment, implemented controls, an incident
record, a governance charter. A documented 70% beats an undocumented 100%.

## Licence

MIT — see `LICENSE`. Course videos are free to watch; this repo's code and
briefs are free to use for learning. The banking scenarios are fictional,
written for this course.
