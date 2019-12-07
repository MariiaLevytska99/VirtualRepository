from flask_restful import Resource
from models.account_session import AccountSession

from resources.sessions import SessionBridgeResource
from resources.account_specifications import AttemptResource
from db import db

class AccountSessionsResource(Resource):

    def get(self):

        accounts_sessions = AccountSession.query.all()

        result = []
        for account_session in accounts_sessions:
             result.append({
                 'id': account_session.account_session_id,
                 'sessionId': account_session.session_id,
                 'accountId': account_session.account_id,
        })

        return {'content': result}

    def put(self, specificationId, accountId):
        account_session = AccountSession()
        account_session.session_id = SessionBridgeResource.put(self, specificationId)
        account_session.account_id = accountId
        db.session.commit()
        AttemptResource.post(self, accountId, specificationId)
        return  account_session.session_id

