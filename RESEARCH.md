# M3C Research Program

## Goal

Develop a structural improvement to M3C that improves or preserves performance across Phone, Word, Utterance and MDD, with emphasis on large PCC gains and lower MSE rather than isolated phone-level gains.

The research strategy is mechanism-first:
code observation -> bottleneck -> generic ML problem -> external method -> adapted hypothesis -> experiment.

## Current M3C structure

### Feature level
M3C separates vowels and consonants, applies CCC-based processing to GOP-style features, compresses HuBERT/Wav2Vec2/WavLM SSL features with a shared CCC, concatenates them with duration and energy, and applies a fusion MLP.

### Phone level
The fused representation receives a V/C bit. Explicit triphones are created with a fixed radius of one neighbor on each side and passed through a phone CCC. Phone regression and MDD classification use separate projections and aspect interaction.

### Word level
Phone representations are grouped by word ID, padded to a fixed word context, processed by a word CCC, and mapped to Accuracy / Stress / Total outputs.

### Utterance level
Word representations are processed by an utterance CCC. Phone scores, MDD outputs and word scores are injected through ScoreRestraintAttentionPooling before five utterance-level aspect regressors.

## Core research questions

### RQ1 — Hierarchical propagation
Does one-way Phone -> Word -> Utterance compression lose information needed by higher-level scores?

Candidate generic problems:
- hierarchical message passing
- multi-scale feature propagation
- coarse-to-fine / fine-to-coarse feedback
- cross-level residual learning

### RQ2 — Feature topology
Does the fixed matrix/CCC organization impose locality that does not match the semantic dependency structure of heterogeneous pronunciation features?

Candidate generic problems:
- learnable topology
- relation-aware feature interaction
- dynamic sparse routing
- graph structure learning
- set modeling

### RQ3 — Fusion noise
Does early concatenation followed by a single MLP force incompatible sources to mix and propagate noise?

Candidate generic problems:
- selective feature fusion
- conditional routing
- gated expert fusion
- reliability-aware fusion
- shared/private decomposition

### RQ4 — Context rigidity
Is fixed triphone context too restrictive for pronunciation errors whose evidence spans variable phonetic context?

Candidate generic problems:
- adaptive receptive fields
- dynamic context selection
- local-global interaction
- context-conditioned aggregation

### RQ5 — Multi-aspect interaction
Are pronunciation aspects coupled with a fixed late-stage interaction mechanism when their relationships may vary by sample?

Candidate generic problems:
- task relationship learning
- task-conditioned routing
- task graphs
- shared/private multi-task representation

### RQ6 — APA/MDD interaction
Do regression and mispronunciation classification provide complementary supervision, or do their gradients conflict?

Candidate generic problems:
- multi-task gradient conflict
- auxiliary-task routing
- uncertainty-based weighting
- gradient surgery
- representation disentanglement

## Research order

Initial priority:
1. RQ1 hierarchical propagation
2. RQ2 feature topology
3. RQ3 fusion noise

Reason: these three directly address the requirement that Phone, Word and Utterance metrics improve together and connect to the core structural contributions of M3C.

## Success criterion

Do not use a single scalar "winner" score.

A candidate should show a favorable Pareto pattern:
- Phone PCC not meaningfully worse
- Phone MSE not meaningfully worse
- Word metrics improve or remain stable
- Utterance metrics improve or remain stable
- MDD F1 does not collapse
- gains are consistent across seeds
- parameter/compute increase is justified

## Compute funnel

Many ideas
-> mechanism filter
-> at most 6 hypotheses
-> 1 epoch smoke tests
-> 5 epoch seed-0 screening
-> 10 epoch seeds 0/1/2
-> top 1–2 methods at 50 epochs
-> component ablation
-> final 5-seed report
