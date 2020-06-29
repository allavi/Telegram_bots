import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import cats_api
import bot_api

tg_bot = bot_api.Telegram_bot()
cat_image = cats_api.Cats()

cat_image

