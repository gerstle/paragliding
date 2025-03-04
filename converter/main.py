import typer
from types import SimpleNamespace
from commands.convert import cli as convert_cli


cli = typer.Typer(rich_markup_mode=None)
cli.add_typer(convert_cli)

@cli.callback()
def setup(
    ctx: typer.Context
):
    ctx.obj = SimpleNamespace()


if __name__ == "__main__":
    cli()
