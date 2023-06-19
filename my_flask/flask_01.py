from flask import Flask
from datetime import datetime
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def time_now():
    return f'{datetime.now()}'


if __name__ == '__main__':
    app.run()
