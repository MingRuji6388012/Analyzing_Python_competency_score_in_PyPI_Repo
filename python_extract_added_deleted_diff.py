import csv
import ast
import os
import sys

# Increase the CSV field size limit
csv.field_size_limit(sys.maxsize)

# Replace with the actual path to "Python_commits" folder
input_folder = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/Python_commits'
# Replace with the actual path to "Python_diff_added" folder
output_folder_added = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/Python_diff_added'
# Replace with the actual path to "Python_diff_deleted" folder
output_folder_deleted = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/Python_diff_deleted'

def main():
    # Create the output folders if they don't exist
    os.makedirs(output_folder_added, exist_ok=True)
    os.makedirs(output_folder_deleted, exist_ok=True)

    # Dictionary to store added and deleted lines for each commit
    added_lines_dict = {}
    deleted_lines_dict = {}

    for filename in os.listdir(input_folder):
        input_csv_file = os.path.join(input_folder, filename)

        with open(input_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for commit in reader:
                commit_diff = ast.literal_eval(commit['diff_parsed'])

                # Extract added and deleted lines from the diff_parsed attribute
                added_lines = commit_diff.get('added', [])
                deleted_lines = commit_diff.get('deleted', [])

                # Combine the added and deleted lines into a single Python file for each commit
                added_content = '\n'.join([line_str for _, line_str in added_lines])
                deleted_content = '\n'.join([line_str for _, line_str in deleted_lines])

                # Get the commit hash as the file name
                commit_hash = commit['hash']

                # Save the combined content into separate .py files based on the label (added or deleted)
                output_file_added = os.path.join(output_folder_added, f"{commit_hash}_added.py")
                output_file_deleted = os.path.join(output_folder_deleted, f"{commit_hash}_deleted.py")

                with open(output_file_added, 'w', encoding='utf-8') as f:
                    f.write(added_content)
                
                with open(output_file_deleted, 'w', encoding='utf-8') as f:
                    f.write(deleted_content)

    print("Python code from each commit has been extracted and saved into separate .py files.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")