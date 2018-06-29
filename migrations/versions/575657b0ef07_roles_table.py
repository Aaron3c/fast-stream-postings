"""roles table

Revision ID: 575657b0ef07
Revises: 
Create Date: 2018-06-27 15:21:34.599888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575657b0ef07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organisation_id', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('region_id', sa.Text(), nullable=True),
    sa.Column('private_office', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    # ### end Alembic commands ###