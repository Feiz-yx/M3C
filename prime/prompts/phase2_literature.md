# Phase 2 — Cross-domain literature and hypothesis generation

Read all baseline/model-map/failure-analysis artifacts.

Select the THREE strongest evidence-backed M3C bottlenecks.

For each:
1. point to the exact M3C mechanism;
2. cite empirical failure evidence;
3. abstract it into a generic ML problem;
4. search recent literature, prioritizing 2024–2026 top ML/AI venues;
5. inspect the actual method and ablations;
6. inspect source code when available;
7. map the source mechanism back to M3C;
8. estimate implementation and GPU cost.

Do not rank by title similarity or recency.

For each paper record:
title, venue, year, source problem, mechanism, key ablation, repository,
M3C bottleneck, transfer mapping, adaptation, risk, compute cost.

Write:
- research/03_literature/literature_matrix.csv
- supporting markdown notes by problem family

Then invoke a separate Mechanism Transfer subagent.

Create at most SIX active hypothesis cards using:
research/04_hypotheses/HYPOTHESIS_TEMPLATE.md

Do not implement code in this phase.
