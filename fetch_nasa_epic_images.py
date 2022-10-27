import argparse
import os
import datetime

import requests
from dotenv import load_dotenv

from images_api import load_image


def fetch_nasa_epic_image(token: str, date: str = ''):
    params = {
        'api_key': f"{token}",
    }
    nasa_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params=params)
    nasa_response.raise_for_status()
    if not nasa_response.json():
        return "No images were delivered by this request"
    for i, img_item in enumerate(nasa_response.json()):
        img_name = img_item.get('image')
        if img_name:
            img_date = datetime.datetime.strptime(img_item.get('date'), '%Y-%m-%d %H:%M:%S').date()
            str_img_date = img_date.strftime('%Y/%m/%d')
            img_link = f"https://api.nasa.gov/EPIC/archive/natural/{str_img_date}/png/{img_name}.png"
            load_image(img_link, f'nasa_epic_{i}.png', params)
            return "Process finished"
        else:
            return "Process failed: Server didn't return expected information for downloading images"


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(description="downloads image of current date to '.images' folder "
                                                 "from https://epic.gsfc.nasa.gov/. ")
    parser.add_argument("date", nargs='?', default='', help="pass the argument (YYYY-MM-DD) to download photos "
                                                            "from specific date")
    args = parser.parse_args()
    print(fetch_nasa_epic_image(token, args.date))
