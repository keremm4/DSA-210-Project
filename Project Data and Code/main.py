# main.py - Screen Time and Productivity Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load your collected data
file_path = "screen_time_data.csv"
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])

# --- Initial Data Check ---
print("\n📋 Dataset Preview:")
print(df.head())
print("\n📊 Summary Statistics:")
print(df.describe())

# --- Univariate Analysis ---
plt.figure(figsize=(10, 5))
sns.histplot(df['Productivity_Score'], kde=True, bins=10, color='skyblue')
plt.title('Distribution of Productivity Scores')
plt.xlabel('Score (0–10)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# --- Bivariate Analysis ---
sns.pairplot(df[['Total_Screen_Time', 'Productive_Screen_Time', 'Non_Productive_Screen_Time', 'Productivity_Score']])
plt.suptitle('Pairplot of Variables', y=1.02)
plt.show()

# --- Correlation Heatmap ---
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# --- Time Series Trends ---
df.set_index('Date')[['Productive_Screen_Time', 'Non_Productive_Screen_Time']].plot(figsize=(12, 6))
plt.title('Screen Time Over Time')
plt.ylabel('Hours')
plt.grid(True)
plt.show()

# --- Hypothesis Testing ---
print("\n🔍 Hypothesis Test:")
correlation, p_value = stats.pearsonr(df['Total_Screen_Time'], df['Productivity_Score'])
print(f"Pearson Correlation Coefficient: {correlation:.2f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: Reject the null hypothesis. Screen time is likely affecting productivity.")
else:
    print("Conclusion: Fail to reject the null hypothesis. No significant relationship detected.")

# --- Save Processed Data ---
df.to_csv("processed_screen_time_data.csv", index=False)
print("\n✅ Analysis complete. Processed data saved as 'processed_screen_time_data.csv'")
