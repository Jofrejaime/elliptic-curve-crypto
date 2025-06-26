
from ecdsa import SigningKey, SECP256k1

def demo_ecdsa():
    msg = b"Curvas elípticas são seguras!"
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key
    sig = sk.sign(msg)
    print("Assinatura:", sig.hex())
    print("Assinatura válida?", vk.verify(sig, msg))
