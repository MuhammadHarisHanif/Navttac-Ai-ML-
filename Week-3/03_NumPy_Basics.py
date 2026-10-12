

# NAVTTC AI/ML - Week 3
# NumPy Basics - Tasks 28 to 40

import numpy as np

# Task 28: Create arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array =", arr)

# Create arrays using built-in methods
zeros = np.zeros(3)
ones = np.ones(3)
sequence = np.arange(1, 6)

print("Zeros =", zeros)
print("Ones =", ones)
print("Sequence =", sequence)

# Task 29: Array indexing
print("First Element =", arr[0])
print("Last Element =", arr[-1])

# Task 30: Array slicing
print("First Three Elements =", arr[:3])
print("Elements from Index 2 =", arr[2:])

# Task 31: Data types
float_arr = np.array([1.5, 2.5, 3.5])
print("Data Type =", float_arr.dtype)

integer_arr = float_arr.astype(int)
print("Converted Array =", integer_arr)

# Task 32: Copy and view
original = np.array([1, 2, 3])
copied = original.copy()
viewed = original.view()

original[0] = 100

print("Original =", original)
print("Copy =", copied)
print("View =", viewed)

# Task 33: Array shape and attributes
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape =", matrix.shape)
print("Size =", matrix.size)
print("Dimensions =", matrix.ndim)
print("Maximum =", matrix.max())
print("Minimum =", matrix.min())
print("Index of Maximum =", matrix.argmax())
print("Index of Minimum =", matrix.argmin())

# Task 34: Reshape array
arr2 = np.arange(1, 7)
reshaped = arr2.reshape(2, 3)

print("Reshaped Array =")
print(reshaped)

# Task 35: Iterate through array
for value in arr:
    print("Value =", value)

# Task 36: Join arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

joined = np.concatenate((a, b))
print("Joined Array =", joined)

# Task 37: Split arrays
split_arrays = np.array_split(joined, 2)
print("Split Arrays =", split_arrays)

# Task 38: Search array
search_result = np.where(joined == 4)
print("Position of 4 =", search_result)

# Task 39: Sort array
unsorted = np.array([30, 10, 50, 20, 40])
print("Sorted Array =", np.sort(unsorted))

# Task 40: Random values
random_values = np.random.randint(1, 100, size=5)
print("Random Values =", random_values)
