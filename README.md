# Space Telegram
The set of scripts for downloading space photos and posting it to telegram channel.

## Getting Started
Run appropriate script

```
python fetch_nasa_epic_images.py 2022/10/17
python fetch_nasa_epic_images.py
python fetch_nasa_images.py
python fetch_spacex_images.py
python image_posting.py spacex_6.jpg
python images_period_posting.py 0.5
```
### Prerequisites
1. Crete a bot in telegram using https://t.me/BotFather.
2. Create a channel in telegram.
3. Add your bot to your channel as administrator.
4. Create environment variables in "your_project_folder\.env" file:

   NASA_TOKEN=  <- generate your "API Key" on https://api.nasa.gov/
   
   TG_TOKEN= <- get token for your telegram bot from https://t.me/BotFather
   
   TG_CHANNEL= <- your tg channel to post images to, for example @MelSpaceImages
   
   POST_PERIOD=4 <- default period of posting images, hours
   
5. Python3 should be already installed.

   Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
   -> packages, listed in requirements should be successfully installed. 

### Usage
1. "fetch_nasa_epic_images.py" downloads image of current date to ".images" folder
   from https://epic.gsfc.nasa.gov/
    
   You may pass the argument date (YYYY-MM-DD) to download photos from specific date.
2. "fetch_nasa_images.py" downloads image of current date to ".images" folder
   from https://apod.nasa.gov/apod/astropix.html
   
   You may pass the argument date (YYYY-MM-DD) to download photos from specific date.
3. "fetch_spacex_images.py" downloads the latest image of SpaceX launch to .images folder
    
   You may pass the argument "id" to download photos of specific launch, example:
```
python fetch_spacex_images.py 5eb87d46ffd86e000604b388
```
   
After scripts 1-3 execution it prints success or fail message.

4. "images_period_posting.py" posts images from ".images" folder to "TG_CHANNEL"
   telegram channel every "POST_PERIOD" hours. When all images were posted, it starts posting the same
   images again in random sequence.
   
   You may change the period of posting by passing an argument "period" in hours.
5. "image_posting.py" posts "image.ext" from ".images" folder to "TG_CHANNEL" 
   telegram channel.
   Posts random image from ".image" folder if no arguments passed.
## Authors
* **Evgeny Melnikov** - *Initial work* - [Evgeny Melnikov](https://github.com/MelnikovEI)
## Acknowledgments
* Inspired by [Devman](https://dvmn.org/)