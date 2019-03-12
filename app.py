# coding: utf-8

from datetime import datetime

from flask import Flask, redirect
from flask import render_template
from flask_sockets import Sockets

from views.todos import todos_view
from forms import VipListForm, make_choice

app = Flask(__name__)
sockets = Sockets(app)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = VipListForm()
    platforms = make_choice('platformlist')
    if form.validate():
        new_url = form.parser.data + form.url.data
        return redirect(new_url)
    return render_template('index.html', form=form, platforms=platforms)


@app.route('/time')
def time():
    return str(datetime.now())


@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)
