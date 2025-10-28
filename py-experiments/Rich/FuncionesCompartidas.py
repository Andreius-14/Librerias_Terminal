import time
from time import sleep

# [Importante]
# from rich import print as rprint

# [Mayor Control]
from rich.console import Console

# [Barra de Carga]
from rich.progress import track
from rich.progress import Progress
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel

# from rich.text import Text
from rich import inspect
from rich.text import Text
from rich.pretty import Pretty

from rich.table import Table

console = Console()


def header(nivel, titulo):
    console.print()
    console.print()
    console.print()
    console.print(Markdown(f"{nivel} {titulo}"))


def crear_tabla(titulo, datos):
    table = Table(title=titulo, border_style="blue")
    table.add_column("Columna 1", justify="center")
    table.add_column("Columna 2", justify="center")

    for fila in datos:
        table.add_row(*fila)

    return table
