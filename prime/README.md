# Prime Agent Quickstart for M3C

Run from the repository root.

## 1. Start Prime Agent

```bash
prime-agent
```

Set the persistent goal:

```text
/goal
Develop a scientifically justified structural improvement to M3C.
Optimize for consistent Phone, Word, Utterance and MDD performance.
Follow AGENTS.md and RESEARCH.md.
Do not modify the model until baseline reconstruction is complete.
```

## 2. Phase 0 — understand the repository

Give Prime Agent:

```text
Read and execute the instructions in:
prime/prompts/phase0_architecture.md
```

Expected outputs:
- research/00_baseline/baseline_protocol.md
- research/01_model_map/architecture.md
- research/01_model_map/dataflow.md
- research/01_model_map/bottlenecks.md

## 3. Establish a reproducible baseline

Example cheap baseline:

```bash
EPOCHS=5 SEED=0 TAG=baseline bash scripts/run_screening.sh
```

Full matched baseline:

```bash
EPOCHS=50 SEED=0 TAG=baseline bash scripts/run_screening.sh
```

The output directory follows:

```text
exp/prime-<TAG>-e<EPOCHS>-s<SEED>
```

## 4. Register the run

From repository root:

```bash
python scripts/summarize_experiment.py \
  exp/prime-baseline-e5-s0 \
  --experiment-id BASE-E5-S0 \
  --hypothesis-id BASE \
  --method baseline \
  --stage screen5 \
  --seed 0 \
  --epochs 5
```

This appends the result to:

```text
experiments/registry.csv
```

## 5. Phase 1 — failure analysis

Give Prime Agent:

```text
Read and execute:
prime/prompts/phase1_failure.md
```

Do not ask it to propose methods yet.

## 6. Phase 2 — literature transfer

After failure analysis:

```text
Read and execute:
prime/prompts/phase2_literature.md
```

This phase should produce no more than six falsifiable hypotheses.

## 7. Validate one hypothesis at a time

For a selected hypothesis:

```text
Validate H001 according to:
prime/prompts/validate_hypothesis.md
```

Suggested experiment funnel:

```text
Stage 0  static / forward
Stage 1  1 epoch, seed 0
Stage 2  5 epochs, seed 0
Stage 3  10 epochs, seeds 0/1/2
Stage 4  50 epochs, seeds 0/1/2
Stage 5  final 5 seeds + ablation
```

## 8. Compare matched runs

```bash
python scripts/compare_runs.py \
  --baseline exp/prime-baseline-e5-s0 \
  --candidate exp/prime-H001-e5-s0
```

The comparison script flags visible regressions but does not declare a scientific winner.

## 9. Autonomous mode

Use autonomous mode only after a hypothesis is explicit.

Example:

```text
/autonomous

Validate H001 only.
Follow AGENTS.md experiment gates.
Do not introduce unrelated changes.
Stop after the hypothesis has a documented conclusion.
```

## 10. Research memory

After every experiment update:
- experiments/registry.csv
- research/05_analysis/EXPXXX.md
- research/decisions.md

Use `/refine` only after repeated empirical evidence supports a reusable lesson.
