"""v0.9.0 migration

Revision ID: 7217cc0eee8c
Revises: 0158771b9f18
Create Date: 2025-02-12 12:06:28.789923

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = "7217cc0eee8c"
down_revision: Union[str, None] = "0158771b9f18"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "server_settings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "units",
            sa.Integer(),
            nullable=False,
            comment="User units (one digit)(1 - metric, 2 - imperial)",
        ),
        sa.Column(
            "public_shareable_links",
            sa.Boolean(),
            nullable=False,
            comment="Allow public shareable links (true - yes, false - no)",
        ),
        sa.Column(
            "public_shareable_links_user_info",
            sa.Boolean(),
            nullable=False,
            comment="Allow show user info on public shareable links (true - yes, false - no)",
        ),
        sa.CheckConstraint("id = 1", name="single_row_check"),
        sa.PrimaryKeyConstraint("id"),
    )
    # Add the new entry to the server_settings table
    op.execute(
        """
    INSERT INTO server_settings (id, units, public_shareable_links, public_shareable_links_user_info) VALUES
    (1, 1, FALSE, FALSE);
    """
    )
    # Create table for users_default_gear
    op.create_table(
        "users_default_gear",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False,
            comment="User ID that the default gear belongs",
        ),
        sa.Column(
            "run_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default run activity type belongs",
        ),
        sa.Column(
            "trail_run_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default trail run activity type belongs",
        ),
        sa.Column(
            "virtual_run_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default virtual run activity type belongs",
        ),
        sa.Column(
            "ride_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default ride activity type belongs",
        ),
        sa.Column(
            "gravel_ride_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default gravel ride activity type belongs",
        ),
        sa.Column(
            "mtb_ride_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default MTB ride activity type belongs",
        ),
        sa.Column(
            "virtual_ride_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default virtual ride activity type belongs",
        ),
        sa.Column(
            "ows_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default OWS activity type belongs",
        ),
        sa.Column(
            "walk_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default walk activity type belongs",
        ),
        sa.Column(
            "hike_gear_id",
            sa.Integer(),
            nullable=True,
            comment="Gear ID that the default hike activity type belongs",
        ),
        sa.ForeignKeyConstraint(
            ["gravel_ride_gear_id"], ["gear.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["hike_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["mtb_ride_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["ows_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["ride_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["run_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["trail_run_gear_id"], ["gear.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["virtual_ride_gear_id"], ["gear.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["virtual_run_gear_id"], ["gear.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["walk_gear_id"], ["gear.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_users_default_gear_gravel_ride_gear_id"),
        "users_default_gear",
        ["gravel_ride_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_hike_gear_id"),
        "users_default_gear",
        ["hike_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_mtb_ride_gear_id"),
        "users_default_gear",
        ["mtb_ride_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_ows_gear_id"),
        "users_default_gear",
        ["ows_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_ride_gear_id"),
        "users_default_gear",
        ["ride_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_run_gear_id"),
        "users_default_gear",
        ["run_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_trail_run_gear_id"),
        "users_default_gear",
        ["trail_run_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_user_id"),
        "users_default_gear",
        ["user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_virtual_ride_gear_id"),
        "users_default_gear",
        ["virtual_ride_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_virtual_run_gear_id"),
        "users_default_gear",
        ["virtual_run_gear_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_users_default_gear_walk_gear_id"),
        "users_default_gear",
        ["walk_gear_id"],
        unique=False,
    )
    # Insert a default row for each user
    connection = op.get_bind()
    connection.execute(text("INSERT INTO users_default_gear (user_id) SELECT id FROM users;"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # drop table for server_settings
    op.drop_table("server_settings")
    # drop table for users_default_gear
    op.drop_index(
        op.f("ix_users_default_gear_walk_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_virtual_run_gear_id"),
        table_name="users_default_gear",
    )
    op.drop_index(
        op.f("ix_users_default_gear_virtual_ride_gear_id"),
        table_name="users_default_gear",
    )
    op.drop_index(
        op.f("ix_users_default_gear_user_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_trail_run_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_run_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_ride_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_ows_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_mtb_ride_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_hike_gear_id"), table_name="users_default_gear"
    )
    op.drop_index(
        op.f("ix_users_default_gear_gravel_ride_gear_id"),
        table_name="users_default_gear",
    )
    op.drop_table("users_default_gear")
    # ### end Alembic commands ###
