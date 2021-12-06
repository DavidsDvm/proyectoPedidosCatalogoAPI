"""init

Revision ID: 84ad94299cf8
Revises: 
Create Date: 2021-11-17 19:00:38.155711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84ad94299cf8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=False),
        sa.Column('user_identification', sa.String, unique=True, nullable=False),
        sa.Column('user_namevarchar', sa.String, nullable=False),
        sa.Column('user_birthday', sa.DateTime, nullable=False),
        sa.Column('user_monthBirthday', sa.String, nullable=False),
        sa.Column('user_address', sa.String, nullable=False),
        sa.Column('user_cellphone', sa.String, nullable=False),
        sa.Column('user_email', sa.String, nullable=False, unique=True),
        sa.Column('user_passwordvarchar', sa.String, nullable=False),
        sa.Column('user_zone', sa.String, nullable=False),
        sa.Column('user_type', sa.String, nullable=False)
    )

    op.create_table(
        'cookware',
        sa.Column('cookware_reference', sa.String, primary_key=True, autoincrement=False),
        sa.Column('cookware_brand', sa.String, nullable=False),
        sa.Column('cookware_category', sa.String, nullable=False),
        sa.Column('cookware_material', sa.String, nullable=False),
        sa.Column('cookware_dimentions', sa.String, nullable=False),
        sa.Column('cookware_description', sa.String, nullable=False),
        sa.Column('cookware_availability', sa.Boolean, nullable=False),
        sa.Column('cookware_price', sa.Float, nullable=False),
        sa.Column('cookware_quantity', sa.Integer, nullable=False),
        sa.Column('cookware_photo', sa.String, nullable=False)
    )

    op.create_table(
        'cookware_and_order',
        sa.Column('cookware_reference', sa.String),
        sa.Column('order_id', sa.Integer),
        sa.Column('order_quantity', sa.Integer, nullable=True)
    )

    op.create_table(
        'user_and_order',
        sa.Column('user_id', sa.Integer),
        sa.Column('order_id', sa.Integer)
    )

    op.create_table(
        'order',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=False),
        sa.Column('order_register', sa.DateTime, nullable=False),
        sa.Column('order_status', sa.String, nullable=False),
    )



def downgrade():
    op.drop_table('user')
    op.drop_table('cookware')
    op.drop_table('cookware_and_order')
    op.drop_table('user_and_order')
    op.drop_table('order')
