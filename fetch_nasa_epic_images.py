import argparse
import os
import datetime

import requests
from dotenv import load_dotenv

from images_api import load_image


def fetch_nasa_epic_image(token: str, date: str=''):
    params = {
        'api_key': f"{token}",
    }
    nasa_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params=params)
    nasa_response.raise_for_status()
    for i, img_item in enumerate(nasa_response.json()):
        img_name = img_item.get('image')
        img_date = datetime.datetime.strptime(img_item.get('date'), '%Y-%m-%d %H:%M:%S').date()
        str_img_date = img_date.strftime('%Y/%m/%d')
        img_link = f"https://api.nasa.gov/EPIC/archive/natural/{str_img_date}/png/{img_name}.png" \
                   f"?api_key={params['api_key']}"
        load_image(img_link, './images', f'nasa_epic_{i}.png')


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument("date", nargs='?', default='')
    args = parser.parse_args()
    fetch_nasa_epic_image(token, args.date)
