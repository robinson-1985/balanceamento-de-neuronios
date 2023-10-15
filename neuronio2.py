def main():
    # Declaração das Entradas
    X = [
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]
    Ye = [0, 1, 1, 1]
    W = [0, 0, 0]

    # Áreas de Trabalho
    Neta = 1.0

    for Ep in range(1, 6):  # Para cada Época, faça
        for i in range(4):  # Aplicando Todos padrões de Entrada
            print(f"\n {Ep} W0 = {W[0]:.1f} W1 = {W[1]:.1f} W2 = {W[2]:.1f}")
            Soma = 0
            for j in range(3):  # Para cada entrada gere a Soma
                Soma = Soma + X[i][j] * W[j]
            if Soma > 0:
                Ys = 1
            else:
                Ys = 0  # Ativação do Neurônio
            Erro = Ye[i] - Ys  # Cálculo do Erro
            if Erro != 0:  # Teste do Erro
                for j in range(3):  # Alteração dos Pesos
                    W[j] = W[j] + Neta * Erro * X[i][j]
            input()

    print("\n  Acabou")

if __name__ == "__main__":
    main()

