from flask_restful import Resource
from flask import request
from db import db

from models.specification_requirement import SpecificationRequirement
from models.requirement import Requirement
from models.specification import Specification

class SpecificationRequirementResource(Resource):

    def get(self, id):
        requirements = db.session.query(SpecificationRequirement).filter(SpecificationRequirement.specification_id == id).all()
        result = []
        for specification_requirement in requirements:
            result.append(
                {
                    'id': specification_requirement.requirement.requirement_id,
                    'text': specification_requirement.requirement.requirement_text,
                    'typeId': specification_requirement.requirement.type_id
                }
            )
        return {'content': result}


class SpecificationAddRequirementResource(Resource):

    def put(self, id):
        payload = request.get_json(force=True)
        new_requirement = Requirement()
        new_requirement.requirement_text = payload.get('text')
        new_requirement.type_id = payload.get('typeId')
        _id = new_requirement.requirement_id
        db.session.add(new_requirement)
        db.session.commit()

        new_specification_requirement = SpecificationRequirement()
        new_specification_requirement.specification_id = id
        new_specification_requirement.requirement_id = new_requirement.requirement_id
        db.session.add(new_specification_requirement)
        db.session.commit()

class SpecificationDeleteRequirementResource(Resource):

    def delete(self, specificationId, id):
        db.session.query(SpecificationRequirement).filter(SpecificationRequirement.requirement_id == id).filter(SpecificationRequirement.specification_id == specificationId).delete()
        db.session.query(Requirement).filter(Requirement.requirement_id == id).delete
        db.session.commit()


class SpecificationUpdateRequirementResource(Resource):

    def post(self, specificationId, id):
        payload = request.get_json(force=True)
        update_requirement = Requirement.query.filter(Requirement.requirement_id == id).first()
        update_requirement.requirement_text = payload.get('text')
        update_requirement.type_id = payload.get('typeId')
        db.session.commit()



