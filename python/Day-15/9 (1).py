# using scikit learn train the svm classifier on a dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('D:\course\Day_15_Practice_question\students.csv')

# Separate features and target
features = data.drop(['student_id', 'grade'], axis=1)
target = data['grade']

# Encode the target variable
label_encoder = LabelEncoder()
target = label_encoder.fit_transform(target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the SVM classifier
clf = SVC(kernel='linear', random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, labels=[0, 1, 2, 3], target_names=label_encoder.classes_))

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1, 2, 3]))
