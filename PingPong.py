import pygame
import sys


pygame.init()


LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Ping Pong")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


RAQUETE_LARGURA, RAQUETE_ALTURA = 10, 100
BOLA_TAMANHO = 15


VEL_RAQUETE = 5
VEL_BOLA = 4


raquete_esquerda = pygame.Rect(20,(ALTURA // 2) - (RAQUETE_ALTURA // 2), RAQUETE_LARGURA, RAQUETE_ALTURA)
raquete_direita = pygame.Rect(LARGURA - 30, (ALTURA // 2) - (RAQUETE_ALTURA // 2), RAQUETE_LARGURA, RAQUETE_ALTURA)


bola = pygame.Rect(LARGURA // 2, ALTURA // 2, BOLA_TAMANHO, BOLA_TAMANHO)
bola_vel_x, bola_vel_y = VEL_BOLA, VEL_BOLA


placar_esquerda = 0
placar_direita = 0


fonte = pygame.font.Font(None, 50)


def desenhar():
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, BRANCO, raquete_esquerda)
    pygame.draw.rect(TELA, BRANCO, raquete_direita)
    pygame.draw.ellipse(TELA, BRANCO, bola)
    pygame.draw.aaline(TELA, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    texto_placar = fonte.render(f"{placar_esquerda} - {placar_direita}", True, BRANCO)
    TELA.blit(texto_placar, (LARGURA // 2 - texto_placar.get_width() // 2, 20))

    pygame.display.flip()

tempo_ultimo_ponto = pygame.time.get_ticks()
TEMPO_INCREMENTO = 5000
INCREMENTO_VELOCIDADE = 1

def mover_bola():
    global bola_vel_x, bola_vel_y, placar_esquerda, placar_direita, tempo_ultimo_ponto

    bola.x += bola_vel_x
    bola.y += bola_vel_y
    
    
    if bola.top <= 0 or bola.bottom >= ALTURA:
        bola_vel_y *= -1


    if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
            bola_vel_x *= -1


    if bola.left <=0:
            placar_direita += 1
            reiniciar_bola()
            tempo_ultimo_ponto = pygame.time.get_ticks()
    if bola.right >= LARGURA:
            placar_esquerda += 1
            reiniciar_bola()
            tempo_ultimo_ponto = pygame.time.get_ticks()
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_ultimo_ponto > TEMPO_INCREMENTO:
            bola_vel_x += INCREMENTO_VELOCIDADE if bola_vel_x > 0 else -INCREMENTO_VELOCIDADE
            bola_vel_y += INCREMENTO_VELOCIDADE if bola_vel_y > 0 else -INCREMENTO_VELOCIDADE
            tempo_ultimo_ponto = tempo_atual

def reiniciar_bola():
      global bola_vel_x, bola_vel_y
      bola.center = (LARGURA // 2, ALTURA // 2)
      bola_vel_x  = VEL_BOLA if bola_vel_x > 0 else -VEL_BOLA
      bola_vel_y = VEL_BOLA if bola_vel_y > 0 else -VEL_BOLA
      


def mover_raquetes():
      keys = pygame.key.get_pressed()


      if keys[pygame.K_w] and raquete_esquerda.top > 0:
            raquete_esquerda.y -= VEL_RAQUETE
      if  keys[pygame.K_s] and raquete_esquerda.bottom < ALTURA:
            raquete_esquerda.y += VEL_RAQUETE


      if keys[pygame.K_UP] and raquete_direita.top > 0:
            raquete_direita.y -= VEL_RAQUETE
      if keys[pygame.K_DOWN] and raquete_direita.bottom < ALTURA:
            raquete_direita.y += VEL_RAQUETE


relogio = pygame.time.Clock()
while True:
      for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
            
      mover_raquetes()
      mover_bola()
      desenhar()

      relogio.tick(60)