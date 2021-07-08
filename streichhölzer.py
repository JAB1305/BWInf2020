import pygame
from datetime import datetime
import random
 #  
task_id = input("Welches Beispiel soll getestet werden? 1, 2, 3, 4, 5, 6 oder 7?")
matches_to_move_count = input("Wie viele Streichhölzer sollen bewegt werden?")
file_path_before = "streichhölzer/before" + task_id + ".txt"
file_path_after = "streichhölzer/after" + task_id + ".txt"
startTime = datetime.now()
file = open(file_path_before, 'r', encoding='utf8')
file_after = open(file_path_after, 'r', encoding='utf8')
lines = file.readlines()
lines_after = file_after.readlines()
matches = []
matches_after = []
colors = [(150, 60, 30), (60, 220, 30), (30, 220, 220), (30, 200, 200), (20, 30, 220)]
used_colors = []
minimal_amount_to_move = 0
max_x = int(lines[0].split(",")[0]) + 1
max_y = int(lines[0].split(",")[1]) + 1
scale_y = 700 / max_y
scale_x = 700 / max_x
pygame.init()
pause = False


class Match:
    def __init__(self, surface, x_start, x_end, y_start, y_end, color, after):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        if color is None:
            self.color = (255, 255, 255)
        else:
            self.color = color
        self.after = after
        self.surface = surface

    def paint(self):
        if not self.after:
            pygame.draw.line(self.surface, self.color, (50 + scale_x * self.x_start, 700 - scale_y * self.y_start),
                             (50 + scale_x * self.x_end, 700 - scale_y * self.y_end), 5)
        else:
            pygame.draw.line(self.surface, self.color,
                             (50 + scale_x * self.x_start + 800, 700 - scale_y * self.y_start),
                             (50 + scale_x * self.x_end + 800, 700 - scale_y * self.y_end), 5)


def possible(minimal_amount, requested_amount):
    if requested_amount < requested_amount:
        return False
    elif requested_amount == minimal_amount:
        return True
    diff = requested_amount - minimal_amount
    if (diff % 2) == 0:
        return True
    return False


print(possible(3, 6))

for index in range(len(lines) - 1):
    index = index + 1
    start_coords = lines[index].replace("(", "").replace(")", "").split(",")
    x_start = float(start_coords[0])
    y_start = float(start_coords[1])
    x_end = float(start_coords[2])
    y_end = float(start_coords[3])
    matches.append(Match(None, x_start, x_end, y_start, y_end, None, False))

for index in range(len(lines_after) - 1):
    index = index + 1
    start_coords = lines_after[index].replace("(", "").replace(")", "").split(",")
    x_start = float(start_coords[0])
    y_start = float(start_coords[1])
    x_end = float(start_coords[2])
    y_end = float(start_coords[3])
    matches_after.append(Match(None, x_start, x_end, y_start, y_end, None, True))

while not pause:
    minimal_amount_to_move = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    DISPLAYSURF = pygame.display.set_mode((1600, 800))
    WHITE = (255, 255, 255)
    GRAY = (153, 153, 153)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
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
    for index in range(len(matches)):
        for index_after in range(len(matches_after)):
            if matches[index].x_start == matches_after[index_after].x_start:
                if matches[index].y_start == matches_after[index_after].y_start and matches[index].x_end == \
                        matches_after[index_after].x_end and matches[index].y_end == matches_after[index_after].y_end:
                    matches[index].color = GRAY
                    matches_after[index_after].color = GRAY
    for index in range(len(matches)):
        for index_after in range(len(matches_after)):
            if matches[index].color == (255, 255, 255) and matches_after[index_after].color == (255, 255, 255):
                color_new = random.choice(colors)
                while color_new in used_colors:
                    color_new = random.choice(colors)
                used_colors.append(color_new)
                matches[index].color = color_new
                matches_after[index_after].color = color_new
                minimal_amount_to_move = minimal_amount_to_move + 1
    for match_obj in matches:
        match_obj.surface = DISPLAYSURF
        match_obj.paint()
    for match_obj in matches_after:
        match_obj.surface = DISPLAYSURF
        match_obj.paint()
    pygame.display.update()
