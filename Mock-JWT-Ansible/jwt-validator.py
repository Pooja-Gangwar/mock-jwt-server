from pathlib import Path

import jwt
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
        audience="https://coffeemesh.io/orders",
    )


token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJqd3QuY29uanVyLmN5YmVyYXJrLmNvbSIsInN1YiI6NDU2NzY1NDQ1Njg3LCJhdWQiOiJodHRwczovL2NvZmZlZW1lc2guaW8vb3JkZXJzIiwiaWF0IjoxNjY1NDg0ODU3LCJleHAiOjE2NjU1NzEyNTcuOTIwMTM5fQ.GZuvhcQJUdl1y1-gBTwabIKKpN8DnoGX9TibNJoajp8tkmjG0MMeCjeawZt_OEjyUIw4Vo_b0dap5bUBW5qEUzzo8a4IKAzo8mS4_DsXp0Y_NKaFYelsenE7BmttQDWCLnf8J7c86J-WMT_WjzEJ1hKXr6mByKzLTpfFI0nT_hAG4m6Kwh-bHRNH5ZuvkWXzTglUSBxcfZi0zQ8I-n-2CxtFrOcmJqGK4b6ShiCBPRjjUmUnniEedzpwzyNrXidEbgKQoUGWOdVZWprvuY1lAuxoVZKjQtIRnQk7h4ZBNYZk2PswngY2yURLkgaHR45XhQfqi3WKG50MOy7B7HSaQA"

print(decode_and_validate_token(token))