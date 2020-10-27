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


def runde_ko_system(players, strengths):  # returns winners
    if (len(players) % 2) == 0:
        winners = []
        for battle in range(int(len(players)/2)):
            player1 = players[battle*2]
            player2 = players[battle*2+1]
            strength_p1 = int(strengths[player1 + 1])
            strength_p2 = int(strengths[player2 + 1])
            win, lose = winner(player1, player2, strength_p1, strength_p2)
            winners.append(win)
        return winners
    else:
        print("An error occured! One of the rounds ended up in a odd count of players")
        return None


def ko_system(players_count, strengths):
    players = []
    for i in range(players_count):
        players.append(i)
    rundenzahl = math.log(players_count, 2)
    for runde_id in range(int(rundenzahl)):
        winners = runde_ko_system(players, strengths)
        players = winners.copy()
    return players[0]


def league_system(players_count, strengths):
    wins = {} #  Dictionary to count wins of each player
    winner = None
    wins_highest = None
    for player in range(players_count):
        wins[player] = 0
    for player1 in wins.keys():
        for player2 in wins.keys():
            if not player1 == player2:
                strength_p1 = int(strengths[player1 + 1])
                strength_p2 = int(strengths[player2 + 1])
                win, lose = winner(player1, player2, strength_p1, strength_p2)
                wins[win] = wins[win] + 1
    for player in wins.keys():
        if wins[player] > wins_highest:
            winner = player
            wins_highest = wins[player]
    return winner


file_path = "tobis_turnier/spielstaerken1.txt"
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()
players_count = len(lines) - 1
highest_strength = 0
player_highest = 0
for line in range(len(lines) - 1):
    if int(lines[line + 1]) > highest_strength:
        highest_strength = int(lines[line + 1])
        player_highest = line
print("Spielerzahl: " + str(players_count))
print("Erwarteter Sieger anch Spielstärke: " + str(player_highest))
print("Sieger des K.O.-Turniers: " + str(ko_system(players_count, lines)))
print("Sieger der Liga: " + str(league_system(players_count, lines)))
