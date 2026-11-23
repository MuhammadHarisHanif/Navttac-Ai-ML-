
# Muhammad Haris Assignment
# NAVTTC AI/ML - Week 6
# Task 55: Time Series Analysis

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create sample monthly sales data
data = {
    "Date": pd.date_range(
        start="2025-01-01",
        periods=12,
        freq="MS"
    ),
    "Sales": [
        120, 135, 128, 150, 160, 155,
        175, 180, 172, 195, 205, 220
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set Date as the index
df.set_index("Date", inplace=True)

# Display the original dataset
print("Monthly Sales Data:")
print(df)

# Display basic statistical information
print("\nStatistical Summary:")
print(df.describe())

# Calculate moving average
df["Moving_Average"] = df["Sales"].rolling(window=3).mean()

print("\nSales with 3-Month Moving Average:")
print(df)

# Calculate monthly percentage change
df["Percentage_Change"] = df["Sales"].pct_change() * 100

print("\nMonthly Sales Percentage Change:")
print(df["Percentage_Change"])

# Plot original sales and moving average
plt.figure(figsize=(10, 5))

plt.plot(
    df.index,
    df["Sales"],
    marker="o",
    label="Monthly Sales"
)

plt.plot(
    df.index,
    df["Moving_Average"],
    marker="o",
    label="3-Month Moving Average"
)

plt.title("Monthly Sales Time Series Analysis")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the graph
plt.show()
