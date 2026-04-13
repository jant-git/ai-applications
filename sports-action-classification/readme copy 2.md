# Sports Action Classification

This app compares 3 image classification approaches on sports action images:

- Fine-tuned ViT model [`lnlywlf/sports-vit`](https://huggingface.co/lnlywlf/sports-vit)
- Zero-shot CLIP (`openai/clip-vit-large-patch14`)
- OpenAI vision model (`gpt-4o-mini`)

## Dataset

- Source: [HES-XPLAIN/SportsImageClassification](https://huggingface.co/datasets/HES-XPLAIN/SportsImageClassification) (subset)
- Number of classes: 10
- Classes: baseball, basketball, boxing, cricket, football, hockey, surfing, swimming, tennis, volleyball
- Total images: ~1,573 (varying per class, ~120-200 each)
- Split: 80% train, 10% validation, 10% test

## Preprocessing

- Images resized to 224x224 pixels using `AutoImageProcessor` from `google/vit-base-patch16-224`
- All images converted to RGB format
- Pixel values normalized per ViT processor defaults (mean/std normalization)
- No additional data augmentation applied

## Model and Evaluation

### Fine-tuned ViT

- Base model: [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224)
- Transfer learning: all base layers frozen, only classifier head trained
- Training: 5 epochs, batch size 16, learning rate 3e-4
- Trainable parameters: ~7,690 out of ~86M total

### Training Performance

| Training Loss | Epoch | Validation Loss | Accuracy |
|---:|---:|---:|---:|
| *to be filled after training* | 1 | - | - |
| - | 2 | - | - |
| - | 3 | - | - |
| - | 4 | - | - |
| - | 5 | - | - |

## Links

- Model: [https://huggingface.co/lnlywlf/sports-vit](https://huggingface.co/lnlywlf/sports-vit)
- App: [https://huggingface.co/spaces/lnlywlf/sports-action-classification](https://huggingface.co/spaces/lnlywlf/sports-action-classification)

## Comparison Results

| Image | True Class | ViT Top-3 (score) | CLIP Top-3 (score) | OpenAI (label, confidence) |
|---|---|---|---|---|
| `baseball.jpg` | baseball | *to be filled* | *to be filled* | *to be filled* |
| `basketball.jpg` | basketball | *to be filled* | *to be filled* | *to be filled* |
| `boxing.jpg` | boxing | *to be filled* | *to be filled* | *to be filled* |
| `swimming.jpg` | swimming | *to be filled* | *to be filled* | *to be filled* |
| `tennis.jpg` | tennis | *to be filled* | *to be filled* | *to be filled* |
| `surfing.jpg` | surfing | *to be filled* | *to be filled* | *to be filled* |
