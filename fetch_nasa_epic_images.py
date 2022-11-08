import argparse
import os
import datetime

import requests
from dotenv import load_dotenv

from images_api import load_image


def get_nasa_epic_img_links(token: str, date: str = ''):
    params = {
        'api_key': token,
    }
    nasa_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params=params)
    nasa_response.raise_for_status()
    return nasa_response.json()


def fetch_nasa_epic_image(token: str, img_item_date: str):
    params = {
        'api_key': token,
    }
    img_datetime = datetime.datetime.strptime(img_item_date, '%Y-%m-%d %H:%M:%S')
    img_date = img_datetime.date()
    str_img_date = img_date.strftime('%Y/%m/%d')
    img_link = f"https://api.nasa.gov/EPIC/archive/natural/{str_img_date}/png/{img_name}.png"
    load_image(img_link, f'nasa_epic_{i}.png', params)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(description="downloads image of current date to '.images' folder "
                                                 "from https://epic.gsfc.nasa.gov/. ")
    parser.add_argument("date", nargs='?', default='', help="pass the argument (YYYY-MM-DD) to download photos "
                                                            "from specific date")
    args = parser.parse_args()

    nasa_epic_links = get_nasa_epic_img_links(token, args.date)
    if nasa_epic_links is None:
        print("Process failed: Server didn't return expected information for downloading images")
    for i, img_item in enumerate(nasa_epic_links):
        img_name = img_item['image']
        img_item_date = img_item.get('date')
        fetch_nasa_epic_image(token, img_item_date)
