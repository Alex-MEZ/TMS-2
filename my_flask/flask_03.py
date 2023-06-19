# Создать сайт.
# При запросе по урлу /my_word/[word], в случае если длина слова четна -
# выводит строку содержащую все нечетные элементы строки(abcdef -> ace).
# В ином случае перенаправлять на домашнюю страницу.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f'hello world'


@app.route('/my_word/<word>/')
def my_word(word):
    if len(word) % 2:
        return redirect(url_for('/'))
    else:
        result = word[::2]
        return result


if __name__ == '__main__':
    app.run()
