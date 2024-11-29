import requests
from rich.console import Console
from rich.table import Table
import os
import json

console = Console()

# Carregar chaves de API (se necessário)
def load_api_keys():
    api_keys = {}
    config_path = os.path.join(os.path.dirname(__file__), 'api_keys.json')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            api_keys = json.load(f)
    return api_keys

# Análise do perfil do GitHub usando a API pública
def analyze_github(username):
    console.print(f"[yellow]Analisando perfil do GitHub: {username}[/yellow]")
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            table = Table(title=f"Perfil de {data.get('login')}", show_lines=True)
            table.add_column("Atributo", style="cyan", no_wrap=True)
            table.add_column("Valor", style="magenta")

            table.add_row("Nome", data.get("name", "N/A"))
            table.add_row("Empresa", data.get("company", "N/A"))
            table.add_row("Localização", data.get("location", "N/A"))
            table.add_row("Bio", data.get("bio", "N/A"))
            table.add_row("Seguidores", str(data.get("followers", 0)))
            table.add_row("Seguindo", str(data.get("following", 0)))
            table.add_row("Repositórios Públicos", str(data.get("public_repos", 0)))
            table.add_row("URL", data.get("html_url", "N/A"))

            console.print(table)
        else:
            console.print("[red]Não foi possível acessar o perfil do GitHub.[/red]")
    except requests.RequestException as e:
        console.print(f"[red]Erro ao acessar a API do GitHub: {e}[/red]")

# Análise do perfil do Twitter usando a API pública
def analyze_twitter(username, api_key, api_secret_key, access_token, access_token_secret):
    console.print(f"[yellow]Analisando perfil do Twitter: {username}[/yellow]")
    # Implementação usando a biblioteca Tweepy
    try:
        import tweepy
    except ImportError:
        console.print("[red]A biblioteca 'tweepy' não está instalada. Instale usando 'pip install tweepy'.[/red]")
        return

    # Autenticação com as chaves da API
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(screen_name=username)
        table = Table(title=f"Perfil de @{user.screen_name}", show_lines=True)
        table.add_column("Atributo", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta")

        table.add_row("Nome", user.name)
        table.add_row("Localização", user.location or "N/A")
        table.add_row("Bio", user.description or "N/A")
        table.add_row("Seguidores", str(user.followers_count))
        table.add_row("Seguindo", str(user.friends_count))
        table.add_row("Tweets", str(user.statuses_count))
        table.add_row("URL", f"https://twitter.com/{user.screen_name}")

        console.print(table)
    except tweepy.TweepError as e:
        console.print(f"[red]Erro ao acessar a API do Twitter: {e}[/red]")

# Função principal para análise de um perfil
def analyze_profile(url):
    console.print(f"[yellow]📊 Analisando perfil: {url}[/yellow]\n")
    api_keys = load_api_keys()

    if "github.com" in url:
        username = url.rstrip('/').split('/')[-1]
        analyze_github(username)
    elif "twitter.com" in url:
        username = url.rstrip('/').split('/')[-1]
        # Verificar se as chaves da API do Twitter estão disponíveis
        required_keys = ["twitter_api_key", "twitter_api_secret_key", "twitter_access_token", "twitter_access_token_secret"]
        if all(key in api_keys for key in required_keys):
            analyze_twitter(
                username,
                api_key=api_keys["twitter_api_key"],
                api_secret_key=api_keys["twitter_api_secret_key"],
                access_token=api_keys["twitter_access_token"],
                access_token_secret=api_keys["twitter_access_token_secret"]
            )
        else:
            console.print("[red]Chaves da API do Twitter não encontradas. Atualize 'api_keys.json'.[/red]")
    else:
        console.print("[red]Análise para esta plataforma ainda não está implementada.[/red]")
