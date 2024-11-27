import json
from asyncio import exceptions

import requests

import jwt

OPERATION_JWT_JWKS_URL = "https://keycloak-dev.mateusmais.com.br/realms/operation/protocol/openid-connect/certs"
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3ZVZXVnhSUmxSblVncVBoSlFKNWZzQ3doSXRLeFlIRG5NVVp3SzF0UnR3In0.eyJleHAiOjE3MzI1NDE0NTgsImlhdCI6MTczMjU0MTE1OCwiYXV0aF90aW1lIjoxNzMyNTM3NDgzLCJqdGkiOiIwMDViYmM2Yy0xYTNhLTRhZDItOGQ3ZC1kY2Y3YmY3NzI2N2UiLCJpc3MiOiJodHRwczovL3Joc3NvLWRldi5ncnVwb21hdGV1cy5jb20uYnIvYXV0aC9yZWFsbXMvZ3J1cG9tYXRldXMiLCJhdWQiOiJnbXN1aXRlLW10bS1hbnRpZnJhdWRlIiwic3ViIjoiYzE3MjhiYWMtOGE0My00YzM1LWJhODItNjU1ZWE1ZWE2MDY5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZ21zdWl0ZSIsIm5vbmNlIjoiZTU0N2I3OWUtZDFmNi00NDY3LTg1N2MtYmViYjJjMTY1MDUwIiwic2Vzc2lvbl9zdGF0ZSI6IjhkZjlmMmUyLWYxYmMtNGQyYi1hMzhiLTZmYTI3YTkyMzNmMCIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1ncnVwb21hdGV1cyIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJnbXN1aXRlLW10bS1hbnRpZnJhdWRlIjp7InJvbGVzIjpbImFkbWluLWFudGlmcmF1ZGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwic2lkIjoiOGRmOWYyZTItZjFiYy00ZDJiLWEzOGItNmZhMjdhOTIzM2YwIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJodHRwczovL2hhc3VyYS5pby9qd3QvY2xhaW1zIjp7IngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6Imhhc3VyYS11c2VyIiwieC1oYXN1cmEtdXNlci1pZCI6ImMxNzI4YmFjLThhNDMtNGMzNS1iYTgyLTY1NWVhNWVhNjA2OSJ9LCJuYW1lIjoiVklMTUFSIEZFUlJFSVJBIEdPTUVTIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGowMDYzMDQ2IiwiZ2l2ZW5fbmFtZSI6IlZJTE1BUiIsImZhbWlseV9uYW1lIjoiRkVSUkVJUkEgR09NRVMifQ.ENjBewlBP6I2tiy4DmIfR1JJHeCheh56EYzMPjJ3hubpGDoHMDtqLttG0c7ccf-5lgHkbFejwcZBHMKLUDicQHxMBTDzhIYbO59Lv6ZU5LcYgUT2N1nR2c1slA9xkGsXx9wamFqhK6J_mw81Pz-8Dmj0iIioy3fBZm7vI4EPe9LFDnGFkybixQNzvblwIOssdNidFJJFWxUd5r-fTYEGt5QY8tuVk7_57ktAPoYZ0003dW8X9BWaw1I_nR-YFGIJJDdMCM-kIswJLqOXWpeBOhTAk66YwSKsdS0rfus6x34qbkpmpNlBiD9Yp6_mAKWmYCSqZau-2gJ4abwWEcPzPw"


class OperationsJWTAuthentication:
    def get_jwk_url(self):
        try:
            return str(OPERATION_JWT_JWKS_URL)
        except Exception:
            return None

    def get_header(self, request):
        authorization_header = request.headers.get("Authorization", None)
        if not authorization_header:
            return None
        if "Bearer " not in authorization_header:
            return None
        return authorization_header

    def get_token(self, header):
        return header.replace("Bearer ", "")

    def get_alg_kid(self, token):
        token_header = jwt.get_unverified_header(token)
        return (token_header["alg"], token_header["kid"])

    def get_key(self, url, kid):
        server_keys_response = requests.get(url)
        token_key = server_keys_response.json()
        public_keys = {}
        for jwk in token_key["keys"]:
            kid = jwk["kid"]
            public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

        key = public_keys[kid]
        return key

    def decode(self, token, alg, key):
        try:
            token_data = jwt.decode(
                token, algorithms=[alg], key=key, audience="account"
            )
            return token_data
        except jwt.exceptions.ExpiredSignatureError:
            raise Exception("token expirado")
        except Exception:
            raise Exception("falha ao validar token")

    # def get_user(self, token_data):
    #     try:
    #         email = token_data["email"]
    #         user = User.objects.get(email=email)
    #         return user
    #     except User.DoesNotExist:
    #         raise exceptions.AuthenticationFailed("usuario não existe")

    def authenticate(self):
        jwk_url = self.get_jwk_url()
        if not jwk_url:
            return None

        # header = self.get_header(request)
        # if not header:
        #     return None

        try:
            # token = self.get_token(header)
            alg, kid = self.get_alg_kid(TOKEN)
            key = self.get_key(jwk_url, kid)
        except Exception:
            raise exceptions.AuthenticationFailed("falha ao validar token")

        token_data = self.decode(TOKEN, alg, key)
        print("token_data", token_data)
        # user = self.get_user(token_data)

        # return (user, None)
        return None


op = OperationsJWTAuthentication()

print(op.get_alg_kid(TOKEN))
op.authenticate()
