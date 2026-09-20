# Project 3: Word Embeddings

## Course Information

**Student:** Alok Dubey  
**University:** University of the Cumberlands  
**Course:** Deep Learning and Natural Language Processing (PhDAI-831-A01)  
**Term:** Fall 2026 – First Bi-Term  

## Project Overview

This project explores text representation using Term Frequency-Inverse Document Frequency (TF-IDF) and dimensionality reduction using the mathematical principles of Principal Component Analysis (PCA).

A small corpus of 12 documents from three topic categories—Technology, Sports, and Business—was converted into TF-IDF vectors. The dimensionality of the resulting representation was then reduced manually by computing the feature means, centering the data, constructing the covariance matrix, calculating eigenvalues and eigenvectors, sorting the principal components, and projecting the data into a lower-dimensional space.

The project demonstrates how dimensionality reduction can preserve much of the information contained in a high-dimensional text representation while using fewer numerical features.

## Project Files

- `Project03_Word_Embeddings.ipynb` — Main implementation and analysis notebook.
- `README.md` — Project overview and implementation summary.

## Environment

- Python 3.11.9
- NumPy 1.26.4
- Pandas 2.3.3
- Scikit-learn 1.8.0
- Matplotlib 3.10.8

## Dataset

The project uses a manually defined collection of 12 short text documents:

- 4 Technology documents
- 4 Sports documents
- 4 Business documents

The small corpus allows the intermediate mathematical calculations to remain interpretable while still demonstrating the complete dimensionality-reduction process.

## Methodology

The project follows these major steps:

1. Create a sample text corpus.
2. Convert the documents into TF-IDF vectors.
3. Compute the mean of every TF-IDF feature.
4. Center the TF-IDF data by subtracting the feature means.
5. Compute the covariance matrix.
6. Calculate the eigenvalues and eigenvectors of the covariance matrix.
7. Sort the eigenvalues and corresponding eigenvectors from largest to smallest.
8. Calculate the explained variance of each principal component.
9. Select enough principal components to preserve at least 80% of the total variance.
10. Project the centered TF-IDF vectors into the reduced-dimensional space.
11. Visualize the documents using the first two principal components.

## Key Results

The TF-IDF transformation produced:

- 12 documents
- 60 TF-IDF features

The covariance matrix had dimensions:

- 60 × 60

Because the centered dataset contains 12 observations, it produced 11 meaningful non-zero eigenvalues.

Using an 80% cumulative explained-variance threshold:

- Original dimensions: 60
- Selected principal components: 9
- Variance preserved: 84.62%

The resulting dimensionality reduction was:

`60 features → 9 principal components`

The first two principal components were also used to visualize the document representations in two dimensions.

## Key Concepts Demonstrated

- Term Frequency-Inverse Document Frequency (TF-IDF)
- Mean centering
- Variance
- Covariance
- Covariance matrix
- Eigenvalues
- Eigenvectors
- Principal components
- Explained variance
- Dimensionality reduction
- PCA-based projection

## Validation

The covariance matrix was computed manually using:

`(X_centered.T @ X_centered) / (n - 1)`

The result was verified against NumPy's built-in `np.cov()` implementation and produced a matching result.

The notebook was restarted and executed from beginning to end to verify that all cells run successfully and reproduce the project results.

## AI Use Disclosure

ChatGPT by OpenAI was used as a learning and development aid to support project planning, explanation of TF-IDF and PCA concepts, code review, and improvement of written explanations.

All code was executed by the author. Intermediate and final results were reviewed and verified, including TF-IDF values, mean centering, covariance calculations, eigenvalues, eigenvectors, explained variance, dimensionality reduction, and visualization.

The author remains responsible for the accuracy, originality, and integrity of the submitted work.