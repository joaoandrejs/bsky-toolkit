from colorama import Fore
from core import ui, painel
from atproto import models
import requests
from PIL import Image
from io import BytesIO
import os
from main import client

def reduce_image_quality(image_path, output_path, quality=70):
    # Abre a imagem existente
    img = Image.open(image_path)
    
    # Salva a imagem com a qualidade especificada (de 1 a 100)
    img.save(output_path, "JPEG", quality=quality)
    
    return os.path.abspath(output_path)

def image_post(image_path, mensagem="Posted by bluesky toolkit", image_alt='Alt image'):
    try:

        # Verifica se o arquivo existe antes de tentar postar
        if os.path.exists(image_path):
            
            with open(image_path, 'rb') as f:
                img_data = f.read()
                
                upload = client.upload_blob(img_data)
                images = [models.AppBskyEmbedImages.Image(alt=image_alt, image=upload.blob)]
                embed = models.AppBskyEmbedImages.Main(images=images)

                client.com.atproto.repo.create_record(
                    models.ComAtprotoRepoCreateRecord.Data(
                        repo=client.me.did,
                        collection=models.ids.AppBskyFeedPost,
                        record=models.AppBskyFeedPost.Record(
                            created_at=client.get_current_time_iso(), 
                            text=mensagem,
                            embed=embed
                        ),
                    )
                )
    except Exception as ex:
        return ex

def post():
    
    ui.clear()
    ui.logo()
    ui.title("Criando postagem\n")

    while True:

        text = input(f"Digite a mensagem da postagem: {Fore.LIGHTBLACK_EX}(0 p/ cancelar{Fore.RESET})\n⤷  ")
        if text == '0':
            break

        if len(text) < 1:
            ui.error("Você não quer dizer nada?")
            continue
        
        ui.clear()

        print(f"""
\'\'\'
{text}
\'\'\'
              """)
        
        painel.painel(["Postar"], "Cancelar")

        question = int(input("⤷  "))
        if question == 1:
            try:
                post = client.send_post(text)
                client.like(post.uri, post.cid)
            except Exception as Ex:
                return ui.error(Ex)
            break
        else:
            break