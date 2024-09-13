from colorama import Fore
from core import ui
from atproto import models
from PIL import Image
import os
from main import client


def painel(items, sair='Sair'):
    formatted_items = [
        f"{Fore.GREEN}[{index+1}]{Fore.WHITE} {item}"
        for index,
        item in enumerate(items)
    ]
    result = "\n".join(formatted_items)

    print(f"""{result}
{Fore.RED}[0]{Fore.WHITE} {sair}\n""")


def input_text(text, text2=''):
    b = Fore.BLUE
    c = Fore.WHITE

    if (len(text2) >= 1):
        text2 = f'{b}({c}{text2}{b}){c}'

    text = f'''{b}┌[{c}{text}{b}]{c} {text2}
{b}└>{c}  '''
    return text


def reduce_image_quality(image_path, output_path, quality=70):
    # Abre a imagem existente
    img = Image.open(image_path)

    # Salva a imagem com a qualidade especificada (de 1 a 100)
    img.save(output_path, "JPEG", quality=quality)

    return os.path.abspath(output_path)


def image_post(image_path,
               mensagem="Posted by Bluesky Toolkit",
               image_alt='Posted by Bluesky Toolkit'):
    try:

        # Verifica se o arquivo existe antes de tentar postar
        if os.path.exists(image_path):

            with open(image_path, 'rb') as f:
                img_data = f.read()

                upload = client.upload_blob(img_data)
                images = [models.AppBskyEmbedImages.Image(
                        alt=image_alt,
                        image=upload.blob)]
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


def text_post(text):
    try:
        post = client.send_post(text)
        client.like(post.uri, post.cid)
    except Exception as Ex:
        return ui.centralized(f"{Fore.RED}{Ex}")


def delete_post(post_uri):
    client.delete_post(post_uri)
