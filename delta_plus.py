import os
import random
import string
import shutil

def secure_delete(file_path, passes=3):
    """
    Overwrites the given file with random data multiple times to prevent recovery.
    
    :param file_path: The path to the file to be deleted
    :param passes: Number of times to overwrite the file
    """
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    file_size = os.path.getsize(file_path)

    try:
        with open(file_path, 'ba+', buffering=0) as f:
            for i in range(passes):
                f.seek(0)
                random_data = os.urandom(file_size)
                f.write(random_data)
                print(f"Pass {i + 1}: Overwritten with random data.")
            f.flush()
    except Exception as e:
        print(f"Error during overwriting file: {e}")
        return

    try:
        os.remove(file_path)
        print(f"The file {file_path} has been securely deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def rename_and_delete(file_path):
    """
    Renames the file with random names multiple times before deletion to prevent name-based recovery.
    
    :param file_path: The path to the file to be renamed and deleted
    """
    dir_name = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    for _ in range(5):
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        new_path = os.path.join(dir_name, new_name)
        try:
            os.rename(file_path, new_path)
            file_path = new_path
            print(f"File renamed to {new_name}")
        except Exception as e:
            print(f"Error renaming file: {e}")
            return

    secure_delete(file_path)

def destroy_files(file_paths):
    """
    Destroys all files in the list by securely deleting them.
    
    :param file_paths: List of file paths to be destroyed
    """
    for file_path in file_paths:
        print(f"Destroying file: {file_path}")
        rename_and_delete(file_path)

if __name__ == "__main__":
    files_to_destroy = [
        "path/to/your/sensitive_file1.txt",
        "path/to/your/sensitive_file2.txt",
        # Add more file paths as needed
    ]

    destroy_files(files_to_destroy)