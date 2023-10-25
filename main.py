import argparse
import os
import zipfile
from tqdm import tqdm

# Create an argument parser
parser = argparse.ArgumentParser(
    description='Unzip and merge folders based on a specific name.')

# Add arguments for zip directory, target folder name, and merge directory
parser.add_argument('--zip_dir', type=str,
                    help='Path to the directory containing the zip files')
parser.add_argument('--target', type=str,
                    help='Name of the folder to unzip')
parser.add_argument('--merge_dir', type=str,
                    help='Path to the directory where contents will be merged')
parser.add_argument('--delete', type=bool, default=False,
                    help='Option to delete zip files after copying (True or False)')


# Parse the command-line arguments
args = parser.parse_args()

# Declare variable for total number of files
count_files = 0

# Verify that the provided directories exist
if not os.path.exists(args.zip_dir):
    print("The provided zip directory does not exist.")
    print('Do check if there is a typo in the directory path.')
    print('Also check if there are spaces in the directory path.')
    exit(1)

if not os.path.exists(args.merge_dir):
    os.makedirs(args.merge_dir)

# List all the files in the zip_dir
discovered_files = []
for root, dirs, files in os.walk(args.zip_dir):
    for file in files:
        if file.startswith(args.target) and file.endswith('.zip'):
            discovered_files.append(file)

# Display the list of discovered files
print("Discovered files in the specified folder:")
for i, file in enumerate(discovered_files, start=1):
    print(f"{i}. {file}")

print('Summary:')
print(f'Files discovered {len(discovered_files)}')
print('File types: .zip')

# Ask the user to proceed
proceed = input(
    "Do you want to proceed with extracting these files? (y/n): ").strip().lower()
if proceed != 'y':
    print("Extraction aborted.")
    exit(0)


# Extract the selected files
count_files = 0
for file in discovered_files:
    zip_file_path = os.path.join(args.zip_dir, file)
    count_files += 1
    # Unzip the file to the merge directory with tqdm progress bar
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_info in tqdm(zip_ref.infolist(), desc=f'Extracting {file}'):
            zip_ref.extract(file_info, args.merge_dir)

if not args.delete:
    # Delete the zip files if the delete option is True
    for file in discovered_files:
        zip_file_path = os.path.join(args.zip_dir, file)
        os.remove(zip_file_path)
        print(f"Deleted {file}")

# Print the total number of files extracted
print("Total number of files extracted: ", count_files)
print("Done!")