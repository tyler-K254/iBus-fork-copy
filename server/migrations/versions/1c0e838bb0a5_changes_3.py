"""changes 3

Revision ID: 1c0e838bb0a5
Revises: b80372ab21be
Create Date: 2023-07-30 22:49:01.198540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c0e838bb0a5'
down_revision = 'b80372ab21be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.BLOB(), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('company')

    # ### end Alembic commands ###
