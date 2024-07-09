#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic_auth import BasicAuth

auth = BasicAuth()

print(auth.extract_user_credentials(None))
print(auth.extract_user_credentials(89))
print(auth.extract_user_credentials("Holberton School"))
print(auth.extract_user_credentials("Holberton:School"))
print(auth.extract_user_credentials("bob@gmail.com:toto1234"))
