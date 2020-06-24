import requests
import json

url = "YOUR URL"

class Telegram_bot(object):
    """Telegram bot API"""

    def __init__(self, url):
        self.api_url = url

    def getUpdates(self, offset=None, limit=100, timeout=0, allowed_updates=[]):
        params = {'offset': offset, 'limit': limit,
                  'timeout': timeout, 'allowed_updates': allowed_updates}
        response = requests.get(self.api_url + 'getUpdates', data=params)
        return response.json()

    def setWebhook(self, url, certificate, max_connections, allowed_updates):
        pass

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
        response = requests.get(self.api_url + 'User', data=params)
        return response.json()

    def Chat(self, id, type, title, username, first_name, last_name, 
             photo, description, invite_link, pinned_message, 
             permissions, slow_mode_delay, sticker_set_name, can_set_sticker_set):
        pass

if __name__ == '__main__':
    bot = Telegram_bot(url)
    print(bot.getUpdates())
