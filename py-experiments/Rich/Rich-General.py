import time
from time import sleep

# [Importante]
from rich import print as rprint

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


console = Console()


def imprimir_basico(valorSimple, mensaje="Texto Simple"):
    panelBasico = Panel(
        valorSimple,  # Contenido del panel
        title=mensaje,  # Título del panel
        border_style="blue",  # Estilo del borde
        padding=(1, 2),  # Espaciado interno
    )
    console.print(panelBasico)


def imprimir_textos(*contenidos):
    contenido_completo = Text.from_markup("\n".join(contenidos))

    panel = Panel(
        contenido_completo,  # Contenido formateado
        title="Contenido en Panel",  # Título del panel
        border_style="blue",  # Estilo del borde
        padding=(1, 2),  # Espaciado interno
    )

    console.print(panel)


def imprimte_Coleccion(mensaje, objetoColeccion):
    panelColeccion = Panel(
        Pretty(objetoColeccion, expand_all=True),
        title=mensaje,
        border_style="blue",
        padding=(1, 2),
    )
    console.print(panelColeccion)


def header(nivel, titulo):
    console.print()
    console.print()
    console.print()
    console.print(Markdown(f"{nivel} {titulo}"))


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃              BASICO                   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# console.print(Markdown("# Rich - Basico"))
header("#", "Rich - Basico")

imprimir_textos(
    "[bold red]This is bold red text[/bold red]",
    "[italic blue]This is italic blue text[/italic blue]",
    "[bold magenta]Hello, [yellow]Rich[/yellow]![/bold magenta]",
    "Where [bold cyan]Will[/bold cyan] the [u]is[/u] a [i]way[/i].",
)
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃            Colecciones                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# console.print(Markdown("# Rich - Colecciones"))
header("#", "Rich - Colecciones")

nums_tuple = (1, 2, 3, 4)
nums_list = [1, 2, 3, 4]
nums_dict = {"nums_list": nums_list, "nums_tuple": nums_tuple}
bool_list = [True, False]

objeto = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "intereses": ["programación", "música", "viajes"],
}

# inspect(objeto)

imprimte_Coleccion("Objeto", objeto)
imprimte_Coleccion("Lista", nums_list)
imprimte_Coleccion("Tupla", nums_tuple)
imprimte_Coleccion("Diccionario", nums_dict)
imprimte_Coleccion("Booleano", bool_list)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                 LOAD                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

header("#", "Rich - Cargadores")


def process_data():
    sleep(0.02)


for _ in track(range(100), description="[green]Processing data"):
    process_data()


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                 LOAD                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Installing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                Tablas                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
header("#", "Rich - Tablas")

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃      Tabla 01      ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃      Tabla 02      ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
table2 = Table(title="Table 02")

table2.add_column("Name", style="cyan")
table2.add_column("Age", justify="right", style="magenta")
table2.add_column("City", style="green")

table2.add_row("Alice", "24", "New York")
table2.add_row("Bob", "30", "Los Angeles")
table2.add_row("Charlie", "35", "San Francisco")

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃      Tabla 03      ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
table3 = Table(title="Table 03")

table3.add_column("Name", style="cyan")
table3.add_column("Profession", style="magenta")
table3.add_column("Favourite Colour", style="green")

table3.add_row("Arjan", "Developer / YouTuber", "Turquoise")
table3.add_row("Alyce", "Developer / Writer", "Purple")
table3.add_row("Andreas", "Developer / Writer", "Green")

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃       Imprime      ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
console.print(table)
console.print(table2)
console.print(table3)

imprimir_basico(table)
# Crear el panel con la tabla dentro
# panelx = Panel(table, title="Datos de Usuarios", border_style="blue")

# Imprimir el panel con la tabla
# console.print(panelx)
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               Markdown                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
header("#", "Rich - Markdown")

markdown1 = Markdown("# Rich!\n\nThis **markdown**")

markdown2 = Markdown("## Rich!\n\nThis **markdown** ")

markdown3 = Markdown("### Rich!\n\nThis **markdown** ")

console.print(markdown1)
console.print(markdown2)
console.print(markdown3)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                Panel                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
header("#", "Rich - Panel")

panel1 = Panel(
    "This is a panel.", title="Panel Title", subtitle="Subtitle", border_style="red"
)

console.print(panel1)
# console.print(panel2)
