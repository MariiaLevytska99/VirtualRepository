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
                'email': account.email,
                'password': account.password
            })
        return {'content': result}

    def post(self):
        payload = request.get_json(force=True)
        print("data is " + format(payload))
        accounts = Account.query.all()
        print("accounts are " + format(accounts))

        for account in accounts:
            if payload.get('username') == account.username:
                if payload.get('password') == account.password:
                    return {}, 200

        return {}, 400

    def put(self):
        payload = request.get_json(force=True)
        print("data is " + format(payload))
        if payload is None:
            payload = {}
        new_account = Account(payload.get('username'), payload.get('email'), payload.get('password'))
        db.session.add(new_account)
        db.session.commit()

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
        return {'content': result}, 200


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
        return {'content': result}, 200
