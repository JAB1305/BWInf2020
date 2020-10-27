#  Turnierformen:
#  K.O.-System
#  Liga-System
#  Best of 5 K.O.

import random
import math
from datetime import datetime


def most_frequent(list):
    return max(set(list), key=list.count)


def winner(p1, p2, strength_p1, strength_p2):  # returns winner, loser
    chance_p1 = strength_p1 / (strength_p1 + strength_p2)
    p1_wins = random.random() < chance_p1
    if p1_wins:
        return p1, p2
    return p2, p1


def runde_ko_system(players, strengths):  # returns winners
    if (len(players) % 2) == 0:
        winners = []
        for battle in range(int(len(players) / 2)):
            player1 = players[battle * 2]
            player2 = players[battle * 2 + 1]
            strength_p1 = int(strengths[player1 + 1])
            strength_p2 = int(strengths[player2 + 1])
            win, lose = winner(player1, player2, strength_p1, strength_p2)
            winners.append(win)
        return winners
    else:
        print("An error occured! One of the rounds ended up in a odd count of players")
        return None


def runde_ko_system_x5(players, strengths):  # returns winners
    if (len(players) % 2) == 0:
        winners = []
        for battle in range(int(len(players) / 2)):
            player1, player2 = players[battle * 2], players[battle * 2 + 1]
            strength_p1, strength_p2 = int(strengths[player1 + 1]), int(strengths[player2 + 1])
            wins_p1, wins_p2 = 0, 0
            for i in range(5):
                win, lose = winner(player1, player2, strength_p1, strength_p2)
                if win == player1:
                    wins_p1 = wins_p1 + 1
                else:
                    wins_p2 = wins_p2 + 1
            if wins_p1 > wins_p2:
                winners.append(player1)
            else:
                winners.append(player2)
        return winners
    else:
        print("An error occured! One of the rounds ended up in a odd count of players")
        return None


def ko_system(players_count, strengths, x5):
    players = []
    for i in range(players_count):
        players.append(i)
    rundenzahl = math.log(players_count, 2)
    for runde_id in range(int(rundenzahl)):
        if not x5:
            winners = runde_ko_system(players, strengths)
        else:
            winners = runde_ko_system_x5(players, strengths)
        players = winners.copy()
    return players[0]


def league_system(players_count, strengths):
    wins = {}  # Dictionary to count wins of each player
    winner_player = None
    wins_highest = 0
    for player in range(players_count):
        wins[player] = 0
    for player1 in wins.keys():
        for player2 in wins.keys():
            if not player1 == player2:
                strength_p1, strength_p2 = int(strengths[player1 + 1]), int(strengths[player2 + 1])
                win, lose = winner(player1, player2, strength_p1, strength_p2)
                wins[win] = wins[win] + 1
    for player in wins.keys():
        if wins[player] > wins_highest:
            winner_player, wins_highest = player, wins[player]
    return winner_player


file_path = "tobis_turnier/spielstaerken" + input("Welches Beispiel soll getestet werden? 1, 2, 3 oder 4?") + ".txt"
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()
players_count = len(lines) - 1
highest_strength = 0
player_highest = 0
for line in range(len(lines) - 1):
    if int(lines[line + 1]) > highest_strength:
        highest_strength = int(lines[line + 1])
        player_highest = line
start = datetime.now()
average_ko = []
average_ko_x5 = []
average_league = []
for test in range(1000):
    average_ko.append(ko_system(players_count, lines, False))
    average_ko_x5.append(ko_system(players_count, lines, True))
    average_league.append(league_system(players_count, lines))
print("Spielerzahl: " + str(players_count))
print("Erwarteter Sieger anch Spielstärke: " + str(player_highest))
print("Durschnittlicher Sieger des K.O.-Turniers: " + str(most_frequent(average_ko)))
print("Durschnittlicher Sieger des K.O.-Turniers x5: " + str(most_frequent(average_ko_x5)))
print("Durschnittlicher Sieger der Liga: " + str(most_frequent(average_league)))
print("Dauer: " + str(datetime.now() - start))
