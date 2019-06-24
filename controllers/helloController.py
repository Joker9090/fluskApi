from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('hello', __name__, url_prefix='/hello')

@bp.route('/<name>', methods=('GET', 'POST'))
def hello(name):
    if request.method == 'GET':
        if session.get(name):
            print('session')
            print(session)
            return 'welcome %s' % name
        else:
            return redirect(url_for('hello.start'))
    else:
        print('where are you going?')
        return 'where are you going?'

@bp.route('/')
def start():
    return 'need to login'

@bp.route('/login/<name>')
def login(name):
    session.clear()
    session[name] = True
    return 'logged %s' % name
