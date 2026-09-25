# Phase 1 — Baseline and failure analysis

Read AGENTS.md, RESEARCH.md and Phase-0 artifacts.

First reproduce the baseline with an explicit matched seed.

Do not modify architecture.

Record:
- command/configuration
- seed
- git commit
- parameter count
- epoch time
- GPU memory when available
- full Phone/Word/Utterance/MDD metrics

Analyze failure patterns conditioned on available data:
- vowel vs consonant
- phone type/frequency
- word length
- utterance length
- score range
- correctly vs incorrectly detected pronunciation
- APA/MDD disagreement
- cross-granularity disagreement

Important cases:
- phone correct, word wrong
- word correct, utterance wrong
- APA confident, MDD wrong
- low-level gains that vanish at higher levels

Classify evidence into possible bottleneck families:
A. representation
B. fusion
C. local context
D. hierarchical aggregation
E. task interaction

Do not turn a correlation into a causal claim.

Produce:
- research/00_baseline/baseline_analysis.md
- research/02_failure_analysis/phone.md
- research/02_failure_analysis/word.md
- research/02_failure_analysis/utterance.md
- research/02_failure_analysis/cross_level.md
