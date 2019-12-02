"""empty message

Revision ID: 976a66207d4c
Revises: 00008
Create Date: 2019-11-23 14:49:33.397833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00009'
down_revision = '00008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_specification',
    sa.Column('account_specification_id', sa.Integer(), nullable=False),
    sa.Column('specification_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('attempts', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.account_id'], name='fk_accpunt_specificatio'),
    sa.ForeignKeyConstraint(['specification_id'], ['specification.specification_id'], name='fk_account_specification'),
    sa.PrimaryKeyConstraint('account_specification_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_specification')
    # ### end Alembic commands ###