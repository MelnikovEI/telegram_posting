import argparse
import os
import random

import telegram
from dotenv import load_dotenv

from images_api import get_files_list, send_files_to_channel

load_dotenv()
token = os.environ['TG_TOKEN']
default_period = float(os.environ['POST_PERIOD'])

parser = argparse.ArgumentParser(description='Posts images from "image" folder to "@MelSpaceImages" telegram channel')
parser.add_argument("period", nargs='?', type=float, default=default_period,
                    help='Period of photo posting, hours (positive float number). Default = 4h.')
args = parser.parse_args()
period = float(args.period)*3600

bot = telegram.Bot(token=token)
chat_id = os.environ['TG_CHANNEL']

img_list = get_files_list('images')

send_files_to_channel(img_list, bot, chat_id, period)
while True:
    random.shuffle(img_list)
    send_files_to_channel(img_list, bot, chat_id, period)
