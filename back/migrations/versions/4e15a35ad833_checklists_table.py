"""checklists table

Revision ID: 4e15a35ad833
Revises:
Create Date: 2025-07-14 08:14:42.931350

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from migrations.utils import audit_fields

# revision identifiers, used by Alembic.
revision: str = "4e15a35ad833"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    default = audit_fields()
    op.create_table(
        "checklists",
        *default,
    )

    op.create_table(
        "checklists_points",
        *default,
        sa.Column(
            "checklist_id", sa.Integer(), sa.ForeignKey("checklists.id"), nullable=False
        ),
        sa.Column("pointname", sa.String()),
    )

    op.create_table(
        "checklists_points_record",
        *default,
        sa.Column(
            "checklists_point_id",
            sa.Integer(),
            sa.ForeignKey(
                "checklists_points.id",
            ),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.Boolean(),
            server_default=sa.text("false"),
        ),
        sa.Column("description", sa.String(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("checklists")
    op.drop_table("checklists_points")
    op.drop_table("checklists_points_record")
