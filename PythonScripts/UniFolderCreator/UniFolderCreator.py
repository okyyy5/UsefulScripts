import typer
import os
from termcolor import colored
import colorama
import sys
from sys import exit
from pathlib import Path

app = typer.Typer(add_completion=False)
colorama.init()

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

    if directory == None:
        print("WARNING:\tNo directory given, would you like to default to the current directory?")
        answer = input("(y/n): ")

        while answer not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            answer = input("(y/n): ")

        if answer == "n":
            print("Please restart the application to enter a new path")
            exit()
        else:
            directory = './'

    if directory[0] != '/' and directory[0:2] != '~/' and directory[0:2] != './':
        print(coloured_message("red", "ERROR: Directory must start with a '/' or '~/'"))
        exit()

    if dry_run:
        _dry_run = True

    main(Path(directory), units)

def main(folder_dir: Path, units: str) -> None: 
    sub_folders: list = []

    try:
        if units != None:
            sub_folders: list = units.split()

        # Check if chosen DIR doesn't exist
        if not folder_dir.exists():
            print(coloured_message("yellow", f"WARNING: Folder {folder_dir} does not exist! Would you like to create it?"))

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
                    print(coloured_message("red", f"ERROR: Folder {folder_dir} could not be created. {str(e)}"))
                    exit()
                else:
                    print(coloured_message("green", f"SUCCESS: Folder {folder_dir} successfully created."))

        # Create a subdirectory for each specified unit
        if len(sub_folders) > 0:
            for folder in sub_folders:
                if not Path(f'{folder_dir}/{folder}').exists(): 
                    try:
                        os.makedirs(f'{folder_dir}/{folder}')
                    except Exception as e:
                        print(coloured_message("red", f"ERROR: Folder {folder} could not be created. {str(e)}"))
                    else:
                        print(coloured_message("green", f"SUCCESS: Folder {folder} successfully created."))
                else:
                    print(coloured_message("blue", f"INFO: Folder {folder} already exists."))
                    
    except Exception:
        print(coloured_message("red", "ERROR:\tThe entered path is not valid"))
        exit()

    # Create a subfolder for each week of the semester for each subject folder.
    subs = get_subdirectories(folder_dir)

    if len(subs) == 0:
        print(coloured_message("red", "ERROR: Create the main folders for your respective classes before running script!"))
        exit()
        
    for sub in subs:
        make_directories(sub, SEMESTER_WEEKS)
   
    print(coloured_message("blue", "\nINFO: Unit structure has been created"))
    ptree(f'{folder_dir}')
    print("")

def get_subdirectories(directory: Path) -> list[Path]:
    '''Returns each top-level subdirectory in a folder.'''
    return [f for f in directory.iterdir() if f.is_dir()]

def make_directories(parent: Path, weeks: int) -> None:
    '''Creates a folder for each week in the specified parent.'''
    for week in range(1, weeks+1):
        new_folder_name = f"Week {week}"
        full_path: Path = parent.joinpath(new_folder_name)

        if full_path.exists():
            print(coloured_message("yellow", f"WARNING: Folder {full_path} already exists!"))
            pass
        else:
            try:
                if not _dry_run:
                    full_path.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(coloured_message("red", f"ERROR:\tFolder {full_path} could not be created. {str(e)}"))

def coloured_message(colour: str, text: str) -> str:
    return colored(text, colour)

if __name__ == '__main__':
    app() 
