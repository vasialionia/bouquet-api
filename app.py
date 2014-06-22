from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)


import models
import views


views.ComplimentView.register(app)


if __name__ == '__main__':
    app.run()
