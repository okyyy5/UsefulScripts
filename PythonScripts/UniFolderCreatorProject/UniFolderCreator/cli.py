import typer
import os
from sys import exit
from pathlib import Path

from UniFolderCreator import __settings__, tree
from UniFolderCreator.dir_utility import *
from UniFolderCreator.colour_utility import coloured_message
from UniFolderCreator.callbacks import _version_callback, _dry_run_callback

app = typer.Typer(add_completion=False)

@app.command()
def main(
    version: bool = typer.Option(None, "--version", "-v", help="Show version", callback=_version_callback, is_eager=True),
      directory: str = typer.Argument(None, help="Directory to create folders at."),
        units: str = typer.Argument(None, help="Set of units provided as a string separated by a space e.g. 'IFB102 IFB104'.", rich_help_panel="Secondary Arguments"), 
            dry_run: bool = typer.Option(False, "--dry-run", "-dr", help="Run the script without creating any folders.", callback=_dry_run_callback)):
    """
    Create a set of week folders (1-12) for UNITS at DIRECTORY
    """

    if directory == None:
        print(coloured_message("red", "ERROR: Please provide a directory to create folders at."))
        exit()

    if directory[0] != '/' and directory[0:2] != '~/' and directory[0:2] != './':
        print(coloured_message("red", "ERROR: Directory must start with a '/' or '~/' or './'"))
        exit()

    dir_exists(Path(directory))

    logic(Path(directory), units)

def logic(folder_dir: Path, units: str) -> None: 
    sub_folders: list = []

    try:
        if units != None:
            sub_folders: list = units.split()

        # Check if chosen DIR doesn't exist
        dir_exists(folder_dir)

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
                    
    except Exception as error:
        print(coloured_message("red", f"ERROR: {error}"))
        exit()

    # Create a subfolder for each week of the semester for each subject folder.
    subs = get_subdirectories(folder_dir)

    if len(subs) == 0:
        print(coloured_message("red", "ERROR: Create the main folders for your respective classes before running script!"))
        exit()
        
    for sub in subs:
        make_directories(sub, __settings__.semester_weeks, __settings__.dry_run)
   
    print(coloured_message("blue", "\nINFO: Unit structure has been created"))
    tree.ptree(f'{folder_dir}')
    print("")


