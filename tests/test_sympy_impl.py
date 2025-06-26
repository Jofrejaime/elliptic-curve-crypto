import unittest
from src.sympy_impl.sympy_elliptic_curve import SympyEllipticCurve

class TestSympyEllipticCurve(unittest.TestCase):

    def setUp(self):
        # Define a sample elliptic curve y^2 = x^3 + ax + b over a finite field
        self.a = 2
        self.b = 3
        self.curve = SympyEllipticCurve(self.a, self.b)

    def test_point_addition(self):
        # Test point addition on the elliptic curve
        P = (3, 6)
        Q = (9, 7)
        R = self.curve.add_points(P, Q)
        expected_R = (6, 8)  # Expected result of P + Q
        self.assertEqual(R, expected_R)

    def test_point_doubling(self):
        # Test point doubling on the elliptic curve
        P = (3, 6)
        R = self.curve.double_point(P)
        expected_R = (9, 7)  # Expected result of 2P
        self.assertEqual(R, expected_R)

    def test_scalar_multiplication(self):
        # Test scalar multiplication on the elliptic curve
        P = (3, 6)
        k = 2
        R = self.curve.scalar_multiply(k, P)
        expected_R = (9, 7)  # Expected result of 2P
        self.assertEqual(R, expected_R)

    def test_curve_non_singularity(self):
        # Test the non-singularity condition of the curve
        self.assertTrue(self.curve.is_non_singular())

if __name__ == '__main__':
    unittest.main()