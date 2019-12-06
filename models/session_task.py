from db import db

class SessionTask(db.Model):
    _tablename_ = 'session_task'

    session_task_id = db.Column(db.Integer, primary_key=True, nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.session_id', name='fk_session_session_task'), nullable=False)
    requirement_id = db.Column(db.Integer, db.ForeignKey('requirement.requirement_id',name='fk_requirement_session_task'),nullable=False)
    requirement_type_answer = db.Column(db.Integer, db.ForeignKey('requirement_type.type_id',name='fk_requirement_type_answer_session_task'),nullable=True)

    session = db.relationship("Session")
    requirement = db.relationship("Requirement")
    requirement_answer = db.relationship("RequirementType")


    def __index__(self, session_id, requirement_id, answer_id):
        self.requirement_id = requirement_id
        self.session_id = session_id
        self.requirement_type_answer = answer_id

    def __repr__(self):
        return '<Session % r Requirement %r Answer %r>' % (self.session_id, self.requirement_id, self.requirement_type_answer)