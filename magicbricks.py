import sys
import pygame
app = True
pygame.init()
clock = pygame.time.Clock()

screen_height = 600;
screen_width = 600;
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Magic Bricks")
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 -15, 30 , 30)


while app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          app = False  

    pygame.draw.rect(screen, (0,30,4), ball)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()