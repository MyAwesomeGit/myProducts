class Roles:
    permissions = {
        "administrator": ["create", "read", "update", "delete"],
        "user": ["read", "update"],
        "guest": ["read"]
    }
