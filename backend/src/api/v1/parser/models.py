from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from backend.src.database.base import Base


class ADModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    ad_id: Mapped[int]
    header: Mapped[str]
    author: Mapped[str]
    views: Mapped[int]
    position: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('usermodel.id', ondelete='CASCADE'), nullable=True)

