from db import db

class AccountSession(db.Model):
    _tablename_ = 'account_session'

    account_session__id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id', name='fk_account_account_session'), nullable=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.session_id', name='fk_session_account_session'), nullable=True)

    accounts = db.relationship("Account")
    sessions = db.relationship("Session")

    def __index__(self, session_id, account_id):
        self.session_id = session_id
        self.account_id = account_id

    def __repr__(self):
        return '<Session-Account %r %r>'% (self.session_id_id, self.account_id)