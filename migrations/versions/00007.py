"""empty message

Revision ID: 00007
Revises: 00006
Create Date: 2019-10-31 15:26:19.236787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00007'
down_revision = '00006'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_session',
    sa.Column('account_session__id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.account_id'], name='fk_account_account_session'),
    sa.ForeignKeyConstraint(['session_id'], ['session.session_id'], name='fk_session_account_session'),
    sa.PrimaryKeyConstraint('account_session__id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_session')
    # ### end Alembic commands ###
