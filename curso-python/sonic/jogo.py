#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUÇÃO DO DESAFIO 2
---
Construa um jogo com uma imagem
de cenário e uma imagem de personagem
que consegue se mover e pular.
"""

import pygame
import sys
from pathlib import Path

# Diretório atual
DIRETORIO_ATUAL = str(Path(__file__).parent.absolute())

# Inicializar Pygame
pygame.init()

# Configurações da tela
tela = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Jogo com Sonic")

# Configurar o relógio
clock = pygame.time.Clock()

# Carregar imagens e música
sonic = pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'knucles-front.png')
sonic_left= pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'knucles-back.png')
sonic_right= pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'knucles-front.png')
tilesheet = pygame.image.load(Path(DIRETORIO_ATUAL) / 'imagens' / 'green-hills.png')
pygame.mixer.init()
pygame.mixer.music.load(Path(DIRETORIO_ATUAL) / 'musicas' / '01 Green Hill Zone Act 1.mp3')
pygame.mixer.music.play(-1)  # Reproduzir música em loop

# Configurações do personagem
sonic_x, sonic_y = 100, 350
sonic_speed = 5
jump_speed = -15  # Velocidade inicial do pulo
gravity = 1  # Força da gravidade
velocity_y = 0  # Velocidade vertical
is_jumping = False  # Estado de pulo

# Configurações da hit box
hitbox = pygame.Rect(sonic_x, sonic_y, sonic.get_width(), sonic.get_height())
hitbox_color = (0, 0, 0)

# Definir o retângulo do chão
chao_y = 500
chao = pygame.Rect(0, chao_y, 800, 100)  # (x, y, largura, altura)

# Tamanho do tile
tile_size = 30 # Ajuste conforme o tamanho dos tiles no seu tilesheet


def get_tile(x, y, tilesheet, tile_size):
    """Extrai um tile do tilesheet."""
    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    tile = pygame.Surface((tile_size, tile_size))
    tile.blit(tilesheet, (0, 0), rect)
    return tile


def draw_background(tela, tilesheet, tile_size, screen_width, screen_height):
    """Desenha o fundo usando tiles do tilesheet."""
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            tile = get_tile((x // tile_size) % (tilesheet.get_width() // tile_size),
                            (y // tile_size) % (tilesheet.get_height() // tile_size),
                            tilesheet, tile_size)
            tela.blit(tile, (x, y))


def handle_movement(keys):
    global sonic,sonic_x, sonic_y, velocity_y, is_jumping, hitbox

    if keys[pygame.K_a]:
        sonic=sonic_left
        sonic_x -= sonic_speed
    if keys[pygame.K_d]:
        sonic=sonic_right
        sonic_x += sonic_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = jump_speed
        is_jumping = True

    # Aplicar gravidade
    velocity_y += gravity
    sonic_y += velocity_y

    # Atualizar a hit box com a nova posição
    hitbox.topleft = (sonic_x, sonic_y)

    # Verificar colisão com o chão
    if hitbox.colliderect(chao) and hitbox.bottom > chao.top:
        sonic_y = chao.top - hitbox.height
        velocity_y = 0
        is_jumping = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    handle_movement(keys)

    # Atualizar a tela
    draw_background(tela, tilesheet, tile_size, 800, 600)  # Desenhar o fundo
    tela.blit(sonic, (sonic_x, sonic_y))

    # Desenhar o chão para visualização
    #pygame.draw.rect(tela, (0, 0, 0), chao)

    pygame.display.flip()
    clock.tick(60)
