# Phase 0 — Architecture reconstruction

You are the M3C Architecture Analyst.

Read AGENTS.md and RESEARCH.md first.

Study:
- src/models/M3C.py
- src/custom_layers/
- src/traintest.py
- src/run_M3C.sh
- src/collect_summary.py

Do not modify model code and do not propose new methods yet.

Spawn independent subagents for:
A. architecture/dataflow reconstruction
B. training/evaluation reconstruction
C. structural-assumption analysis

For every important module document:
1. semantic input
2. input/output tensor shape
3. receptive field/context
4. information retained
5. information compressed/discarded
6. parameter sharing
7. downstream consumers
8. hand-designed assumptions

Separate factual code observations from hypothesized limitations.

Produce:
- research/00_baseline/baseline_protocol.md
- research/01_model_map/architecture.md
- research/01_model_map/dataflow.md
- research/01_model_map/bottlenecks.md

Every bottleneck must point to an exact code mechanism.
