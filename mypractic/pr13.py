import pygame
from pygame.color import THECOLORS
import time

pygame.init()
size = ((500, 400))
dis = pygame.display.set_mode(size)
font = pygame.font.SysFont('courierew', 40)
for y in range(-50, size[1] + 50, 1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    dis.fill(THECOLORS["blue"])
    #шары
    pygame.draw.circle(dis, (255, 255, 255), (250, 300), 60)
    pygame.draw.circle(dis, (255, 255, 255), (250, 200), 45)
    pygame.draw.circle(dis, (255, 255, 255), (250, 125), 30)

    #нос
    pygame.draw.polygon(dis, (255, 165, 0), [(250, 120), (250, 130), (280, 125)])

    #глаза
    pygame.draw.circle(dis, (0, 0, 0), (240, 115), 5)
    pygame.draw.circle(dis, (0, 0, 0), (260, 115), 5)

    fot = pygame.font.SysFont('couriernew', 40)
    text = fot.render(('HELLO'), True, THECOLORS['green'])
    dis.blit(text, (50, y))
    text = fot.render(('HELLO'), True, THECOLORS['black'])
    dis.blit(text, (50, y - 4))
    time.sleep(0.01)
    pygame.display.update()
quit()