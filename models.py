from app import db


class Compliment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String)
    sex = db.Column(db.String)
    text = db.Column(db.String)

    def __init__(self, lang, sex, text):
        self.lang = lang
        self.sex = sex
        self.text = text

    def to_json(self):
        return {'id': self.id, 'lang': self.lang, 'sex': self.sex, 'text': self.text}
