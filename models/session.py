from db import db

class Session(db.Model):
    _tablename_ = 'session'

    session_id = db.Column(db.Integer, primary_key=True, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=True)
    score = db.Column(db.DECIMAL, nullable=False)
    completed = db.Column(db.Boolean, nullable=True)
    specification_id = db.Column(db.Integer, db.ForeignKey('specification.specification_id', name='fk_session_specificatio'),nullable=False)

    specification = db.relationship("Specification")

    def __index__(self, start, end, score, completed, specification_id):
        self.score = score
        self.start = start
        self.end = end
        self.completed = completed
        self.specification_id = specification_id

    def __repr__(self):
        return '<Session %r start %r end %r score %r completed %r specification %r>' % (self.session_id, self.start, self.end, self.score, self.completed, self.specification_id)