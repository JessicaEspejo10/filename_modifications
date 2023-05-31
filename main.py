import utils

#option to rename files
rename = True

folder_path = r".\documents"
ids = utils.list_files(folder_path, rename)

for i in range(len(ids)):
    print(ids[i])