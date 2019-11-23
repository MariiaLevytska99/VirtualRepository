from flask_restful import Resource
from flask import request
from db import db

from models.account_specification import AccountSpecification

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