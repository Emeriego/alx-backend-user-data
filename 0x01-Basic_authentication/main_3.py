#!/usr/bin/env python3
""" Main 3
"""
from api.v1.auth.basic_auth import BasicAuth

auth = BasicAuth()

print(auth.decode_base64_authorization_header(None))
print(auth.decode_base64_authorization_header(89))
print(auth.decode_base64_authorization_header("Holberton School"))
print(auth.decode_base64_authorization_header("SG9sYmVydG9u"))
print(auth.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
print(auth.decode_base64_authorization_header(auth.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))
