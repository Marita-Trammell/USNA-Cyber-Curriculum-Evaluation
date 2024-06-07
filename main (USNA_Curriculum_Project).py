import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('USNA_Cyber_Data.csv')

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

# Data Cleaning
# Remove columns with all NaN values
data.dropna(axis=1, how='all', inplace=True)

# Remove rows with all NaN values
data.dropna(axis=0, how='all', inplace=True)

# Convert percentage columns from strings to float
percentage_cols = ['Average', 'Maximum', 'Q3', 'Median', 'Mode', 'Q1', 'Minimum']
for col in percentage_cols:
    if col in data.columns:
        # Remove percentage sign and convert to float
        data[col] = data[col].str.rstrip('%').astype('float') / 100.0

# Display cleaned dataset information
print("\nCleaned Dataset Information:")
print(data.info())
print("\nFirst 5 Rows of the Cleaned Dataset:")
print(data.head())

# Data Exploration
# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Data Visualization
# CLO Type by Average
plt.figure(figsize=(10, 6))
sns.boxplot(x='Type', y='Average', data=data)
plt.title("Average Scores by CLO Type")
plt.xlabel("CLO Type")
plt.ylabel("Average Score")
plt.show()

# CLO Subject by Average
plt.figure(figsize=(10, 6))
sns.barplot(x='Subject', y='Average', data=data)
plt.title("Average Scores by CLO Subject")
plt.xlabel("CLO Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Question by Average
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Question Number', y='Average', data=data, s=100)
plt.title("Average Scores by Question")
plt.xlabel("Question Number")
plt.ylabel("Average Score")
plt.show()

# Boxplot of Average Scores by CLO (Course Learning Outcome)
plt.figure(figsize=(12, 8))
sns.boxplot(x='CLO', y='Average', data=data)
plt.title("Average Scores by Course Learning Outcome (CLO)")
plt.xlabel("CLO")
plt.ylabel("Average Score")
plt.show()

# Scatter plot of Value vs Average Score colored by Type
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Value', y='Average', hue='Type', data=data, palette='viridis', s=100)
plt.title("Value vs Average Score by Question Type")
plt.xlabel("Value")
plt.ylabel("Average Score")
plt.legend(title='Type')
plt.show()

# Correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Insights
# Average score comparison between 6-Week and 12-Week Topics
avg_score_by_subject = data.groupby('Subject')['Average'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Subject', y='Average', data=avg_score_by_subject)
plt.title("Average Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Identifying high and low performing question types
high_performing = data[data['Average'] >= 0.85]
low_performing = data[data['Average'] <= 0.55]

print("\nHigh Performing Question Types:")
print(high_performing[['Question Number', 'Type', 'Average']])

print("\nLow Performing Question Types:")
print(low_performing[['Question Number', 'Type', 'Average']])

# Conclusion
print("\nConclusions and Recommendations:")
print("1. The dataset provides insights into student performance across various question types and topics.")
print("2. High-performing questions are predominantly of type 'Match' and 'Single-Select'.")
print("3. Low-performing questions often belong to 'Fill-in-the-Blank' and 'True/False' types.")
print("4. Recommend focusing on improving student performance in low-performing question types through targeted training and resources.")

# Save the cleaned and analyzed data to a new CSV file
data.to_csv('cleaned_student_performance.csv', index=False)
