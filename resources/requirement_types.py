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
                    'typeName': type.type_name
                }
            )
        return {'content': result}

    def post(self):
        payload = request.get_json(force=True)
        new_type = RequirementType(payload.get('type_name'))
        try:
            db.session.add(new_type)
            db.session.commit()
            res = []
            types = RequirementType.query.all()
            for type in types:
                try:
                    res.append({
                        'id': type.requirement_type_id,
                        'typeName': type.type_name
                    })
                except:
                    pass
            return {'content': res}, 201

        except:
            return {'message': "can't add requirement type, sorry"}, 400



