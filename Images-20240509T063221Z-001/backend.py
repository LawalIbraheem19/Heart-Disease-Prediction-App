import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the dataset
heart_data = pd.read_csv("heart.csv")
print(heart_data.head())
# # Check for missing values
# print(heart_data.isnull().sum())

# # Statistical measures about the data
# print(heart_data.describe())

# # Distribution of the target variable
# print(heart_data["target"].value_counts())

# Separate the features and target variable
X = heart_data.drop(columns="target", axis=1)
Y = heart_data["target"]

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Print the first few rows of training and testing data
# print(X_train.head())
# print(X_test.head())
# print(Y_train.head())
# print(Y_test.head())

# Create a pipeline with scaling and logistic regression
pipeline = make_pipeline(
    StandardScaler(), LogisticRegression(max_iter=1000, solver="lbfgs")
)

# Fit the model
pipeline.fit(X_train, Y_train)

# Accuracy on training data
X_train_prediction = pipeline.predict(X_train)
# training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
# print("Accuracy on Training data : ", training_data_accuracy)

# # Ensure X_test is a DataFrame with the same feature names as X_train
# X_test = pd.DataFrame(X_test, columns=X_train.columns)

# # Accuracy on test data
# X_test_prediction = pipeline.predict(X_test)
# test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
# print("Accuracy on Test data : ", test_data_accuracy)

# # Input data for prediction
# input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)

# # Convert input data to a DataFrame with the same column names as the training data
# input_data_as_dataframe = pd.DataFrame([input_data], columns=X_train.columns)

# # Predict using the pipeline
# prediction = pipeline.predict(input_data_as_dataframe)
# print(prediction)

# # Print the prediction result
# if prediction[0] == 0:
#     print("The Person does not have a Heart Disease")
# else:
#     print("The Person has Heart Disease")
