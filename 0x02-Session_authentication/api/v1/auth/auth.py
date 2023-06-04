#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Authenticate"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false"""
        if excluded_paths is None or excluded_paths == []:
            return True
        if path is None:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """return None"""
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        ses = getenv("SESSION_NAME")
        if ses is None:
            return None
        return request.cookies.get(ses)
