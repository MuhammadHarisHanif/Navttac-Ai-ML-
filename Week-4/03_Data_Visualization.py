

# NAVTTC AI/ML - Week 4
# Data Visualization using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Marks": [85, 90, 78, 92, 75],
    "Attendance": [90, 95, 80, 98, 85],
    "Study_Hours": [3, 5, 2, 6, 2]
}

df = pd.DataFrame(data)

# Example 1: Bar chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Example 2: Line chart
plt.figure()
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Marks Comparison")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Example 3: Histogram
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Example 4: Scatter plot
plt.figure()
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Example 5: Box plot
plt.figure()
sns.boxplot(x=df["Marks"])
plt.title("Marks Distribution")
plt.tight_layout()
plt.show()

# Example 6: Seaborn scatter plot
plt.figure()
sns.scatterplot(data=df, x="Study_Hours", y="Marks")
plt.title("Study Hours and Marks")
plt.tight_layout()
plt.show()

# Example 7: Correlation heatmap
plt.figure()
correlation = df[["Marks", "Attendance", "Study_Hours"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
