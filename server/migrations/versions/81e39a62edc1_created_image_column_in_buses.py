"""created image column in  buses

Revision ID: 81e39a62edc1
Revises: 0b96bc714742
Create Date: 2023-08-02 17:00:19.481609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81e39a62edc1'
down_revision = '0b96bc714742'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('buses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('buses', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###