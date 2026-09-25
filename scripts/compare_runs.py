#!/usr/bin/env python3
import argparse
import os
import pandas as pd

HIGHER_BETTER = [
    "phone_test_pcc",
    "word_test_pcc_accuracy",
    "word_test_pcc_stress",
    "word_test_pcc_total",
    "utt_test_pcc_accuracy",
    "utt_test_pcc_completeness",
    "utt_test_pcc_fluency",
    "utt_test_pcc_prosodic",
    "utt_test_pcc_total",
    "f1_mdd",
    "precision_mdd",
    "recall_mdd",
]
LOWER_BETTER = ["phone_test_mse"]

def load(exp_dir):
    path = os.path.join(exp_dir, "result.csv")
    df = pd.read_csv(path)
    if len(df) != 1:
        raise ValueError(f"Expected one best-result row in {path}, found {len(df)}")
    return df.iloc[0]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--baseline", required=True)
    p.add_argument("--candidate", required=True)
    p.add_argument("--pcc-regression", type=float, default=0.01,
                   help="absolute drop treated as a visible regression")
    p.add_argument("--mse-regression", type=float, default=0.002,
                   help="absolute MSE increase treated as a visible regression")
    args = p.parse_args()

    b = load(args.baseline)
    c = load(args.candidate)

    regressions = []
    print("Matched run comparison")
    print("=" * 84)

    for name in LOWER_BETTER:
        raw = float(c[name]) - float(b[name])
        improvement = -raw
        flag = raw > args.mse_regression
        if flag:
            regressions.append(name)
        print(f"{name:30s} baseline={b[name]:.6f} candidate={c[name]:.6f} "
              f"improvement={improvement:+.6f} {'REGRESSION' if flag else ''}")

    for name in HIGHER_BETTER:
        improvement = float(c[name]) - float(b[name])
        flag = improvement < -args.pcc_regression
        if flag:
            regressions.append(name)
        print(f"{name:30s} baseline={b[name]:.6f} candidate={c[name]:.6f} "
              f"improvement={improvement:+.6f} {'REGRESSION' if flag else ''}")

    print("=" * 84)
    if regressions:
        print("Visible regressions:", ", ".join(regressions))
        print("Interpret scientifically before promoting the hypothesis.")
    else:
        print("No metric crossed the configured visible-regression threshold.")
        print("This is NOT proof of superiority; inspect seeds and full-training behavior.")

if __name__ == "__main__":
    main()
