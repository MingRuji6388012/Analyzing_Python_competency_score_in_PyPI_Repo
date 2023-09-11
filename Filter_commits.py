#classify which records have filename .py 
import csv
import os

# Replace with the actual path to "all_python_commits.csv"
input_csv_file = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/all_python_commits.csv'
output_folder = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/'

# Expand the field size to eligible for collecting all commits 
# This is the commend I added to demonstrate how code diff works   
csv.field_size_limit(2000000)

def replace_none_values(data):
    # Replace None values in data dictionary with appropriate placeholders
    for key, value in data.items():
        if value is None:
            data[key] = "N/A"  # You can use any other placeholder if you prefer
    return data

def remove_null_lines(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            for line in infile:
                if '\x00' not in line:
                    outfile.write(line)

def save_commit_data_to_csv(commit_data):
    output_filename = os.path.join(output_folder, 'filtered_python_commits.csv')
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

    # Preprocess the CSV file and remove NUL characters
    cleaned_csv_file = '/work/Ming_PyDrillerPythonFileCommitHistory/Apache Airflow/Python_commit_data_cleaned.csv'
    remove_null_lines(input_csv_file, cleaned_csv_file)

    # Read and filter commit data from "all_python_commits.csv"
    filtered_commit_data = []
    with open(cleaned_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row.get('filename')
            if filename and filename.endswith('.py'):  # Check if filename exists and is not None
                filtered_commit_data.append(row)

    # Save filtered commit data into a new CSV file
    save_commit_data_to_csv(filtered_commit_data)

    print(f"Filtered commits with Python files have been saved in 'filtered_python_commits.csv'")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")