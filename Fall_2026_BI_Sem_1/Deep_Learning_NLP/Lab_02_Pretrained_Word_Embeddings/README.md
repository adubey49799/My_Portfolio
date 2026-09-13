# Lab 2: Pre-Trained Word Embeddings

## Course
Deep Learning and Natural Language Processing  
PhDAI-831-A01  
University of the Cumberlands

## Overview
This lab implements a text classification model using a feed-forward neural network and pre-trained GloVe word embeddings on the AG News Topic Classification dataset.

The implementation includes:

- Loading and preprocessing the AG News dataset
- Tokenizing text using NLTK
- Loading pre-trained GloVe word embeddings
- Measuring vocabulary coverage
- Converting text into padded token sequences
- Building a two-layer feed-forward neural network in PyTorch
- Training and validating the model
- Evaluating performance on the test dataset

## Dataset
AG News Topic Classification Dataset

Classes:

1. World
2. Sports
3. Business
4. Sci/Tech

## Main Technologies
- Python
- PyTorch
- NumPy
- Pandas
- NLTK
- tqdm
- GloVe pre-trained word embeddings

## Files
- `Lab02_Pretrained_Word_Embeddings.ipynb` – main lab implementation
- `data/` – AG News dataset files
- `embeddings/` – pre-trained GloVe files

Large datasets and embedding files are excluded from Git.