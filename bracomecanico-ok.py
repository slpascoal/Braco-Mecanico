# feito por Silas Lopes Pascoal

import pygame
import math

# Iniciando o pygame
pygame.init()

# Definindo as cores usadas
BLACK = (0, 0, 0) #cor do braço
WHITE = (255, 255, 255) #fundo da tela

# Setando a tela
LARGURA_JANELA = 800
ALTURA_JANELA = 600
TITULO_JANELA = "Simulador: Braço Mecânico"
FPS = 60

# Configurando o braço mecânic e pinça
BASE_X = LARGURA_JANELA // 2
BASE_Y = ALTURA_JANELA - 50
LARGURA_BASE = 250
ALTURA_BASE = 10
COMPRIMENTO_BRACO = 150
COMPRIMENTO_ANTEBRACO = 150
COMPRIMENTO_PINCA = 20

# Declarando a tela
tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption(TITULO_JANELA)
relogio = pygame.time.Clock()

# Declarando a fonte
pygame.font.init()
fonte = pygame.font.SysFont('Arial', 24)

# Desenhar o braço mecânico na tela
def desenhar_braco(angulo_braco, angulo_antebraco, abertura_pinca):
    # Calculando as coordenadas do fim do braço
    fim_braco_x = BASE_X + COMPRIMENTO_BRACO * math.cos(angulo_braco)
    fim_braco_y = BASE_Y - COMPRIMENTO_BRACO * math.sin(angulo_braco)

    # Calculando as coordenadas do fim do antebraço
    fim_antebraco_x = fim_braco_x + COMPRIMENTO_ANTEBRACO * math.cos(angulo_braco + angulo_antebraco)
    fim_antebraco_y = fim_braco_y - COMPRIMENTO_ANTEBRACO * math.sin(angulo_braco + angulo_antebraco)

    # Calculando as coordenadas dos ganchos
    gancho1_x = fim_antebraco_x + COMPRIMENTO_PINCA * math.cos(angulo_braco + angulo_antebraco + abertura_pinca / 2)
    gancho1_y = fim_antebraco_y - COMPRIMENTO_PINCA * math.sin(angulo_braco + angulo_antebraco + abertura_pinca / 2)
    gancho2_x = fim_antebraco_x + COMPRIMENTO_PINCA * math.cos(angulo_braco + angulo_antebraco - abertura_pinca / 2)
    gancho2_y = fim_antebraco_y - COMPRIMENTO_PINCA * math.sin(angulo_braco + angulo_antebraco - abertura_pinca / 2)

    # Desenhando o braço mecânico
    pygame.draw.line(tela, BLACK, (BASE_X, BASE_Y), (fim_braco_x, fim_braco_y), 10)
    pygame.draw.line(tela, BLACK, (fim_braco_x, fim_braco_y), (fim_antebraco_x, fim_antebraco_y), 10)
    pygame.draw.line(tela, BLACK, (fim_antebraco_x, fim_antebraco_y), (gancho1_x, gancho1_y), 5)
    pygame.draw.line(tela, BLACK, (fim_antebraco_x, fim_antebraco_y), (gancho2_x, gancho2_y), 5)
    pygame.draw.rect(tela, BLACK, (BASE_X - LARGURA_BASE // 2, BASE_Y - ALTURA_BASE // 2, LARGURA_BASE, ALTURA_BASE))

# Escrever mensagem na tela
def desenhar_instrucoes():
    instrucoes = [
        '← e → para mover o braço',
        '↑ e ↓ para mover o antebraço',
        'W e S para abrir e fechar a pinça'
    ]
    for i, linha in enumerate(instrucoes):
        texto_renderizado = fonte.render(linha, True, BLACK)
        tela.blit(texto_renderizado, (10, 10 + i * 30))

# Main
executando = True
angulo_braco = 0
angulo_antebraco = 0
abertura_gancho = math.pi / 6  # Abertura inicial dos ganchos

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        angulo_antebraco += 0.05
    if teclas[pygame.K_DOWN]:
        angulo_antebraco -= 0.05
    if teclas[pygame.K_RIGHT]:
        angulo_braco -= 0.05
        if angulo_braco < 0:  # Limite inferior do braço
            angulo_braco = 0
    if teclas[pygame.K_LEFT]:
        angulo_braco += 0.05
        if angulo_braco > math.pi:  # Limite superior do braço
            angulo_braco = math.pi
    if teclas[pygame.K_w]:
        abertura_gancho += 0.05
        if abertura_gancho > math.pi:  # Limite superior da abertura da pinça
            abertura_gancho = math.pi
    if teclas[pygame.K_s]:
        abertura_gancho -= 0.05
        if abertura_gancho < 0:  # Limite inferior da abertura da pinça
            abertura_gancho = 0

    # Limpeza da tela
    tela.fill(WHITE)

    # Desenho do braço mecânico
    desenhar_braco(angulo_braco, angulo_antebraco, abertura_gancho)

    # Desenho das instruções
    desenhar_instrucoes()

    # Atualização da tela
    pygame.display.flip()

    # Limitação de taxa de quadros (FPS)
    relogio.tick(FPS)

# Finalização do Pygame
pygame.quit()
