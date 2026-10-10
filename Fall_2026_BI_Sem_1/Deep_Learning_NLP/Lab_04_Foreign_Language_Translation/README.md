# Lab 4: Foreign Language Translation

## English-to-Romanian Machine Translation Using a Pre-trained Transformer

This lab demonstrates machine translation from English to Romanian using a pre-trained sequence-to-sequence Transformer model from Hugging Face.

## Objectives

The lab covers:

- Importing and initializing PyTorch, NumPy, Transformers, Datasets, and evaluation libraries
- Loading a pre-trained English-to-Romanian translation model
- Loading an English-Romanian dataset from Hugging Face
- Implementing a reusable translation function
- Applying the translation model to test data
- Evaluating translation quality using SacreBLEU
- Analyzing both quantitative and qualitative translation results

## Model

The pre-trained model used is:

`Helsinki-NLP/opus-mt-en-ro`

This model translates English text into Romanian.

## Dataset

The dataset used is:

`Helsinki-NLP/opus-100`

Configuration:

`en-ro`

Dataset sizes:

- Train: 1,000,000 examples
- Validation: 2,000 examples
- Test: 2,000 examples

For evaluation, 100 examples from the test split were selected.

## Translation Workflow

The translation pipeline follows these steps:

1. Input English sentence
2. Tokenize the sentence
3. Convert tokens to PyTorch tensors
4. Pass inputs to the pre-trained Transformer model
5. Generate Romanian token IDs
6. Decode the generated tokens into readable Romanian text

## Evaluation

Translation quality was evaluated using the SacreBLEU metric.

### Result

**BLEU Score: 32.75**

The score indicates a moderate level of similarity between the model-generated translations and the human reference translations.

BLEU should not be interpreted as a direct accuracy percentage. Valid translations may use wording that differs from the reference while preserving the same meaning.

## Example

**English**

`She wants to help Olivia.`

**Reference Romanian**

`Vrea s-o ajute pe Olivia.`

**Model Prediction**

`Vrea s-o ajute pe Olivia.`

## Technologies Used

- Python
- PyTorch
- NumPy
- Hugging Face Transformers
- Hugging Face Datasets
- Hugging Face Evaluate
- SacreBLEU
- Jupyter Notebook

## Files

- `Lab04_English_to_Romanian_Translation.ipynb`
- `README.md`