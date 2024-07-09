#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

auth = Auth()

print(auth.require_auth(None, None))
print(auth.require_auth(None, []))
print(auth.require_auth("/api/v1/status/", []))
print(auth.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(auth.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(auth.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(auth.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
