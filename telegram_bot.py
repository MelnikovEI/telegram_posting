import telegram


bot = telegram.Bot(token='5788361372:AAHAUGNM1v7QNNHZRuV1C4f-c7nssUxhcNg')
print(bot.get_me())
print(bot.get_updates()[-1])
chat_id = '@MelSpaceImages'
#bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
#bot.send_document(chat_id=chat_id, document=open('images/nasa_apod.png', 'rb'))
#bot.send_photo(chat_id=chat_id, document=open('images/nasa_apod.png', 'rb'))
media_1 = telegram.InputMediaDocument(media=open('images/nasa_apod.png', 'rb'))
bot.send_media_group(chat_id=chat_id, media=[media_1])
