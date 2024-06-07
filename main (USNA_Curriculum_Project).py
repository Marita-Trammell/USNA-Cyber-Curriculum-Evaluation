import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset, treat 'Unnamed' columns as NaN
data = pd.read_csv('USNA Curriculum Data.csv', na_values='Unnamed')

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Display basic information about the dataset
print("Dataset Information:")
print("\nFirst 5 Rows of the Dataset:")
print(data.iloc[:, :12].head())  # Show only the first 12 columns

# Add this line to display plots inline in Jupyter Notebook
%matplotlib inline

# Data Cleaning
# Remove columns with no header
data = data.dropna(axis=1, how='all')

# Remove rows with all NaN values
data = data.dropna(axis=0, how='all')

# Convert percentage columns from strings to float
percentage_cols = ['Average', 'Maximum', 'Q3', 'Median', 'Mode', 'Q1', 'Minimum']
data[percentage_cols] = data[percentage_cols].replace('%', '', regex=True).astype(float) / 100.0

# Fill NaN values in 'Type' column with a default color
default_color = 'gray'  # You can choose any color you prefer for NaN values
data['Type'] = data['Type'].fillna(default_color)

# Convert 'Type' column to categorical codes
data['Type'] = pd.Categorical(data['Type'])
data['Type'] = data['Type'].cat.codes

# Display cleaned dataset information
print("\nFirst 5 Rows of the Cleaned Dataset:")
print(data.iloc[:, :12].head())  # Show only the first 12 columns

# Data Exploration
# Statistical summary
print("\nStatistical Summary:")
# Select columns for statistical summary (excluding 'Question Number' and 'Value')
stat_summary_cols = [col for col in data.columns if col not in ['Question Number', 'Value']]
print(data[stat_summary_cols].describe().drop('count'))

# Data Visualization
# CLO Type by Average
plt.figure(figsize=(10, 6))
data.boxplot(column='Average', by='Type', figsize=(10, 6))
plt.title("Average Scores by CLO Type")
plt.xlabel("CLO Type")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# CLO Subject by Average
plt.figure(figsize=(10, 6))
data.groupby('Subject')['Average'].mean().plot(kind='bar')
plt.title("Average Scores by CLO Subject")
plt.xlabel("CLO Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Question by Average
plt.figure(figsize=(12, 8))
plt.scatter(data['Question Number'], data['Average'], s=100, c=data['Type'], cmap='viridis')
plt.title("Average Scores by Question")
plt.xlabel("Question Number")
plt.ylabel("Average Score")
plt.show()

# Boxplot of Average Scores by CLO (Course Learning Outcome)
plt.figure(figsize=(12, 8))
data.boxplot(column='Average', by='CLO', figsize=(12, 8))
plt.title("Average Scores by Course Learning Outcome (CLO)")
plt.xlabel("CLO")
plt.ylabel("Average Score")
plt.show()

# Scatter plot of Value vs Average Score colored by Type
plt.figure(figsize=(12, 8))
plt.scatter(data['Value'], data['Average'], c=data['Type'], cmap='viridis', s=100, alpha=0.5)
plt.title("Value vs Average Score by Question Type")
plt.xlabel("Value")
plt.ylabel("Average Score")
plt.colorbar(label='Type')
plt.show()

# Correlation matrix
plt.figure(figsize=(12, 8))
corr = data.corr(numeric_only=True)
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix")
plt.show()

# Insights
# Average score comparison between 6-Week and 12-Week Topics
avg_score_by_subject = data.groupby('Subject')['Average'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_score_by_subject['Subject'], avg_score_by_subject['Average'])
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
print("4. Recommend focusing on improving student performance in low-performing question types")

