import os
from sys import exit

# Directory path to wherever you have your folder for the semester.
# Eg 'C:\Users\Tim\Google Drive\2023 Sem 2'
folder_dir = r"E:\QUT\2023 Semester 1"
semester_weeks = 15 # Modify this if needed

# Given a path to a folder, returns all folders within.
def get_subdirectories(directory):
    return [f.name for f in os.scandir(folder_dir) if f.is_dir()]
    
# Create a subfolder for each week of the semester for each subject folder.
subs = get_subdirectories(folder_dir)
if subs == []:
    print("Create the main folders for your respective classes before running script!")
    exit()
    
for sub in subs:
    for week in range(1, semester_weeks+1):
        new_folder = f"Week {week}"
        full_path = f"{folder_dir}\\{sub}\\{new_folder}"
        print(f"Creating folder at {full_path}")
        if os.path.exists(full_path):
            print("Folder already exists!")
            pass
        else:
            os.makedirs(full_path)
            print(f"Folder successfully created at {full_path}")
