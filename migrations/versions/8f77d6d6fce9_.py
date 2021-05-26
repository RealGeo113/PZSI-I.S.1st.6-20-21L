"""empty message

Revision ID: 8f77d6d6fce9
Revises: 
Create Date: 2021-05-22 15:32:51.433029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f77d6d6fce9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('username', sa.String(length=150), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('registration_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_banned', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('note',
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('creation_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('note_id')
    )
    op.create_table('private_message',
    sa.Column('private_message_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('user_sender_id', sa.Integer(), nullable=True),
    sa.Column('user_receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_receiver_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['user_sender_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('private_message_id')
    )
    op.create_table('roles_and_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('roomname', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('roomtype', sa.String(length=150), nullable=True),
    sa.Column('user_limit', sa.Integer(), nullable=True),
    sa.Column('accesstype', sa.String(length=150), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('room_id'),
    sa.UniqueConstraint('roomname')
    )
    op.create_table('user_relation',
    sa.Column('user_relation_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('relating_user_id', sa.Integer(), nullable=True),
    sa.Column('related_user_id', sa.Integer(), nullable=True),
    sa.Column('action_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['action_user_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['related_user_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['relating_user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_relation_id')
    )
    op.create_table('user_settings',
    sa.Column('user_settings_id', sa.Integer(), nullable=False),
    sa.Column('app_theme', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_settings_id')
    )
    op.create_table('allowed_participant',
    sa.Column('allowed_participant_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('allowed_participant_id')
    )
    op.create_table('blocked_participant',
    sa.Column('blocked_participant_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('blocked_participant_id')
    )
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_saved', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('participant',
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.room_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('participant_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant')
    op.drop_table('message')
    op.drop_table('blocked_participant')
    op.drop_table('allowed_participant')
    op.drop_table('user_settings')
    op.drop_table('user_relation')
    op.drop_table('room')
    op.drop_table('roles_and_users')
    op.drop_table('private_message')
    op.drop_table('note')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
