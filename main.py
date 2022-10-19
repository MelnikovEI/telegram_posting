import datetime
import os.path
import random
import urllib.parse

import requests
from pathlib import Path
from dotenv import load_dotenv


def load_image(url, save_path, file_name):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{save_path}/{file_name}', 'wb') as file_to_save:
        file_to_save.write(response.content)


def get_ext(url: str) -> str:
    split_url = urllib.parse.urlsplit(url)
    split_path = os.path.split(split_url.path)
    split_file_name = os.path.splitext(split_path[1])
    return split_file_name[1]


def fetch_spacex_last_launch():
    space_x_response = requests.get("https://api.spacexdata.com/v5/launches/latest")
    space_x_response.raise_for_status()
    picture_links = space_x_response.json().get('links').get('flickr').get('original')
    for i, picture_link in enumerate(picture_links):
        if picture_link:
            load_image(picture_link, './images', f'spacex_{i}{get_ext(picture_link)}')


def fetch_nasa_apod(token: str):
    params = {
        'api_key': f"{token}",
        'count': 5
    }
    nasa_response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    nasa_response.raise_for_status()
    for i, img_item in enumerate(nasa_response.json()):
        img_link = img_item.get('hdurl')
        if img_link:
            load_image(img_link, './images', f'nasa_apod_{i}{get_ext(img_link)}')


def fetch_nasa_epic(token: str):
    params = {
        'api_key': f"{token}",
    }
    nasa_response = requests.get("https://api.nasa.gov/EPIC/api/natural", params=params)
    nasa_response.raise_for_status()
    rand_responses = random.choices(nasa_response.json(), k=5)
    for i, img_item in enumerate(rand_responses):
        img_name = img_item.get('image')
        img_date = datetime.datetime.strptime(img_item.get('date'), '%Y-%m-%d %H:%M:%S').date()
        str_img_date = img_date.strftime('%Y/%m/%d')
        img_link = f"https://api.nasa.gov/EPIC/archive/natural/{str_img_date}/png/{img_name}.png" \
                   f"?api_key={params['api_key']}"
        load_image(img_link, './images', f'nasa_epic_{i}.png')


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_spacex_last_launch()
    fetch_nasa_apod(token)
    fetch_nasa_epic(token)
