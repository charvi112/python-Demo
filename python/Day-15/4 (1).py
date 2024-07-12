# csv file has customers feature data and their churn status (target) split the data into training and testing

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('D:\course\Day_15_Practice_question\customers.csv')

# Separate features and target
features = data.drop('churn', axis=1)
target = data['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Print the shapes of the resulting splits
print(f"Training features shape: {X_train.shape}")
print(f"Test features shape: {X_test.shape}")
print(f"Training target shape: {y_train.shape}")
print(f"Test target shape: {y_test.shape}")
