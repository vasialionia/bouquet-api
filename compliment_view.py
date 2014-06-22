# -*- coding: utf-8 -*-
# TODO remove me


from flask.views import MethodView
from flask import Response
import json


class ComplimentView(MethodView):

    def get(self, compliment_id=None):
        if not compliment_id:
            return Response(json.dumps([{'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'}, {'sex': 'female', 'lang': 'ru', 'text': 'Ты самая лучшая!'}], ensure_ascii=False), 200)
        else:
            return Response(json.dumps({'sex': 'male', 'lang': 'ru', 'text': 'Ты самый лучший!'}, ensure_ascii=False), 200)

    @classmethod
    def register(cls, app):
        compliment_view = cls.as_view('compliment_view')

        app.add_url_rule('/compliment', view_func=compliment_view, methods=['GET', 'POST'])
        app.add_url_rule('/compliment/<int:compliment_id>', view_func=compliment_view, methods=['GET', 'DELETE', 'PUT'])
