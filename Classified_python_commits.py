
import csv
import os

# Replace with the actual path to "all_python_commits.csv"
input_csv_file = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/all_python_commits.csv'
output_folder = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/Python_commits'


csv.field_size_limit(200000)

def replace_none_values(data):
    # Replace None values in data dictionary with appropriate placeholders
    for key, value in data.items():
        if value is None:
            data[key] = "N/A"  # You can use any other placeholder if you prefer
    return data

def save_commit_data_to_csv(file_name, commit_data):
    # Remove the file extension from the filename
    file_name_without_extension = os.path.splitext(file_name)[0]

    output_filename = os.path.join(output_folder, f'{file_name_without_extension}.csv')
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'hash', 'author_name', 'author_email', 'committer_name', 'committer_email',
            'author_date', 'author_timezone', 'committer_date', 'committer_timezone',
            'branches', 'in_main_branch', 'merge', 'modified_files',
            'project_name', 'project_path', 'old_path', 'new_path', 'filename', 'diff', 'diff_parsed',
            'added_lines', 'deleted_lines', 'source_code', 'source_code_before',
            'methods', 'methods_before', 'changed_methods'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for data in commit_data:
            data = replace_none_values(data)
            writer.writerow(data)

def main():
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a dictionary to store commit data for each filename
    filename_commits_dict = {}

    # Read and extract commit data from "all_python_commits.csv"
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = os.path.basename(row['filename'])
            if filename not in filename_commits_dict:
                filename_commits_dict[filename] = []
            filename_commits_dict[filename].append(row)

    # Save commit data for each filename into separate CSV files
    for filename, commit_data in filename_commits_dict.items():
        save_commit_data_to_csv(filename, commit_data)

    print(f"Commits have been classified and saved into separate CSV files.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")