import gradio as gr
import base64
import os
import re
import json
from transformers import pipeline
from openai import OpenAI

# Model 1: Fine-tuned ViT
vit_classifier = pipeline("image-classification", model="lnlywlf/sports-vit")

# Model 2: CLIP Zero-Shot
clip_classifier = pipeline(
    model="openai/clip-vit-large-patch14",
    task="zero-shot-image-classification",
)

SPORTS_LABELS = [
    "baseball", "basketball", "boxing", "cricket", "football",
    "hockey", "surfing", "swimming", "tennis", "volleyball",
]


def encode_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def classify_with_openai(image_path):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set"}

    client = OpenAI(api_key=api_key)
    b64 = encode_image_base64(image_path)

    prompt = (
        f"Classify the sport shown in this image. "
        f"Choose exactly one from: {', '.join(SPORTS_LABELS)}. "
        f'Return only valid JSON: {{"label": "<sport>", "confidence": <0.0-1.0>}}'
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                    },
                ],
            }
        ],
        max_tokens=200,
    )

    text = response.choices[0].message.content
    text = re.sub(r"```json?\n?|\n?```", "", text).strip()
    try:
        result = json.loads(text)
        return {result["label"]: result["confidence"]}
    except (json.JSONDecodeError, KeyError):
        return {"raw_response": text}


def classify_sports(image):
    # Model 1: Fine-tuned ViT
    vit_results = vit_classifier(image)
    vit_output = {r["label"]: round(r["score"], 4) for r in vit_results}

    # Model 2: CLIP Zero-Shot
    clip_results = clip_classifier(image, candidate_labels=SPORTS_LABELS)
    clip_output = {r["label"]: round(r["score"], 4) for r in clip_results}

    # Model 3: OpenAI GPT-4o-mini
    openai_output = classify_with_openai(image)

    return {
        "ViT Fine-tuned": vit_output,
        "CLIP Zero-Shot": clip_output,
        "OpenAI GPT-4o-mini": openai_output,
    }


example_images = [
    ["example_images/baseball.jpg"],
    ["example_images/basketball.jpg"],
    ["example_images/boxing.jpg"],
    ["example_images/swimming.jpg"],
    ["example_images/tennis.jpg"],
    ["example_images/surfing.jpg"],
]

iface = gr.Interface(
    fn=classify_sports,
    inputs=gr.Image(type="filepath"),
    outputs=gr.JSON(),
    title="Sports Action Classification - 3 Model Comparison",
    description=(
        "Upload a sports image to compare predictions from:\n"
        "1. A fine-tuned ViT model\n"
        "2. CLIP zero-shot classification\n"
        "3. OpenAI GPT-4o-mini vision"
    ),
    examples=example_images,
)

iface.launch()
