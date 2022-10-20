import argparse
import os

import requests
from dotenv import load_dotenv

from images_api import load_image, get_ext


def fetch_spacex_launch(id: str = ''):
    if id:
        space_x_response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
        print('by id')
    else:
        space_x_response = requests.get("https://api.spacexdata.com/v5/launches/latest")
        print('latest')
    space_x_response.raise_for_status()
    picture_links = space_x_response.json().get('links').get('flickr').get('original')
    for i, picture_link in enumerate(picture_links):
        if picture_link:
            load_image(picture_link, './images', f'spacex_{i}{get_ext(picture_link)}')


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("id", nargs='?')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)
    # 5eb87d42ffd86e000604b384
