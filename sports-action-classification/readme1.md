# Sports Action Classification

This app compares 3 image classification approaches on sports action images:

- Fine-tuned ViT model [`lnlywlf/sports-vit`](https://huggingface.co/lnlywlf/sports-vit)
- Zero-shot CLIP (`openai/clip-vit-large-patch14`)
- OpenAI vision model (`gpt-4o-mini`)

## Dataset Used For Training

- Hugging Face dataset source: [HES-XPLAIN/SportsImageClassification](https://huggingface.co/datasets/HES-XPLAIN/SportsImageClassification) (subset)
- Loaded with: `load_dataset("imagefolder", data_dir="data/sports")`
- Number of classes: `10`
- Classes: baseball, basketball, boxing, cricket, football, hockey, surfing, swimming, tennis, volleyball
- Total images: ~1,573 (~120-200 per class)
- Split: 80% train (1,258), 10% validation (157), 10% test (158)

## Preprocessing

- Images resized to 224x224 pixels using `AutoImageProcessor` from `google/vit-base-patch16-224`
- All images converted to RGB format
- Pixel values normalized with mean=0.5 and std=0.5 per channel
- No additional data augmentation applied

## Trained Model

- Hugging Face model link: [https://huggingface.co/lnlywlf/sports-vit](https://huggingface.co/lnlywlf/sports-vit)
- Base model: [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224)
- Transfer learning: all base layers frozen, only classifier head trained
- Training: 5 epochs, batch size 16, learning rate 3e-4
- Trainable parameters: 7,690 out of 85,806,346 total

## Training Performance

| Training Loss | Epoch | Validation Loss | Accuracy |
|---:|---:|---:|---:|
| 1.1480 | 1.0 | 0.1741 | 0.9554 |
| 0.1054 | 2.0 | 0.0549 | 0.9873 |
| 0.0387 | 3.0 | 0.0307 | 0.9936 |
| 0.0224 | 4.0 | 0.0182 | 0.9936 |
| 0.0117 | 5.0 | 0.0138 | 0.9936 |

Test set evaluation: **100% accuracy** (eval_loss: 0.0138)

## Links

- Model: [https://huggingface.co/lnlywlf/sports-vit](https://huggingface.co/lnlywlf/sports-vit)
- App: [https://huggingface.co/spaces/lnlywlf/sports-action-classification](https://huggingface.co/spaces/lnlywlf/sports-action-classification)

## Example Image Results

The table below reports the true class and Top-3 predictions for ViT and CLIP, and the OpenAI classification.

| Image | True Class | ViT Top-3 (score) | CLIP Top-3 (score) | OpenAI (label, confidence) |
|---|---|---|---|---|
| `baseball.jpg` | baseball | `baseball` (0.9998)<br>`cricket` (0.0001)<br>`volleyball` (0.0000) | `baseball` (0.9839)<br>`cricket` (0.0103)<br>`volleyball` (0.0019) | `baseball` (0.95) |
| `basketball.jpg` | basketball | `basketball` (0.9997)<br>`volleyball` (0.0001)<br>`boxing` (0.0001) | `basketball` (0.9712)<br>`volleyball` (0.0159)<br>`boxing` (0.0047) | `basketball` (0.95) |
| `boxing.jpg` | boxing | `boxing` (0.9999)<br>`basketball` (0.0000)<br>`hockey` (0.0000) | `boxing` (0.9956)<br>`basketball` (0.0014)<br>`hockey` (0.0012) | `boxing` (0.95) |
| `swimming.jpg` | swimming | `swimming` (0.9998)<br>`surfing` (0.0001)<br>`volleyball` (0.0000) | `swimming` (0.9451)<br>`surfing` (0.0321)<br>`volleyball` (0.0078) | `swimming` (0.95) |
| `tennis.jpg` | tennis | `tennis` (0.9999)<br>`cricket` (0.0001)<br>`baseball` (0.0000) | `tennis` (0.9823)<br>`cricket` (0.0072)<br>`baseball` (0.0041) | `tennis` (0.95) |
| `surfing.jpg` | surfing | `surfing` (0.9997)<br>`swimming` (0.0001)<br>`volleyball` (0.0001) | `surfing` (0.9687)<br>`swimming` (0.0148)<br>`volleyball` (0.0053) | `surfing` (0.95) |
