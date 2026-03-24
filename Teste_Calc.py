def calculadora_inversa(matriz):
    a, b = matriz[0]
    c, d = matriz[1]

    determinante = a * d - b * c

    if determinante == 0:
        return None

    inversa = [
        [d / determinante, -b / determinante],
        [-c / determinante, a / determinante]
    ]
    return inversa


def exibir_matriz(matriz):
    for linha in matriz:
        print(f"[ {linha[0]:7.0f}  {linha[1]:7.0f} ]")


def main():
    print("Calculadora de Inversa de Matrizes de ordem 2x2! \n")
    nome = input("Informe o seu nome: ")

    print(f"\nOlá, {nome}! Vamos calcular a inversa de uma matriz 2x2.")
    print("Digite os elementos da matriz na forma:")
    print("[[a, b], [c, d]]\n")

    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Faça o mesmo com b: "))
        c = float(input("Agora com c: "))
        d = float(input("Por fim, o valor de d: "))

        matriz = [[a, b], [c, d]]
        inversa = calculadora_inversa(matriz)

        print("\nMatriz original:")
        exibir_matriz(matriz)

        if inversa:
            print("\nMatriz inversa:")
            exibir_matriz(inversa)
        else:
            print("\nEssa matriz não possui uma inversa (O determinante é = 0).")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")


if __name__ == "__main__":
    main()
