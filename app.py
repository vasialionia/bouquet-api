from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config.DebugConfig)
db = SQLAlchemy(app)


import models
import views


views.ComplimentView.register(app)


@app.route('/')
def index():
    return render_template('index.html', compliments=models.Compliment.query.order_by(models.Compliment.lang, models.Compliment.sex, models.Compliment.text).all())


if __name__ == '__main__':
    app.run()
