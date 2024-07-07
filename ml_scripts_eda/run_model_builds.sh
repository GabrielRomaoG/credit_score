#!/bin/sh

# Run the first model build script
python ml_scripts_eda/credit_score_1/cs1_model_build.py ml_scripts_eda/credit_score_1/credit_score_dataset_1.csv ml_scripts_eda/credit_score_1/cs1_model

# Run the second model build script
python ml_scripts_eda/credit_score_2/cs2_model_build.py ml_scripts_eda/credit_score_2/credit_score_dataset_2.csv ml_scripts_eda/credit_score_2/cs2_model
