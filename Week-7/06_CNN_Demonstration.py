
# Muhammad Haris Assignment
# Task 63: Demonstration of Convolutional Neural Network (CNN)

# Import required libraries
import tensorflow as tf
from tensorflow.keras import layers, models

# Load MNIST handwritten digit dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize image values
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add channel dimension
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Build CNN model
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),

    # Convolutional layer
    layers.Conv2D(32, (3, 3), activation="relu"),

    # Pooling layer
    layers.MaxPooling2D((2, 2)),

    # Second convolutional layer
    layers.Conv2D(64, (3, 3), activation="relu"),

    # Pooling layer
    layers.MaxPooling2D((2, 2)),

    # Flatten feature maps
    layers.Flatten(),

    # Fully connected layer
    layers.Dense(64, activation="relu"),

    # Output layer for 10 digit classes
    layers.Dense(10, activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Display model architecture
model.summary()

# Train CNN model
model.fit(
    x_train,
    y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.1
)

# Evaluate model
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("\nCNN Demonstration Results")
print("-------------------------")
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)
