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
from decimal import Decimal
from flask import jsonify


class BestScoreResource(Resource):

    def get(self, accountId, specificationId):
        query = """SELECT MAX(s.score) FROM session s
                            JOIN account_session asS on s.session_id = asS.session_id 
                            JOIN account a on asS.account_id = a.account_id 
                            JOIN specification spec on s.specification_id = spec.specification_id 
                            where a.account_id = :accountId and spec.specification_id = :specificationId"""
        content = db.session.execute(query,  {'accountId': accountId, 'specificationId': specificationId}).fetchone()
        print("CONTENT", content)
        # json_data = json.dumps(content, ensure_ascii=False, default=str)
        # return json_data
        return {'content': content}


