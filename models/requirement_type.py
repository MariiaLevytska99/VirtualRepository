from db import db

class RequirementType(db.Model):
    _tablename_ = 'requirement_type'

    type_id = db.Column(db.Integer, primary_key=True, nullable=False)
    type_name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self):
        return '<Requiremnt type %r>' % (self.type_name)
