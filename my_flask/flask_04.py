from flask import Flask
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/<name>/<lastname>')
def success(name, lastname):
    return f'hello {name} {lastname}'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form, type(request.form))
        user = request.form['name']
        lastname = request.form['lastname']
        return redirect(url_for('success', name=user, lastname=lastname))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()
