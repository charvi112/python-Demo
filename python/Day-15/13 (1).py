# use scikit learn for the naive bayes classifier on a dataset
 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

data = {
    'Feature1': [1.2, 2.3, 0.9, 1.8, 1.0],
    'Feature2': [0.7, 1.8, 0.6, 1.4, 0.9],
    'Label': ['A', 'B', 'A', 'B', 'A']
}

df = pd.DataFrame(data)

X = df[['Feature1', 'Feature2']]
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
