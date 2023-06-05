#!/usr/bin/env python3
""" User module
"""
import hashlib
from models.base import Base


class UserSession(Base):
    """usersession class"""
    def __init__(self, *args: list, **kwargs: dict):
        """initialize usersession instance"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
