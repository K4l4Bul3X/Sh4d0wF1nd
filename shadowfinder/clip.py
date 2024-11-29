import click
from shadowfinder.search import find_profiles, find_public_files
from shadowfinder.analyze import analyze_profile
from shadowfinder.utils import validate_username, show_banner

@click.group()
def cli():
    """ShadowFinder: Ferramenta para rastrear perfis em redes sociais."""
    show_banner()

@cli.command()
@click.option('--username', '-u', required=True, help="Nome de usuário a ser pesquisado.")
@click.option('--tor', is_flag=True, help="Usar a rede Tor para realizar as buscas.")
@click.option('--export', '-o', help="Caminho do arquivo para exportar os resultados.")
def search(username, tor, export):
    """Busca perfis de redes sociais pelo nome de usuário."""
    if not validate_username(username):
        click.echo("[bold red]Nome de usuário inválido![/bold red]")
        return
    find_profiles(username, use_tor=tor, export_path=export)

@cli.command()
@click.option('--username', '-u', required=True, help="Nome de usuário a ser pesquisado.")
def search_files(username):
    """Busca por arquivos públicos associados ao nome de usuário."""
    if not validate_username(username):
        click.echo("[bold red]Nome de usuário inválido![/bold red]")
        return
    find_public_files(username)

@cli.command()
@click.option('--url', '-u', required=True, help="URL de perfil para análise detalhada.")
def analyze(url):
    """Analisa detalhes de um perfil."""
    analyze_profile(url)

if __name__ == "__main__":
    cli()
