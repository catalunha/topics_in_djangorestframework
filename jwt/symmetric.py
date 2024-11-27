import jwt

print("+++ Caso 01")
key = "secret"
tokenJwt = jwt.encode(payload={"some": "payload"}, key=key, algorithm="HS256")
print("tokenJwt", tokenJwt)
header = jwt.get_unverified_header(tokenJwt)
print("header", header)


payload = jwt.decode(tokenJwt, key, algorithms="HS256")
print("Assinatura correta. Pois usamos a mesma key para encode e decode")
print("payload", payload)

print("+++ Caso 02")
try:
    payload = jwt.decode(tokenJwt, "another_key", algorithms="HS256")
    print("payload", payload)
except jwt.exceptions.InvalidSignatureError:
    print("Erro na verificação da assinatura na etapa de decodificação do token.")
except Exception:
    print("Outro erro na decodificação do token.")
