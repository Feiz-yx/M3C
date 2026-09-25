#!/usr/bin/env bash
set -euo pipefail

# Controlled M3C screening runner.
# Usage from repository root:
#   EPOCHS=5 SEED=0 TAG=baseline bash scripts/run_screening.sh
#   EPOCHS=10 SEED=1 TAG=H001 bash scripts/run_screening.sh
#
# The arguments below intentionally mirror src/run_M3C.sh.

EPOCHS="${EPOCHS:-5}"
SEED="${SEED:-0}"
TAG="${TAG:-screen}"
LR="${LR:-1e-3}"
BATCH_SIZE="${BATCH_SIZE:-2}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}/src"

MODEL=m3c
AM=features_vc_clean_embbedings_norm
EMBED_DIM=24

NUM_CONVS_VC=32
INPUT_DIM_VOWELS=15
INPUT_DIM_CONSONANTS=24
OUTPUT_DIM_VC=30
DROPOUT_CNN_VC=0.4
DROPOUT_MLP_VC=0.

NUM_CONVS_SSL=2
INPUT_DIM_SSL=1024
OUTPUT_DIM_SSL=30
DROPOUT_CNN_SSL=0.8
DROPOUT_MLP_SSL=0.

FUSION_DIM=30
DROPOUT_MLP_FUSION=0.3

NUM_CONVS_PHN=32
OUTPUT_DIM_PHN=30
DROPOUT_CNN_PHN=0.
DROPOUT_MLP_PHN=0.

NUM_CONVS_WORD=32
OUTPUT_DIM_WORD=30
DROPOUT_CNN_WORD=0.2
DROPOUT_MLP_WORD=0.

NUM_CONVS_UTT=32
OUTPUT_DIM_UTT=30
DROPOUT_CNN_UTT=0.
DROPOUT_MLP_UTT=0.

ALPHA_MDD=0.03

EXP_DIR="../exp/prime-${TAG}-e${EPOCHS}-s${SEED}"
mkdir -p "${EXP_DIR}"

echo "Running M3C screening: tag=${TAG} epochs=${EPOCHS} seed=${SEED}"
echo "Output: ${EXP_DIR}"

python ./traintest.py   --lr "${LR}"   --exp-dir "${EXP_DIR}"   --batch_size "${BATCH_SIZE}"   --embed_dim "${EMBED_DIM}"   --model "${MODEL}"   --am "${AM}"   --n-epochs "${EPOCHS}"   --seed "${SEED}"   --alpha_mdd "${ALPHA_MDD}"   --num_convs_vc "${NUM_CONVS_VC}"   --input_dim_vowels "${INPUT_DIM_VOWELS}"   --input_dim_consonants "${INPUT_DIM_CONSONANTS}"   --output_dim_vc "${OUTPUT_DIM_VC}"   --dropout_cnn_vc "${DROPOUT_CNN_VC}"   --dropout_mlp_vc "${DROPOUT_MLP_VC}"   --num_convs_ssl "${NUM_CONVS_SSL}"   --input_dim_ssl "${INPUT_DIM_SSL}"   --output_dim_ssl "${OUTPUT_DIM_SSL}"   --dropout_cnn_ssl "${DROPOUT_CNN_SSL}"   --dropout_mlp_ssl "${DROPOUT_MLP_SSL}"   --fusion_dim "${FUSION_DIM}"   --dropout_mlp_fusion "${DROPOUT_MLP_FUSION}"   --num_convs_phn "${NUM_CONVS_PHN}"   --output_dim_phn "${OUTPUT_DIM_PHN}"   --dropout_cnn_phn "${DROPOUT_CNN_PHN}"   --dropout_mlp_phn "${DROPOUT_MLP_PHN}"   --num_convs_word "${NUM_CONVS_WORD}"   --output_dim_word "${OUTPUT_DIM_WORD}"   --dropout_cnn_word "${DROPOUT_CNN_WORD}"   --dropout_mlp_word "${DROPOUT_MLP_WORD}"   --num_convs_utt "${NUM_CONVS_UTT}"   --output_dim_utt "${OUTPUT_DIM_UTT}"   --dropout_cnn_utt "${DROPOUT_CNN_UTT}"   --dropout_mlp_utt "${DROPOUT_MLP_UTT}"

echo "Finished: ${EXP_DIR}"
