import jwt
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "jwt.conjur.cyberark.com",
        "sub": 456765445687,
        "aud": "https://www.conjur.org/",
        "iat": now,
        "exp": (now + timedelta(hours=24)).timestamp(),
        "scope": "openid"
    }

    return jwt.encode(payload=payload, key="secret_key", algorithm="HS256")

# subprocess.call(["./keys.sh"])

print(generate_jwt())
f = open("token.txt", "w+")
f.write(generate_jwt())
f.close()