from flask import Flask, request, redirect, jsonify
from datetime import datetime
from etc.base_definitions import *

from utils.send_telegram import telegram_signal_send

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    data = request.stream.read().decode('UTF-8')

    telegram_signal_send(
        chat_id=TELEGRAM_CHAT_ID,
        api_key=TELEGRAM_API_KEY,
        text=data
    )

    return f"data -> {data}"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
