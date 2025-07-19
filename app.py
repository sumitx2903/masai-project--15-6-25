import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a 'static' folder to save plots
os.makedirs("static", exist_ok=True)

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Total score column
df['total_score'] = df[['math score', 'reading score', 'writing score']].sum(axis=1)

# Plot 1: Total Score Distribution
fig1 = px.histogram(df, x='total_score', nbins=30, title='Total Score Distribution')
fig1.write_image("static/total_score_distribution.png")

# Plot 2: Average Scores by Gender
avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().reset_index()
fig2 = px.bar(avg_scores, x='gender', y=['math score', 'reading score', 'writing score'],
              barmode='group', title='Average Scores by Gender')
fig2.write_image("static/avg_scores_by_gender.png")

# Plot 3: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/correlation_heatmap.png")
plt.close()

print("✅ Dashboard images saved to 'static/' folder.")
