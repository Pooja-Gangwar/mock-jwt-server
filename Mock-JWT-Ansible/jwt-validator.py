import jwt
from pathlib import Path
from cryptography.x509 import load_pem_x509_certificate


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    x509_certificate = load_pem_x509_certificate(
        Path("public_key.pem").read_text().encode()
    ).public_key()
    return jwt.decode(
        access_token,
        key=x509_certificate,
        algorithms=unverified_headers["alg"],
        audience="https://www.conjur.org/",
    )

token = Path("token.txt").read_text()
print(decode_and_validate_token(token))