# What this notebook does

- Builds a feature-engineering workflow to improve apartment price prediction.
- Starts from a baseline feature set and evaluates model quality with cross-validated RMSE.
- Cleans data by removing missing values, duplicates, and extreme outliers.
- Creates new engineered features from numeric fields, including `room_per_m2`.
- Extracts binary text features from listing descriptions (for example `luxurious`, `temporary`, `furnished`) using keyword patterns.
- Runs error analysis on model residuals and exports high-error cases for manual review.
- Tunes model hyperparameters with `GridSearchCV` and `RandomizedSearchCV`.
- Saves the enriched dataset for later modeling steps.

# Key concepts to reuse

- Baseline-first iteration: measure a simple baseline before adding features.
- Reproducible evaluation: fix `random_state` and use cross-validation for stable comparisons.
- Data-quality-first modeling: clean data before feature engineering and training.
- Domain-driven feature creation: encode business hints from text into binary indicators.
- Leakage checks: avoid features derived from the target (for example `price_per_m2`) during training.
- Error-driven improvement loop: inspect large residuals to discover missing features or data issues.
- Hyperparameter search strategy: combine small grid search and randomized search for efficient tuning.
- Persist intermediate artifacts (enriched data, error slices) to support downstream notebooks and project reports.
