

import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


# accept input coordinates x, y and z from user
@app.command("convert")
def sample_func():
    print("hey")

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")


if __name__ == "__main__":
   app()    