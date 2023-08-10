"""update

Revision ID: 1daef146fe85
Revises: a721d449b47d
Create Date: 2023-08-05 14:35:12.699692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1daef146fe85'
down_revision = 'a721d449b47d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('visits', sa.Integer(), nullable=True),
    sa.Column('bus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bus_id'], ['buses.id'], name=op.f('fk_uploads_bus_id_buses')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_uploads'))
    )
    op.drop_table('upload')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_upload')
    )
    op.drop_table('uploads')
    # ### end Alembic commands ###