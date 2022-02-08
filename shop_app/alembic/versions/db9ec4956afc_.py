"""empty message

Revision ID: db9ec4956afc
Revises: 4c2eb02f0976
Create Date: 2022-02-08 21:21:48.962104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9ec4956afc'
down_revision = '4c2eb02f0976'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('art_shop', sa.Column('rest', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('art_shop', 'rest')
    # ### end Alembic commands ###