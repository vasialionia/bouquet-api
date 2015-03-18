from flask import Flask
from flask import session
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config.DebugConfig)
db = SQLAlchemy(app)


import models
import views


views.ComplimentView.register(app)


def is_logged_in():
    return session.get('login') == app.config['ADMIN_LOGIN'] and session.get('pass') == app.config['ADMIN_PASS']


@app.route('/')
def index():
    if is_logged_in():
        return redirect(url_for('compliments'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        session['login'] = request.form.get('login')
        session['pass'] = request.form.get('pass')
        return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    session['login'] = None
    session['pass'] = None
    return redirect(url_for('index'))

@app.route('/compliments')
def compliments():
    if not is_logged_in():
        return redirect(url_for('index'))
    else:
        return render_template('index.html', compliments=models.Compliment.query.order_by(models.Compliment.lang, models.Compliment.sex, models.Compliment.text).all())

if __name__ == '__main__':
    app.run()
