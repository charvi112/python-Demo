# evaluate the performance of the model using accuracy score

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.metrics import accuracy_score

def train_logistic_regression_model(features, target):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train the model
model, X_test, y_test = train_logistic_regression_model(X, y)

# Print the coefficients
print("Coefficients:", model.coef_)

# Print the intercept
print("Intercept:", model.intercept_)

# Make predictions
predictions = model.predict(X_test)

# Print the predictions
print("Predictions:", predictions)

# Calculate the accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
