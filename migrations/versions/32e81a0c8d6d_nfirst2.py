"""nfirst2

Revision ID: 32e81a0c8d6d
Revises: e26453e5d56b
Create Date: 2020-05-06 17:00:24.280949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32e81a0c8d6d'
down_revision = 'e26453e5d56b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=False,default=0)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
