from flask_restful import Resource
from flask import request
from db import db

from models.requirement import Requirement
class RequirementResource(Resource):

    def get(self):
        requirements = Requirement.query.all()
        result = []

        for requirement in requirements:
            result.append(
                {
                    'id': requirement.requirement_id,
                    'text': requirement.requirement_text,
                    'typeId': requirement.type_id
                }
            )
        return {'content':result}


    def put(self):
        payload = request.get_json(force=True)
        new_requirement = Requirement()
        new_requirement.requirement_text = payload.get('text')
        new_requirement.type_id = payload.get('typeId')
        db.session.add(new_requirement)
        db.session.commit()



