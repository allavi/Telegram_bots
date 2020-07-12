import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import cats_api
import bot_api

with open("token.txt") as file:
    bot_token = file.readline()

tg_url = "https://api.telegram.org/bot" + bot_token
cat_url = "https://api.thecatapi.com/v1/images/search"

tg_bot = bot_api.Telegram_bot(tg_url)
cat_image = cats_api.Cats(cat_url)

while True:
    last_update = tg_bot.getLastUpdates(timeout=60)
    if last_update != None:
        last_chat_id = last_update['message']['chat']['id']
        if last_update['message']['text'].lower() == "cat":
            cat_image.search()
            tg_bot.sendPhoto(last_chat_id, cat_image.get_img_url())