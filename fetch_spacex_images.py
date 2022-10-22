import argparse

import requests

from images_api import load_image, get_ext


def fetch_spacex_launch(id: str = ''):
    if id:
        space_x_response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    else:
        space_x_response = requests.get("https://api.spacexdata.com/v5/launches/latest")
    space_x_response.raise_for_status()
    picture_links = space_x_response.json().get('links').get('flickr').get('original')
    for i, picture_link in enumerate(picture_links):
        if picture_link:
            load_image(picture_link, './images', f'spacex_{i}{get_ext(picture_link)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='downloads the latest image of SpaceX launch to ".images" folder.')
    parser.add_argument("id", nargs='?', help='id of specific launch')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)
