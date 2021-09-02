import requests


def telegram_signal_send(chat_id, text, api_key):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': text
    }
    req = requests.post(url, data=data)

    print(req.content)
