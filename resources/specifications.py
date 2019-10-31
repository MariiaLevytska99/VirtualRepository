from flask_restful import Resource
from flask import request
from db import db

from models.specification import Specification

class SpecificationResource(Resource):

    def get(self):
        specifications = Specification.query.all()
        result = []
        for specification in specifications:
            result.append(
                {
                    'id': specification.specification_id,
                    'specification_name': specification.specification_name,
                    'specification_description': specification.specification_description
                }
            )
        return {'specifications': result}