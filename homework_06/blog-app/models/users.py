from sqlalchemy import Column, String, Integer
from .database import db
from .mixins import TimestampMixin


class Users(db.Model, TimestampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"

    def __str__(self):
        return f"Name: {self.name}   |   " \
               f"Username: {self.username}   |   " \
               f"Email: {self.email}   |   " \
               f"Created At {self.created_at}"
