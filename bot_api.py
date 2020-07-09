import requests
import json


class Telegram_bot(object):
    """Telegram bot API"""

    def __init__(self, url):
        self.api_url = url
        self.updates_offset = None

    def getUpdates(self, offset=None, limit=100, timeout=0, allowed_updates=[]):
        params = {'offset': offset, 'limit': limit,
                  'timeout': timeout, 'allowed_updates': allowed_updates}
        response = requests.get(self.api_url + '/getUpdates', data=params)
        return response.json()

    def getLastUpdates(self):
        self.resp = self.getUpdates(offset=self.updates_offset, timeout=2)
        if(len(self.resp['result']) != 0):
            self.updates_offset = self.resp['result'][len(self.resp['result'])-1]['update_id'] + 1
            return self.resp['result'][len(self.resp['result'])-1]
        else:
            return None

    def setWebhook(self, certificate="", max_connections=40, allowed_updates=[]):
        params = {'certificate': certificate, 'max_connections': max_connections,
                  'allowed_updates': allowed_updates}
        response = requests.get(self.api_url + '/setWebhook', data=params)
        return response.json()

    def deleteWebhook(self):
        pass

    def getWebhookInfo(self):
        pass

    def WebhookInfo(self, url, has_custom_certificate, pending_update_count, 
                    last_error_date, last_error_message, max_connections, 
                    allowed_updates):
        pass

    def User(self, id, is_bot, first_name, last_name="", username="", 
             language_code="", can_join_groups=True, 
             can_read_all_group_messages=False, supports_inline_queries=True):
        params = {'id': id, 'is_bot': is_bot, 'first_name': first_name,
                  'last_name': last_name, 'username': username}
        response = requests.get(self.api_url + '/User', data=params)
        return response.json()

    def Chat(self, id, type, title, username, first_name, last_name, 
             photo, description, invite_link, pinned_message, 
             permissions, slow_mode_delay, sticker_set_name, can_set_sticker_set):
        pass

    def sendMessage(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.api_url + '/sendMessage', data=params)
        return response.json()

    def sendPhoto(self, chat_id, photo, photo_url=True):
        """ if photo_url == True argument photo must be an url else arg photo must be a file """
        files = {'photo': photo}
        if photo_url:
            params = {'chat_id': chat_id, 'photo': photo}
            response = requests.post(self.api_url + '/sendPhoto', data=params)
        else:
            params = {'chat_id': chat_id}
            response = requests.post(self.api_url + '/sendPhoto', data=params, files=files)
        return response.json()


if __name__ == '__main__':
    with open("Cats/token.txt") as file:
        api_token = file.readline()

    url = "https://api.telegram.org/bot" + api_token

    test_text = None

    bot = Telegram_bot(url)

    while test_text != 'ABC':
        last_update = bot.getLastUpdates()
        print(last_update)
        if last_update != None:
            last_chat_id = last_update['message']['chat']['id']
            bot.sendMessage(last_chat_id, last_update['message']['text'])
            bot.sendPhoto(last_chat_id, "https://cdn2.thecatapi.com/images/ba.jpg")
            test_text = last_update['message']['text']