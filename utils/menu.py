# Menu interativo com entrada de dados e execução das operações do projeto

from core.curve import point_add, scalar_mult
from core.ecdh import ecdh
from lib.ecdsa_demo import run_ecdsa_demo

def get_curve_parameters():
    """Lê os parâmetros da curva elíptica do usuário."""
    p = int(input("Digite o valor de p (primo): "))
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    return p, a, b

def get_point(name):
    """Lê um ponto (x, y) do usuário."""
    x = int(input(f"{name}.x = "))
    y = int(input(f"{name}.y = "))
    return (x, y)

def menu():
    while True:
        print("\n====== MENU - CRIPTOGRAFIA COM CURVAS ELÍPTICAS ======")
        print("1. Adição de dois pontos (P + Q)")
        print("2. Multiplicação escalar de um ponto (n * P)")
        print("3. Simulação do protocolo ECDH")
        print("4. Assinatura digital com ECDSA (lib ecdsa)")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            p, a, b = get_curve_parameters()
            print("\nDigite o ponto P:")
            P = get_point("P")
            print("\nDigite o ponto Q:")
            Q = get_point("Q")
            R = point_add(P, Q, a, p)
            print(f"\nResultado: P + Q = {R}")

        elif op == '2':
            p, a, b = get_curve_parameters()
            print("\nDigite o ponto P:")
            P = get_point("P")
            k = int(input("Digite o escalar k: "))
            R = scalar_mult(k, P, a, p)
            print(f"\nResultado: {k} * P = {R}")

        elif op == '3':
            p, a, b = get_curve_parameters()
            print("\nDigite o ponto base G:")
            G = get_point("G")
            privA = int(input("Digite a chave privada de Alice: "))
            privB = int(input("Digite a chave privada de Bob: "))

            pubA, pubB, sharedA, sharedB = ecdh(p, a, b, G, privA, privB)

            print(f"\n🔐 Chave pública de Alice: {pubA}")
            print(f"🔐 Chave pública de Bob:   {pubB}")
            print(f"\n🔑 Chave compartilhada de Alice: {sharedA}")
            print(f"🔑 Chave compartilhada de Bob:   {sharedB}")

            if sharedA == sharedB:
                print("✅ Sucesso: As chaves compartilhadas coincidem!")
            else:
                print("❌ Erro: As chaves não coincidem!")

        elif op == '4':
            print("\nExecutando demonstração de assinatura digital com ECDSA...")
            run_ecdsa_demo()

        elif op == '0':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
