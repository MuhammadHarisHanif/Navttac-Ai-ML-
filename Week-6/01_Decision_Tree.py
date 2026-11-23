# Muhammad Haris Assignement.
# NAVTTC AI/ML - Week 06
# Task 53: Decision Tree Classification

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the Iris dataset
iris = load_iris()

# Separate input features and target labels
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Display actual and predicted values
print("Actual Classes:")
print(y_test)

print("\nPredicted Classes:")
print(predictions)

# Evaluate model performance
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

# Predict the class of a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_prediction = model.predict(new_flower)

print("\nNew Flower Prediction:")
print(iris.target_names[new_prediction[0]])

