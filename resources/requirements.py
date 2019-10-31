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
                    'type_id': requirement.type_id
                }
            )
        return {'requirements':result}

