"""empty message

Revision ID: 380ac0a1c08a
Revises: 
Create Date: 2021-12-16 20:53:49.148533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '380ac0a1c08a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrators',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('customer', 'worker', 'admin', name='roletype'), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.create_table('customers',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('customer', 'worker', 'admin', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.create_table('workers',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('customer', 'worker', 'admin', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workers')
    op.drop_table('customers')
    op.drop_table('administrators')
    # ### end Alembic commands ###
