#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authenticate"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """return None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
