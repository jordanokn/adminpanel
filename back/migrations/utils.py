import sqlalchemy as sa


def audit_fields() -> list[sa.Column]:
    return [
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=False),
            nullable=False,
            server_default=sa.text("clock_timestamp()"),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=False),
            nullable=False,
            server_default=sa.text("clock_timestamp()"),
            server_onupdate=sa.text("clock_timestamp()"),
        ),
    ]
