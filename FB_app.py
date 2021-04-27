from flask import Flask, request
import json
#from FB_BOT import Bot


VERIFTY_TKOEN = 'kenjitest'
page_access_token = 'EAAM0O287ANIBAFUMZAi1eXQVAkoZA29pYsgNZCFGuKiNKthw4i4e2VKHquAreYqbTrgZArk5ZBPiODFG948ZAG7P32KVMphhTRoVEz6FLZBYXl7umNOOQ54acHZARQZBl3QvgZADYZCsaRfS0ENnlIPJmZCXvSjUEla6BfqBGFJ1GFpvsQZDZD'

Key_word = '+1'
other_word = 'no'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webwook():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == 'kenjitest':
            return str(challenge)

        return "400"

    else:
        print(request.data)
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        #bot = Bot(page_access_token)

        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')

            #response_text = 'hi'

            # if text_input == Key_word:
            #response_text = user_id + 'GOGO'
            #bot.send_text_message(user_id, text_input)

        return '200'


if __name__ == '__main__':
    app.run(debug=True)
