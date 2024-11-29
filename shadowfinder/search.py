import requests
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor
import json
import os

console = Console()

# Função para carregar as plataformas do arquivo config.json
def load_platforms():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config['platforms']

# Função para obter uma sessão de requests, com ou sem Tor
def get_session(use_tor=False):
    session = requests.Session()
    if use_tor:
        session.proxies = {
            'http': 'socks5h://localhost:9050',
            'https': 'socks5h://localhost:9050'
        }
    return session

# Função para verificar um perfil em uma plataforma
def check_profile(platform, url, session):
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            return platform, url
    except requests.RequestException as e:
        console.log(f"[red]Erro ao verificar {url}: {e}[/red]")
    return platform, None

# Função principal para buscar perfis
def find_profiles(username, use_tor=False, export_path=None):
    platforms = load_platforms()
    results = {}
    session = get_session(use_tor)
    console.print(f"[yellow]🔍 Iniciando busca para '{username}'...[/yellow]\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for platform, url_template in platforms.items():
            url = url_template.format(username=username)
            futures.append(executor.submit(check_profile, platform, url, session))

        for future in futures:
            platform, url = future.result()
            if url:
                results[platform] = url

    if results:
        console.print("[green]✅ Perfis encontrados:[/green]")
        for platform, url in results.items():
            console.print(f"[cyan][{platform}][/cyan] {url}")
    else:
        console.print("[red]Nenhum perfil encontrado![/red]")

    if export_path:
        with open(export_path, 'w') as f:
            json.dump(results, f)
        console.print(f"[green]Resultados exportados para {export_path}[/green]")

    return results

# Função para buscar arquivos públicos associados ao nome de usuário
def find_public_files(username):
    console.print(f"[yellow]🔍 Buscando arquivos públicos para '{username}'...[/yellow]\n")
    # Exemplo usando a API do GitHub
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            if repos:
                console.print("[green]✅ Repositórios encontrados:[/green]")
                for repo in repos:
                    console.print(f"[cyan]{repo['name']}[/cyan]: {repo['html_url']}")
            else:
                console.print("[red]Nenhum repositório público encontrado![/red]")
        else:
            console.print("[red]Não foi possível acessar a API do GitHub.[/red]")
    except requests.RequestException as e:
        console.log(f"[red]Erro ao acessar a API do GitHub: {e}[/red]")
