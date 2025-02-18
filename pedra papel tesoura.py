import random

def pedra_papel_tesoura():
    opcoes = ['pedra' , 'papel' , 'tesoura']
    
    print("Bem vindo ao Jogo de Pedra, Papel e Tesoura!")
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou digite 'sair' para encerrar)").lower()
        
        if jogador == 'sair':
            print("jogo encerrado. Obrigado por jogar!")
            break
        if jogador not in opcoes:
            print("Escolha inválida! Tente novamente.")
            continue


        computador = random.choice(opcoes)
        print(f"Você escolher: {jogador}")
        print(f"O computador escolher: {computador}")

        if jogador == computador:
            print("Empate!")
        elif(jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        print("-")

if __name__ == "__main__":
    pedra_papel_tesoura()    