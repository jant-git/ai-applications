# Model Iterations Documentation
## Task: Apartment Price Prediction (Regression) — Canton Zurich

---

## Summary of Iterative Process

| Iteration | Objective | Key Changes vs. Previous | Models Used | CV Mean RMSE (CHF) | CV Mean R² | CV R² Std Dev | Change in R² | Fit Diagnosis |
|---|---|---|---|---|---|---|---|---|
| **1** | Establish baseline with existing features | First model run — 13 existing features, default hyperparameters, no tuning | LinearRegression (R²=0.51), RandomForest n=100 (R²=0.49) | LR: 690.6 / RF: 716.5 | LR: 0.51 / RF: 0.49 | LR: ±0.10 / RF: ±0.05 | — | LinearRegression: underfitting; RandomForest: high variance (overfitting) |
| **2** | Add geospatial feature + hyperparameter tuning | Added `dist_to_nearest_station_km` (14th feature); RandomizedSearchCV (20 iter, 5-fold) on RandomForest and LightGBM | RF Tuned (R²=0.57), LightGBM Tuned (R²=0.56) | RF: 661.8 / LGB: 668.9 | RF: 0.57 / LGB: 0.56 | RF: ±0.05 / LGB: ±0.05 | +0.06 (vs best iter 1) | Good fit — reduced variance; **RF Tuned selected as final model** (lower CV RMSE) |

---

## Notes

### Metric
- **5-Fold Cross-Validation** on full cleaned dataset
- Metrics reported: **RMSE** (Root Mean Squared Error, CHF) and **R²** (coefficient of determination)

### Data Preprocessing Steps
- Load `apartments_data_enriched_with_new_features.csv`
- Drop rows with missing values in model features, `lat`, `lon`, and `price`
- Remove duplicate rows
- Filter price range: 750 CHF ≤ price ≤ 8,000 CHF (removes outliers consistent with prior work in week2)
- Compute new feature `dist_to_nearest_station_km` via Haversine distance to nearest of 15 major train stations
- Apply `StandardScaler` to continuous numeric features; binary features passed through unchanged

### New Feature Created
**`dist_to_nearest_station_km`**
Haversine distance (km) from the apartment's GPS coordinates (`lat`, `lon`) to the nearest of 15 major train stations in Canton Zurich (Zürich HB, Winterthur, Uster, Bülach, Dietikon, Wädenswil, Thalwil, Kloten, Dübendorf, Regensdorf, Pfäffikon ZH, Horgen, Schlieren, Effretikon, Zollikon).

Transit proximity is a known driver of rental prices in Switzerland: apartments near S-Bahn stations command higher rents, so including this feature adds real predictive signal that is not captured by the existing demographic features.

### Final Selected Features (Iteration 2 — 14 features)

| Feature | Type | Source |
|---|---|---|
| `rooms` | Numeric | Original data |
| `area` | Numeric | Original data |
| `room_per_m2` | Numeric | Engineered in week2 |
| `area_cat_ecoded` | Ordinal (0/1/2) | Engineered in week2 |
| `pop` | Numeric | BFS municipality data |
| `pop_dens` | Numeric | BFS municipality data |
| `frg_pct` | Numeric | BFS municipality data |
| `emp` | Numeric | BFS municipality data |
| `tax_income` | Numeric | BFS municipality data |
| `luxurious` | Binary | Engineered in week2 (text flags) |
| `temporary` | Binary | Engineered in week2 (text flags) |
| `furnished` | Binary | Engineered in week2 (text flags) |
| `zurich_city` | Binary | Engineered in week2 (geodata) |
| `dist_to_nearest_station_km` | Numeric | **New — engineered in this exercise** |

### Excluded Features
- `price_per_m2`: excluded due to **target leakage** (derived directly from `price`)
- `lat`, `lon`: raw coordinates excluded as direct features; encoded indirectly via `dist_to_nearest_station_km`
- `description_raw`: raw text not processed in this exercise

### Final Selected Model
**RandomForest** (`RandomForestRegressor`) with tuned hyperparameters found via `RandomizedSearchCV` (20 iterations, 5-fold CV).

Best hyperparameters: `n_estimators=500`, `max_depth=20`, `max_features=0.5`, `min_samples_leaf=2`, `min_samples_split=4`.

Selected over the tuned LightGBM because it achieves lower CV RMSE (661.8 vs 668.9 CHF) and slightly higher R² (0.566 vs 0.560).
The full sklearn `Pipeline` (preprocessor + model) is saved to `model.pkl`.

---

## How to Run

### Modeling Notebook
```bash
jupyter lab modeling.ipynb
# Run all cells top-to-bottom; model.pkl is saved in the last section
```

### Gradio App
```bash
pip install -r requirements.txt
python app.py
# Opens at http://127.0.0.1:7860
```
