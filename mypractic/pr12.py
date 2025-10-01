'''class Dog:
    def __init__(self, name):
        self.name = name
        self.value = "Гав"

class Cat:
    def __init__(self, name):
        self.name = name
        self.value = "Мяу"

dog = Dog("Тузик")
cat = Cat("Мурка")

print(f"{dog.name} говорит", dog.value)
print(f"{cat.name} говорит", cat.value)'''

import pygame

pygame.init()
dis = pygame.display.set_mode((500, 400))
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    r1 = pygame.Rect(175, 170, 200, 215)
    color1 = (155, 100, 30)
    pygame.draw.rect(dis, color1, r1, 0)

    r2 = pygame.Rect(295, 200, 50, 50)
    color2 = (156, 40, 100)
    pygame.draw.rect(dis, color2, r2, 0)

    r3 = pygame.Rect(200, 300, 40, 80)
    color3 = (55, 10, 30)
    pygame.draw.rect(dis, color3, r3, 0)

    color4 = (250, 20, 70)
    pygame.draw.line(dis, color, start_pos={295,175}, end_pos={250, 75}, width=3)
    pygame.draw.line(dis, color, start_pos={250,75}, end_pos={350, 175}, width=3)
    pygame.display.update()


quit()

