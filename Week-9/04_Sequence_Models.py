
# Muhammad Haris Assignment
# Week 9: Sequence Models

# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Sample sequential dataset
X = np.random.random((100, 5, 1))
y = np.random.random((100, 1))

print("Sequence Model Demonstrations")
print("-----------------------------")

# --------------------------------
# 1. One-to-One Model
# --------------------------------

one_to_one = models.Sequential([
    layers.Input(shape=(1,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(1)
])

one_to_one.compile(
    optimizer="adam",
    loss="mse"
)

print("\n1. One-to-One Architecture")
one_to_one.summary()

# --------------------------------
# 2. One-to-Many Model
# --------------------------------

one_to_many = models.Sequential([
    layers.Input(shape=(1,)),
    layers.Dense(32, activation="relu"),
    layers.RepeatVector(5),
    layers.SimpleRNN(16, return_sequences=True),
    layers.TimeDistributed(layers.Dense(1))
])

one_to_many.compile(
    optimizer="adam",
    loss="mse"
)

print("\n2. One-to-Many Architecture")
one_to_many.summary()

# --------------------------------
# 3. Many-to-One Model
# --------------------------------

many_to_one = models.Sequential([
    layers.Input(shape=(5, 1)),
    layers.SimpleRNN(16),
    layers.Dense(1)
])

many_to_one.compile(
    optimizer="adam",
    loss="mse"
)

print("\n3. Many-to-One Architecture")
many_to_one.summary()

# --------------------------------
# 4. Many-to-Many Model
# --------------------------------

many_to_many = models.Sequential([
    layers.Input(shape=(5, 1)),
    layers.SimpleRNN(16, return_sequences=True),
    layers.TimeDistributed(layers.Dense(1))
])

many_to_many.compile(
    optimizer="adam",
    loss="mse"
)

print("\n4. Many-to-Many Architecture")
many_to_many.summary()

# Demonstrate prediction using Many-to-One
prediction = many_to_one.predict(X[:1])

print("\nSample Many-to-One Prediction:")
print(prediction)
