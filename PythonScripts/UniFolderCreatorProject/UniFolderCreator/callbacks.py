import typer
from UniFolderCreator import __settings__, __app_name__, __version__

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def _dry_run_callback(value: bool) -> None:
    __settings__.change_dry_run(value)