from flask_restful import Resource
from flask import request
from db import db

from models.specification import Specification
from models.account_specification import AccountSpecification
from resources.best_score import BestScoreResource
from resources.account_specifications import AttemptResource
from models.account_session import AccountSession
from models.session import Session

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


class SpecificationDetails(Resource):
     def get(self, specificationId, accountId):
         specification = Specification.query.filter(Specification.specification_id == specificationId).first()
         score = BestScoreResource.get(self, accountId, specificationId).get('content')
         attempts = AttemptResource.get(self, accountId, specificationId)
         result = {
             'id': specification.specification_id,
             'name': specification.specification_name,
             'description': specification.specification_description,
             'attempts': attempts,
             'score': score
         }
         return {'content': result}


class SpecificationDetailsBySesionResource(Resource):

    def get(self, sessionId):
        specification_id = Session.query.filter(Session.session_id == sessionId).first().specification_id
        account = AccountSession.query.filter(AccountSession.session_id == sessionId).first().account_id

        specification = Specification.query.filter(Specification.specification_id == specification_id).first()
        score = BestScoreResource.get(self, account, specification_id).get('content')
        attempts = AttemptResource.get(self, account, specification_id)
        result = {
            'id': specification.specification_id,
            'name': specification.specification_name,
            'description': specification.specification_description,
            'attempts': attempts,
            'score': score
        }

        return {'content': result}
