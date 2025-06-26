from .curve import scalar_mult

def ecdh(p, a, b, G, privA, privB):
    pubA = scalar_mult(privA, G, a, p)
    pubB = scalar_mult(privB, G, a, p)
    sharedA = scalar_mult(privA, pubB, a, p)
    sharedB = scalar_mult(privB, pubA, a, p)
    return sharedA, sharedB
