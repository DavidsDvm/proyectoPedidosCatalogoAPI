from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_email = Column(String(50), nullable=False, unique=True)
    user_namevarchar = Column(String(80), nullable=False)
    user_passwordvarchar = Column(String(50), nullable=False)

    def __init__(self, user_email, user_namevarchar, user_passwordvarchar):
        self.user_email = user_email
        self.user_namevarchar = user_namevarchar
        self.user_passwordvarchar = user_passwordvarchar