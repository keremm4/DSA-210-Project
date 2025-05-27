
# 📊 Screen Time vs Productivity

This project explores the relationship between screen time and productivity using a self-collected dataset. The hypothesis under investigation is:

> **"Increased screen time reduces productivity."**

The analysis distinguishes between productive and non-productive screen time, recognizing that while excessive screen use (especially for entertainment) may decrease productivity, digital tools are also essential for academic and professional work.

---

## 📁 Dataset Summary

- **Date Range:** March 11, 2025 – April 25, 2025
- **Data Columns:**
  - `Date`: Date of entry
  - `Total_Screen_Time`: Total daily screen time (in hours)
  - `Productive_Screen_Time`: Time spent on academic or work-related tasks
  - `Non_Productive_Screen_Time`: Time spent on entertainment, social media, etc.
  - `Productivity_Score`: Self-assessed score from 0–10

---

## 🔍 Exploratory Data Analysis (EDA)

### 📌 1. Distribution of Productivity Scores
- Most scores cluster between **5 and 8**.
- Very few days scored below 4 or above 9.
- Indicates a consistent productivity level across most days.

### 📌 2. Pairplot
- Shows relationships between screen time and productivity.
- Some patterns suggest inverse relationships between non-productive screen time and productivity.

### 📌 3. Correlation Matrix
- **Negative correlation** between `Non_Productive_Screen_Time` and `Productivity_Score`.
- **Positive correlation** between `Productive_Screen_Time` and `Productivity_Score`.
- Weak overall correlation with total screen time due to mixed activity types.

### 📌 4. Time Series Trends
- Weekday trends show spikes in productivity and screen use.
- Weekends often have higher entertainment screen time and lower productivity.

---

## 📈 Hypothesis Testing

A **Pearson correlation test** was performed between `Total_Screen_Time` and `Productivity_Score`:

- If the **p-value < 0.05**, screen time likely impacts productivity.
- If the **p-value ≥ 0.05**, no statistically significant relationship is confirmed.

---

## 💾 How to Use

1. Run the Jupyter Notebook (`Screen_Time_Analysis.ipynb`) on Google Colab.
2. Upload `custom_screen_time_data.csv`.
3. Run each cell to visualize the analysis and results.

---

## ✅ Outcome

- This project presents a balanced discussion on how screen time can both help and hinder productivity.
- It offers a basis for individuals to evaluate and manage their own digital habits effectively.
