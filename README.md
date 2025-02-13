# DeltaPlus

DeltaPlus is a Python-based tool designed to securely destroy sensitive files on Windows systems. It employs advanced algorithms to ensure that the files cannot be recovered once deleted. 

## Features

- **Multiple Overwrites**: Files are overwritten with random data multiple times.
- **Rename and Delete**: Files are renamed with random strings before deletion to further prevent recovery.
- **Easy to Use**: Simply specify the files you want to destroy, and DeltaPlus does the rest.

## Requirements

- Python 3.x
- Windows OS

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/deltaplus.git
   ```
2. Navigate to the project directory:
   ```bash
   cd deltaplus
   ```

## Usage

1. Open `delta_plus.py` in a text editor.
2. Modify the `files_to_destroy` list with the paths of the files you wish to securely delete.
3. Run the script:
   ```bash
   python delta_plus.py
   ```

## Warning

This program will permanently delete files. Use with caution and ensure you have backups of any important data before using DeltaPlus.

## Contributing

Feel free to submit issues or pull requests to contribute to the development of DeltaPlus.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.