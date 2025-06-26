class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

        if not self.is_non_singular():
            raise ValueError("The curve is singular.")

    def is_non_singular(self):
        return (4 * self.a**3 + 27 * self.b**2) % self.p != 0

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        if P != Q:
            slope = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, self.p) % self.p
        else:
            slope = (3 * P[0]**2 + self.a) * pow(2 * P[1], -1, self.p) % self.p

        x_r = (slope**2 - P[0] - Q[0]) % self.p
        y_r = (slope * (P[0] - x_r) - P[1]) % self.p

        return (x_r, y_r)

    def point_doubling(self, P):
        return self.point_addition(P, P)

    def scalar_multiplication(self, k, P):
        R = None
        for i in range(k.bit_length() - 1, -1, -1):
            R = self.point_doubling(R)  # Double the point
            if (k >> i) & 1:
                R = self.point_addition(R, P)  # Add the point if the bit is 1
        return R