from flask_restful import Resource
from models.session import Session
from models.account_session import AccountSession



class BestScoreResource(Resource):

    def get(self, accountId, specificationId):
        specification_sessions = Session.query.filter(Session.specification_id == specificationId)
        account_sessions = AccountSession.query.filter(AccountSession.account_id == accountId)
        filter_arr = [0]
        for session in account_sessions:
            for spec in specification_sessions:
                if spec.session_id == session.session_id:
                    filter_arr.append(float(spec.score))
        result = max(filter_arr)
        return {'content': result}





