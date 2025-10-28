import time
import random
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from datetime import datetime

console = Console()


# Dashboard Layout
def make_layout():
    """Defines the layout of the dashboard."""
    layout = Layout()

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3),
    )

    return layout


# Edit Plantilla
layout = make_layout()

# BASURA - INICIO
layout["header"].update(Panel("[bold magenta]📊 Live CLI Dashboard[/bold magenta]"))
layout["footer"].update(Panel("[bold cyan]Press Ctrl+C to exit[/bold cyan]"))

# BASURA - FIN


def generate_table():
    """Creates a table with random data"""
    table = Table(title="📈 System Stats")
    table.add_column("Metric", style="cyan", justify="right")
    table.add_column("Value", style="magenta", justify="right")

    table.add_row("CPU Usage", f"{random.randint(10, 90)}%")
    table.add_row("Memory Usage", f"{random.randint(30, 80)}%")
    table.add_row("Disk Space", f"{random.randint(50, 95)}%")

    return table


with Progress() as progress:
    task = progress.add_task("[green]Processing...[/green]", total=100)

    while not progress.finished:
        layout["main"].update(
            Panel(generate_table(), title=f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        )
        console.print(layout)
        progress.update(task, advance=random.randint(1, 10))
        time.sleep(1)
