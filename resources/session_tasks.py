from flask_restful import Resource
from flask import request
from db import db

from models.session_task import SessionTask

class SessionTaskResource(Resource):

    def get(self):
        session_tasks = SessionTask.query.all()
        result = []
        for task in session_tasks:
            result.append(
                {
                    'id': task.session_task_id,
                    'session_id': task.session_id,
                    'requirement_id': task.requirement_id,
                    'answer_id': task.requirement_type_answe
                }
            )
        return {'session_tasks': result}