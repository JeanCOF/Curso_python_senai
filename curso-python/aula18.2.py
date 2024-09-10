import pygame

pygame.init()

# Define o tamanho da janela
janela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Minha Tela")

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Corrigido: não usar parênteses
            deve_continuar = False

pygame.quit()
