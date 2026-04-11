# Transformer-Based Model Evaluation for Medical Text Classification

## Project Overview
This project evaluates and compares traditional machine learning models and transformer-based models for medical text classification using the Medical Transcriptions dataset. The goal is to determine which model performs best in terms of classification performance, robustness, interpretability, and practical suitability for healthcare-related applications.

## Objective
The objective of this project is to evaluate multiple AI models, including traditional machine learning approaches and transformer-based architectures, for medical text classification and clinical decision support. The models are compared using performance metrics such as accuracy, macro precision, macro recall, and macro F1-score.

## Dataset
The project uses the **Medical Transcriptions** dataset, which contains clinical transcription text labeled by medical specialty.

### Original Dataset Columns
- `description`
- `medical_specialty`
- `sample_name`
- `transcription`
- `keywords`

### Final Modeling Choice
For this project:
- `medical_specialty` was used as the target label
- `transcription` was used as the input text

### Data Cleaning
- removed rows with missing transcription text
- stripped extra spaces from labels and text
- filtered out very rare specialties with fewer than 50 records

### Final Dataset Used
- **4647 records**
- **22 medical specialty classes**

## Models Evaluated

### Traditional Machine Learning Models
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

### Transformer-Based Models
- RoBERTa
- Bio_ClinicalBERT

## Methodology

### 1. Data Preprocessing
- loaded the dataset from CSV
- selected the target and text columns
- removed missing values
- filtered rare classes
- encoded labels using `LabelEncoder`
- split the data into training and testing sets using stratified sampling

### 2. Traditional Machine Learning Pipeline
- converted text into TF-IDF features
- trained and evaluated:
  - Logistic Regression
  - SVM
  - Random Forest

### 3. Transformer Pipeline
- prepared train, validation, and test datasets
- tokenized text using pretrained tokenizers
- trained:
  - RoBERTa
  - Bio_ClinicalBERT
- evaluated transformer models using validation metrics

### 4. Evaluation Metrics
The following metrics were used:
- Accuracy
- Macro Precision
- Macro Recall
- Macro F1-score

Macro F1-score was treated as the most important metric because the dataset is imbalanced across multiple specialty classes.

## Final Results

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|------|---------:|----------------:|-------------:|---------:|
| Logistic Regression | 0.3387 | 0.3397 | 0.5108 | 0.3911 |
| SVM | 0.1656 | 0.1830 | 0.2338 | 0.2023 |
| RoBERTa | 0.3683 | 0.2147 | 0.1698 | 0.1629 |
| Random Forest | 0.1355 | 0.1252 | 0.1346 | 0.1292 |
| Bio_ClinicalBERT | 0.3280 | 0.1139 | 0.1247 | 0.1068 |

## Key Findings
- Logistic Regression achieved the best overall performance based on Macro F1-score.
- SVM performed worse than Logistic Regression but better than the transformer models in this project setup.
- Random Forest was the weakest traditional machine learning model.
- RoBERTa performed better than Bio_ClinicalBERT, but both transformer models underperformed compared with Logistic Regression.
- Transformer performance was likely limited by:
  - CPU-only training
  - shorter training schedules
  - reduced sequence lengths
  - class imbalance

## Conclusion
For this project, **Logistic Regression with TF-IDF features was the best-performing model** for balanced multiclass medical text classification. Although transformer models are more advanced and context-aware, they did not outperform the simpler baseline under the available training conditions.

## Project Structure
```text
Project - Transformer-Based Model Evaluation/
│
├── Transformer_Medical_Text_Evaluation.ipynb
├── README.md
├── requirements.txt
├── data/
│   └── mtsamples.csv
└── figures/