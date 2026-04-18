# Case Study Part 1 - Model Performance and Error Analysis

## Project Title
Credit Risk Assessment with Comprehensive Validation

## Objective
The objective of this case study is to build and evaluate a robust credit risk classification model for predicting loan default. The project emphasizes rigorous model validation, class imbalance handling, feature selection, bootstrap analysis, and error analysis.

## Dataset
- Source dataset file: `data/loan.csv`
- Domain: Credit risk / loan default prediction

## Key Workflow
1. Load and inspect the dataset
2. Define a binary target variable from loan status
3. Remove leakage-prone and non-predictive columns
4. Engineer date-based credit history features
5. Create train-test split with stratification
6. Build preprocessing and baseline Logistic Regression model
7. Evaluate model performance and analyze classification errors
8. Compare cross-validation strategies
9. Compare class imbalance handling methods
10. Apply feature selection using Mutual Information, RFE, and L1 regularization
11. Perform bootstrap analysis and confidence interval estimation
12. Summarize final modeling findings

## Main Findings
- The baseline Logistic Regression model achieved high accuracy but very poor recall for defaults.
- Resampling methods substantially improved recall and reduced false negatives.
- Random Oversampling provided the best balance among the tested core resampling methods.
- Bootstrap analysis indicated that the selected model was reasonably stable across repeated resampled training datasets.

## Key Output Files
Saved result tables are available in the `outputs/` folder:
- `baseline_vs_resampling_comparison.csv`
- `mutual_information_scores.csv`
- `rfe_results.csv`
- `l1_feature_selection_results.csv`
- `bootstrap_confidence_intervals.csv`
- `final_summary_comparison.csv`

## Environment
This project was developed in VS Code using the shared Python environment:
- `.venv_global`