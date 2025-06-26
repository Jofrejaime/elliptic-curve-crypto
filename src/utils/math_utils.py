def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, p):
    if gcd(a, p) != 1:
        raise ValueError("Inverse does not exist")
    return pow(a, p - 2, p)

def modular_add(a, b, p):
    return (a + b) % p

def modular_subtract(a, b, p):
    return (a - b) % p

def modular_multiply(a, b, p):
    return (a * b) % p

def modular_divide(a, b, p):
    return (a * mod_inverse(b, p)) % p if b != 0 else None

def is_square(n, p):
    return pow(n, (p - 1) // 2, p) == 1

def sqrt_mod(n, p):
    if not is_square(n, p):
        raise ValueError("No square root exists")
    # Tonelli-Shanks algorithm or other methods can be implemented here for efficiency
    for x in range(p):
        if (x * x) % p == n:
            return x
    return None