from flask_restful import Resource
from db import db
import datetime
from models.account_specification import AccountSpecification
from models.specification import Specification
from models.session import Session
from models.account_session import AccountSession

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

class CancelTaskResource(Resource):
    def post(self, sessionId):
        session = Session.query.filter(Session.session_id == sessionId).first()
        account_id = AccountSession.query.filter(AccountSession.session_id == sessionId).first().account_id
        update_attempts = AccountSpecification.query.filter(AccountSpecification.specification_id == session.specification_id).filter(\
            AccountSpecification.account_id == account_id).first()
        update_attempts.attempts = update_attempts.attempts + 1
        session.end = datetime.datetime.now()
        db.session.commit()
