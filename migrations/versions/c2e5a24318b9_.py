"""empty message

Revision ID: c2e5a24318b9
Revises: 8d8d2ac97bc8
Create Date: 2024-07-20 12:32:10.438572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e5a24318b9'
down_revision = '8d8d2ac97bc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_discount',
    sa.Column('discount_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_barcode', sa.String(length=100), nullable=False),
    sa.Column('discount_description', sa.String(length=100), nullable=False),
    sa.Column('discount_percent', sa.String(length=5), nullable=True),
    sa.Column('discount_value', sa.Double(), nullable=True),
    sa.Column('discount_status', sa.Boolean(), nullable=True),
    sa.Column('discount_date_added', sa.String(length=11), nullable=True),
    sa.Column('discount_year_added', sa.String(length=4), nullable=True),
    sa.Column('discount_month_added', sa.String(length=20), nullable=True),
    sa.Column('discount_date_updated', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('discount_id')
    )
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('product_date_added',
               existing_type=sa.DATE(),
               type_=sa.String(length=11),
               existing_nullable=True)
        batch_op.alter_column('product_datetime_added',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('product_date_updated',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=20),
               existing_nullable=True)

    with op.batch_alter_table('stock', schema=None) as batch_op:
        batch_op.drop_column('product_discount')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_discount', sa.DOUBLE(), nullable=True))

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('product_date_updated',
               existing_type=sa.String(length=20),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('product_datetime_added',
               existing_type=sa.String(length=20),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('product_date_added',
               existing_type=sa.String(length=11),
               type_=sa.DATE(),
               existing_nullable=True)

    op.drop_table('products_discount')
    # ### end Alembic commands ###