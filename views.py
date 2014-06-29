from flask.views import MethodView
from flask import Response
from flask import request
import json
from app import db
import models


class ComplimentView(MethodView):

    def get(self, compliment_id=None):
        if not compliment_id:
            return Response(json.dumps([c.to_json() for c in models.Compliment.query.all()], ensure_ascii=False), status=200, mimetype='application/json')
        else:
            return Response(json.dumps(models.Compliment.query.get(compliment_id).to_json(), ensure_ascii=False), status=200, mimetype='application/json')

    def post(self):
        c = models.Compliment(lang=request.form.get('lang'), sex=request.form.get('sex'), text=request.form.get('text'))
        db.session.add(c)
        db.session.commit()
        return Response(json.dumps(c.to_json(), ensure_ascii=False), status=200, mimetype='application/json')

    def delete(self, compliment_id):
        c = models.Compliment.query.get(compliment_id)
        db.session.delete(c)
        db.session.commit()
        return Response(None, status=200, mimetype='application/json')

    def put(self, compliment_id):
        c = models.Compliment.query.get(compliment_id)
        c.lang = request.form.get('lang')
        c.sex = request.form.get('sex')
        c.text = request.form.get('text')
        db.session.commit()
        return Response(json.dumps(c.to_json(), ensure_ascii=False), status=200, mimetype='application/json')

    @classmethod
    def register(cls, app):
        compliment_view = cls.as_view('compliment_view')

        app.add_url_rule('/compliment', view_func=compliment_view, methods=['GET', 'POST'])
        app.add_url_rule('/compliment/<int:compliment_id>', view_func=compliment_view, methods=['GET', 'DELETE', 'PUT'])
