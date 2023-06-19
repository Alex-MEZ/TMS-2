# Создать сайт. При запросе по урлу /two_pow/[number] возвращает 2 в степени number

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/hello')
def hello():
    return f'hello world'


@app.route('/hello/<int:number_id>/')
def number_id(number_id):
    assert isinstance(number_id, int)
    return f'Два в степени номера страницы = {2 ** number_id}'


if __name__ == '__main__':
    app.run()
