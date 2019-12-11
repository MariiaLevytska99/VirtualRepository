import smtplib
import ssl
import random
import string
import os
import hashlib
import binascii
import datetime

from flask import request
from flask_restful import Resource

from db import db
from models.account import Account
from models.account_specification import AccountSpecification
from models.specification import Specification
from models.account_session import AccountSession
from models.session import Session
from resources.best_score import BestScoreResource


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

    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


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
                    if PasswordManager.verify_password(account.password, payload.get('password')):
                        return {'id': account.account_id,
                                'username': account.username,
                                'email': account.email,
                                'token': 'fake-jwt-token'}, 200

        return {}, 400

    def put(self):
        payload = request.get_json(force=True)
        accounts = Account.query.all()

        hashed_password = PasswordManager.hash_password(payload.get('password'))

        if payload is None:
            payload = {}
        new_account = Account(email=payload.get('email'), username=payload.get('login'), password=hashed_password)

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


class AccountById(Resource):
    def delete(self, user_id):
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

    def get(self, accountId):
        account = Account.query.filter(Account.account_id == accountId).first()
        tests = len(AccountSession.query.filter(AccountSession.account_id == accountId).all())
        themes = len(AccountSpecification.query.filter(AccountSpecification.account_id == accountId) \
                     .filter(AccountSpecification.attempts < 3).all())
        ac_sessions = AccountSession.query.filter(AccountSession.account_id == accountId).all()
        time = datetime.datetime.now() - datetime.datetime.now()
        sessions = Session.query.all()
        for ac_session in ac_sessions:
            for session in sessions:
                if session.session_id == ac_session.session_id:
                    time_delta = session.end - session.start
                    time = time + time_delta

        s = str(time)
        time_spent = s

        result = {
            'username': account.username,
            'email': account.email,
            'tests': tests,
            'themes': themes,
            'time': time_spent
        }
        return result


class StatisticResource(Resource):

    def get(self, accountId):
        ac_sessions = AccountSession.query.filter(AccountSession.account_id == accountId).all()
        sessions = Session.query.all()
        labels = []
        scores = []
        points= []
        start = 0


        for ac_session in ac_sessions:
            for session in sessions:
                if session.session_id == ac_session.session_id:
                    labels.append(session.specification.specification_name)
                    scores.append(BestScoreResource.get(self, accountId, session.specification_id).get('content'))
                    start += 10
                    points.append(start)

        result = {
            'labels': labels,
            'dataY': scores,
            'data': points
        }

        return result
