from pathlib import Path
from UniFolderCreator.colour_utility import coloured_message

def get_subdirectories(directory: Path) -> list[Path]:
    '''Returns each top-level subdirectory in a folder.'''
    return [f for f in directory.iterdir() if f.is_dir()]

def make_directory(path: str) -> None:
    '''Creates a folder at the specified path.'''
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(coloured_message("red", f"ERROR: Folder {path} could not be created. {str(e)}"))
        exit()
    else:
        print(coloured_message("green", f"SUCCESS: Folder {path} successfully created."))

def make_directories(parent: Path, weeks: int, _dry_run: bool) -> None:
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

def dir_exists(directory: Path) -> bool:
  if not directory.exists():
      print(coloured_message("yellow", f"WARNING: Folder {directory} does not exist! Would you like to create it?"))

      answer = input("(y/n): ")

      while answer not in ["y", "n"]:
          print("Please enter 'y' or 'n'.")
          answer = input("(y/n): ")

      if answer == "n":
          print("Please restart the application to enter a new path")
          exit()
      elif answer == "y":
          make_directory(directory)