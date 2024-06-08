import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset, treat 'Unnamed' columns as NaN
question_data = pd.read_csv('Question_Data.csv', na_values='Unnamed')
instructor_data = pd.read_csv('Instructor_Data.csv', na_values='Unnamed')

# Strip whitespace from column names
question_data.columns = question_data.columns.str.strip()
instructor_data.columns = instructor_data.columns.str.strip()

# Display basic information about the dataset
print("Dataset Information:")
print("\nFirst 5 Rows of the Dataset:")
print(question_data.iloc[:, :12].head())  # Show only the first 12 columns

# Add this line to display plots inline in Jupyter Notebook
%matplotlib inline

# Data Cleaning
def clean_data(data):
    # Remove columns with no header
    data = data.dropna(axis=1, how='all')
    # Remove rows with all NaN values
    data = data.dropna(axis=0, how='all')
    return data

question_data = clean_data(question_data)
instructor_data = clean_data(instructor_data)

# Convert percentage columns from strings to float
percentage_cols = ['Average', 'Maximum', 'Q3', 'Median', 'Mode', 'Q1', 'Minimum']
question_data[percentage_cols] = question_data[percentage_cols].replace('%', '', regex=True).astype(float) / 100.0

# Convert 'Average' to numeric
instructor_data['Average'] = instructor_data['Average'].str.rstrip('%').astype(float) / 100.0

# Round columns to desired decimal places
decimal_places = {'Average': 2, 'Maximum': 2, 'Q3': 2, 'Median': 2, 'Mode': 2, 'Q1': 2, 'Minimum': 2}
question_data = question_data.round(decimal_places)

# Format 'Question Number' column to remove decimal places
question_data['Question Number'] = question_data['Question Number'].astype(int)

# Fill NaN values in 'Type' column with a default color
default_color = 'gray'  # You can choose any color you prefer for NaN values
question_data['Type'] = question_data['Type'].fillna(default_color)

# Convert 'Type' column to categorical codes and create type mapping
question_data['Type'] = pd.Categorical(question_data['Type'])
type_mapping = dict(enumerate(question_data['Type'].cat.categories))  # Mapping of categorical codes to original strings
question_data['Type'] = question_data['Type'].cat.codes

# Display cleaned dataset information
print("\nFirst 5 Rows of the Cleaned Dataset:")
print(question_data.iloc[:, :12].head())  # Show only the first 12 columns

# Data Exploration

# Statistical summary for Question Data
print("\nStatistical Summary for Question Data:")
question_summary_cols = [col for col in question_data.columns if col not in ['Question Number', 'Value']]
question_summary = question_data[question_summary_cols].describe().drop('count').round(2)
print(question_summary)

# Statistical summary for Instructor Data
print("\nStatistical Summary for Instructor Data:")
instructor_summary = instructor_data.describe().drop('count').round(2)
print(instructor_summary)

# Data Visualization

# Box plot of Average Scores by Section ID
plt.figure(figsize=(12, 8))
instructor_data.boxplot(column='Average', by='Section ID')
plt.title("Average Scores by Section ID")
plt.xlabel("Section ID")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Replace categorical codes with original string values for Type column
question_data['Type'] = question_data['Type'].map(type_mapping)

# CLO Type by Average
plt.figure(figsize=(10, 6))
question_data.boxplot(column='Average', by='Type', figsize=(10, 6))
plt.title("Average Scores by Question Type")
plt.xlabel("Question Type")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# CLO Subject by Average
plt.figure(figsize=(10, 6))
question_data.groupby('Subject')['Average'].mean().plot(kind='bar')
plt.title("Average Scores by Question Subject")
plt.xlabel("Question Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Question by Average
plt.figure(figsize=(12, 8))
colors = question_data['Type'].map({'Match': 'blue', 'Fill-in-the-Blank': 'orange',
                                    'Multiple Select': 'green', 'Single-Select': 'red',
                                    'Solve': 'purple', 'True/False': 'brown'})
for question_type, color in zip(question_data['Type'].unique(), colors.unique()):
    plt.scatter(question_data[question_data['Type'] == question_type]['Question Number'],
                question_data[question_data['Type'] == question_type]['Average'],
                s=100, c=color, label=question_type)
plt.title("Question Number vs Average Scores by Question Type")
plt.xlabel("Question Number")
plt.ylabel("Average Score")
plt.legend(title='Question Type')
plt.show()

# Boxplot of Average Scores by CLO (Course Learning Outcome)
plt.figure(figsize=(12, 8))
question_data.boxplot(column='Average', by='CLO', figsize=(12, 8))
plt.title("Average Scores by Course Learning Outcome (CLO)")
plt.xlabel("CLO")
plt.ylabel("Average Score")
plt.show()

# Insights
# Average score comparison between 6-Week and 12-Week Topics
avg_score_by_subject = question_data.groupby('Subject')['Average'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_score_by_subject['Subject'], avg_score_by_subject['Average'])
plt.title("Average Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()

# Identifying high and low performing question types
high_performing = question_data[question_data['Average'] >= 0.85]
low_performing = question_data[question_data['Average'] <= 0.55]

print("\nHigh Performing Question Types:")
print(high_performing[['Question Number', 'Type', 'Average']])

print("\nLow Performing Question Types:")
print(low_performing[['Question Number', 'Type', 'Average']])


# Identifying high and low performing subjects
high_performing_subjects = question_data.groupby('Subject').filter(lambda x: x['Average'].mean() >= 0.85)['Subject'].unique()
low_performing_subjects = question_data.groupby('Subject').filter(lambda x: x['Average'].mean() <= 0.55)['Subject'].unique()

print("\nHigh Performing Question Subjects:")
print(high_performing[['Question Number', 'Subject', 'Average']])

print("\nLow Performing Question Subjects:")
print(low_performing[['Question Number', 'Subject', 'Average']])

