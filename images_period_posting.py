import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


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
img_list = []
for root, dirs, files in os.walk('images'):
    for file in files:
        img_file = os.path.join(root, file)
        img_list.append(img_file)
        bot.send_document(chat_id=chat_id, document=open(img_file, 'rb'))
        time.sleep(period)
while True:
    random.shuffle(img_list)
    for img_file in img_list:
        bot.send_document(chat_id=chat_id, document=open(img_file, 'rb'))
        time.sleep(period)
