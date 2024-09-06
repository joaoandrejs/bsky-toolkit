from atproto import Client
from colorama import Fore
from core import ui, painel
import sys
import os
from dotenv import load_dotenv
load_dotenv()

try:
    EMAIL = os.getenv("EMAIL")
    SENHA = os.getenv("SENHA")

    client = Client()
    profile = client.login(EMAIL, SENHA)
except Exception as ex:
    ui.error("Email ou senha inválido. Erro ao acessar esta conta")
    sys.exit()

def main():
    ui.title('TOOLKIT\n')
    ui.title(f'Logado em: {profile.display_name} (@{profile.handle})\n')
    
    print(f'Status atual:\n\nSeguidores: {profile.followers_count}\nSeguindo: {profile.follows_count}\nPosts: {profile.posts_count}')
    
    painel.painel(["Ferramentas"], "Sair")
    
    iniciar = int(input('⤷  '))

    if iniciar == 1:
        painel.start()
    else:
        ui.title(f"{Fore.GREEN}Volte sempre ;) {Fore.RESET}")
        sys.exit()

if __name__ == '__main__':
    ui.clear()

    while True:
        try:
            ui.logo()
            main()

        except Exception as ex:
            ui.clear()
            ui.title(f'{Fore.RED}Ocorreu um erro, tente novamente!\n{ex}')
            continue