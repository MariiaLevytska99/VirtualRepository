import datetime
import random

from flask_restful import Resource
from flask import request
from db import db

from models.session import Session
from models.session_task import SessionTask
from models.requirement import Requirement
from models.specification_requirement import SpecificationRequirement
from resources.account_specifications import AttemptResource
from decimal import Decimal

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


class SessionUpdateScoreResource(Resource):

    def post(self, sessionId):
        payload = request.get_json(force=True)
        update_session = Session.query.filter(Session.session_id == sessionId).first()
        session_tasks = SessionTask.query.filter(SessionTask.session_id == sessionId)
        n = 0
        m = 0
        for session_task in session_tasks:
            m += 1
            requirement = Requirement.query.filter(Requirement.requirement_id == session_task.requirement_id)
            if requirement.type_id == session_task.requirement_type_answer:
                n += 1
            #я хер знает правильно ли
            elif session_task.requirement_type_answer is not None:
                m += 2

        update_session.score = int(n / m * 100)
        db.session.commit()

class SessionBridgeResource(Resource):

    def put(self, specificationId):
        payload = request.get_json(force=True)
        new_session = Session()
        new_session.start = datetime.datetime.utcnow()
        new_session.specification_id = specificationId
        new_session.completed = False
        new_session.score = 0
        db.session.add(new_session)
        db.session.commit()
        return {'content': new_session.session_id}

class SessionGetResultResource(Resource):

    def get(self, sessionId):
        session = Session.query.filter(Session.session_id == sessionId).first()
        session_tasks = SessionTask.query.filter(SessionTask.session_id == sessionId).all()
        n = 0
        m = 0
        for session_task in session_tasks:
            print('1', session_task)
            m += 1
            requirement = Requirement.query.filter(Requirement.requirement_id == session_task.requirement_id).first()
            if requirement.type_id == session_task.requirement_type_answer:
                print('2')
                n += 1
            elif session_task.requirement_type_answer is not None:
                print('3')
                m += 2
        passingPoints = (int)(m * 0.75)

        session.score = n
        session.completed = (n >= passingPoints)
        session.end = datetime.datetime.utcnow()
        db.session.commit()

        result = {
            'score': float(n),
            'passed': n >= passingPoints,
            'passingScore': float(passingPoints),
            'percentage': float(session.score)
        }

        return {'content': result}
