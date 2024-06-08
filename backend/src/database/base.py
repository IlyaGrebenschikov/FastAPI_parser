from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):
    __abstract__: bool = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
