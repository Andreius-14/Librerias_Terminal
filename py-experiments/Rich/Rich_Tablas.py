import FuncionesCompartidas as fc

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

from rich.columns import Columns

# [Importante]
# from rich import print as rprint

console = Console()
layout = Layout()

table1 = fc.crear_tabla("Tabla 1", [["A1", "B1"], ["A2", "B2"], ["A3", "B3"]])
table2 = fc.crear_tabla("Tabla 2", [["C1", "D1"], ["C2", "D2"], ["C3", "D3"]])
table3 = fc.crear_tabla("Tabla 3", [["E1", "F1"], ["E2", "F2"], ["E3", "F3"]])


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃        Tablas - Layout y Panel        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Tablas Into Layout")

# [MOLDE]
layout.split(Layout(name="head", size=5), Layout(name="body", size=10))

# [EDITAR]
layout["head"].update(Panel("📊 Tablas en Columnas", border_style="bold cyan"))
layout["body"].split_row(
    Layout(
        Panel(
            table1,
            title="1 - Usuarios",
            border_style="blue",
        )
    ),
    Layout(
        Panel(
            table2,
            title="2 - Productos",
            border_style="green",
        )
    ),
)

# [IMPRIME]
console.print(layout)
console.print(layout.tree)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃        Tablas -  Panel Puro           ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Tabla into Panel")

varible = Panel(
    Columns([table1, table2, table3]),  # 👈 Apilamos tablas en vertical
    title="Layout con múltiples tablas (Vertical)",
    border_style="green",
    padding=(1, 2),
)

console.print(varible)


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃      Tablas -  Uso de Funcione        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

fc.header("#", "Automatizacion")


# Función para crear una tabla pequeña
def grupos(arrayGrupo):
    # MODO -- 01
    # FOR y arrayGrupo, Un panel por Item , Agrupo en []
    # Paso Objetos.Panel a Panel.Column  (Redundante)

    # MODO -- 02
    # Paso Objetos.Tablas a Panel.Column
    layoutPanel = Panel(
        Columns([*arrayGrupo]),
        title="Layout con múltiples tablas (Vertical)",
        border_style="green",
        padding=(1, 2),
    )

    console.print(layoutPanel)


grupos([table1, table2, table3])
