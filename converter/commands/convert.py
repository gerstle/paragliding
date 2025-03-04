import typer
from typing_extensions import Annotated
from rich import print
import importlib
import os

kml_module = importlib.import_module("models.kml")
wpt_module = importlib.import_module("models.wpt")

cli = typer.Typer()
types = {
    '.kml': getattr(kml_module, "KML"),
    '.wpt': getattr(wpt_module, "WPT"),
}


@cli.command()
def convert(
        ctx: typer.Context,
        source_file: Annotated[
            str,
            typer.Option('--source', '-s', help='Source file to convert from')
        ],
        destination_file: Annotated[
            str,
            typer.Option('--destionation', '-d', help='destination_file file to convert to')
        ],
        verbose: Annotated[
            bool,
            typer.Option('--verbose', '-v', help='verbose output')
        ] = False,
):
    if not os.path.exists(source_file):
        raise RuntimeError(f"source file '{source_file}' does not exist!")

    if os.path.exists(destination_file):
        overwrite = typer.confirm(f"destination file '{destination_file}' already exists, overwrite?")
        if not overwrite:
            raise typer.Abort()

    print(f"convert [blue]{source_file}[/blue] --> [green]{destination_file}[/green]")

    source = types[os.path.splitext(source_file)[1]](source_file)
    destination = types[os.path.splitext(destination_file)[1]]()
    print(f"found [green]{len(source.waypoints)}[/green] waypoints")
    for it in source.waypoints:
        print(f"  {it.name}")
        if verbose == True:
            print(f"    description: {it.description}")
            print(f"    coordinates: {it.lat} {it.long} {it.altitude}")

    destination.waypoints = source.waypoints
    destination.to_file(destination_file)
