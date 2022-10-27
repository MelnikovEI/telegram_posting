import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv

from images_api import get_img_list

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

img_list = get_img_list()

first_reconnection = True
for img_file in img_list:
    with open(img_file, 'rb') as file_to_send:
        while True:
            try:
                bot.send_document(chat_id=chat_id, document=file_to_send)
            except telegram.error.NetworkError:
                if first_reconnection:
                    first_reconnection = False
                    time.sleep(1)
                else:
                    time.sleep(10)
                #bot = telegram.Bot(token=token)
            else:
                break
    time.sleep(period)
while True:
    random.shuffle(img_list)
    for img_file in img_list:
        with open(img_file, 'rb') as file_to_send:
            bot.send_document(chat_id=chat_id, document=file_to_send)
        time.sleep(period)
