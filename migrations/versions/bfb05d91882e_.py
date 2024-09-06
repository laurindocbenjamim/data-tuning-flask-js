"""empty message

Revision ID: bfb05d91882e
Revises: 9031bee52eb8
Create Date: 2024-06-29 16:29:59.824990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bfb05d91882e'
down_revision = '9031bee52eb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth_user_historic', schema=None) as batch_op:
        batch_op.alter_column('date_logged_in',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth_user_historic', schema=None) as batch_op:
        batch_op.alter_column('date_logged_in',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
