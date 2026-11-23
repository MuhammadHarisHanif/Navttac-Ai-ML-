
# Muhammad Haris Assignment
# Task 59: Neural Network Loss Functions

# Import required libraries
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import log_loss

# Actual values
y_true = np.array([1, 0, 1, 1, 0])

# Predicted probabilities
y_pred = np.array([0.9, 0.2, 0.8, 0.7, 0.1])

# Convert probabilities into binary predictions
y_pred_class = (y_pred >= 0.5).astype(int)

# Calculate Mean Squared Error
mse = mean_squared_error(y_true, y_pred)

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)

# Calculate Binary Cross-Entropy
binary_cross_entropy = log_loss(y_true, y_pred)

# Display results
print("Neural Network Loss Functions")
print("-----------------------------")

print("Actual Values:", y_true)
print("Predicted Probabilities:", y_pred)

print("\nMean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("Binary Cross-Entropy:", binary_cross_entropy)

print("\nPredicted Classes:", y_pred_class)
