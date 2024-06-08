from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from backend.src.database.base import Base


class UserModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
