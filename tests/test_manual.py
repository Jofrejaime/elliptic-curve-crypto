# Teste automático da chave compartilhada no ECDH manual

import unittest
from core.ecdh import ecdh

class TestManualECC(unittest.TestCase):
    def test_ecdh_shared_key(self):
        p = 9739
        a = 497
        b = 1768
        G = (1804, 5368)
        privA = 1829
        privB = 4726

        _, _, sharedA, sharedB = ecdh(p, a, b, G, privA, privB)
        self.assertEqual(sharedA, sharedB)

if __name__ == "__main__":
    unittest.main()
# Teste manual da assinatura digital com a biblioteca ecdsa