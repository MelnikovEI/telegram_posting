import argparse
import os

import requests
from dotenv import load_dotenv

from images_api import load_image, get_ext


def fetch_nasa_image(token: str, date: str=''):
    params = {
        'api_key': f"{token}",
    }
    if date:
        params.update({'date': f"{date}"})
    nasa_response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    nasa_response.raise_for_status()
    img_item = nasa_response.json()
    img_link = img_item.get('hdurl')
    if img_link:
        load_image(img_link, './images', f'nasa_apod{get_ext(img_link)}')


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("date", nargs='?')
    args = parser.parse_args()
    fetch_nasa_image(token, args.date)
