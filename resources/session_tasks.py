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
                    'sessionId': task.session_id,
                    'requirementId': task.requirement_id,
                    'answerId': task.requirement_type_answe
                }
            )
        return {'content': result}