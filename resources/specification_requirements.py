from flask_restful import Resource
from flask import request
from db import db

from models.specification_requirement import SpecificationRequirement

class SpecificationRequirementResource(Resource):

    def get(self):
        specification_requirements = SpecificationRequirement.query.all()
        result = []
        for specification_requirement in specification_requirements:
            result.append(
                {
                    'id': specification_requirement.specification_requirement_id,
                    'specification_id': specification_requirement.specification_id,
                    'requirement_id': specification_requirement.requirement_id
                }
            )
        return {'specification_requirements': result}