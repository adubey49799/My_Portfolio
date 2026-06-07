# Project 3: Exploring Neural Networks with Keras

## Course
Fundamentals of AI Enabled Systems

## Project Objective
This project explores Artificial Neural Networks using Keras with TensorFlow backend. The goal is to understand how neural networks are built, trained, evaluated, and interpreted for a classification problem.

## Dataset
The project uses the Fashion MNIST dataset included with Keras. The dataset contains grayscale images of clothing items across 10 categories.

- Training images: 60,000
- Test images: 10,000
- Image size: 28 x 28 pixels
- Classes: 10 clothing categories

A validation set of 5,000 images was separated from the training data. The final split used in the notebook was:

- Training set: 55,000 images
- Validation set: 5,000 images
- Test set: 10,000 images

## Model Architecture
The neural network was built using Keras Sequential API.

Architecture:

- Input layer: 28 x 28 image
- Flatten layer: converts image to 784 input values
- Dense hidden layer: 300 neurons, ReLU activation
- Dense hidden layer: 100 neurons, ReLU activation
- Output layer: 10 neurons, Softmax activation

Total trainable parameters: 266,610

## Training Configuration
The model was compiled using:

- Loss function: sparse categorical crossentropy
- Optimizer: stochastic gradient descent
- Metric: accuracy
- Epochs: 30

## Results
Final model performance:

- Training accuracy: 91.91%
- Validation accuracy: 88.88%
- Test accuracy: 88.44%
- Test loss: 0.3308

The model performed strongly on categories such as Trouser, Bag, Sandal, Sneaker, and Ankle boot. It had more difficulty with visually similar classes such as Shirt, Pullover, Coat, and T-shirt/top.

## Files
- `notebooks/Project_3_Exploring_Neural_Networks_with_Keras.ipynb`: Main project notebook
- `outputs/`: Output files if generated
- `screenshots/`: Screenshots for assignment submission
- `reports/`: Final project report

## Reference
Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*.
Chapter 10: Introduction to Artificial Neural Networks with Keras.