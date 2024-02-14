"""Create user table

Revision ID: 395483af9a87
Revises: 
Create Date: 2024-02-14 15:24:58.621124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "395483af9a87"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("USER_ID", sa.String(length=20), nullable=False),
        sa.Column("NAME", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("USER_ID"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
