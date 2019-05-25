"""initial migration

Revision ID: eca4c1b02135
Revises: 
Create Date: 2019-05-25 12:57:16.549480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca4c1b02135'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('taskdate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('taskitem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_taskitem_item'), 'taskitem', ['item'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_taskitem_item'), table_name='taskitem')
    op.drop_table('taskitem')
    op.drop_table('taskdate')
    # ### end Alembic commands ###