#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract_base64_authorization_header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        r = authorization_header.split(' ')[-1]
        return r
