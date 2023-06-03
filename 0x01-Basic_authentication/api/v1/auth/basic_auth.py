#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """decodes base64"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            d = b64decode(base64_authorization_header.encode('utf-8'))
            return d.decode('utf-8')
        except BaseException:
            return None
