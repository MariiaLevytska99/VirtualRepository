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

    def post(self, sessionId):
        payload = request.get_json(force=True)
        unselectedRequiremenets = payload.get('requirementsUnselected')
        selectedRequirements = payload.get('requirements')
        for unselect in unselectedRequiremenets:
            print(unselect.get('id'))
            SessionTaskResource.putReq(self, sessionId, unselect.get('id'), None)

        for select in selectedRequirements:
            for req in select.get('requirements'):
                SessionTaskResource.putReq(self, sessionId, req.get('id'), select.get('value'),)


    def putReq(self, sessionId, reqId, answerId):
        task = SessionTask()
        task.session_id = sessionId
        task.requirement_id = reqId
        task.requirement_type_answer = answerId
        db.session.add(task)
        db.session.commit()