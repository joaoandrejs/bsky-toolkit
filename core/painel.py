from core import ui, functions as funcs, lastfm
from colorama import Fore

def painel(items, sair='Sair'):
    formatted_items = [f"{Fore.GREEN}[{index+1}]{Fore.RESET} {item}" for index, item in enumerate(items)]
    result = "\n".join(formatted_items)

    print(f"""{result}
{Fore.RED}[0]{Fore.WHITE} {sair}\n""")
    

def start():
    while True:
        ui.clear()
        ui.logo()
        ui.title("TOOLKIT PAINEL")

        painel(["Fazer um post", "Last.FM Collage", "Skicircle"], "Voltar")
        
        question = int(input('Selecione uma opção acima\n⤷  '))
        
        if question == 0:
            ui.clear()
            break
        elif question == 1:
            funcs.post()
        elif question == 2:
            lastfm.start()
        else:
            ui.clear()
            ui.error('Ocorreu um erro, tente novamente por favor!')
            break