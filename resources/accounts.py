import smtplib
import ssl
import random
import string

from flask import request
from flask_restful import Resource

from db import db
from models.account import Account
from models.account_specification import AccountSpecification
from models.specification import Specification


class PasswordManager():
    def randomString(stringLength=10):
        return ''.join(random.choice(string.ascii_letters + string.punctuation) for x in range(10))

    def send(self, receiver_email):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "virtual.laboratory.restore"
        password = "newpassword12345"
        message = """New password """

        pm = PasswordManager()
        rand = pm.randomString()
        message += rand
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            return rand


class AccountsResource(Resource):
    def putAttempts(self, specification_id, account_id):
        account_specification_new = AccountSpecification()
        account_specification_new.attempts = 3
        account_specification_new.specification_id = specification_id
        account_specification_new.account_id = account_id
        db.session.add(account_specification_new)
        db.session.commit()

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
        accounts = Account.query.all()

        if not payload.get('password'):
            for account in accounts:
                if payload.get('email') == account.email:
                    psw_man = PasswordManager()
                    pas = ""
                    pas += psw_man.send(account.email)
                    db.session.query(Account).filter(Account.email == account.email).update(dict(password=pas))
                    db.session.commit()
                    return {}, 200
        else:
            for account in accounts:
                if payload.get('username') == account.username:
                    if payload.get('password') == account.password:
                        return {'id': account.account_id,
                                'username': account.username,
                                'token': 'fake-jwt-token'}, 200

        return {}, 400

    def put(self):
        payload = request.get_json(force=True)
        accounts = Account.query.all()
        if payload is None:
            payload = {}
        new_account = Account(email=payload.get('email'), username=payload.get('login'), password=payload.get('password'))

        for account in accounts:
            if new_account.username == account.username:
                return {}, 400
            if new_account.email == account.email:
                return {}, 400

        db.session.add(new_account)
        db.session.commit()

        specifications = Specification.query.all()
        for specification in specifications:
            self.putAttempts(specification.specification_id, new_account.account_id)

        return {}, 200

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
