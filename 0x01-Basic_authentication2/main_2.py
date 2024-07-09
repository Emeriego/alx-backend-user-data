#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.basic_auth import BasicAuth

auth = BasicAuth()

print(auth.extract_base64_authorization_header(None))
print(auth.extract_base64_authorization_header(89))
print(auth.extract_base64_authorization_header("Holberton School"))
print(auth.extract_base64_authorization_header("Basic Holberton"))
print(auth.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(auth.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(auth.extract_base64_authorization_header("Basic1234"))
