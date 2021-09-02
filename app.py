from celery import Celery
from datetime import datetime
from etc.base_definitions import *
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

celery = Celery(CELERY_NAME, broker=CELERY_BROKER, backend=CELERY_BACKEND)


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

    task_args = {
        'text': data,
        'api_key': TELEGRAM_API_KEY,
        'chat_id': TELEGRAM_CHAT_ID
    }

    celery.send_task(
        'celery_worker.send_telegram', args=[task_args]
    )

    return f"data -> {data}"


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT, use_reloader=True)
