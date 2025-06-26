import unittest
from src.ecdsa_impl.ecdsa_example import ECDSAExample

class TestECDSAExample(unittest.TestCase):

    def setUp(self):
        self.ecdsa = ECDSAExample()
        self.message = b'Test message for ECDSA'
        self.private_key, self.public_key = self.ecdsa.generate_keys()

    def test_signing(self):
        signature = self.ecdsa.sign_message(self.private_key, self.message)
        self.assertIsNotNone(signature)

    def test_verification(self):
        signature = self.ecdsa.sign_message(self.private_key, self.message)
        is_valid = self.ecdsa.verify_signature(self.public_key, self.message, signature)
        self.assertTrue(is_valid)

    def test_invalid_verification(self):
        signature = self.ecdsa.sign_message(self.private_key, self.message)
        altered_message = b'Altered message'
        is_valid = self.ecdsa.verify_signature(self.public_key, altered_message, signature)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()