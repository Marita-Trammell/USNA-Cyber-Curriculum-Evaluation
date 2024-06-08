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
Proposed Changes to SY110 Course Learning Objectives

Based on the findings from the data analysis, the following changes to the SY110 Course Learning Outcomes are proposed to address identified gaps and enhance the learning experience:

## Refine CLOs to Focus on Practical Skills:
- **Current CLO**: "Analyze and explain the output of programs and the results of shell commands and infer why certain actions are permitted or not in an information system."
- **Proposed Change**: "Analyze and interpret the output of programs and shell commands, and troubleshoot issues in information systems to determine the reasons for permitted or restricted actions."

## Enhance Understanding of Technical Foundations:
- **Current CLO**: "Describe computers, operating systems, networks, the Internet and the Web with respect to: digital representations of information, their basic operation and associated tools, and the underlying architectures and protocols and how they may be vulnerable to attack."
- **Proposed Change**: "Explain the fundamental components and operations of computers, operating systems, networks, the Internet, and the Web, and identify their vulnerabilities to various types of cyber attacks."

## Strengthen Focus on Defense Mechanisms:
- **Current CLO**: "Identify and describe the principles and desired properties of defensible information systems, and the techniques and tools that are used to provide them. Explain representative attacks and their prevention and mitigation measures."
- **Proposed Change**: "Identify and evaluate the principles and properties of defensible information systems, and apply techniques and tools for their implementation. Analyze representative cyber attacks and develop strategies for their prevention and mitigation."

## Improve User-Centric Security Awareness:
- **Current CLO**: "Describe cyber domain scenarios in which user decisions affect security, identifying the user's versus the technology's responsibilities, and explain the consequences of potential user actions in terms of risk and the tradeoff between services and security."
- **Proposed Change**: "Analyze cyber domain scenarios where user decisions impact security, distinguish between user and technology responsibilities, and evaluate the consequences of user actions in terms of risk and the balance between services and security."

## Incorporate Advanced Defensive Techniques:
- **Current CLO**: "Explain, differentiate, and perform basic actions related to reconnaissance, attack, defense, and forensics of information systems."
- **Proposed Change**: "Demonstrate advanced techniques in reconnaissance, attack, defense, and forensics of information systems, and apply these techniques in simulated environments."

## Conclusion
The data analysis of the SY110 course has provided valuable insights into student performance and the effectiveness of current learning objectives. By refining and enhancing the CLOs to focus more on practical skills, technical understanding, defense mechanisms, user-centric security, and advanced techniques, the course can better prepare students to meet the challenges of the cyber domain.

These proposed changes aim to bridge identified gaps, improve student engagement and performance, and ensure that the learning outcomes are aligned with the evolving requirements of the field of cybersecurity.
