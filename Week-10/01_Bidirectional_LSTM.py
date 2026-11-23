
# Muhammad Haris Assignment
# Week 10: Bidirectional LSTM Demonstration

# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Generate sample sequential data
data = np.array([i for i in range(1, 201)], dtype=float)

# Normalize data
data = data / 200.0

# Prepare sequences
X = []
y = []

for i in range(len(data) - 5):
    X.append(data[i:i + 5])
    y.append(data[i + 5])

X = np.array(X)
y = np.array(y)

# Reshape input data
# Samples, time steps, features
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build Bidirectional LSTM model
model = models.Sequential([
    layers.Input(shape=(5, 1)),

    # Bidirectional LSTM layer
    layers.Bidirectional(
        layers.LSTM(32, activation="tanh")
    ),

    # Output layer
    layers.Dense(1)
])

# Compile model
model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

# Display model architecture
model.summary()

# Train model
model.fit(
    X,
    y,
    epochs=50,
    batch_size=8,
    validation_split=0.2
)

# Prepare sample for prediction
sample = np.array([196, 197, 198, 199, 200], dtype=float)
sample = sample / 200.0
sample = sample.reshape((1, 5, 1))

# Make prediction
prediction = model.predict(sample)

# Convert prediction to original scale
predicted_value = prediction[0][0] * 200

print("\nBidirectional LSTM Results")
print("--------------------------")
print("Input Sequence:", sample.flatten() * 200)
print("Predicted Next Value:", predicted_value)
