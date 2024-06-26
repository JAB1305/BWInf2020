from datetime import datetime


def geschenke_verteilen(first_wishes, second_wishes, third_wishes, class_members):
    stats = {
        "first_wishes": 0,
        "second_wishes": 0,
        "third_wishes": 0,
        "no_wish": 0
    }
    old_stats, pupils = stats.copy(), [pupil_id for pupil_id in range(class_members)]
    for pupil_id in range(class_members):
        stats = {
            "first_wishes": 0,
            "second_wishes": 0,
            "third_wishes": 0,
            "no_wish": 0
        }
        relation = {}
        for pupil in pupils:
            if first_wishes[pupil] not in relation.values():
                relation[pupil] = first_wishes[pupil]
                stats["first_wishes"] = stats["first_wishes"] + 1
            elif second_wishes[pupil] not in relation.values():
                relation[pupil] = second_wishes[pupil]
                stats["second_wishes"] = stats["second_wishes"] + 1
            elif third_wishes[pupil] not in relation.values():
                relation[pupil] = third_wishes[pupil]
                stats["third_wishes"] = stats["third_wishes"] + 1
            else:
                stats["no_wish"] = stats["no_wish"] + 1
        if is_better(old_stats, stats):
            old_stats = stats.copy()
        pupils = pupils[1:] + pupils[:1]
    return old_stats, relation


def is_better(stats_old, stats_new):  # Vergleicht die Statistik zweier Druchläufe
    if stats_old["first_wishes"] < stats_new["first_wishes"]:
        return True
    elif stats_old["first_wishes"] == stats_new["first_wishes"] \
            and stats_old["second_wishes"] < stats_new["second_wishes"]:
        return True
    elif stats_old["first_wishes"] == stats_new["first_wishes"] \
            and stats_old["second_wishes"] == stats_new["second_wishes"] \
            and stats_old["third_wishes"] < stats_new["third_wishes"]:
        return True
    else:
        return False


file_path = "wichteln/wichteln" + input("Welches Beispiel soll getestet werden? 1, 2, 3, 4, 5, 6 oder 7?") + ".txt"
startTime = datetime.now()
file = open(file_path, 'r', encoding='utf8')
lines = file.readlines()
class_members = int(lines[0])
first_wishes, second_wishes, third_wishes = {}, {}, {}
print("Geschenke werden zugeordnet ... \n\n")
for pupil in range(class_members):  # Extract wishes from text file into lists
    wishes = lines[pupil + 1].split(" ")
    for i in range(len(wishes)):
        if i == 0 and wishes[i] == "":
            wishes.remove(wishes[i])
        if i == 1 and wishes[i] == "":
            wishes.remove(wishes[i])
        if i == 2 and wishes[i] == "":
            wishes.remove(wishes[i])
        if i == len(wishes):
            break
        wishes[i] = wishes[i].replace("\n", "")
    first_wishes[pupil], second_wishes[pupil], third_wishes[pupil] = wishes[0], wishes[1], wishes[2]
solution, solution_dic = geschenke_verteilen(first_wishes, second_wishes, third_wishes, class_members)
print("Erste Wünsche erfüllt: " + str(solution["first_wishes"]))
print("Zweite Wünsche erfüllt: " + str(solution["second_wishes"]))
print("Dritte Wünsche erfüllt: " + str(solution["third_wishes"]))
print("Zufällig zuzuordnende Geschenke: " + str(solution["no_wish"]))
print("Zuordnung der Geschenke:" + str(solution_dic))
print("Dauer: " + str(datetime.now() - startTime))
