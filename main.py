import argparse
import os
import zipfile
from tqdm import tqdm
import os

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
for root, dirs, files in os.walk(args.zip_dir):
    for file in files:
        if file.startswith(args.target) and file.endswith('.zip'):
            zip_file_path = os.path.join(root, file)
            count_files += 1
            # Unzip the file to the merge directory with tqdm progress bar
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                for file_info in tqdm(zip_ref.infolist(), desc=f'Extracting {file}'):
                    zip_ref.extract(file_info, args.merge_dir)
            if args.delete:
                # Delete the zip file if the delete option is True
                os.remove(zip_file_path)

# Print the total number of files extracted
print("Total number of files extracted: ", count_files)
print("Done!")