import FuncionesCompartidas as fc
from rich.columns import Columns

from rich import print
from rich.panel import Panel

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃       BASICO       ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
print(Panel("Hello, [red]World!"))
print(Panel.fit("Hello, [red]World!"))

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃    PERSONALIZADO   ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))
print(Panel.fit("Hello, [red]World!", title="Welcome", subtitle="Thank you"))


# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃  RAMDOM ELEMENTOS  ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛

table1 = fc.crear_tabla("Tabla 1", [["A1", "B1"], ["A2", "B2"], ["A3", "B3"]])
table2 = fc.crear_tabla("Tabla 2", [["C1", "D1"], ["C2", "D2"], ["C3", "D3"]])
table3 = fc.crear_tabla("Tabla 3", [["E1", "F1"], ["E2", "F2"], ["E3", "F3"]])

varible = Panel(
    Columns([table1, table2, table3]),  # 👈 Apilamos tablas en vertical
    title="Layout con múltiples tablas (Vertical)",
    border_style="green",
    padding=(1, 2),
)

print(varible)

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃  RAMDOM ELEMENTOS  ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
panel = Panel(
    "Este es un panel con espaciado interno",
    title="Panel con Padding",
    border_style="bold cyan",
    padding=(4, 10),  # 2 líneas verticales, 4 espacios horizontales
)

# Imprimir el Panel en la consola
print(panel)

# ┏━━━━━━━━━━━━━━━━━━━━┓
# ┃  RAMDOM ELEMENTOS  ┃
# ┗━━━━━━━━━━━━━━━━━━━━┛
panel_externo = Panel(
    panel,
    title="Panel Externo",
    border_style="bold red",
    padding=(1, 2),
)

# Imprimir el Panel en la consola
print(panel_externo)
