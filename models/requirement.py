from db import db

class Requirement(db.Model):
    _tablename_ = 'requirement'

    requirement_id = db.Column(db.Integer, primary_key=True, nullable=False)
    requirement_text = db.Column(db.Text, nullable=False, unique=False)
    type_id = db.Column(db.Integer, db.ForeignKey('requirement_type.type_id', name='fk_requirement_requirement_type'), nullable=False)

    type = db.relationship("RequirementType")


    def __index__(self, text, type_id):
        self.requirement_text = text
        self.type_id = type_id

    def __repr__(self):
        return '<Requirememt % r Type %r>' % (self.requirement_text, self.type_id)


