import argparse

import requests

from images_api import load_image, get_ext


def fetch_spacex_launch(launch_id: str = 'latest'):
    space_x_response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    space_x_response.raise_for_status()
    picture_links = space_x_response.json()['links']['flickr']['original']
    if picture_links:
        for i, picture_link in enumerate(picture_links):
            if picture_link:
                load_image(picture_link, f'spacex_{i}{get_ext(picture_link)}')
        return True
    else:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='downloads the latest image of SpaceX launch to ".images" folder.')
    parser.add_argument("id", nargs='?', help='id of specific launch', default='latest')
    args = parser.parse_args()
    if fetch_spacex_launch(args.id) is None:
        print("Process failed: Server didn't return expected information for downloading images")
