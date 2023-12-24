from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '9426142a11c3'
down_revision: Union[str, None] = '1bc4290e4d11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        -- SQL commands to implement the changes for adding methods to models
        -- For example, you can create stored procedures, functions, etc.
    """)


def downgrade() -> None:

    op.execute("""
        -- SQL commands to revert the changes made in the upgrade function
    """)
