import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

block_size = 20
x = 100
y = 100
dx = 0
dy = 0

snake = [[x, y]]
snake_length = 1


apple_x = random.randint(0, 580) // block_size * block_size
apple_y = random.randint(0, 380) // block_size * block_size

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -block_size
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = block_size
            elif event.key == pygame.K_LEFT and dx == 0:
                dx = -block_size
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = block_size
                dy = 0

    x += dx
    y += dy

    
    snake.append([x, y])

  
    if len(snake) > snake_length:
        del snake[0]

    
    if x == apple_x and y == apple_y:
        apple_x = random.randint(0, 580) // block_size * block_size
        apple_y = random.randint(0, 380) // block_size * block_size
        snake_length += 1
        score += 1

  
    if x < 0 or x >= 600 or y < 0 or y >= 400:
        print("Game Over (mur)")
        break

   
    for part in snake[:-1]:
        if part == [x, y]:
            print("Game Over (soi-même)")
            break


    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, block_size, block_size))

    
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*part, block_size, block_size))

    
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)
