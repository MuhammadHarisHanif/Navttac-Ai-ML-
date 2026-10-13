
# NAVTTC AI/ML - Week 5
# Task 51: Linear Regression

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Example dataset: Study hours and exam marks
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([35, 40, 50, 55, 60, 65, 70, 80, 85, 95])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

print("Actual Marks:", y_test)
print("Predicted Marks:", predictions)

# Evaluate the model
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Predict marks for a student who studies 6 hours
new_prediction = model.predict(np.array([[6]]))
print("Predicted marks for 6 study hours:", new_prediction[0])
