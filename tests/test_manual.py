import unittest
from src.manual.elliptic_curve import EllipticCurve
from src.manual.keygen import KeyGenerator

class TestEllipticCurve(unittest.TestCase):

    def setUp(self):
        # Define a sample elliptic curve y^2 = x^3 + ax + b over a finite field
        self.a = 2
        self.b = 3
        self.p = 97  # A prime number for the finite field
        self.curve = EllipticCurve(self.a, self.b, self.p)

    def test_point_addition(self):
        # Test point addition on the elliptic curve
        P = (3, 6)
        Q = (10, 7)
        R = self.curve.add_points(P, Q)
        expected_R = (6, 4)  # Expected result of P + Q
        self.assertEqual(R, expected_R)

    def test_point_doubling(self):
        # Test point doubling on the elliptic curve
        P = (3, 6)
        R = self.curve.double_point(P)
        expected_R = (80, 10)  # Expected result of 2P
        self.assertEqual(R, expected_R)

    def test_scalar_multiplication(self):
        # Test scalar multiplication on the elliptic curve
        P = (3, 6)
        k = 2
        R = self.curve.scalar_multiply(k, P)
        expected_R = (80, 10)  # Expected result of kP
        self.assertEqual(R, expected_R)

class TestKeyGenerator(unittest.TestCase):

    def setUp(self):
        self.curve = EllipticCurve(2, 3, 97)
        self.keygen = KeyGenerator(self.curve)

    def test_key_generation(self):
        private_key, public_key = self.keygen.generate_keypair()
        self.assertIsInstance(private_key, int)
        self.assertIsInstance(public_key, tuple)
        self.assertEqual(len(public_key), 2)

if __name__ == '__main__':
    unittest.main()