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
      directory: Path = typer.Argument(None, help="Directory to create folders at."),
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

    dir_exists(directory)

    try:
        # Check if chosen DIR doesn't exist
        dir_exists(directory)

        # Create a subdirectory for each specified unit
        if units != None:
            sub_folders: list = units.split()

            for folder in sub_folders:
                if not Path(f'{directory}/{folder}').exists():
                    if make_directory(f'{directory}/{folder}') == -1:
                      exit()
                else:
                    print(coloured_message("blue", f"INFO: Folder {folder} already exists."))
                    
    except Exception as error:
        print(coloured_message("red", f"ERROR: {error}"))
        exit()

    # Create a subfolder for each week of the semester for each subject folder.
    subs = get_subdirectories(directory)

    if len(subs) == 0:
        print(coloured_message("red", "ERROR: Create the main folders for your respective classes before running script!"))
        exit()
        
    for sub in subs:
        make_directories(sub, __settings__.semester_weeks, __settings__.dry_run)
   
    print(coloured_message("blue", "\nINFO: Unit structure has been created"))
    tree.ptree(f'{directory}')
    print("")


