# Funções básicas sobre curvas elípticas sobre Fp

def inverse_mod(k, p):
    """Retorna o inverso modular de k mod p (k⁻¹ mod p)."""
    return pow(k, -1, p)

def point_add(P, Q, a, p):
    """Soma de dois pontos P e Q na curva y² = x³ + ax + b sobre Fp."""
    if P is None: return Q
    if Q is None: return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return None  # P + (-P) = O (ponto no infinito)

    if P != Q:
        m = (y2 - y1) * inverse_mod(x2 - x1, p) % p
    else:
        m = (3 * x1**2 + a) * inverse_mod(2 * y1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P, a, p):
    """Multiplica escalarmente o ponto P por k: R = k * P."""
    R = None
    N = P
    while k > 0:
        if k & 1:
            R = point_add(R, N, a, p)
        N = point_add(N, N, a, p)
        k >>= 1
    return R

