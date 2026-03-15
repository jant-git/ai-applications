# What this notebook does

- Loads a pre-trained `RandomForestRegressor` model from `random_forest_regression.pkl`.
- Loads municipality-level context data (`bfs_municipality_and_tax_data.csv`) and prepares numeric fields.
- Defines a town-to-BFS mapping used to join user input with municipality statistics.
- Implements a prediction function (`predict_apartment`) that combines user features (`rooms`, `area`, `town`) with external municipality features.
- Validates lookup results and returns a rounded predicted apartment price.
- Wraps the prediction logic into an interactive Gradio app with numeric inputs, a town dropdown, and example inputs.
- Launches a local web interface for fast manual testing of the trained model.

# Key concepts to reuse

- Model inference pipeline: separate model training from deployment by loading serialized models (`pickle`).
- Feature consistency: ensure inference uses the exact same feature order and columns as training.
- Data enrichment at inference time: combine user inputs with external lookup tables (BFS/municipality metadata).
- Mapping strategy: use dictionary-based key mapping (town -> BFS number) for deterministic joins.
- Input validation: guard against ambiguous or missing lookup results before prediction.
- Lightweight app deployment: use Gradio for quick, reproducible ML demos without full backend setup.
- Reusable prediction wrapper: keep `predict_apartment(...)` as a clean function so it can later be reused in APIs or batch scripts.
