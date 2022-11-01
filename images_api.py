import os
import time
import urllib
from pathlib import Path

import requests
import telegram
from retry import retry


def load_image(url, file_name, params=None):
    Path(Path.cwd() / 'images').mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(Path.cwd() / 'images' / file_name, 'wb') as file_to_save:
        file_to_save.write(response.content)


def get_ext(url: str) -> str:
    split_url = urllib.parse.urlsplit(url)
    split_path = os.path.split(split_url.path)
    split_file_name = os.path.splitext(split_path[1])
    return split_file_name[1]


def get_files_list(folder: str) -> list:
    files_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list


@retry(telegram.error.NetworkError, delay=1, backoff=2, max_delay=30)
def send_file_to_channel(file_name: str, bot: telegram.Bot, chat_id: str):
    with open(file_name, 'rb') as file_to_send:
        bot.send_document(chat_id=chat_id, document=file_to_send)


def send_files_to_channel(files_list, bot, chat_id, period):
    for file_name in files_list:
        send_file_to_channel(file_name, bot, chat_id)
    time.sleep(period)
