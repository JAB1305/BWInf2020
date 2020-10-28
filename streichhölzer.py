import pygame
from datetime import datetime

task_id = input("Welches Beispiel soll getestet werden? 1, 2, 3, 4, 5, 6 oder 7?")
file_path_before = "streichhölzer/before" + task_id + ".txt"
file_path_after = "streichhölzer/after" + task_id + ".txt"
startTime = datetime.now()
file = open(file_path_before, 'r', encoding='utf8')
file_after = open(file_path_after, 'r', encoding='utf8')
lines = file.readlines()
lines_after = file_after.readlines()
matches = []
matches_target = []
matches_to_be_moved_left = []
matches_to_be_moved_right = []
match_colors = {}
colors = [(220, 60, 30), (60, 220, 30), (30, 60, 220), (30, 200, 200), (220, 30, 220)]

max_x = int(lines[0].split(",")[0]) + 1
max_y = int(lines[0].split(",")[1]) + 1
scale_y = 700 / max_y
scale_x = 700 / max_x
pygame.init()
pause = False


def add_match(surface, color, color_highlight, coords):
    start_coords = coords.replace("(", "").replace(")", "").split(",")
    x_start = float(start_coords[0])
    y_start = float(start_coords[1])
    x_end = float(start_coords[2])
    y_end = float(start_coords[3])
    match = (str(x_start) + ", " + str(y_start) + ", " + str(x_end) + ", " + str(y_end))
    matches.append(match)
    already_exists = False
    for match_target in matches_target:
        if match_target == (str(x_start) + ", " + str(y_start) + ", " + str(x_end) + ", " + str(y_end)):
            already_exists = True
    if already_exists:
        pygame.draw.line(surface, color_highlight, (50 + scale_x * x_start, 700 - scale_y * y_start),
                         (50 + scale_x * x_end, 700 - scale_y * y_end), 5)
    else:
        pygame.draw.line(surface, color, (50 + scale_x * x_start, 700 - scale_y * y_start),
                         (50 + scale_x * x_end, 700 - scale_y * y_end), 5)
        if not match in match_colors:
            match_colors[match] = colors  # TODO: Each match that has to be moved, gets a color. Same color is used later


def add_match_after(surface, color, color_highlight, coords):
    start_coords = coords.replace("(", "").replace(")", "").split(",")
    x_start = float(start_coords[0])
    y_start = float(start_coords[1])
    x_end = float(start_coords[2])
    y_end = float(start_coords[3])
    already_exists = False
    for match in matches:
        if match == (str(x_start) + ", " + str(y_start) + ", " + str(x_end) + ", " + str(y_end)):
            already_exists = True
    if already_exists:
        pygame.draw.line(surface, color_highlight, (50 + scale_x * x_start + 800, 700 - scale_y * y_start),
                         (50 + scale_x * x_end + 800, 700 - scale_y * y_end), 5)
    else:
        pygame.draw.line(surface, color, (50 + scale_x * x_start + 800, 700 - scale_y * y_start),
                         (50 + scale_x * x_end + 800, 700 - scale_y * y_end), 5)
    matches_target.append(str(x_start) + ", " + str(y_start) + ", " + str(x_end) + ", " + str(y_end))


while not pause:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    DISPLAYSURF = pygame.display.set_mode((1600, 800))
    WHITE = (255, 255, 255)
    GRAY = (203, 203, 203)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
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
    for index in range(len(lines) - 1):
        index = index + 1
        add_match(DISPLAYSURF, WHITE, GREEN, lines[index])
    for index in range(len(lines_after) - 1):
        index = index + 1
        add_match_after(DISPLAYSURF, GRAY, GREEN, lines_after[index])
    pygame.display.update()
