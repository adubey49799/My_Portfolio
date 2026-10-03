# Lab 3: Part-of-Speech Tagger Using Transformer Networks

## Overview

This lab implements a Spanish part-of-speech (POS) tagger using a pretrained multilingual Transformer model.

The Spanish AnCora Universal Dependencies dataset is used for training, validation, and testing. The implementation uses Hugging Face Transformers and fine-tunes `distilbert-base-multilingual-cased` for token classification.

## Dataset

Spanish AnCora Universal Dependencies:

- Training sentences: 14,287
- Validation sentences: 1,654
- Test sentences: 1,721
- POS categories: 16

## Model

Pretrained model:

`distilbert/distilbert-base-multilingual-cased`

The model was adapted for token classification with 16 POS output labels.

## Tokenization and Label Alignment

The DistilBERT tokenizer may split individual words into multiple subword tokens.

POS labels are assigned only to the first token corresponding to each original word. Additional subword tokens and special tokens are assigned `-100` so that they are ignored during loss calculation.

## Training Configuration

- Epochs: 1
- Learning rate: 2e-5
- Training batch size: 8
- Evaluation batch size: 8
- Weight decay: 0.01
- Hardware: CPU

## Validation Results

- Validation Loss: 0.051593
- Accuracy: 98.66%
- Precision: 98.65%
- Recall: 98.66%
- F1 Score: 98.65%

## Test Results

- Test Loss: 0.053345
- Accuracy: 98.59%
- Precision: 98.59%
- Recall: 98.59%
- F1 Score: 98.58%

## Conclusion

The fine-tuned multilingual DistilBERT model achieved strong performance on Spanish POS tagging. The close validation and test results indicate that the model generalized effectively to unseen sentences.

## Files

- `Lab03_POS_Tagger_Transformers.ipynb` – Complete implementation, training, evaluation, and analysis
- `README.md` – Project summary and results