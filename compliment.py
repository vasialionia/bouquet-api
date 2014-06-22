from database import Base
from sqlalchemy import Column, Integer, String


class Compliment(Base):
    __tablename__ = 'compliment'

    id = Column(Integer, primary_key=True)
    lang = Column(String)
    sex = Column(String)
    text = Column(String)

    def __init__(self, lang, sex, text):
        self.lang = lang
        self.sex = sex
        self.text = text
