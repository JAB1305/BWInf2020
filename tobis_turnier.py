#  Turnierformen:
#  K.O.-System
#  Liga-System
#  Best of 5 K.O.

import random
import math


def winner(p1, p2, strength_p1, strength_p2):  # returns winner, loser
    chance_p1 = strength_p1/(strength_p1 + strength_p2)
    p1_wins = random.random() < chance_p1
    if p1_wins:
        return p1, p2
    return p2, p1


def runde(players, strengths):
    if (len(players) % 2) == 0:
        for battle in range(int(len(players)/2)):
            winners = []
            player1 = players[battle*2]
            player2 = players[battle*2+1]
            strength_p1 = int(strengths[player1 + 1])
            strength_p2 = int(strengths[player2 + 1])
            win, lose = winner(player1, player2, strength_p1, strength_p2)
            winners.append(win)
        print(winners)
    else:
        print("An error occured! One of the rounds ended up in a odd count of players")
        return None


def ko_system(players_count, strengths):
    print("Players: " + str(players_count))
    players = []
    for i in range(players_count):
        players.append(i)
    rundenzahl = math.log(players_count, 2)
    for runde_id in range(int(rundenzahl)):
        runde(players, strengths)
    return None


file_path = "tobis_turnier/spielstaerken1.txt"
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()
players_count = len(lines) - 1
print(ko_system(players_count, lines))
