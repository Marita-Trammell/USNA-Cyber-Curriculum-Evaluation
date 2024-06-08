# Naval Academy Cyber Curriculum Analysis

## Project Overview
This repository contains Python code for analyzing student performance data with the goal of restructuring the curriculum for cyber courses at the Naval Academy. The project aims to provide insights into student performance across various question types and subjects to enhance teaching quality and learning outcomes in cyber-related disciplines.

## Project Structure
- **question_data.csv**: Dataset containing student performance data for cyber course questions.
- **instructor_data.csv**: Dataset containing instructor performance data.
- **data_analysis.ipynb**: Jupyter Notebook containing data cleaning, analysis, and visualization code.
- **Question_Data_Cleaning.py**: Python script for data cleaning.
- **Question_Data_Analysis.ipynb**: Jupyter Notebook focusing on detailed data analysis.
- **README.md**: This file, providing an overview of the project.

## Requirements
- Python 3
- Libraries: pandas, numpy, matplotlib

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/marita-trammell/naval-academy-cyber-curriculum.git
2. Navigate to the project directory:
   ```bash
   cd naval-academy-cyber-curriculum
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
4. Run the Python script in Jupyter Notebooks to perform data analysis and visualization.

## Data Set
- question_data.csv: Contains student performance data for cyber course questions.
- instructor_data.csv: Contains instructor performance data.

## Data Cleaning
- Removed columns with no headers and rows with all NaN values.
- Converted percentage columns to float.
- Rounded numerical columns to desired decimal places.

## Data Exploration 
- Provided statistical summaries for question and instructor data.
- Explored relationships between various factors affecting student performance.

## Data Visualization 
- Box plots, bar plots, and scatter plots to visualize student performance and relationships between variables.

## Insights 
- Identified high and low performing question types and subjects.
- Provided recommendations for restructuring the curriculum based on performance insights.

## Conclusions and Recommendations
The analysis aims to provide insights into student performance in cyber courses at the Naval Academy.
High-performing question types and subjects will be emphasized in the curriculum restructuring.
Low-performing areas will be targeted for improvement to enhance teaching effectiveness.
Recommendations:
- Adjust curriculum focus based on high-performing question types and subjects.
- Provide additional support or resources for topics identified as low-performing.
- Incorporate effective teaching strategies identified from high-performing sections.
- Continuously monitor student performance to adapt the curriculum as needed.
- Collaborate with instructors to improve teaching quality and student learning outcomes.
