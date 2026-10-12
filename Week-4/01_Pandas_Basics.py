

# NAVTTC AI/ML - Week 4
# Tasks 41-45: Pandas Basics, Series, DataFrame and CSV Files

# Install Pandas if needed:
# pip install pandas

import pandas as pd

# Task 41: Basic Pandas operations
numbers = [10, 20, 30, 40, 50]
series = pd.Series(numbers)

print("Pandas Series:")
print(series)

# Task 42: Check Pandas version
print("Pandas Version:", pd.__version__)

# Task 43: Create a Series
marks = pd.Series([85, 90, 78, 92], index=["Ali", "Sara", "Ahmed", "Ayesha"])

print("\nStudent Marks:")
print(marks)

print("Marks of Sara:", marks["Sara"])

# Task 44: Create a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

# Display first rows
print("\nFirst Two Rows:")
print(df.head(2))

# Display column names
print("\nColumns:", df.columns.tolist())

# Select one column
print("\nStudent Names:")
print(df["Name"])

# Task 45: Save data to a CSV file
df.to_csv("students.csv", index=False)
print("\nData saved to students.csv")

# Read data from a CSV file
loaded_df = pd.read_csv("students.csv")

print("\nData Read from CSV:")
print(loaded_df)
