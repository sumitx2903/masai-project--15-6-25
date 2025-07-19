import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("static", exist_ok=True)

# Load core dataset
df_scores = pd.read_csv("StudentsPerformance.csv")
df_scores['total_score'] = df_scores[['math score','reading score','writing score']].sum(axis=1)

# Optional: Load alcohol dataset if available
try:
    df_alc = pd.read_csv("student-mat.csv", sep=';')
    df_alc = df_alc[['studytime','G1','G2','G3']]
    df_alc.rename(columns={'G3':'final_grade'}, inplace=True)
    # Combine a sample (first 1000) with main
    df = df_scores.head(len(df_alc)).copy()
    df['studytime'] = df_alc['studytime']
    df['final_grade'] = df_alc['final_grade']
except FileNotFoundError:
    df = df_scores.copy()
    df['studytime'] = np.nan
    print("student-mat.csv not found; skipping alcohol data")

# Histograms: math, reading, writing, total
scores = ['math score','reading score','writing score','total_score']
for subj in scores:
    fig = px.histogram(df, x=subj, nbins=30, title=f"{subj.replace('_',' ').title()} Distribution")
    fig.write_image(f"static/{subj.replace(' ','_')}_histogram.png")

# Bar plot: gender - average scores
avg_gender = df.groupby('gender')[['math score','reading score','writing score']].mean().reset_index()
fig = px.bar(avg_gender,x='gender',y=['math score','reading score','writing score'], barmode='group',
             title="Average Scores by Gender")
fig.write_image("static/avg_scores_by_gender.png")

# Line chart: study time vs average subject scores
if 'studytime' in df.columns and df['studytime'].notna().all():
    study_avg = df.groupby('studytime')[['math score','reading score','writing score']].mean().reset_index()
    fig = px.line(study_avg, x='studytime', y=['math score','reading score','writing score'],
                  markers=True, title="Grades vs Study Time")
    fig.write_image("static/grades_vs_studytime.png")
else:
    print("Skipping Study Time chart—no studytime column")

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/correlation_heatmap.png")
plt.close()

# Combined gender comparison histogram
m_df = df[df['gender']=='male'][scores]
f_df = df[df['gender']=='female'][scores]
combined = pd.concat([m_df.mean().rename('Male'), f_df.mean().rename('Female')], axis=1).reset_index()
fig = px.bar(combined, x='index', y=['Male','Female'], barmode='group',
             title="Male vs Female Mean Scores")
fig.write_image("static/male_female_comparison.png")
