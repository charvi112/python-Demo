# csv file has data about student score features and grade targets and split the data into training and testing

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('D:\course\Day_15_Practice_question\students.csv')

features = data.drop(['student_id', 'grade'], axis=1)
target = data['grade']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

print(f"Training features shape: {X_train.shape}")
print(f"Test features shape: {X_test.shape}")
print(f"Training target shape: {y_train.shape}")
print(f"Test target shape: {y_test.shape}")
