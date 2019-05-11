"""created Post table

Revision ID: 624119fc77eb
Revises: 
Create Date: 2019-05-10 17:48:54.616535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624119fc77eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=True),
    sa.Column('email', sa.String(length=700), nullable=True),
    sa.Column('comment', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###