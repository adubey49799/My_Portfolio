# Project 4: Next-Word Prediction Using Word Embeddings and a Neural Language Model

## Overview

This project implements a neural language model that predicts the next word in a sequence using Word2Vec embeddings and a feedforward neural network built with PyTorch.

The project demonstrates the complete natural language processing pipeline, including:

- Dataset collection
- Text cleaning
- Lowercase conversion
- Punctuation removal
- Tokenization
- Vocabulary construction
- Training-sequence generation
- Word2Vec embedding generation
- Neural-network training
- Model validation
- Next-word prediction

## Dataset

The project uses Jane Austen's *Emma* from the NLTK Gutenberg corpus.

After preprocessing:

- Total tokens: 161,980
- Original unique tokens: 7,103
- Final vocabulary size: 4,348
- Context length: 3 words
- Context-target pairs: 161,977

Rare words occurring only once were represented using the `<UNK>` token.

## Word Embeddings

Word embeddings were generated using Gensim Word2Vec with the Skip-gram method.

Key parameters:

- Embedding dimension: 100
- Context window: 5
- Architecture: Skip-gram
- Training epochs: 10

The resulting embedding matrix had the shape:

```text
(4348, 100)