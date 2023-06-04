#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """session authentication"""
    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        s_id = uuid4()
        self.user_id_by_session_id[s_id] = user_id
        return s_id
