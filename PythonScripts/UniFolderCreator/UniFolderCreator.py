import os
import sys
from sys import exit
from pathlib import Path

# Directory path to wherever you have your folder for the semester.
# Eg 'C:\Users\Tim\Google Drive\2023 Sem 2'
try:
    FOLDER_DIR: Path = Path(sys.argv[1])
except Exception:
    print("ERROR:\tThe entered path is not valid")
    exit()
SEMESTER_WEEKS: int = 12 # Modify this if needed
DRY_RUN: bool = True

def main() -> None:
    # Create a subfolder for each week of the semester for each subject folder.
    subs = get_subdirectories(FOLDER_DIR)

    if len(subs) == 0:
        print("ERROR:\tCreate the main folders for your respective classes before running script!")
        exit()
        
    for sub in subs:
        make_directories(sub, SEMESTER_WEEKS)

def get_subdirectories(directory: Path) -> list[Path]:
    '''Returns each top-level subdirectory in a folder.'''
    return [f for f in directory.iterdir() if f.is_dir()]

def make_directories(parent: Path, weeks: int) -> None:
    '''Creates a folder for each week in the specified parent.'''
    for week in range(1, weeks+1):
        new_folder_name = f"Week {week}"
        full_path: Path = parent.joinpath(new_folder_name)

        if full_path.exists():
            print(f"WARNING:\tFolder {full_path} already exists!")
            pass
        else:
            # print(f"INFO:\tFolder {full_path} being created...")
            try:
                if not DRY_RUN:
                    full_path.mkdir(parents=True, exist_ok=True)
                else:
                    print(f"INFO: Dry run, pretending we created {full_path}...")
            except Exception as e:
                print(f"ERROR:\tFolder {full_path} could not be created. {str(e)}")
            else:
                print(f"INFO:\tFolder {full_path} successfully created.")

if __name__ == '__main__':
    main()
