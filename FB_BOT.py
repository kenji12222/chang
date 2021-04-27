from flask import request
import json


FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v10.0/me/'


class Bot(object):
    def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    def send_text_message(self, psid, message, messaging_type="RESPONSE"):

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'messageing_type': messaging_type,
            'recipient': {'id': psid},
            'message': {'text': message}
        }

        params = {'access_token': self.access_token}
        self.api_url = self.api_url + 'messages'

        response = request.post(self.api_url,
                                headers=headers,
                                params=params,
                                data=json.dumps(data))

        print(response.content)


bot = Bot('EAAM0O287ANIBAFUMZAi1eXQVAkoZA29pYsgNZCFGuKiNKthw4i4e2VKHquAreYqbTrgZArk5ZBPiODFG948ZAG7P32KVMphhTRoVEz6FLZBYXl7umNOOQ54acHZARQZBl3QvgZADYZCsaRfS0ENnlIPJmZCXvSjUEla6BfqBGFJ1GFpvsQZDZD')
bot.send_text_message(103378301890193, 'Testing')
