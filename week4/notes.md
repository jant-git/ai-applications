# What this notebook does

- Loads the enriched apartment dataset and performs core cleaning (`dropna`, `drop_duplicates`).
- Validates required feature columns and conditionally includes optional features when available.
- Builds a train/test split for regression modeling with a fixed random seed.
- Trains and evaluates a `RandomForestRegressor` as a strong tree-based baseline.
- Trains an `MLPRegressor` on standardized features and tracks train/test RMSE across epochs.
- Visualizes neural-network training dynamics with RMSE and loss curves.
- Implements a custom PyTorch regression network for the same prediction task.
- Trains the PyTorch model over many epochs and compares train/test loss and RMSE.
- Produces diagnostic plots, including actual vs predicted prices, to assess model behavior.

# Key concepts to reuse

- Feature schema checks before training: fail early when required columns are missing.
- Optional-feature pattern: include additional columns only if present to keep pipelines robust.
- Baseline-to-advanced progression: compare classic ML (`RandomForest`) with neural models (`MLP`, PyTorch).
- Model-specific preprocessing: standardize inputs for MLP-style models while tree models usually do not require scaling.
- Learning-curve diagnostics: monitor train/test RMSE over epochs to detect overfitting and underfitting.
- Framework comparison workflow: evaluate the same task in scikit-learn and PyTorch for practical tradeoff analysis.
- Regression diagnostics: use RMSE plus actual-vs-predicted plots for a fuller quality check.
- Reproducibility discipline: keep `random_state` fixed across splits and models for consistent comparisons.
