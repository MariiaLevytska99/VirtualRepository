from flask_restful import Resource
from flask import request
from db import db

from models.account_specification import AccountSpecification
from models.specification import Specification

class AccountSpecificationResource(Resource):

    def get(self):
        account_specification = AccountSpecification.query.all()
        result = []
        for acc_sp in account_specification:
            result.append(
                {
                    'id': acc_sp.account_specification_id,
                    'accountId': acc_sp.account_id,
                    'specificationId': acc_sp.specification_id,
                    'attempts': acc_sp.attempts
                }
            )
        return {'content': result}

    def putAttempts(self,specification_id, account_id):
        account_specification_new = AccountSpecification()
        account_specification_new.attempts = 3
        account_specification_new.specification_id = specification_id
        account_specification_new.account_id = account_id
        db.session.add(account_specification_new)
        db.session.commit()

    def put(self, accountId):

        specifications = Specification.query.all()
        for specification in specifications:
            self.putAttempts(specification.specification_id, accountId)


class AttemptResource(Resource):
    def get(self, accountId, specificationId):
        attempts = AccountSpecification.query.filter(AccountSpecification.specification_id == specificationId).filter(\
            AccountSpecification.account_id == accountId).first().attempts
        return attempts

    def post(self, accountId, specificationId):
        update_attempts = AccountSpecification.query.filter(AccountSpecification.specification_id == specificationId).filter(\
            AccountSpecification.account_id == accountId).first()
        update_attempts.attempts = update_attempts.attempts - 1
        db.session.commit()
