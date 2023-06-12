#!/usr/bin/env python3
"""hashpasswrd method"""


import bcrypt
from uuid import uuid4
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generates a string representation of uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """takes email and password arguments and returns
            a User object
        """
        if email is None or password is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pwd = _hash_password(password)
            new_user = self._db.add_user(email, pwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """validates login on user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                pwd = user.hashed_password
                if bcrypt.checkpw(password.encode('utf-8'), pwd):
                    return True
                return False
        except NoResultFound:
            return False
  
    def create_session(self, email: str) -> str:
        """creates a session id for the logged in user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """finds a user coressponding with the provided session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroys a user's session ID and updates it to none"""
        try:
            user = self._db.find_user_by(user_id=user_id)
            if user:
                a = {'session_id': None}
                self._db.update_user(user.id, a)
                return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """generates a reset token for a user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                token = _generate_uuid()
                self._db.update_user(user.id, reset_token=token)
                return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """updates password based on info provided"""
        if reset_token is None or password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            npwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=npwd)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
