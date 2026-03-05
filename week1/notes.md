# What this notebook does

- Loads and cleans apartment data (dropna, drop_duplicates), then defines features X and target y=price.
- Splits data into train/test (80/20, fixed seed for reproducibility).
- Trains two regression models: LinearRegression and RandomForestRegressor.
- Evaluates with R² and RMSE on train and test.
- Interprets model behavior with feature importance and residual/error analysis.
- Exports high-error listing descriptions for manual inspection.

# Key concepts to reuse

- Baseline-first modeling (simple vs more complex model).
- Reproducible experiments (random_state).
- Train vs test comparison to detect over/underfitting.
- Multiple metrics (R², RMSE) for better judgment.
- Error-driven improvement (analyze residuals, inspect worst predictions).