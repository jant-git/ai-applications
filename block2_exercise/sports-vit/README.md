---
library_name: transformers
license: apache-2.0
base_model: google/vit-base-patch16-224
tags:
- image-classification
- sports
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: sports-vit
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: sports-action-classification
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sports-vit

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) on the sports-action-classification dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0138
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.1481        | 1.0   | 79   | 0.0995          | 0.9936   |
| 0.0306        | 2.0   | 158  | 0.0510          | 0.9936   |
| 0.0275        | 3.0   | 237  | 0.0432          | 0.9936   |
| 0.0176        | 4.0   | 316  | 0.0404          | 0.9936   |
| 0.0117        | 5.0   | 395  | 0.0398          | 0.9936   |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.10.0
- Datasets 4.6.1
- Tokenizers 0.22.2
