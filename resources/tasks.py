import random

from flask_restful import Resource
from db import db

from models.session import Session
from models.specification_requirement import SpecificationRequirement


class TaskResource(Resource):

    def get(self, id):
        specification = db.session.query(Session).filter(Session.session_id == id).first().specification_id;
        numberfCorrectRequirements = random.randint(10, 15)
        numberOfIncorrectRequirements = 15 - numberfCorrectRequirements
        correctRequirements = random.choices(db.session.query(SpecificationRequirement).filter(SpecificationRequirement.specification_id == specification).all(), k=numberfCorrectRequirements)
        incorrectRequiremnts =  random.choices(db.session.query(SpecificationRequirement).filter(SpecificationRequirement.specification_id != specification).all(), k=numberOfIncorrectRequirements)
        requirements = correctRequirements + incorrectRequiremnts
        result_req = []
        for requirement in requirements:
            result_req.append(
                {
                    'id': requirement.requirement_id,
                    'text': requirement.requirement.requirement_text
                }
            )
        result = {'id': id, 'requirements': result_req}



        return {'content': result}

