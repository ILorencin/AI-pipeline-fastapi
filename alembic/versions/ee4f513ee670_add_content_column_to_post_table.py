"""add content column to post table

Revision ID: ee4f513ee670
Revises: c86535ac7e95
Create Date: 2023-11-10 12:09:14.387539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee4f513ee670'
down_revision: Union[str, None] = 'c86535ac7e95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
