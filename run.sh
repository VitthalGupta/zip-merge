#!/bin/bash

if [[ "$(uname)" == "Darwin" ]]; then
  # macOS specific env:
  export PYTORCH_ENABLE_MPS_FALLBACK=1
  export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
elif [[ "$(uname)" != "Linux" ]]; then
  echo "Unsupported operating system."
  exit 1
fi

if [ -d ".venv" ]; then
  echo "Activating venv..."
  source .venv/bin/activate
else
  echo "Creating venv..."
  requirements_file="requirements.txt"

  # Check if Python 3.8 is installed
  if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Attempting to install 3.8..."
    if [[ "$(uname)" == "Darwin" ]] && command -v brew &> /dev/null; then
      brew install python@3.8
    elif [[ "$(uname)" == "Linux" ]] && command -v apt-get &> /dev/null; then
      sudo apt-get update
      sudo apt-get install python3.8
    else
      echo "Please install Python 3.8 manually."
      exit 1
    fi
  fi

  python3 -m venv .venv
  source .venv/bin/activate

  # Check if required packages are installed and install them if not
  if [ -f "${requirements_file}" ]; then
    installed_packages=$(python3 -m pip freeze)
    while IFS= read -r package; do
      [[ "${package}" =~ ^#.* ]] && continue
      package_name=$(echo "${package}" | sed 's/[<>=!].*//')
      if ! echo "${installed_packages}" | grep -q "${package_name}"; then
        echo "${package_name} not found. Attempting to install..."
        python3 -m pip install --upgrade "${package}"
      fi
    done < "${requirements_file}"
  else
    echo "${requirements_file} not found. Please ensure the requirements file with required packages exists."
    exit 1
  fi
fi

if [[ $? -ne 0 ]]; then
  exit 1
fi

# Prompt the user for input
read -p "Enter the path to the zip directory (--zip_dir): " zip_dir
read -p "Enter the target ZIP initial name (--target): " target_folder_name
read -p "Enter the path to the merge directory (--merge_dir): " merge_dir
read -p "Do you want to delete the zip files after extraction? (y/n) (Default: n): " delete_input

# Translate 'y' to 'True' and 'n' to 'False'
if [ "$delete_input" = "y" ]; then
  delete_zip_files="True"
else
  delete_zip_files="False"
fi

# Run the main script with the provided parameters
python3 main.py --zip_dir "$zip_dir" --target "$target_folder_name" --merge_dir "$merge_dir" --delete "$delete_zip_files"
