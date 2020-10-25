import random


def liste_rotieren(list):
    return list[1:] + list[:1]


def geschenke_verteilen(erste_wünsche, zweite_wünsche, dritte_wünsche, class_members):
    stats = {
        "first_wishes": 0,
        "second_wishes": 0,
        "third_wishes": 0,
        "no_wish": 0
    }
    old_stats = stats.copy()
    pupils_without_gifts = []
    pupils = []
    for i in range(class_members):
        pupils.append(i)
    for j in range(class_members):
        stats = {
            "first_wishes": 0,
            "second_wishes": 0,
            "third_wishes": 0,
            "no_wish": 0
        }
        solution_dic = {}
        for pupil in pupils:
            if erste_wünsche[pupil] not in solution_dic.values():
                solution_dic[pupil] = erste_wünsche[pupil]
                stats["first_wishes"] = stats["first_wishes"] + 1
            elif zweite_wünsche[pupil] not in solution_dic.values():
                solution_dic[pupil] = zweite_wünsche[pupil]
                stats["second_wishes"] = stats["second_wishes"] + 1
            elif dritte_wünsche[pupil] not in solution_dic.values():
                solution_dic[pupil] = dritte_wünsche[pupil]
                stats["third_wishes"] = stats["third_wishes"] + 1
            else:
                pupils_without_gifts.append(pupil)
                stats["no_wish"] = stats["no_wish"] + 1
        if is_better(old_stats, stats):
            old_stats = stats.copy()
        pupils = liste_rotieren(pupils)
    return old_stats


def is_better(stats_old, stats_new):
    if stats_old["first_wishes"] < stats_new["first_wishes"]:
        return True
    elif stats_old["first_wishes"] == stats_new["first_wishes"] and stats_old["second_wishes"] < stats_new["second_wishes"]:
        return True
    elif stats_old["second_wishes"] == stats_new["second_wishes"] and stats_old["third_wishes"] < stats_new["third_wishes"]:
        return True
    else:
        return False


file_path = "wichteln4.txt"
file = open(file_path, 'r', encoding='utf8')

lines = file.readlines()

class_members = int(lines[0])

erste_wünsche = {}
zweite_wünsche = {}
dritte_wünsche = {}

for pupil in range(class_members):  # Extract wishes from text file into lists
    wishes = lines[pupil + 1]
    wishes = wishes.split(" ")
    for i in range(len(wishes)):
        if i == 0 and wishes[i] == "":
            wishes.remove(wishes[i])
    for i in range(len(wishes)):
        if i == 1 and wishes[i] == "":
            wishes.remove(wishes[i])
    for i in range(len(wishes)):
        if i == 2 and wishes[i] == "":
            wishes.remove(wishes[i])
    for i in range(len(wishes)):
        wishes[i] = wishes[i].replace("\n", "")
    erste_wünsche[pupil] = wishes[0]
    zweite_wünsche[pupil] = wishes[1]
    dritte_wünsche[pupil] = wishes[2]
    print(erste_wünsche)
    print(zweite_wünsche)
    print(dritte_wünsche)
print("Start:")
print(geschenke_verteilen(erste_wünsche, zweite_wünsche, dritte_wünsche, class_members))
