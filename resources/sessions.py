from flask_restful import Resource
from flask import request
from db import db

from models.session import Session

class SessionResource(Resource):

    def get(self):
        sessions = Session.query.all()
        result = []
        for session in sessions:
            result.append(
                {
                    'id': session.session_id,
                    'start': session.start,
                    'end': session.end,
                    'score': session.score,
                    'completed': session.completed
                }
            )
        return {'content': result}