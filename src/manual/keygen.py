class KeyGenerator:
    def __init__(self, curve):
        self.curve = curve

    def generate_private_key(self):
        import random
        return random.randint(1, self.curve.order - 1)

    def derive_public_key(self, private_key):
        return self.curve.scalar_multiply(private_key, self.curve.generator)