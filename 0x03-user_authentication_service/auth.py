#!/usr/bin/env python3
"""hashpasswrd method"""


import bcrypt
from user import User
from db import DB

def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password, bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
        
    def register_user(self, email: str, password: str) -> User:
        """takes email and password arguments and returns
            a User object
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f'User {email} already exists')
        pwd = _hash_password(password)
        new_user = self._db.add_user(email, pwd)
        return new_user

        
        
