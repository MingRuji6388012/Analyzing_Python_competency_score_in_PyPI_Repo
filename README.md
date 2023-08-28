# Analyzing the code competency of Python scripts in PyPI project GitHub repository using PyCefr and PyDriller.

---
## What is this project?
- This repo is the project I conducted during my internship at Nara Institute of Science and Technology, Japan.

## How to run (Step-by-step)
1) ### In ```All_python_commits.py```
- Edit the ```repo_url``` to the "GitHub repository URL.git" you need to collect data.
- Edit ```output_folder``` to the path to the directory you need to record the data.
- Run the script (This step may take 3-5 hours to collect data).
- After running the script, you will get the CSV file named ```all_python_commits.csv``` which records attributes we can get in PyDriller. 

2) ### In ```Classified_python_commits.py```
- Edit the ```input_csv_file``` to the CSV file of the python commits list from ```All_Python_commits.py``` (step 1)
- Edit ```output_folder``` to the path to the directory you need to record the data.
- Run the script (This step may take 5-10 minutes to collect data).
- After running the script, you will get the folder containing CSV files which each CSV file contains the list of commits of the **same updated python file in that commit**.

3) ### In ```python_extract_added_deleted_diff.py```
- Edit the ```input_folder``` to the folder of separated python commits CSV files from ```Classified_python_commits.py``` (step 2) .
- Edit the ```output_folder_added``` to the folder you need to contain "added" section of Python code in each commit.
- Edit the ```output_folder_deleted``` to the folder you need to contain "deleted" section of Python code in each commit.
- Run the script (This step may take 3-5 minutes to collect data).
- After running the script, you will get 3 folders (one contains python codes recorded in the attribute "added" from each commit, one contains codes in the attribute "deleted", and one contains code combined with both "added" and "deleted".
