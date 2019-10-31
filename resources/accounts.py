from flask_restful import Resource

from flask import request
from db import db

from models.account import Account


class AccountsResource(Resource):


    def get(self):
        accounts = Account.query.all()

        result = []
        for account in accounts:
            result.append({
                'id': account.account_id,
                'username': account.username,
                'email': account.email
            })
        return {'accounts': result}

    def delete(self, user_id):
        #payload = request.get_json(force=True)
        #db.session.query(Account).filter(Account.account_id == payload.get('userId')).delete()
        db.session.query(Account).filter(Account.account_id == user_id).delete()
        db.session.commit()

        accounts = Account.query.all()

        result = []
        for account in accounts:
            result.append({
                'id': account.account_id,
                'username': account.username,
                'email': account.email
            })
        return {'accounts': result}, 200


class AccountDeleteById(Resource):
    def delete(self, user_id):
        # payload = request.get_json(force=True)
        # db.session.query(Account).filter(Account.account_id == payload.get('userId')).delete()
        db.session.query(Account).filter(Account.account_id == user_id).delete()
        db.session.commit()

        accounts = Account.query.all()

        result = []
        for account in accounts:
            result.append({
                'id': account.account_id,
                'username': account.username,
                'email': account.email
            })
        return {'accounts': result}, 200
