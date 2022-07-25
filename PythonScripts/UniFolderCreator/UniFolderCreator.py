import typer
import os
import sys
from sys import exit
from pathlib import Path

app = typer.Typer(add_completion=False)

_dry_run: bool = False
SEMESTER_WEEKS: int = 12 # Modify this if needed

# Credit: https://stackoverflow.com/a/45599996
# Prints a directory tree after running
def realname(path, root=None):
    if root is not None:
        path=os.path.join(root, path)
    result=os.path.basename(path)
    if os.path.islink(path):
        realpath=os.readlink(path)
        result= '%s -> %s' % (os.path.basename(path), realpath)
    return result

def ptree(startpath, depth=-1):
    prefix=0
    if startpath != '/':
        if startpath.endswith('/'): startpath=startpath[:-1]
        prefix=len(startpath)
    for root, dirs, files in os.walk(startpath):
        level = root[prefix:].count(os.sep)
        if depth >-1 and level > depth: continue
        indent=subindent =''
        if level > 0:
            indent = '|   ' * (level-1) + '|-- '
        subindent = '|   ' * (level) + '|-- '
        print('{}{}/'.format(indent, realname(root)))
        # print dir only if symbolic link; otherwise, will be printed as root
        for d in dirs:
            if os.path.islink(os.path.join(root, d)):
                print('{}{}'.format(subindent, realname(d, root=root)))
        for f in files:
            print('{}{}'.format(subindent, realname(f, root=root)))

@app.command()
def folder_directory(directory: str = typer.Argument(None, help="Directory to create folders at."),
                        units: str = typer.Argument(None, help="Set of units provided as a string seperated by a space e.g. 'IFB102 IFB104'.", rich_help_panel="Secondary Arguments"), 
                            dry_run: bool = typer.Option(False, "--dry-run", "-dr", help="Run the script without creating any folders.")):
    """
    Create a set of week folders (1-12) for UNITS at DIRECTORY
    """
    global _dry_run 

    if directory[0] != '/':
        print("ERROR:\tDirectory must start with a '/' or '~/'")
        exit()

    if dry_run:
        _dry_run = True

    main(Path(directory), units)

def main(folder_dir: Path, units: str) -> None: 
    sub_folders: list = []

    # Directory path to wherever you have your folder for the semester.
    # Eg 'C:\Users\Tim\Google Drive\2023 Sem 2'
    try:
        if units != None:
            sub_folders: list = units.split()


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
    
    print("SUCCESS: Unit structure has been created")
    ptree(f'{folder_dir}')    

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
            print(f"INFO:\tFolder {full_path} being created...")
            try:
                if not _dry_run:
                    full_path.mkdir(parents=True, exist_ok=True)
                else:
                    print(f"INFO: Dry run, pretending we created {full_path}...")
            except Exception as e:
                print(f"ERROR:\tFolder {full_path} could not be created. {str(e)}")
            else:
                print(f"INFO:\tFolder {full_path} successfully created.")

if __name__ == '__main__':
    app() 
