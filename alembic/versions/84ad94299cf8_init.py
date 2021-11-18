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
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_email', sa.String, nullable=False, unique=True),
        sa.Column('user_namevarchar', sa.String, nullable=False),
        sa.Column('user_passwordvarchar', sa.String, nullable=False)
    )



def downgrade():
    op.drop_table('user')
