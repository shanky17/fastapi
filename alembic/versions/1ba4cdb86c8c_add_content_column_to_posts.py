"""add content column to posts

Revision ID: 1ba4cdb86c8c
Revises: c5d557d294f7
Create Date: 2024-05-22 14:30:42.380988

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1ba4cdb86c8c"
down_revision: Union[str, None] = "c5d557d294f7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
