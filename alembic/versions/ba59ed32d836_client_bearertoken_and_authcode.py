"""Client, BearerToken and AuthCode

Revision ID: ba59ed32d836
Revises: 3d0645977378
Create Date: 2018-11-28 21:23:10.376907

"""

# revision identifiers, used by Alembic.
revision = 'ba59ed32d836'
down_revision = '3d0645977378'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('grant_type', sa.String(length=18), nullable=True),
    sa.Column('response_type', sa.String(length=4), nullable=True),
    sa.Column('scopes', sa.Text(), nullable=True),
    sa.Column('redirect_urls', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('authcode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('scopes', sa.Text(), nullable=True),
    sa.Column('code', sa.String(length=100), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('bearertokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('scopes', sa.Text(), nullable=True),
    sa.Column('access_token', sa.String(length=100), nullable=True),
    sa.Column('refresh_token', sa.String(length=100), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('refresh_token')
    )
    op.drop_table('beaker_cache')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beaker_cache',
    sa.Column('namespace', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('accessed', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('namespace', name='beaker_cache_pkey')
    )
    op.drop_table('bearertokens')
    op.drop_table('authcode')
    op.drop_table('clients')
    # ### end Alembic commands ###
