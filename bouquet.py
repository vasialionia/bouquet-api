from flask import Flask
from compliment_view import ComplimentView
import database


app = Flask(__name__)
app.config['DATABASE_PATH'] = 'sqlite:///database.db'

ComplimentView.register(app)

db_session = None


@app.before_first_request
def before_first_request():
    global db_session
    db_session = database.init(app.config['DATABASE_PATH'])

@app.teardown_appcontext
def teardown_appcontext(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
