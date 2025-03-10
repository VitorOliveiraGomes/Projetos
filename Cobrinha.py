import pygame
import sys
import random

pygame.init()

LARGURA, ALTURA = 600, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

TAMANHO_BLOCO = 20
FPS = 10

def exibir_mensagem(texto):
    fonte = pygame.font.Font(None, 50)
    mensagem = fonte.render(texto, True, VERMELHO)
    TELA.blit(mensagem, (LARGURA // 2 - mensagem.get_width() // 2, ALTURA // 2 - mensagem.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

def jogo():
    cobra = [[100, 100]]
    direcao = "DIREITA"

    comida = [random.randrange(0, LARGURA, TAMANHO_BLOCO), random.randrange(0, ALTURA, TAMANHO_BLOCO)]

    pontuacao = 0

    relogio = pygame.time.Clock()
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direcao != "BAIXO":
            direcao = "CIMA"
        if keys[pygame.K_DOWN] and direcao != "CIMA":
            direcao = "BAIXO"
        if keys[pygame.K_LEFT] and direcao != "DIREITA":
            direcao = "ESQUERDA"
        if keys[pygame.K_RIGHT] and direcao != "ESQUERDA":
            direcao = "DIREITA"

        x, y = cobra[0]
        if direcao == "CIMA":
            y -= TAMANHO_BLOCO
        if direcao == "BAIXO":
            y += TAMANHO_BLOCO
        if direcao == "ESQUERDA":
            x -= TAMANHO_BLOCO
        if direcao == "DIREITA":
            x += TAMANHO_BLOCO
        
        nova_cabeca = [x, y]
        cobra.insert(0, nova_cabeca)

        if nova_cabeca == comida:
            pontuacao += 1
            while comida in cobra:
                comida = [random.randrange(0, LARGURA, TAMANHO_BLOCO), random.randrange(0, ALTURA, TAMANHO_BLOCO)]
        else:
            cobra.pop()
        
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            exibir_mensagem(f"Fim de Jogo! Pontuação: {pontuacao}")
            rodando = False

        if nova_cabeca in cobra[1:]:
            exibir_mensagem(f"Fim de Jogo! Pontuação: {pontuacao}")
            rodando = False
        
        TELA.fill(PRETO)

        for segmento in cobra:
           pygame.draw.rect(TELA, VERDE, pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        pygame.draw.rect(TELA, VERMELHO, pygame.Rect(comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        
        pygame.display.flip()

        relogio.tick(FPS)

def main():
    while True:
        pontuacao = jogo()
        exibir_mensagem(f"Fim de Jogo! Pontuação: {pontuacao}")

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                esperando = False
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
main()