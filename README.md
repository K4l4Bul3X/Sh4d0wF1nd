ShadowFinder

ShadowFinder é uma ferramenta de linha de comando (CLI) desenvolvida em Python que permite rastrear perfis de usuários em várias plataformas de redes sociais. Inspirada no Sherlock, o ShadowFinder oferece funcionalidades avançadas, como integração com a rede Tor, busca por arquivos públicos associados a um nome de usuário e análises detalhadas de perfis utilizando APIs oficiais.

Índice

    Recursos
    Pré-requisitos
    Instalação
    Configuração
        Chaves de API (opcional)
        Rede Tor (opcional)
    Uso
        Buscar Perfis por Nome de Usuário
        Usar a Rede Tor para as Buscas
        Exportar Resultados
        Buscar Arquivos Públicos Associados ao Nome de Usuário
        Analisar um Perfil Específico
    Configurações Avançadas
    Contribuição
    Licença
    Aviso Legal

Recursos

    Busca Multiplataforma: Encontre perfis de usuários em diversas redes sociais simultaneamente.
    Integração com Tor: Realize buscas utilizando a rede Tor para aumentar a privacidade.
    Exportação de Resultados: Salve os resultados em formatos como JSON para análise posterior.
    Busca por Arquivos Públicos: Encontre repositórios e arquivos públicos associados a um nome de usuário.
    Análise Detalhada: Obtenha informações detalhadas de perfis usando APIs oficiais (ex.: GitHub, Twitter).
    Interface Intuitiva: CLI simples e fácil de usar, com comandos claros e diretos.

Pré-requisitos

    Python 3.6 ou superior.
    pip (gerenciador de pacotes do Python).

Instalação

    Clone o repositório:

git clone https://github.com/K4l4Bul3X/Sh4d0wF1nd3r
cd shadowfinder

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Unix ou MacOS:
source venv/bin/activate

Instale o pacote e as dependências:

    pip install --editable .

Configuração
Chaves de API (opcional)

Para utilizar funcionalidades que requerem acesso a APIs (como a análise detalhada do Twitter), você precisará fornecer suas chaves de API.

    Obtenha as chaves de API:
        Twitter: Crie uma conta de desenvolvedor no Portal de Desenvolvedores do Twitter e obtenha suas chaves de API.

    Crie o arquivo api_keys.json:

    No diretório shadowfinder/, crie um arquivo chamado api_keys.json com o seguinte conteúdo:

    {
      "twitter_api_key": "SUA_API_KEY",
      "twitter_api_secret_key": "SUA_API_SECRET_KEY",
      "twitter_access_token": "SEU_ACCESS_TOKEN",
      "twitter_access_token_secret": "SEU_ACCESS_TOKEN_SECRET"
    }

    Nota: Substitua os valores pelas suas chaves reais. Mantenha este arquivo seguro e não o compartilhe.

Rede Tor (opcional)

Para utilizar a rede Tor, certifique-se de que o Tor esteja instalado e em execução em sua máquina.

    Instalação no Ubuntu/Debian:

sudo apt-get update
sudo apt-get install tor

Iniciar o serviço Tor:

    sudo service tor start

Uso
Buscar Perfis por Nome de Usuário

shadowfinder search --username "nome_usuario"

Exemplo:

shadowfinder search --username "johndoe"

Usar a Rede Tor para as Buscas

shadowfinder search --username "nome_usuario" --tor

Exemplo:

shadowfinder search --username "johndoe" --tor

Exportar Resultados

Para exportar os resultados para um arquivo JSON:

shadowfinder search --username "nome_usuario" --export "resultados.json"

Exemplo:

shadowfinder search --username "johndoe" --export "johndoe_resultados.json"

Buscar Arquivos Públicos Associados ao Nome de Usuário

shadowfinder search_files --username "nome_usuario"

Exemplo:

shadowfinder search_files --username "johndoe"

Analisar um Perfil Específico

GitHub:

shadowfinder analyze --url "https://github.com/nome_usuario"

Twitter:

shadowfinder analyze --url "https://twitter.com/nome_usuario"

Exemplo:

shadowfinder analyze --url "https://github.com/johndoe"

Nota: Para a análise do Twitter, é necessário configurar as chaves de API conforme descrito na seção de configuração.
Configurações Avançadas

    Adicionar novas plataformas: Edite o arquivo config.json para adicionar ou remover plataformas de redes sociais a serem pesquisadas. Certifique-se de seguir o formato existente para garantir que a ferramenta funcione corretamente.

    Exemplo de config.json:

    {
      "platforms": {
        "Twitter": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}",
        "GitHub": "https://github.com/{username}",
        "LinkedIn": "https://www.linkedin.com/in/{username}",
        "Reddit": "https://www.reddit.com/user/{username}"
      }
    }

    Ajustar parâmetros de busca: Você pode modificar o número de threads, timeout e outras configurações diretamente no código ou implementando novas opções no CLI.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório do GitHub.

    Faça um fork do projeto

    Crie uma branch para sua feature ou correção de bug

git checkout -b minha-feature

Commit suas alterações

git commit -m "Minha nova feature"

Push para a branch

    git push origin minha-feature

    Abra um Pull Request

Licença

Este projeto está licenciado sob a MIT License.
Aviso Legal

O ShadowFinder é uma ferramenta destinada a fins educacionais e de pesquisa. O uso indevido desta ferramenta é estritamente proibido. Sempre respeite as leis locais e as políticas das plataformas utilizadas. O autor não se responsabiliza por qualquer uso inadequado ou ilegal desta ferramenta.
