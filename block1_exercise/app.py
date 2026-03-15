import gradio as gr
import pickle
import pandas as pd

# ── Load model artifact at startup ────────────────────────────────────────────
with open("model.pkl", "rb") as f:
    artifact = pickle.load(f)

pipeline        = artifact["pipeline"]
feature_names   = artifact["feature_names"]
median_defaults = artifact["median_defaults"]


# ── Core prediction function ──────────────────────────────────────────────────
def predict_price(rooms, area_m2, temporary, dist_to_nearest_station_km):
    # Start from stored median values for hidden features
    row = dict(median_defaults)

    # Override with user-supplied values
    row["rooms"]                       = float(rooms)
    row["area"]                        = float(area_m2)
    row["temporary"]                   = int(temporary)
    row["dist_to_nearest_station_km"]  = float(dist_to_nearest_station_km)

    # Recompute derived features that depend on user inputs
    row["room_per_m2"]     = round(float(area_m2) / float(rooms), 4) if rooms > 0 else median_defaults["room_per_m2"]
    row["area_cat_ecoded"] = 0.0 if area_m2 < 50 else (1.0 if area_m2 < 100 else 2.0)

    # Build DataFrame in the exact column order the pipeline expects
    X = pd.DataFrame([row])[feature_names]

    prediction = pipeline.predict(X)[0]
    return f"CHF {round(prediction):,} / month"


# ── Gradio Interface ──────────────────────────────────────────────────────────
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Rooms", value=3.5, minimum=1, maximum=10),
        gr.Number(label="Area (m²)", value=80, minimum=10, maximum=500),
        gr.Radio(
            choices=[0, 1],
            label="Temporary rental? (0 = No, 1 = Yes)",
            value=0,
        ),
        gr.Slider(
            minimum=0,
            maximum=5,
            step=0.1,
            label="Distance to nearest train station (km)",
            value=1.0,
        ),
    ],
    outputs=gr.Textbox(label="Predicted Monthly Rent"),
    title="Canton Zurich Apartment Price Predictor",
    description=(
        "Predict monthly rental prices in Canton Zurich (CHF). "
        "Population density, tax income, and other location factors "
        "are fixed to canton-wide median values."
    ),
    examples=[
        [4.5, 120, 0, 0.5],
        [2.5, 55,  0, 2.0],
        [3.5, 80,  1, 1.0],
        [1.5, 38,  0, 0.3],
    ],
)

if __name__ == "__main__":
    iface.launch()
