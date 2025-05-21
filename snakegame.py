import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 0))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    pygame.display.update()
        