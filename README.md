
# Student Academic Performance Analysis
*A comprehensive data analysis using Python, SQL, and statistical methods.*

---

**Q: What is the goal of this analysis?**  
A: To identify key demographic and behavioral factors that influence students’ exam scores (Math, Reading, Writing) and suggest actionable improvements in education strategy.

---

## Dataset Summary

**Q: What data are we analyzing?**  
- Source: Kaggle Student Performance Dataset  
- Sample Size: Approximately 1000 records  
- Columns:
  - Demographics: Gender, Race, Parental Education, Lunch
  - Behavioral: Test Preparation Course
  - Scores: Math, Reading, Writing

---

## Step 1: Feature Engineering

**Q: Why did we create new features?**  
A: To enhance comparability and analytical depth:
- `total_score`: Sum of all three exam scores
- `average_score`: Mean of the exam scores
- Categorical encoding for modeling purposes

---

## Step 2: Exploratory Data Analysis

**Q: What performance patterns were identified?**  
- Distribution of average scores (via histogram and KDE)
- Gender-based comparison: Female students slightly outperform male students
- Parental education: Higher education levels correlate with better scores

---

## Step 3: SQL-Based Insights

**Q: What did SQL analysis reveal?**  
- Grade classification using CASE-WHEN statements (A: ≥85, B: 70–84, C: <70)
- Identification of top 3 performers based on total score

---

## Step 4: Statistical Analysis

**Q: Are observed differences statistically valid?**  
- T-test: Statistically significant difference in math scores between genders (p < 0.05)
- Regression: Linear model predicting math score using reading, writing, and demographic features

---

## Step 5: Visualizations

Visual outputs included in the dashboard:
- Histogram: Average Score Distribution
- Bar Chart: Gender vs Average Score
- Box Plot: Parental Education vs Average Score
- SQL Table: Grade Distribution
- Regression Summary Table: Coefficients and R² values

---

## Key Insights and Recommendations

| Insight | Recommendation |
|--------|----------------|
| Test preparation is associated with higher scores | Consider mandatory prep programs |
| Students with free/reduced lunch score lower | Implement support interventions |
| Higher parental education correlates with student performance | Provide educational resources and mentorship |

---

## Business Impact

**Q: How can stakeholders apply these findings?**  
- Strategic investment in prep courses for low-performing students
- Use of data models to identify and support at-risk students
- Development of parent-oriented engagement programs to reinforce learning environments

---

## Conclusion

For further exploration, refer to the full notebook and the interactive dashboard version.
