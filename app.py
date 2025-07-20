import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("static", exist_ok=True)

# Load core dataset
df = pd.read_csv("StudentsPerformance.csv")
df['total_score'] = df[['math score','reading score','writing score']].sum(axis=1)
df['studytime'] = np.nan  # Optional: add studytime column as NaN for compatibility

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

# Skip study time chart (no studytime data)
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


# Effect of test preparation course on scores with different color bars
prep_course_avg = df.groupby('test preparation course')[['math score','reading score','writing score','total_score']].mean().reset_index()
fig = px.bar(
    prep_course_avg,
    x='test preparation course',
    y=['math score','reading score','writing score','total_score'],
    barmode='group',
    title="Effect of Test Preparation Course on Scores",
    color_discrete_sequence=px.colors.qualitative.Set2  # Use a distinct color palette
)
# Use fig.write_image only if compatible Plotly and Kaleido versions are installed
try:
    fig.write_image("static/effect_of_test_prep_course.png")
except Exception as e:
    print("Image export failed:", e)
    print("Please upgrade Plotly to >=6.1.1 and/or downgrade Kaleido to 0.2.1 for static image export.")