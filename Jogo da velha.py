def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " ":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " ":
            return tabuleiro[0][i]
        
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
            return tabuleiro[0][0]
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
            return tabuleiro[0][2]
        
    return None
    

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    print("Bem Vindo ao Jogo da Velha!")
    exibir_tabuleiro(tabuleiro)

    for turno in range(9):
        print(f"Vez do jogador {jogador_atual}")

        while True:
            try:
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))

                if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                    print("Coordenadas inválidas! Tente novamente.")
                    continue

                if tabuleiro[linha][coluna] != " ":
                    print("Essa posição já está ocupada! Tente novamente.")
                    continue
                
                tabuleiro[linha][coluna] = jogador_atual
                break
            except ValueError:
                print("Entrada inválida! Digite números inteiros para linha e coluna.")
        
        exibir_tabuleiro(tabuleiro)
        vencedor = verificar_vencedor(tabuleiro)
        
        if vencedor:
            print(f"Parabéns! O jogador {vencedor} venceu!")
            return
        
        jogador_atual = "O" if jogador_atual =="X" else "X"

    print("Empate! O jogo terminou sem vencedor.")

if __name__ == "__main__":
    jogo_da_velha()