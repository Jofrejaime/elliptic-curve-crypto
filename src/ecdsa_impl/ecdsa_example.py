class ECDSAExample:
    def __init__(self):
        from ecdsa import SigningKey, VerifyingKey, SECP256k1
        self.sk = SigningKey.generate(curve=SECP256k1)  # Private key
        self.vk = self.sk.get_verifying_key()  # Public key

    def sign_message(self, message):
        return self.sk.sign(message.encode())

    def verify_signature(self, message, signature):
        return self.vk.verify(signature, message.encode())

# Example usage
if __name__ == "__main__":
    ecdsa_example = ECDSAExample()
    message = "Hello, ECDSA!"
    signature = ecdsa_example.sign_message(message)

    print("Message:", message)
    print("Signature:", signature.hex())

    is_valid = ecdsa_example.verify_signature(message, signature)
    print("Is the signature valid?", is_valid)