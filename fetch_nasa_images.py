import argparse
import os

import requests
from dotenv import load_dotenv

from images_api import load_image, get_ext


def fetch_nasa_image(token: str, date: str = ''):
    params = {
        'api_key': token,
    }
    if date:
        params.update({'date': f"{date}"})
    nasa_response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    nasa_response.raise_for_status()
    img_item = nasa_response.json()
    img_link = img_item['hdurl']
    if img_link:
        load_image(img_link, f'nasa_apod{get_ext(img_link)}')
        return "Process finished"
    else:
        return "Process failed: Server didn't return expected information for downloading images"


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(description="downloads image of current date to '.images' folder "
                                                 "from https://apod.nasa.gov/apod/astropix.html")
    parser.add_argument("date", nargs='?', help="Pass the date (YYYY-MM-DD) to download photos from specific date")
    args = parser.parse_args()
    print(fetch_nasa_image(token, args.date))
