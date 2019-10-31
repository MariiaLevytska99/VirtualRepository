from db import db

class Specification(db.Model):
    _tablename_ = 'specification'

    specification_id = db.Column(db.Integer, primary_key=True, nullable=False)
    specification_name = db.Column(db.String(120), unique=True, nullable=False)
    specification_description = db.Column(db.Text, nullable=True)

    def __init__(self, specification_name, specification_description):
        self.specification_name = specification_name
        self.specification_description = specification_description

    def __repr__(self):
        return '<Specification %r Description %r>' % (self.specification_name, self.specification_description)
