import argparse
import os
import random

import telegram
from dotenv import load_dotenv

from images_api import get_files_list, send_file_to_channel

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
    img_file = random.choice(get_files_list('images'))
send_file_to_channel(img_file, bot, chat_id)
