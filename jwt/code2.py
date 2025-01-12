from jwcrypto import jwk

key = jwk.JWK.generate(kty="RSA", size=2048, alg="RSA-OAEP-256", use="enc", kid="12345")
public_key = key.export_public()
private_key = key.export_private()
print(private_key)
print(public_key)
