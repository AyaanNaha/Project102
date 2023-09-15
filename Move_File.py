import os
import shutil

from_dir = "C:/Users/ayaan/Downloads" # Replace with your computer's downloads directory
to_dir = "C:/Users/ayaan/OneDrive/Desktop/" # Replace with a folder in your computer

list_of_files = os.listdir(from_dir)
# print(list_of_files)

# Checks every file in Downloads folder
for file in list_of_files:
    name, extension = os.path.splitext(file)
    
    # IF file is not a document, skips that file
    extension_is_document = extension in ['.txt', '.doc', '.docx', '.pdf']
    if extension == "" or not extension_is_document:
        continue

    # Sets up path variables
    path1 = f'{from_dir}/{file}'
    path2 = f'{to_dir}/Document_Files'
    path3 = f'{path2}/{file}'

    # If the destination directory exists, moves the file
    # Else: makes the directory and then moves the file
    if os.path.exists(path2):
        print(f'Moving {file}...')
        shutil.move(path1, path3)
    else:
        os.mkdir(path2)
        print(f'Moving {file}...')
        shutil.move(path1, path2)