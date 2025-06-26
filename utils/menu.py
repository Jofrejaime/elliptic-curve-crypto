from core.ecdh import ecdh

def menu():
    print("=== ECC - Simulação ECDH ===")
    p = int(input("Primo p: "))
    a = int(input("Coeficiente a: "))
    b = int(input("Coeficiente b: "))
    Gx = int(input("G.x: "))
    Gy = int(input("G.y: "))
    G = (Gx, Gy)
    privA = int(input("Chave privada Alice: "))
    privB = int(input("Chave privada Bob: "))

    sharedA, sharedB = ecdh(p, a, b, G, privA, privB)
    print(f"\nChave de Alice: {sharedA}")
    print(f"Chave de Bob:   {sharedB}")
    print("Chave compartilhada correta!" if sharedA == sharedB else "Erro na chave!")
