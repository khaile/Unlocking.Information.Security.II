from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')


def sign(m, private_key):
    rsa_private_key = RSA.importKey(private_key)
    return pow(m, rsa_private_key.d, rsa_private_key.n)


def verify(m, s, public_key):
    rsa_public_key = RSA.importKey(public_key)
    return pow(s, rsa_public_key.e, rsa_public_key.n) == m


sig = sign(9, private_key)
print(verify(9, sig, public_key))
