
# Muhammad Haris Assignment
# Week 8: Recurrent Neural Network (RNN)

# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Create sample sequential data
data = np.array([i for i in range(1, 101)], dtype=float)

# Prepare input sequences and target values
X = []
y = []

for i in range(len(data) - 5):
    X.append(data[i:i + 5])
    y.append(data[i + 5])

X = np.array(X)
y = np.array(y)

# Reshape data for RNN
# Samples, time steps, features
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build RNN model
model = models.Sequential([
    layers.Input(shape=(5, 1)),
    layers.SimpleRNN(32, activation="tanh"),
    layers.Dense(1)
])

# Compile model
model.compile(
    optimizer="adam",
    loss="mse"
)

# Display model architecture
model.summary()

# Train model
model.fit(
    X,
    y,
    epochs=50,
    batch_size=8,
    verbose=1
)

# Predict next value
sample = np.array([96, 97, 98, 99, 100], dtype=float)
sample = sample.reshape((1, 5, 1))

prediction = model.predict(sample)

print("\nRNN Prediction")
print("Input Sequence:", sample.flatten())
print("Predicted Next Value:", prediction[0][0])
