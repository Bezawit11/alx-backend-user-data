#!/usr/bin/env python3
"""hashpasswrd method"""


import bcrypt


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password, bcrypt.gensalt())
