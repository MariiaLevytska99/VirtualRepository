from db import db

class Session(db.Model):
    _tablename_ = 'session'

    session_id = db.Column(db.Integer, primary_key=True, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.DECIMAL, nullable=False)

    def __index__(self, start, end, score):
        self.score = score
        self.start = start
        self.end = end

    def __repr__(self):
        return '<Session %r start %r end %r score %r>' % (self.session_id, self.start, self.end, self.score)