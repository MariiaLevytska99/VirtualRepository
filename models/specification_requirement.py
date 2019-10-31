from db import db

class SpecificationRequirement(db.Model):
    _tablename_ = 'specification_requirement'

    specification_requirement_id = db.Column(db.Integer, primary_key=True, nullable=False)
    specification_id = db.Column(db.Integer, db.ForeignKey('specification.specification_id', name='fk_specification_specification_requirement_type'), nullable=False)
    requirement_id = db.Column(db.Integer, db.ForeignKey('requirement.requirement_id',name='fk_requirement_specification_requirement_type'),nullable=False)

    specification = db.relationship("Specification")
    requirement = db.relationship("Requirement")


    def __index__(self, specification_id, requirement_id):
        self.requirement_id = requirement_id
        self.specification_id = specification_id

    def __repr__(self):
        return '<Specification % r Requirement %r>' % (self.specification_id, self.requirement_id)