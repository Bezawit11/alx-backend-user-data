#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


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
        for e in excluded_paths:
            if e[-1] == '*':
                if path.startswith(e[:-1]):
                    return False
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
