#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, bool, TypeVar


class Auth:
    """Authenticate"""
    
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false"""
        return False


    def authorization_header(self, request=None) -> str:
        """return None"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """return None"""
        return None
