
# NAVTTC AI/ML - Week 5
# Task 52: Logistic Regression (Binary Classification)

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Example dataset: Study hours and pass/fail result
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

print("Actual Results:", y_test)
print("Predicted Results:", predictions)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Predict result for a student who studies 6 hours
new_prediction = model.predict(np.array([[6]]))
print("Prediction for 6 study hours:", new_prediction[0])

if new_prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
