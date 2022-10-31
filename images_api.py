import os
import urllib
from pathlib import Path

import requests


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


def get_img_list() -> list:
    img_list = []
    for root, dirs, files in os.walk('images'):
        for file in files:
            img_list.append(os.path.join(root, file))
    return img_list
