import telegram


bot = telegram.Bot(token='5788361372:AAHAUGNM1v7QNNHZRuV1C4f-c7nssUxhcNg')
print(bot.get_me())
print(bot.get_updates()[-1])
chat_id = '@MelSpaceImages'
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
