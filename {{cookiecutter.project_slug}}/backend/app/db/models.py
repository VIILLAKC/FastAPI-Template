from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import mapped_column

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True, index=True)
    email = mapped_column(String, unique=True, index=True, nullable=False)
    first_name = mapped_column(String)
    last_name = mapped_column(String)
    hashed_password = mapped_column(String, nullable=False)
    is_active = mapped_column(Boolean, default=True)
    is_superuser = mapped_column(Boolean, default=False)
