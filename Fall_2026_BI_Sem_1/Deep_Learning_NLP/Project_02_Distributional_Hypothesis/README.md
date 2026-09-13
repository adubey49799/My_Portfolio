# Project 2: Distributional Hypothesis

## Course
Deep Learning and Natural Language Processing (PhDAI-831-A01)

## University
University of the Cumberlands

## Project Overview

This project demonstrates the distributional hypothesis, which states that words appearing in similar contexts tend to have similar meanings.

The implementation uses a small sample corpus to:

- Normalize text by converting it to lowercase and removing punctuation.
- Tokenize sentences into individual words.
- Extract words occurring within a specified distance `d` of a target word `x`.
- Count the frequency of surrounding context words.
- Represent the target word as a numeric distributional vector.

## Implementation

The project is implemented in Python using a Jupyter Notebook.

The main steps are:

1. Define the sample sentences.
2. Normalize and tokenize the text.
3. Extract context words within distance `d`.
4. Count context-word frequencies.
5. Construct a distributional vector.
6. Demonstrate the vector representation using the word `dog`.

## Example

For the target word:

`dog`

with a context distance:

`d = 2`

the extracted context vocabulary is:

```text
['chased', 'played', 'the', 'with']