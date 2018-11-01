import bcrypt

from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    registered_on = Column(DateTime, nullable=False)
    password_hash = Column(String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        # usar bcrypt direto
        self.password_hash = 'teste'

    def check_password(self, password):
        return password == 'teste'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
