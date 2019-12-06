from flask_restful import Resource
from flask import request
from db import db

from models.specification import Specification
from models.account_specification import AccountSpecification

class SpecificationResource(Resource):

    def get(self):
        specifications = Specification.query.all()
        result = []
        for specification in specifications:
            result.append(
                {
                    'id': specification.specification_id,
                    'name': specification.specification_name,
                    'description': specification.specification_description
                }
            )
        return {'content': result}

    def put(self):
        payload = request.get_json(force=True)
        new_specification = Specification(payload.get('name'), payload.get('description'))

        db.session.add(new_specification)
        db.session.commit()




class SpecificationDeleteById(Resource):
    def delete(self, id):
        db.session.query(Specification).filter(Specification.specification_id == id).delete()
        db.session.commit()

class SpecificationUpdateById(Resource):
    def post(self, id):
        payload = request.get_json(force=True)
        update_specification = Specification.query.filter(Specification.specification_id == id).first()
        update_specification.specification_name = payload.get('name')
        update_specification.specification_description = payload.get('description')
        db.session.commit()


    def get(self, id):
        specification = Specification.query().filter(Specification.specification_id == id).first()
        attempts = AccountSpecification.query().filter(AccountSpecification.specification_id == id).first().attempts
        result = {
                'id': specification.specification_id,
                'name': specification.specification_name,
                'description': specification.specification_description,
                'attempts': attempts,
                'score': 0
            }
        return {'content': result}

