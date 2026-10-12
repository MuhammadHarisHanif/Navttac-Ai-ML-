

# NAVTTC AI/ML - Week 3
# NumPy Operations Practice

import numpy as np

# Example 1: Array arithmetic
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Exponentiation =", a ** 2)

# Example 2: Broadcasting
arr = np.array([10, 20, 30])
result = arr + 5
print("Broadcasting Result =", result)

# Example 3: Universal functions
numbers = np.array([1, 4, 9, 16])

print("Square Roots =", np.sqrt(numbers))
print("Exponential =", np.exp(numbers))
print("Absolute Values =", np.abs([-2, -5, 3]))

# Example 4: Append elements
arr = np.array([1, 2, 3])
appended = np.append(arr, 4)
print("After Append =", appended)

# Example 5: Insert an element
inserted = np.insert(arr, 1, 10)
print("After Insert =", inserted)

# Example 6: Delete an element
deleted = np.delete(arr, 1)
print("After Delete =", deleted)

# Example 7: Two-dimensional array indexing
matrix = np.array([[10, 20], [30, 40]])

print("Element at Row 1, Column 2 =", matrix[0, 1])

# Example 8: Logical selection
numbers = np.array([10, 15, 20, 25, 30])
filtered = numbers[numbers > 20]
print("Values Greater Than 20 =", filtered)

# Example 9: Save and load array data
np.save("numbers.npy", numbers)
loaded = np.load("numbers.npy")
print("Loaded Array =", loaded)

# Example 10: Check array dimensions
print("Shape =", matrix.shape)
print("Number of Dimensions =", matrix.ndim)
