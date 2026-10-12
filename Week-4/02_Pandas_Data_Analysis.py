

# NAVTTC AI/ML - Week 4
# Tasks 46-48: Data Analysis, Cleaning and Correlation

import pandas as pd

# Create sample dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Age": [20, 21, 19, None, 23],
    "Marks": [85, 90, 78, 92, None],
    "Attendance": [90, 95, 80, 98, 85]
}

df = pd.DataFrame(data)

# Example 1: Display dataset
print("Original Data:")
print(df)

# Example 2: Basic information
print("\nDataset Information:")
print(df.info())

# Example 3: Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Example 4: Select a column
print("\nStudent Names:")
print(df["Name"])

# Example 5: Select specific columns
print("\nNames and Marks:")
print(df[["Name", "Marks"]])

# Example 6: Filter rows
print("\nStudents with Marks Above 80:")
print(df[df["Marks"] > 80])

# Example 7: Sort data
print("\nSorted by Marks:")
print(df.sort_values("Marks", ascending=False))

# Example 8: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Example 9: Fill missing numeric values with column means
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nData After Filling Missing Values:")
print(df)

# Example 10: Remove duplicate rows
df = df.drop_duplicates()

# Example 11: Apply a custom function
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 50 else "Fail"
)

print("\nStudent Results:")
print(df[["Name", "Marks", "Result"]])

# Example 12: Group data by result
print("\nAverage Marks by Result:")
print(df.groupby("Result")["Marks"].mean())

# Example 13: Correlation
print("\nCorrelation Matrix:")
print(df[["Age", "Marks", "Attendance"]].corr())

# Example 14: Save cleaned data
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned data saved to cleaned_students.csv")
