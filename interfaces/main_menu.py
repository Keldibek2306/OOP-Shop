from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def home_manu():
    menu_text = """
[bold cyan]1.[/] 🔐 Kirish  
[bold cyan]2.[/] 📝 Ro'yxatdan o'tish  
[bold cyan]3.[/] ❌ Chiqish  
"""
    panel = Panel(
        menu_text,
        title="[bold magenta]🏠 HOME MENU",
        box=box.ROUNDED,
        border_style="bright_magenta"
    )
    console.print(panel)

def main_menu():
    menu_text = """
[bold cyan]1.[/] Mahsulotlar  
[bold cyan]2.[/] Profile  
[bold cyan]3.[/] ❌ Chiqish  
"""
    panel = Panel(
        menu_text,
        title="[bold magenta]🏠 MAIN MENU",
        box=box.ROUNDED,
        border_style="bright_magenta"
    )
    console.print(panel)
    console.print("\n[bold green]Iltimos, menyudan tanlov qiling:[/]\n")
    console.print("1 - Mahsulotlar ro'yxatini ko'rish")
    console.print("2 - Profilga o'tish")
    console.print("3 - Chiqish")
    console.print("\n[bold yellow]Tanlovingizni kiriting:[/]\n")
    console.print(">>> ", end="")
    console.print("\n[bold red]Eslatma:[/] Agar sizda mahsulotlar mavjud bo'lmasa, ularni qo'shishingiz kerak.")
    console.print("\n[bold blue]Yangi mahsulot qo'shish uchun '2'[/]\n")
    console.print("[bold blue]Chiqish uchun '3'[/]\n")  
    console.print("\n[bold green]Iltimos, tanlovingizni kiriting:[/]\n")
    console.print(">>> ", end="")
