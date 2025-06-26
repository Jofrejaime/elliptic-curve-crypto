# Implementação do protocolo ECDH manual

from .curve import scalar_mult

def ecdh(p, a, b, G, privA, privB):
    """Retorna as chaves compartilhadas de Alice e Bob."""
    pubA = scalar_mult(privA, G, a, p)
    pubB = scalar_mult(privB, G, a, p)
    sharedA = scalar_mult(privA, pubB, a, p)
    sharedB = scalar_mult(privB, pubA, a, p)
    return pubA, pubB, sharedA, sharedB
