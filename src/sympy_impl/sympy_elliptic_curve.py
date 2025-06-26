from sympy import symbols, Eq, solve, mod_inverse

class SympyEllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.validate_curve()

    def validate_curve(self):
        # Check if the curve is non-singular
        if (4 * self.a**3 + 27 * self.b**2) % self.p == 0:
            raise ValueError("The curve is singular.")

    def is_on_curve(self, x, y):
        # Check if the point (x, y) lies on the curve
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        
        x1, y1 = P
        x2, y2 = Q

        if P == Q:
            # Point doubling
            m = (3 * x1**2 + self.a) * mod_inverse(2 * y1, self.p) % self.p
        else:
            # Point addition
            m = (y2 - y1) * mod_inverse(x2 - x1, self.p) % self.p

        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiplication(self, k, P):
        R = None
        for i in range(k.bit_length() - 1, -1, -1):
            R = self.point_addition(R, R)  # Double the point
            if (k >> i) & 1:
                R = self.point_addition(R, P)  # Add the point
        return R

    def get_curve_parameters(self):
        return self.a, self.b, self.p