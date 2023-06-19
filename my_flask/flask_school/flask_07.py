# Создать пакет flask_school.
# Описать модель группы(id, fullname).
# Создать сайт. Создать напрямую в базе 3 группы.
# Описать шаблон и вью для получения и отображения списка всех групп.
# Создать шаблон и вью для создания группы.
# Добавить ссылку для перехода на создание группы на странице отображения всех групп.

from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskschoollesson.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def read_group():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)


@app.route('/add', methods=['POST', 'GET'])
def add_group():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        group = Group(fullname=request.form['fullname'])
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('read_group'))


@app.route('/update_group', methods=['POST', 'GET'])
def update_group():
    if request.method == 'Get':
        group_id = request.args.get('group.id')
        return render_template('update_group.html', group_id='group.id')
    else:
        group = Group.query.get(id=request.args.get('group.id'))
        group.name = request.form['name']
        db.session.commit()
        return redirect(url_for('read_group'))
