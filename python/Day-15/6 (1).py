# using scikit lean perform k fold cross validation on a dataset

import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('D:\course\Day_15_Practice_question\customers.csv')

features = data.drop(['customer_id', 'churn'], axis=1)
features = pd.get_dummies(features, drop_first=True)
target = data['churn']

clf = DecisionTreeClassifier(random_state=42)

k_fold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(clf, features, target, cv=k_fold, scoring='accuracy')

print("Cross-validation scores:", scores)

print("Average accuracy:", scores.mean())
