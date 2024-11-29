import re
from rich.console import Console

console = Console()

# Validação de nome de usuário
def validate_username(username):
    if re.match(r"^[a-zA-Z0-9_]{3,30}$", username):
        return True
    return False

# Função para exibir o banner
def show_banner():
    banner = """
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██████╗ ███╗   ██╗███████╗██╗██████╗ 
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗
█████╗  ███████║███████║██████╔╝██║     ██║   ██║██╔██╗ ██║█████╗  ██║██████╔╝
██╔══╝  ██╔══██║██╔══██║██╔═══╝ ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██╔═══╝ 
███████╗██║  ██║██║  ██║██║     ╚██████╗╚██████╔╝██║ ╚████║███████╗██║██║     
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝     

       [bold white]Unveiling the Shadows of the Digital World[/bold white]
    """
    console.print(f"[bold red]{banner}[/bold red]")
