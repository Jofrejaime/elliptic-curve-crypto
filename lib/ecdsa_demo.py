# Demonstração de assinatura digital com biblioteca ecdsa

from ecdsa import SigningKey, SECP256k1

def run_ecdsa_demo():
    """Assina uma mensagem e verifica a assinatura usando a biblioteca ecdsa."""
    message = input("Digite a mensagem a ser assinada: ").encode()

    # Gerar chave privada e pública
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key

    # Assinar a mensagem
    signature = sk.sign(message)
    print(f"\nAssinatura (hex): {signature.hex()}")

    # Verificar assinatura
    if vk.verify(signature, message):
        print("✅ Assinatura válida.")
    else:
        print("❌ Assinatura inválida.")
