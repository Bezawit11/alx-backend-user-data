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
        s_id = str(uuid4())
        self.user_id_by_session_id[s_id] = user_id
        return s_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        if self.session_cookie(request):
            c = self.session_cookie(request)
            i = self.user_id_for_session_id(c)
            return User.get(i)
        else:
            return None

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        s_id = self.session_cookie(request)
        if s_id is None:
            return False
        u_id = self.user_id_for_session_id(s_id)
        if not u_id:
            return False
        del self.user_id_by_session_id[s_id]
        return True
