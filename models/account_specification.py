from db import db

class AccountSpecification(db.Model):
    _tablename_ = 'account_specification'

    account_specification_id = db.Column(db.Integer, primary_key=True, nullable=False)
    specification_id = db.Column(db.Integer, db.ForeignKey('specification.specification_id',
                                                           name='fk_account_specification'),
                                 nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id',
                                                         name='fk_accpunt_specificatio'),
                               nullable=False)
    attempts = db.Column(db.Integer, nullable=False)

    specification = db.relationship("Specification")
    account = db.relationship("Account")

    def __index__(self, specification_id, account_id, attempts):
        self.account_id = account_id
        self.specification_id = specification_id
        self.attempts = attempts

    def __repr__(self):
        return '<Specification % r Account %r Attempts %r>' % (self.specification_id, self.account_id, self.attempts)