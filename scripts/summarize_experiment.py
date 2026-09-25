#!/usr/bin/env python3
import argparse
import csv
import os
import subprocess
import pandas as pd

FIELDS = {
    "phone_test_mse": "phone_test_mse",
    "phone_test_pcc": "phone_test_pcc",
    "word_accuracy_pcc": "word_test_pcc_accuracy",
    "word_stress_pcc": "word_test_pcc_stress",
    "word_total_pcc": "word_test_pcc_total",
    "utt_accuracy_pcc": "utt_test_pcc_accuracy",
    "utt_completeness_pcc": "utt_test_pcc_completeness",
    "utt_fluency_pcc": "utt_test_pcc_fluency",
    "utt_prosodic_pcc": "utt_test_pcc_prosodic",
    "utt_total_pcc": "utt_test_pcc_total",
    "mdd_f1": "f1_mdd",
    "mdd_precision": "precision_mdd",
    "mdd_recall": "recall_mdd",
}

def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return ""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("exp_dir")
    p.add_argument("--experiment-id", required=True)
    p.add_argument("--hypothesis-id", default="BASE")
    p.add_argument("--method", required=True)
    p.add_argument("--stage", required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--epochs", type=int, required=True)
    p.add_argument("--status", default="COMPLETED")
    p.add_argument("--notes", default="")
    p.add_argument("--registry", default="experiments/registry.csv")
    args = p.parse_args()

    path = os.path.join(args.exp_dir, "result.csv")
    if not os.path.isfile(path):
        raise FileNotFoundError(path)

    df = pd.read_csv(path)
    if len(df) != 1:
        raise ValueError(f"Expected one best-result row in {path}, found {len(df)}")
    row = df.iloc[0]

    record = {
        "experiment_id": args.experiment_id,
        "hypothesis_id": args.hypothesis_id,
        "method": args.method,
        "stage": args.stage,
        "seed": args.seed,
        "epochs": args.epochs,
        "git_commit": git_commit(),
    }
    for dst, src in FIELDS.items():
        record[dst] = row[src]
    record["status"] = args.status
    record["notes"] = args.notes

    print("\nExperiment summary")
    print("-" * 72)
    for k, v in record.items():
        print(f"{k}: {v}")

    with open(args.registry, newline="") as f:
        fieldnames = next(csv.reader(f))

    with open(args.registry, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(record)

    print(f"\nAppended to {args.registry}")

if __name__ == "__main__":
    main()
