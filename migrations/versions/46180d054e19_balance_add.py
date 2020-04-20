"""balance add

Revision ID: 46180d054e19
Revises: 
Create Date: 2020-04-02 16:51:57.686400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46180d054e19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('balance', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'balance')
    # ### end Alembic commands ###