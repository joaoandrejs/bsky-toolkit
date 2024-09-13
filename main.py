from atproto import Client
from colorama import Fore
from core import ui, functions as funcs
import requests
from PIL import Image
from io import BytesIO
import sys
import os
from dotenv import load_dotenv
load_dotenv()

try:
    EMAIL = os.getenv("EMAIL")
    SENHA = os.getenv("SENHA")

    client = Client()
    profile = client.login(EMAIL, SENHA)

except KeyError as e:
    ui.clear()
    text = f"Missing environment variable: {str(e)}"
    ui.centralized(f"{Fore.RED} {text}")
    sys.exit()

except Exception as e:
    ui.clear()
    text = f'Email ou senha inválido. Erro ao acessar esta conta:\n{str(e)}'
    ui.centralized(f"{Fore.RED} {text}")
    sys.exit()


def main():
    input_text = funcs.input_text

    ui.centralized(f'{Fore.BLUE}TOOLKIT\n')
    ui.centralized(f'Account: {profile.display_name} (@{profile.handle})\n')

    print(f'''Status atual:
Seguidores: {profile.followers_count}
Seguindo: {profile.follows_count}
Posts: {profile.posts_count}''')

    funcs.painel(["Ferramentas"], "Sair")

    iniciar = int(input(input_text('Selecione uma opção acima')))
    cancel_text = f"{Fore.LIGHTBLACK_EX}0 p/ cancelar{Fore.RESET}"

    if iniciar == 1:
        while True:
            ui.clear()
            ui.logo()
            ui.centralized(f"{Fore.BLUE}TOOLKIT PAINEL")

            funcs.painel(["Fazer um post",
                          "Last.FM Collage",
                          "Skicircle"], "Voltar")

            question = int(input(input_text('Selecione uma opção acima')))

            if question == 0:
                ui.clear()
                break

            elif question == 1:

                while True:
                    ui.clear()
                    ui.logo()
                    ui.centralized(f"{Fore.BLUE}Criando postagem\n")

                    text = input(input_text('Digite a mensagem da postagem',
                                            cancel_text))

                    if text == '0':
                        break
                    else:

                        if len(text) < 1:
                            ui.centralized(Fore.RED +
                                           "Você não quer dizer nada?")
                            continue

                        ui.clear()

                        print(f"""\'\'\'
{text}
\'\'\'""")

                        funcs.painel(["Postar"], "Cancelar")

                        question = int(input(
                            input_text('Selecione uma opção acima')))

                        if question == 1:
                            funcs.text_post(text)

                            ui.centralized(f"{Fore.BLUE} Post feito.")

                            funcs.painel([], "Voltar")
                            question2 = int(
                                input(input_text('Selecione uma opção acima')
                                      ))

                            if question2:
                                break

                        else:
                            break

            elif question == 2:

                def postar(handle, time, size, mensagem='Last.FM Collage'):
                    try:
                        url = (
                            f"https://tapmusic.net/collage.php?user={handle}"
                            f"&type={time}&size={size}&caption=true"
                        )

                        # Salvando a imagem
                        response = requests.get(url)
                        img = Image.open(BytesIO(response.content))
                        img.save("collage_image.png")

                        image_path = os.path.abspath("collage_image.png")

                        # Remove a qualidade para ser postada no bluesky
                        if os.path.exists(image_path):
                            newname = "collage_image_compressed.jpg"
                            funcs.reduce_image_quality(image_path, newname, 60)
                            os.remove(image_path)
                            image_path = "collage_image_compressed.jpg"

                            funcs.image_post(image_path,
                                             mensagem,
                                             image_alt='Last.fm collage')

                            os.remove(image_path)
                    except Exception as ex:
                        return ex

                while True:
                    ui.clear()
                    ui.logo()
                    ui.centralized(f"{Fore.BLUE}Last.fm Collage\n")
                    # URL da imagem

                    handle = str(input(input_text('Seu @ do last.fm',
                                                  cancel_text)))

                    if handle == '0':
                        break

                    ui.centralized(f"{Fore.BLUE}Selecione")

                    funcs.painel(["Semaninha (7 Dias, 5x5)",
                                  "Mês (30 Dias, 10x10)",
                                  "Personalizar"
                                  ], "Voltar")

                    options = int(input(
                                input_text('Selecione uma opção acima')
                                ))
                    link = f'last.fm/user/{handle}/'
                    if options == 0:
                        break
                    elif options == 1:
                        postar(handle,
                               '7day',
                               '5x5',
                               f'Last.FM Colagem - Semaninha\n{link}')

                    elif options == 2:
                        postar(handle,
                               '30day',
                               '10x10',
                               f'Last.FM Colagem - Mês\n{link}')
                    else:
                        ui.clear()
                        ui.logo()
                        ui.centralized(f"{Fore.BLUE}Personalizando colagem")

                        funcs.painel(["7 Dias",
                                      "1 Mês",
                                      "2 Mêses",
                                      "6 Mêses",
                                      "1 Ano",
                                      "Geral"], "Voltar")

                        time = int(
                                input(
                                    input_text('Selecione uma opção acima')
                                    ))
                        if time == 0:
                            break
                        elif time == 1:
                            time = '7day'
                        elif time == 2:
                            time = '1month'
                        elif time == 3:
                            time = '3month'
                        elif time == 4:
                            time = '6month'
                        elif time == 5:
                            time = '12month'
                        elif time == 6:
                            time = 'overall'
                        else:
                            break

                        ui.centralized(f"{Fore.BLUE}Selecione o tamanho")

                        funcs.painel(["3x3", "4x4", "5x5", "10x10"], "Voltar")

                        size = int(input(
                                   input_text('Selecione uma opção acima')
                                   ))

                        if size == 0:
                            break
                        elif size == 1:
                            size = '3x3'
                        elif size == 2:
                            size = '4x4'
                        elif size == 3:
                            size = '5x5'
                        elif size == 4:
                            size = '10x10'
                        else:
                            break

                        mensagem = str(
                                    input(
                                        input_text('Digite a mensagem do post')
                                        )
                                    )

                        postar(handle, time, size, mensagem)

                    ui.centralized(f"{Fore.BLUE} Post feito.")

                    # funcs.painel([], "Voltar")
                    input(input_text('Pressione enter para voltar'))
                    break

            else:
                ui.clear()
                ui.centralized(f'{Fore.RED}Ocorreu um erro, tente novamente!')
                break

    else:
        ui.centralized(f"{Fore.GREEN}Volte sempre ;) {Fore.RESET}")
        sys.exit()


if __name__ == '__main__':
    ui.clear()

    while True:
        try:
            ui.logo()
            main()

        except Exception as ex:
            ui.clear()
            ui.centralized(f"{Fore.RED}Ocorreu um erro.\n{str(ex)}")
            continue
