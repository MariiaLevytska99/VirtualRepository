from flask_restful import Resource
from models.account_session import AccountSession


class AccounSessionsResource(Resource):

    def get(self):

        accounts_sessions = AccountSession.query.all()

        result = []
        for account_session in accounts_sessions:
             result.append({
                 'id': account_session.account_session_id,
                 'session_id': account_session.session_id,
                 'account_id': account_session.account_id,
        })

        return {'account_session': result}