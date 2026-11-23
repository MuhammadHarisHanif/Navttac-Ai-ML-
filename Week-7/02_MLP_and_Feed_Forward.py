
# Muhammad Haris Assignment
# Tasks 57 and 58: MLP and Feed Forward Neural Network

# Import required libraries
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Generate sample dataset
X, y = make_moons(n_samples=500, noise=0.2, random_state=42)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create Feed Forward Neural Network
# MLPClassifier uses fully connected feed-forward layers
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# Train the neural network
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print("Feed Forward Neural Network Results")
print("-----------------------------------")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nNetwork Architecture:")
print("Input Layer: 2 neurons")
print("Hidden Layer 1: 16 neurons")
print("Hidden Layer 2: 8 neurons")
print("Output Layer: 2 classes")
