import os
import re

def rename_files(folder_path,ids):
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
            pattern = r"Correo  - Notificación_ Acta No. (\d+) - ID (\d+).pdf"
            coincidence = re.search(pattern, original_name)

            contract = coincidence.group(1)
            number = coincidence.group(2)
            
            ids.append(number)

            # Create new file name
            new_name = f"{number} - Correo - Notificación_ Acta No. {contract}.pdf"

            # Create a new path with the file new name
            new_path = os.path.join(directory, new_name)

            # Renombrar el archivo
            os.rename(file_path, new_path)
    return ids


folder_path = r".\documents"
ids=[]

ids = rename_files(folder_path, ids)

for i in range(len(ids)):
    print(ids[i])