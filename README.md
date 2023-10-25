# Zip Merge

## Description

This script is designed to unzip files from a specified directory and merge their contents into another directory based on a specific naming convention. It also provides an option to delete the original zip files after extraction.

## Prerequisites

This script assumes that you have a Python 3.8 environment set up and that you are using a Unix-based operating system (macOS or Linux).

### Environment Variables

If you are using macOS, the script sets some environment variables to optimize PyTorch compatibility:

```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
```

### Virtual Environment

The script checks if a virtual environment (venv) exists. If it doesn't, it creates one.

If a virtual environment is not present, it installs Python 3.8 (if necessary) and creates a venv.

### Dependencies

The script also checks for and installs Python packages specified in a `requirements.txt` file if it exists.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/VitthalGupta/zip-merge.git
    ```

2. Run the script:

    ```bash
    cd zip-merge
    sh run.sh
    ```

### OR

1. Activate the virtual environment (if not already activated):

    ```bash
    source .venv/bin/activate
    ```

2. Run the main script with the following parameters:

    - `--zip_dir`: The path to the directory containing the zip files.
    - `--target`: The name of the folder to unzip.
    - `--merge_dir`: The path to the directory where the contents will be merged.
    - `--delete`: (Optional) Set to "True" if you want to delete the zip files after extraction (default is "False").

Here's an example of how to run the script:

```bash
python3 main.py --zip_dir /path/to/zip/files --target MyFiles --merge_dir /path/to/merge/directory --delete True
```

## Troubleshooting

- Ensure that the provided directory paths are correct and free of spaces.
- Check for any errors or issues reported during script execution.

## Support

For any questions or issues, please contact the script author.

## License

This script is open-source and distributed under the [MIT License](LICENSE).

## Contributors

<a href="https://github.com/VitthalGupta/zip-merge/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=VitthalGupta/zip-merge" />
</a>
