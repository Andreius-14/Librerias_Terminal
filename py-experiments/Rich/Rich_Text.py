import FuncionesCompartidas as fc

# from rich.columns import Columns
from rich.console import Console
from rich.text import Text

# from rich import print
from rich.panel import Panel

console = Console()

txt = Text.from_ansi("\033[1mHello, World!\033[0m")
console.print(txt.spans)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                BASICO                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
fc.header("#", "Rich - Basico")

console.print("[bold red]This is bold red text[/bold red]")
console.print("[italic blue]This is italic blue text[/italic blue]")
console.print("[bold magenta]Hello, [yellow]Rich[/yellow]![/bold magenta]")
console.print("Where [bold cyan]Will[/bold cyan] the [u]is[/u] a [i]way[/i].")

texto01 = Text("Texto blanco sobre fondo azul", style="black on blue")
texto02 = Text("Texto con fondo amarillo", style="black on yellow")
texto03 = Text("Texto amarillo sobre fondo morado", style="black on purple")

console.print(texto01)
console.print(texto02)
console.print(texto03)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃           BASIC - EDIT                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
fc.header("#", "Rich - Edicion")

txtEdit1 = Text("Hello, World!")
txtEdit1.stylize("bold magenta", 0, 6)

txtEdit2 = Text("¡Hola Mundo! 👋🌍")
txtEdit2.style = "bold magenta"

console.print(txtEdit1)
console.print(txtEdit2)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃            BASIC - APPEND             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Rich - Parte x Parte")
# [append]

texto20 = Text()
texto20.append("Hola, ", style="bold red")
texto20.append("mundo!", style="italic blue underline")

texto30 = Text()
texto30.append("Línea 1\n", style="bold green")
texto30.append("Línea 2\n", style="italic blue")
texto30.append("Línea 3", style="underline red")

console.print(texto20)
console.print(texto30)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃            Panel + Text               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
fc.header("#", "Rich - Alinear")

panel = Panel(Text("Izquierda", justify="right"), border_style="green")
console.print(panel)

panel = Panel(Text("Centro", justify="center"), border_style="green")
console.print(panel)

panel = Panel(Text("Derecha", justify="left"), border_style="green")
console.print(panel)
