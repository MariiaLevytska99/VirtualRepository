from flask_restful import Resource
from flask import request
from db import db

from models.requirement_type import RequirementType

class RequirementTypeResource(Resource):

    def get(self):
        types = RequirementType.query.all()
        result = []
        for type in types:
            result.append(
                {
                    'id': type.type_id,
                    'type_name': type.type_name
                }
            )
        return {'requirement_types': result}



