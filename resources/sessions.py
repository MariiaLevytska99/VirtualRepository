import datetime
import random

from flask_restful import Resource
from flask import request
from db import db

from models.session import Session
from models.specification_requirement import SpecificationRequirement


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

# start session
    def put(self):
        payload = request.get_json(force=True)
        new_session = Session()
        new_session.start = datetime.datetime.utcnow()
        new_session.specification_id = payload.get('specification')
        new_session.completed = False
        new_session.score = 0
        db.session.add(new_session)
        db.session.commit()
        return {'content': new_session.session_id}

