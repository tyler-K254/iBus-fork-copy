"""modification

Revision ID: c068c8bd24bf
Revises: 154b1cfc815a
Create Date: 2023-07-30 15:58:08.399607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c068c8bd24bf'
down_revision = '154b1cfc815a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(), nullable=False))
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
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
