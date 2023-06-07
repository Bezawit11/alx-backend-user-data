#!/usr/bin/env python3
"""DB Module"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
      
    def add_user(self, email: str, hashed_password: str) -> User:
        """adds/saves new user to database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """finds user from database by querying"""
        for k in kwargs.keys():
            if k not in User.__table__.columns.keys():
                raise InvalidRequestError
        a = self._session.query(User).filter_by(**kwargs).first()
        if a is None:
            raise NoResultFound
        return a

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates users based on the given arguments"""
        user = find_user_by(kwargs)
        if user:
            self._session.query.filter(user).update(**kwargs)
        
