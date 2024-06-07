# Dataset Overview

This dataset provides insights into student performance across various question types and topics.

## Dataset Information

First 5 Rows of the Dataset:

|   | Question Number | CLO   | Value | Type              | Subject           | Average | Maximum | Q3    | Median | Mode | Q1    | Minimum |
|---|-----------------|-------|-------|-------------------|-------------------|---------|---------|-------|--------|------|-------|---------|
| 0 | 1.0             | CLO 2 | 1.5   | Match             | 6-Week Topics     | 96.35%  | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 52.78%  |
| 1 | 2.0             | CLO 2 | 1.5   | Fill-in-the-Blank | 6-Week Topics     | 63.71%  | 98.61%  | 82.99%  | 70.49%  | 68.06%  | 44.62%  | 15.28%  |
...

## Data Cleaning

- Removed columns with no header.
- Removed rows with all NaN values.
- Converted percentage columns from strings to float.
- Filled NaN values in 'Type' column with a default color.
- Converted 'Type' column to categorical codes.

## Data Exploration

- Statistical summary.
- Boxplot of average scores by CLO Type.
- Barplot of average scores by CLO Subject.
- Scatter plot of Question Number vs Average Score.
- Boxplot of Average Scores by CLO.
- Scatter plot of Value vs Average Score colored by Type.
- Correlation matrix.
- Average score comparison between 6-Week and 12-Week Topics.

## Insights

### High Performing Question Types:

|   | Question Number | Type  | Average |
|---|-----------------|-------|---------|
| 0 | 1.0             | 1     | 0.9635  |
| 5 | 6.0             | 2     | 0.8728  |
...

### Low Performing Question Types:

|   | Question Number | Type  | Average |
|---|-----------------|-------|---------|
| 9  | 10.0            | 4     | 0.5489  |
| 11 | 12.0            | 0     | 0.4053  |
...

## Conclusion

1. The dataset provides insights into student performance across various question types and topics.
2. High-performing questions are predominantly of type 'Match' and 'Single-Select'.
3. Low-performing questions often belong to 'Fill-in-the-Blank' and 'True/False' types.
4. Recommend focusing on improving student performance in low-performing question types.
