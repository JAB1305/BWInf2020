def check_for_pattern(x, y):
    y = y + 2
    if (y + 3) in range(len(lines)):  # Wenn y + 3 auch nicht über Maximum
        ispattern1 = False
        ispattern2 = False
        for y_add in range(4):
            if x + 2 in range(len(lines[y + y_add])):
                if y_add == 0 or y_add == 3:
                    if lines[y + y_add][x] == "X":
                        if lines[y + y_add][x + 1] == "X":
                            if lines[y + y_add][x + 2] == "X":
                                ispattern1 = True
                else:
                    if lines[y + y_add][x] == "X":
                        if lines[y + y_add][x + 1] == " ":
                            if lines[y + y_add][x + 2] == "X":
                                ispattern2 = True
        if ispattern1 and ispattern2:
            print(" Hügel gefunden [" + str(y) + "|" + str(x) + " - " + str(y + 3) + "|" + str(x + 2) + "]")
            return True


def debug():
    y = int(input("y-Wert:"))
    x = int(input("x-Wert:"))
    check_for_pattern(x, y)


def count():
    huegel = 0
    print("--- Beginn der Analyse ---")
    for h in range(height):
        for w in range(width):
            if h + 2 in range(len(lines)):
                if w in range(len(lines[h + 2])):  # Wenn Länge nicht über Maximum
                    if lines[h + 2][w] == "X":
                        if check_for_pattern(w, h):
                            huegel = huegel + 1
                    # Von momentaner "Koordinate" aus auf Muster untersuchen
    print("--- Ende der Analyse --- \n")
    print("Auf der Karte wurden " + str(huegel) + " Hügel gefunden.")


input_map = input("Welche Karte soll analysiert werden?")
if input_map != "":
    map_index = int(input_map)
    if map_index in range(7):
        path = "maps/map" + str(map_index) + ".txt"
        f = open(path, "r", encoding="utf-8")
        lines = f.readlines()
        width = int(lines[0])
        height = int(lines[1])
        mode = input("Zum Starten Enter drücken! (Zum debuggen 'debug' eingeben)")
        if mode == "debug":
            debug()
        else:
            count()
    else:
        print("Diese Karte wurde nicht gefunden!")
else:
    print("Diese Karte wurde nicht gefunden!")
