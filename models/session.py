from db import db

class Session(db.Model):
    _tablename_ = 'session'

    session_id = db.Column(db.Integer, primary_key=True, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.DECIMAL, nullable=False)
    completed = db.Column(db.Boolean, nullable=True)

    def __index__(self, start, end, score, completed):
        self.score = score
        self.start = start
        self.end = end
        self.completed = completed

    def __repr__(self):
        return '<Session %r start %r end %r score %r completed %r>' % (self.session_id, self.start, self.end, self.score, self.completed)