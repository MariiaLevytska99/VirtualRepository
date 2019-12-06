import datetime
import random

from flask_restful import Resource
from flask import request
from db import db

from models.session import Session
from models.account_session import AccountSession
from models.specification_requirement import SpecificationRequirement
from db import db_used
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import Config
import json


class BestScoreResource(Resource):

    def get(self, accountId, specificationId):
        # account_sessions = db.session.query(AccountSession.account_session__id)\
        #     .filter(AccountSession.account_id == accountId)
        # print(account_sessions.all())
        # sessions = db.session.query(Session.score).filter(Session.session_id in account_sessions)\
        #     .filter(Session.specification_id == specificationId)
        # print(sessions)
        # result = 0

        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        session = Session(engine)

        query = """SELECT s.score as Score FROM session s
                            JOIN account_session asS on s.session_id = asS.session_id 
                            JOIN account a on asS.account_id = a.account_id 
                            JOIN specification spec on s.specification_id = spec.specification_id 
                            where a.account_id = :accountId and spec.specification_id = :specificationId"""
        content = db.session.execute(query,  {'accountId': accountId, 'specificationId': specificationId}).fetchall()

        return {
            'content': content
        }

