# What this notebook does

- Loads the Iris dataset from scikit-learn using a DataFrame-friendly format.
- Explores class separability visually with a Seaborn pairplot.
- Trains a `RandomForestClassifier` and evaluates it with 5-fold cross-validation.
- Fits the classifier on the full dataset and reports training accuracy.
- Implements a reusable prediction function that accepts four flower measurements.
- Builds an interactive Gradio interface for manual species prediction.
- Adds example inputs to quickly test all three Iris classes in the UI.
- Saves the trained model to disk (`iris_random_forest_classifier.pkl`) for reuse.

# Key concepts to reuse

- End-to-end notebook workflow: data loading, exploration, training, evaluation, and deployment in one pipeline.
- Cross-validation before deployment: validate model reliability before exposing predictions in a UI.
- Reproducibility: set `random_state` in tree-based models for consistent results.
- Prediction wrapper function: encapsulate preprocessing and inference logic into a single callable function.
- Fast prototyping for ML apps: use Gradio to turn model functions into shareable interfaces quickly.
- Example-driven UX: provide realistic sample inputs to make testing easier for users.
- Model persistence: export trained models with `pickle` to decouple training from inference/runtime apps.
