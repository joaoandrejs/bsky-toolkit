from core import ui, painel, functions
import requests
from PIL import Image
from io import BytesIO
import os

def start():

    # while True:
    ui.clear()
    ui.logo()
    ui.title("Last.fm Collage\n")
    # URL da imagem
    
    handle = str(input('Qual o @ da conta no Last.FM (user)\n⤷  '))

    ui.title("Selecione")
    
    painel.painel(["Semaninha (7 Dias, 5x5)", "Mês (30 Dias, 10x10)", "Personalizar"], "Voltar")

    options = int(input('Selecione uma opção acima\n⤷  '))
    if options == 1:
        postar(handle, '7day', '5x5', f'Last.FM Colagem - Semaninha\nhttps://www.last.fm/user/{handle}')
    elif options == 2:
        postar(handle, '30day', '10x10', f'Last.FM Colagem - Mês\nhttps://www.last.fm/user/{handle}')
    else:
        ui.clear()
        ui.logo()
        ui.title("Personalizando colagem")

        painel.painel(["7 Dias", "1 Mês", "2 Mêses", "6 Mêses", "1 Ano", "Geral"], "Voltar")

        time = int(input('Selecione o tempo\n⤷  '))
        if time == 1: # 7 Dias
            time = '7day'
        elif time == 2: # 1 mes
            time = '1month'
        elif time == 3: # 3 meses
            time = '3month'
        elif time == 4:
            time = '6month'
        elif time == 5:
            time = '12month'
        elif time == 6:
            time = 'overall'
        else:
            return
        
        ui.title("Selecione o tamanho")

        painel.painel(["3x3", "4x4", "5x5", "10x10"], "Voltar")
        
        size = int(input('Selecione uma opção acima\n⤷  '))
        if size == 1:
            size = '3x3'
        elif size == 2:
            size = '4x4'
        elif size == 3:
            size = '5x5'
        elif size == 4:
            size = '10x10'

        mensagem = str(input('Digite a mensagem do post:\n⤷  '))
        
        postar(handle, time, size, mensagem)

def postar(handle, time, size, mensagem='Last.FM Collage'):
    try:
        url = f"https://tapmusic.net/collage.php?user={handle}&type={time}&size={size}&caption=true"

        # Salvando a imagem
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save("collage_image.png")
        
        image_path = os.path.abspath("collage_image.png")

        # Verifica se o arquivo existe antes de tentar deletá-lo
        if os.path.exists(image_path):
            # Remove a qualidade para ser postada no bluesky
            functions.reduce_image_quality(image_path, "collage_image_compressed.jpg", 60)
            os.remove(image_path)
            image_path = "collage_image_compressed.jpg"

            functions.image_post(image_path, mensagem, image_alt='Last.fm collage')
            
            os.remove(image_path)
    except Exception as ex:
        return ex