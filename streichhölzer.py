import pygame
from datetime import datetime

file_path = "streichhölzer/streichhölzer" + input(
    "Welches Beispiel soll getestet werden? 1, 2, 3, 4, 5, 6 oder 7?") + ".txt"
startTime = datetime.now()
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()

max_x = int(lines[0].split(",")[0]) + 1
max_y = int(lines[0].split(",")[1]) + 1
scale_y = 700 / max_y
scale_x = 700 / max_x
pygame.init()
pause = False


def add_match(surface, color, coords):
    start_coords = coords.replace("(", "").replace(")", "").split(",")
    x_start = float(start_coords[0])
    y_start = float(start_coords[1])
    x_end = float(start_coords[2])
    y_end = float(start_coords[3])
    pygame.draw.line(surface, color, (50 + scale_x * x_start, 700 - scale_y * y_start), (50 + scale_x * x_end, 700 - scale_y * y_end), 5)


while not pause:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    DISPLAYSURF = pygame.display.set_mode((1600, 800))
    WHITE = (255, 255, 255)
    pygame.draw.line(DISPLAYSURF, WHITE, (50 + scale_x * 1, 700 - scale_y * 1), (50 + scale_x * 2, 700 - scale_y * 1),
                     5)
    pygame.display.set_caption('Streichholzrätsel')
    pygame.draw.rect(DISPLAYSURF, WHITE, (100, 50, 5, 700))  # x axis
    pygame.draw.rect(DISPLAYSURF, WHITE, (50, 700, 700, 5))  # y axis
    pygame.draw.rect(DISPLAYSURF, WHITE, (900, 50, 5, 700))  # x axis
    pygame.draw.rect(DISPLAYSURF, WHITE, (850, 700, 700, 5))  # y axis
    for x in range(max_x - 1):
        x = x + 1
        distance_to_left_border = x * (700 / max_x)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(str(x), True, WHITE)
        DISPLAYSURF.blit(text, (50 + distance_to_left_border - text.get_width() // 2, 720 - text.get_height() // 2))
        DISPLAYSURF.blit(text, ((distance_to_left_border - text.get_width()) + 1650 // 2, 720 - text.get_height() // 2))
    for y in range(max_y - 1):
        y = y + 1
        distance_to_top_border = y * (700 / max_y)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(str((y - max_y) * -1), True, WHITE)
        DISPLAYSURF.blit(text, (30 + text.get_width() // 2, distance_to_top_border - text.get_height() // 2))
        DISPLAYSURF.blit(text, (30 + text.get_width() + 1600 // 2, distance_to_top_border - text.get_height() // 2))
    for index in range(len(lines)-1):
        index = index + 1
        add_match(DISPLAYSURF, WHITE, lines[index])
    pygame.display.update()
