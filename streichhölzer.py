import pygame
from datetime import datetime


file_path = "streichhölzer/streichhölzer" + input("Welches Beispiel soll getestet werden? 1, 2, 3, 4, 5, 6 oder 7?") + ".txt"
startTime = datetime.now()
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()

max_x = int(lines[0].split(",")[0]) + 1
max_y = int(lines[0].split(",")[1]) + 1
pygame.init()
pause = False

while not pause:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    DISPLAYSURF = pygame.display.set_mode((1600, 800))
    WHITE = (255, 255, 255)
    pygame.display.set_caption('Streichholzrätsel')
    pygame.draw.rect(DISPLAYSURF, WHITE, (50, 50, 5, 700))
    pygame.draw.rect(DISPLAYSURF, WHITE, (0, 700, 700, 5))
    pygame.draw.rect(DISPLAYSURF, WHITE, (850, 50, 5, 700))
    pygame.draw.rect(DISPLAYSURF, WHITE, (800, 700, 700, 5))
    for x in range(max_x - 1):
        x = x + 1
        distance_to_left_border = x * (700 / max_x)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(str(x), True, WHITE)
        DISPLAYSURF.blit(text, (distance_to_left_border - text.get_width() // 2, 720 - text.get_height() // 2))
        DISPLAYSURF.blit(text, ((distance_to_left_border - text.get_width()) + 1600 // 2, 720 - text.get_height() // 2))
    for y in range(max_y - 1):
        y = y + 1
        distance_to_top_border = y * (700 / max_y)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(str((y - max_y) * -1), True, WHITE)
        DISPLAYSURF.blit(text, (20 - text.get_width() // 2, distance_to_top_border - text.get_height() // 2))
        DISPLAYSURF.blit(text, (20 - text.get_width() + 1600 // 2, distance_to_top_border - text.get_height() // 2))
    pygame.display.update()
