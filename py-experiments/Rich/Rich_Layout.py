import FuncionesCompartidas as fc

from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()
console = Console()
# --- [LAYOUT:] ---
# Un tipo de Panel, En Grupo es Expansivo
# Abarcara todo el Ancho de la Terminal
# LAUOUT es Un Molde de Panqueques Personalizado

# --- [PANEL: ] ---
# -- El relleno se logra con PANEL

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃             BASICO - 01               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
fc.header("#", "Filas y Columnas")
# --[1 Columna]
# --[Reescribe layout]
layout.split_column(
    Layout(name="upper"),
    Layout(name="centro1"),
    Layout(name="lower"),
)
print(layout)


# --[1 Fila]
# --[Reescribe layout]
layout.split_row(
    Layout(name="upper"),
    Layout(name="centro1"),
    Layout(name="lower"),
)
print(layout)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃             BASICO - 02               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Plantilla Basica")

layout.split_column(
    Layout(name="1"),
    Layout(name="2"),
    Layout(name="3"),
    Layout(name="4"),
    # Layout(name="lower"),
)
print(layout)
print(layout.tree)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃           MOLDE - EDICION             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Molde - Edicion")

# Metodo - Array
layout["2"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

layout["4"].split_row(
    Layout(name="01"),
    Layout(name="02"),
    Layout(name="03"),
)

# Metodo - UPDATE  [Inutil]
# layout["3"].update(
#     "The mystery of life isn't a problem to solve, but a reality to experience."
# )

# layout["01"].update(
#     Panel("🔥 [bold magenta]CLI Dashboard[/bold magenta] 🔥", expand=False)
# )
#
# layout["03"].update(
#     Panel("[bold cyan]Press Ctrl+C to exit[/bold cyan]", expand=False)
# )

# layout["01"].visible = False
# layout["01"].size = 10
layout["02"].ratio = 2


# Imprime
print(layout)
print(layout.tree)

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃           MOLDE - RRELLENO            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Molde - rrelenando")
layout["right"].split_column(Layout(Panel("Hello")), Layout(Panel("World!")))
layout["left"].split_row(Layout(Panel("H")), Layout(Panel("W")), Layout(Panel("W")))

print(layout)
print(layout.tree)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                FUNCION                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def grupos(arrayGrupo):
    array_layouts = []
    layout = Layout()

    for i, valor in enumerate(arrayGrupo, start=1):
        array_layouts.append(
            Layout(Panel(valor, title=f"Tabla {i}", border_style="cyan"))
        )

    # (Al ser layout Abarca todo el Espacio)
    layout.split_row(*array_layouts)
    console.print(layout)
    layout.split_column(*array_layouts)
    console.print(layout)
