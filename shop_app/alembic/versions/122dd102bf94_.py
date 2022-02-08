"""empty message

Revision ID: 122dd102bf94
Revises: ad2b210e2008
Create Date: 2022-02-08 23:38:26.951364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122dd102bf94'
down_revision = 'ad2b210e2008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('art_code', sa.Integer(), nullable=True))
    op.drop_column('article', 'code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('code', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('article', 'art_code')
    # ### end Alembic commands ###
