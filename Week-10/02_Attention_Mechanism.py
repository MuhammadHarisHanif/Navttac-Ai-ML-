
# Muhammad Haris Assignment
# Week 10: Attention Mechanism Demonstration

# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Create sample sequential data
X = np.random.random((200, 5, 10)).astype("float32")
y = np.random.randint(0, 2, size=(200, 1))

# Define a simple attention layer
class AttentionLayer(layers.Layer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, input_shape):
        self.attention_weights = self.add_weight(
            name="attention_weights",
            shape=(input_shape[-1], 1),
            initializer="glorot_uniform",
            trainable=True
        )

        super().build(input_shape)

    def call(self, inputs):
        # Calculate attention scores
        scores = tf.matmul(inputs, self.attention_weights)

        # Normalize scores
        attention_scores = tf.nn.softmax(scores, axis=1)

        # Calculate context vector
        context_vector = tf.reduce_sum(
            inputs * attention_scores,
            axis=1
        )

        return context_vector


# Build neural network with attention
inputs = layers.Input(shape=(5, 10))

# Process sequential data
lstm_output = layers.LSTM(
    32,
    return_sequences=True
)(inputs)

# Apply attention mechanism
attention_output = AttentionLayer()(lstm_output)

# Classification output
output = layers.Dense(
    1,
    activation="sigmoid"
)(attention_output)

# Create model
model = models.Model(
    inputs=inputs,
    outputs=output
)

# Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Display model architecture
model.summary()

# Train model
model.fit(
    X,
    y,
    epochs=10,
    batch_size=16,
    validation_split=0.2
)

# Make prediction
sample = X[:1]

prediction = model.predict(sample)

print("\nAttention Mechanism Results")
print("---------------------------")
print("Predicted Probability:", prediction[0][0])

# Display attention weights
attention_model = models.Model(
    inputs=model.input,
    outputs=model.get_layer(index=2).output
)

print("\nAttention mechanism successfully implemented.")
