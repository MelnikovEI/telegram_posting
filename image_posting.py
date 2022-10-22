import argparse
import os
import random

import telegram
from dotenv import load_dotenv


load_dotenv()
token = os.environ['TG_TOKEN']
bot = telegram.Bot(token=token)
chat_id = os.environ['TG_CHANNEL']

parser = argparse.ArgumentParser(description='Posts "image.ext" from ".images" folder to "@MelSpaceImages"'
                                             'telegram channel. '
                                             'Posts random image from ".images" folder if no arguments passed')
parser.add_argument("post_file", nargs='?', help='name of image file "image.ext" to post')
args = parser.parse_args()
post_file = args.post_file

if post_file:
    img_file = os.path.join("images", post_file)
else:
    img_list = []
    for root, dirs, files in os.walk('images'):
        for file in files:
            img_list.append(os.path.join(root, file))
    img_file = random.choice(img_list)
bot.send_document(chat_id=chat_id, document=open(img_file, 'rb'))
