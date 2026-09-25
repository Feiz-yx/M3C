# M3C Prime Agent Research Protocol

## Mission

This repository is an ML research project built on M3C (Matrix-Structured Hierarchical Convolutional Modeling for Pronunciation Assessment and Mispronunciation Detection).

The objective is to produce scientifically justified improvements, not arbitrary metric optimization or architecture search.

The target is **multi-granularity improvement** across:
- Phone: MSE down, PCC up
- Word: Accuracy / Stress / Total PCC up
- Utterance: Accuracy / Completeness / Fluency / Prosodic / Total PCC up
- MDD: Precision / Recall / F1 preserved or improved

A method is not globally successful when it only improves one granularity while clearly degrading the others.

## Baseline architecture

Read the implementation before proposing changes.

Current path:
heterogeneous GOP + SSL + duration/energy
-> vowel/consonant-specific CCC extraction
-> SSL CCC extraction
-> feature fusion
-> explicit triphone construction
-> phone CCC
-> phone APA and MDD heads
-> word CCC
-> word aspect interaction
-> utterance CCC
-> score-restraint attention pooling
-> utterance aspect interaction

Primary files:
- src/models/M3C.py
- src/custom_layers/attention.py
- src/custom_layers/scoreRestraintAttentionPooling.py
- src/traintest.py
- src/run_M3C.sh
- src/collect_summary.py

## Scientific workflow

Every proposed modification MUST follow:

Observed failure
-> exact code mechanism
-> generic ML problem
-> supporting literature
-> transfer rationale
-> falsifiable hypothesis
-> minimal intervention
-> cheap experiment
-> matched comparison
-> full experiment
-> ablation

Do not implement a method before the hypothesis is written.

## Research priority

Prioritize structural questions in this order:

1. Hierarchical information propagation across Phone -> Word -> Utterance
2. Heterogeneous feature topology / organization
3. Structured feature fusion and feature contamination
4. Context rigidity of fixed triphone modeling
5. Multi-aspect task interaction
6. APA-MDD conflict or collaboration

Do not search for "methods that improve M3C". Search for methods that solve the underlying generic problem.

## Baseline protection

Unless a hypothesis explicitly targets them, preserve:
- official train/test split
- optimizer
- scheduler
- loss definitions
- batch size
- M3C hierarchical task outputs
- evaluation functions
- data normalization

Never overwrite the baseline path just to make a new method easier to implement.

Prefer optional modules and feature flags.

## Reproducibility

The upstream repository used repeat IDs but did not explicitly seed Python/NumPy/PyTorch.

This fork adds an optional --seed argument to src/traintest.py.

Rules:
- Use explicit seed values for research comparisons.
- Compare baseline and candidate with the same seed.
- Screening: seed 0 first.
- Promising candidates: seeds 0,1,2.
- Final candidates: seeds 0,1,2,3,4.
- Record git commit for every experiment.

## Experiment gates

Do not launch full training immediately.

Stage 0: static / shape check
- import succeeds
- forward path succeeds
- tensor shapes match
- no NaN/Inf

Stage 1: 1 epoch smoke test
- training completes
- losses are finite
- metrics are produced

Stage 2: 5 epoch screening
- matched seed
- inspect learning direction
- reject obvious regressions

Stage 3: 10 epoch screening
- seeds 0,1,2 for promising methods
- inspect consistency, not only best seed

Stage 4: 50 epoch full validation
- at least 3 seeds

Stage 5: final validation
- 5 seeds
- component ablation
- efficiency report

## Early screening interpretation

Do NOT assume that the best 5/10-epoch metric must be the final winner.

Use early experiments to reject clearly weak hypotheses and to estimate:
- learning speed
- optimization stability
- direction consistency
- cross-granularity trade-offs

A method should advance only when there is no strong evidence of systematic regression.

## Literature transfer

For every borrowed method record:
- paper title
- year
- venue
- source task/problem
- core mechanism
- strongest ablation evidence
- official/source repository
- corresponding M3C bottleneck
- why the mechanism maps
- required adaptation
- implementation cost
- expected failure mode

A recent paper is not automatically a useful paper.

## Hypothesis standard

Every hypothesis must explicitly state:
- Observation
- Code mechanism
- Structural assumption
- Proposed mechanism
- Expected metric pattern
- Falsification condition
- Minimal experiment
- Compute cost

Maximum active hypotheses: 6.
Prefer high mechanism-match and low-cost tests.

## Coding standard

Research modules should normally live under:
src/models/modules/

Keep new mechanisms independently removable.

One major scientific variable per experiment.
Do not bundle unrelated ideas.

## Result analysis

After every experiment separate:
1. observation
2. mechanism interpretation
3. alternative explanation
4. supporting evidence
5. contradicting evidence

Classify the hypothesis:
- SUPPORTED
- PARTIALLY_SUPPORTED
- INCONCLUSIVE
- REFUTED

Do not equate a metric increase with proof of the proposed mechanism.

## Research memory

Persist research state in the repository, not only in chat.

Update:
- research/decisions.md
- experiments/registry.csv
- research/05_analysis/

Do not repeat experiments that have already falsified the same mechanism unless new evidence justifies it.
