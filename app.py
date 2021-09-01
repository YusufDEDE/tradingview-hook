from flask import Flask, request, redirect, jsonify
from datetime import datetime

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

    return f"data -> {data}"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
