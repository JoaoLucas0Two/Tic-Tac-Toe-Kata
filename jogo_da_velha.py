def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    print("\n   1   2   3")
    for i, linha in enumerate(tabuleiro):
        print(" " + "-" * 13)
        print(f"{i + 1}| {' | '.join(linha)} |")
    print(" " + "-" * 13)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(campo == jogador for campo in linha):
            return True
    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(campo != " " for linha in tabuleiro for campo in linha)

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        print(f"\nVez do jogador {jogador_atual}")
        exibir_tabuleiro(tabuleiro)

        try:
            linha = int(input("Escolha a linha (1, 2, 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2, 3): ")) - 1
        except ValueError:
            print("Entrada inválida. Use números de 1 a 3.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição fora do tabuleiro. Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Campo já ocupado. Escolha outro.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"\nJogador {jogador_atual} venceu!")
            break
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("\nEmpate! Todos os campos foram preenchidos.")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()
