import argparse

import requests

from images_api import load_image, get_ext


def get_spacex_links(launch_id: str = 'latest') -> [str]:
    space_x_response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    space_x_response.raise_for_status()
    return space_x_response.json()['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser(description='downloads the latest image of SpaceX launch to ".images" folder.')
    parser.add_argument("id", nargs='?', help='id of specific launch', default='latest')
    args = parser.parse_args()
    picture_links = get_spacex_links(args.id)
    if picture_links:
        for seq_number, picture_link in enumerate(picture_links):
            if picture_link:
                load_image(picture_link, f'spacex_{seq_number}{get_ext(picture_link)}')
    else:
        print("Process failed: Server didn't return expected images links")


if __name__ == '__main__':
    main()
