import os
import re

def rename_file(number, directory, file_path):
    # Create new file name
    new_name = f"{number[:4]}-{number[4:]}_tripdata.zip"

    # Create a new path with the file new name
    new_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(file_path, new_path)

def list_files(folder_path, rename):
    ids = []
    # Get file names contained in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file_name in files:
        # Get full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Verify if it's a file, not a folder
        if os.path.isfile(file_path):
            # Extract the directory and the original file name
            directory, original_name = os.path.split(file_path)
            
            # Extract file's id using regular expressions
            pattern = r"divvy-tripdata-(\d+).zip"
            coincidence = re.search(pattern, original_name)
            number = str(coincidence.group(1))
            
            ids.append(number)
            
            if rename == True:
                rename_file(number, directory, file_path)

    return ids
