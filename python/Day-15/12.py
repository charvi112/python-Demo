# csv file has an housing prices features and their target lables split the data into training and testing

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('D:\course\Day_15_Practice_question\housing.csv')

label_encoder = LabelEncoder()
df['Location'] = label_encoder.fit_transform(df['Location'])

X = df.drop('PriceCategory', axis=1)
y = df['PriceCategory']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
