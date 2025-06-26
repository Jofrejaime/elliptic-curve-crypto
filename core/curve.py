def inverse_mod(k, p):
    return pow(k, -1, p)

def point_add(P, Q, a, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return None
    if P != Q:
        m = (y2 - y1) * inverse_mod(x2 - x1, p) % p
    else:
        m = (3 * x1**2 + a) * inverse_mod(2 * y1, p) % p
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P, a, p):
    R = None
    N = P
    while k > 0:
        if k & 1:
            R = point_add(R, N, a, p)
        N = point_add(N, N, a, p)
        k >>= 1
    return R
