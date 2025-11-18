import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: LOAD DATA ---
try:
    df = pd.read_csv('/Users/labdhishah/Downloads/Project Files /Strava Fitness/Project Files/Strava Fitness /Bellabeat_Final_Merged.csv')
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print("❌ Error: File not found.")
    exit()

# Fix Date format
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfWeek'] = df['Date'].dt.day_name()

# --- STEP 2: STATISTICS (Display in Terminal) ---
print("\n--- KEY SUMMARY STATISTICS ---")
stats = df[['TotalSteps', 'TotalDistance', 'SedentaryMinutes', 'Calories', 'TotalMinutesAsleep']].describe()
print(stats)

# --- STEP 3: GENERATE & SAVE CHARTS ---

# Chart 1: Correlation Heatmap
plt.figure(figsize=(10, 8))
cols = ['TotalSteps', 'TotalDistance', 'SedentaryMinutes', 'Calories', 'TotalMinutesAsleep']
sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('1_Correlation_Heatmap.png') # <--- SAVES IMAGE
print("\n📸 Saved: 1_Correlation_Heatmap.png")
plt.close() # Closes the plot so the script continues

# Chart 2: Scatter Plot (Steps vs Calories)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TotalSteps', y='Calories', alpha=0.6, color='orange')
sns.regplot(data=df, x='TotalSteps', y='Calories', scatter=False, color='blue')
plt.title('Steps vs. Calories')
plt.savefig('2_Steps_vs_Calories.png') # <--- SAVES IMAGE
print("📸 Saved: 2_Steps_vs_Calories.png")
plt.close()

# Chart 3: Weekly Steps Bar Chart
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['DayOfWeek'] = pd.Categorical(df['DayOfWeek'], categories=ordered_days, ordered=True)
weekly_stats = df.groupby('DayOfWeek', observed=False)['TotalSteps'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=weekly_stats, x='DayOfWeek', y='TotalSteps', palette='Blues_d')
plt.title('Average Steps by Day')
plt.savefig('3_Weekly_Steps.png') # <--- SAVES IMAGE
print("📸 Saved: 3_Weekly_Steps.png")
plt.close()

print("\n✅ ALL DONE! Check your folder for the 3 PNG images.")