# 2024-Data-Analysis-Pathway-Capstone-Project:
# Analyzing Keeneland's 2024 Spring Meet race data to (hopefully) improve future betting performance

### Features Checklist:

1. Loading data - Read in 2 CSV files
2. Clean and operate on the data while combining them - used pandas to clean and merge 2 data sets
3. Visualize/Present data - created a Tableau dashboard, which can be accessed at the link further down
4. Best practices - utilized a virtual environment with instructions located further down
5. Interpretation of data - used Jupyter Notebook markdown cells to annotate code

### Repo Contents Explained:

.ipynb checkpoints folder - automatically generated from using Jupyter Notebook

Keeneland 2024...TableauTemp folder - temp files automatically created from using Tableau Public

myvenv folder - automatically created by VS Code after initiating virtual environment (instructions below)

2024 Data Analysis Capstone Code.py - "rough draft" of code using VS Code because I find it easier to work in

Code.ipynb - **Final Draft** of code with comments using Jupyter Notebook to make it look nicer than the .py file

Keeneland 2024 Spring Meet Visualizations.twb - Tableau Public workbook, **finished dashboard** at the following link:
    https://public.tableau.com/app/profile/william.tyler/viz/Keeneland2024SpringMeetVisualizations/Story1?publish=yes
    
Keenland April 2024 Data for Capstone Project.csv - **main data file** that I manually created using race day results
    info from Keeneland's website
    
Keeneland Race Data Since Oct-2006.csv - **secondary data file** downloaded from Keeneland's website

License - GPL-3.0 standard file

README.md - what you are currently looking through

main_no_scratches.csv - "written" by code after removing horses that scratched from the main data file

main_no_scratches_grouped.csv - same as previous with the additions of "split" columns (explained in Final Draft)

merged_data_sets.csv - "written" by code after merging main data file and secondary data file once they were cleaned up

requirements.txt - used for virtual environment setup

### Virutal Environment Instructions

1. After you have cloned the repo to your machine, navigate to the project 
folder in GitBash/Terminal.
2. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
3. Activate the virtual environment. `source venv/bin/activate`
4. Install the required packages. `pip install -r requirements.txt`
5. When you are done working on your repo, deactivate the virtual environment. 
`deactivate`

[^1]: GitBash on Windows uses “python” instead of “python3”

If you don't want to use the command line and you have VS Code, you can use the info found here:
https://code.visualstudio.com/docs/python/environments

### End of File

