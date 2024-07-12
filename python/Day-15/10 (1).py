# use scikit learn to perform hyperparameter tuning using grid search on a dataset

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Estimator:", grid.best_estimator_)

y_pred = grid.predict(X_test)

target_names = [str(i) for i in iris.target_names]
print("Accuracy:", grid.score(X_test, y_test))
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))
