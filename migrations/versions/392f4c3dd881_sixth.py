"""sixth

Revision ID: 392f4c3dd881
Revises: 6e3b9c0343e8
Create Date: 2020-04-26 22:58:03.169630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '392f4c3dd881'
down_revision = '6e3b9c0343e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
