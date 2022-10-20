import datetime
import os.path
import random

import requests
from dotenv import load_dotenv


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
