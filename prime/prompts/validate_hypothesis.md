# Hypothesis validation protocol

Input: one HXXX hypothesis card.

Do not introduce unrelated changes.

1. Create or use an isolated research branch.
2. Implement the smallest intervention that tests HXXX.
3. Keep baseline behavior available when the new mechanism is disabled.
4. Prefer new reusable modules under src/models/modules/.
5. Record modified files and parameter delta.

Run gates in order:

Stage 0:
- import / syntax
- tensor-shape check
- forward check
- NaN/Inf check

Stage 1:
- 1 epoch, seed 0

Stage 2:
- 5 epochs, seed 0

If Stage 2 has obvious cross-granularity regression, stop and analyze.

Stage 3:
- 10 epochs, seeds 0,1,2

If promising and consistent:
Stage 4:
- 50 epochs, seeds 0,1,2

Only final candidates:
Stage 5:
- seeds 0,1,2,3,4
- ablation

After every run:
python scripts/summarize_experiment.py <exp-dir> --experiment-id EXPXXX --hypothesis-id HXXX --method <name> --stage <stage> --seed <seed> --epochs <epochs>

Compare candidate with matched baseline:
python scripts/compare_runs.py --baseline <baseline-exp-dir> --candidate <candidate-exp-dir>

Write the scientific interpretation to:
research/05_analysis/EXPXXX.md

Classify HXXX:
SUPPORTED / PARTIALLY_SUPPORTED / INCONCLUSIVE / REFUTED

Update research/decisions.md.
