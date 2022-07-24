import os
import sys
from sys import exit
from pathlib import Path

SEMESTER_WEEKS: int = 12 # Modify this if needed
DRY_RUN: bool = True

def main() -> None:
    # Directory path to wherever you have your folder for the semester.
    # Eg 'C:\Users\Tim\Google Drive\2023 Sem 2'
    try:
        folder_dir: Path = Path(get_arg(1))
        sub_folders: list = get_arg(2).split()

        # Check if chosen DIR doesn't exist
        if not folder_dir.exists():
            print(f"ERROR:\tFolder {folder_dir} does not exist! Would you like to create it?")

            answer = input("(y/n): ")

            while answer not in ["y", "n"]:
                print("Please enter 'y' or 'n'.")
                answer = input("(y/n): ")

            if answer == "n":
                print("Please restart the application to enter a new path")
                exit()
            elif answer == "y":
                try:
                    os.makedirs(folder_dir)
                except Exception as e:
                    print(f"ERROR:\tFolder {folder_dir} could not be created. {str(e)}")
                    exit()
                else:
                    print(f"INFO:\tFolder {folder_dir} successfully created.")

        # Create a subdirectory for each specified unit
        if len(sub_folders) > 0:
            for folder in sub_folders:
                try:
                    os.makedirs(f'{folder_dir}/{folder}')
                except Exception as e:
                    print(f"ERROR:\tFolder {folder} could not be created. {str(e)}")
                else:
                    print(f"INFO:\tFolder {folder} successfully created.")
                    
    except Exception:
        print("ERROR:\tThe entered path is not valid")
        exit()

    # Create a subfolder for each week of the semester for each subject folder.
    subs = get_subdirectories(folder_dir)

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

def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


if __name__ == '__main__':
    main()
