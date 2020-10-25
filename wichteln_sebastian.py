from datetime import datetime
startTime = datetime.now()

def main(item):
    wunsch1 = 0
    wunsch2 = 0
    wunsch3 = 0
    zufall = 0
    rest = []
    zuordnung = []

    # alle Personen werden nacheinander betrachtet
    for z in range(0, len(person)):
        wert = person[z]

        # wenn der 1. Wunsch noch in der liste der Gegenstände (=item) ist, wird dieser der Person zugewiesen und aus...
        # ...der Liste der Gegenstände entfernt
        if wert[0] in item:
            item.remove(wert[0])
            wunsch1 = wunsch1 + 1
            nummer = z + k + 1
            if nummer > 10:  # Aufgrund der neusortierung der Liste der Personen, muss die eigentliche Personennummer erechnet werden
                nummer = nummer - 10
            zuordnung = zuordnung + [str(nummer) + " --> " + wert[0]]

        elif wert[1] in item:  # funktioniert der 1. Wunsch nicht, wird der 2. nach dem gleichen Schema geprüft
            item.remove(wert[1])
            wunsch2 = wunsch2 + 1
            nummer = z + k + 1
            if nummer > 10:
                nummer = nummer - 10
            zuordnung = zuordnung + [str(nummer) + " --> " + wert[1]]

        elif wert[2] in item:  # funktioniert der 2. Wunsch auch nicht, wird der 3. nach dem gleichen Schema geprüft
            item.remove(wert[2])
            wunsch3 = wunsch3 + 1
            nummer = z + k + 1
            if nummer > 10:
                nummer = nummer - 10
            zuordnung = zuordnung + [str(nummer) + " --> " + wert[2]]

        # kann kein Wunsch erfüllt werden, wird die Person der Liste "rest" hinzugefügt
        else:
            nummer = z + k + 1
            if nummer > 10:
                nummer = nummer - 10
            rest = rest + [str(nummer)]

    # die restlichen Personen bekommen dann einen der restlichen Gegenstände zugewiesen
    for l in range(0, len(rest)):
        zuordnung = zuordnung + [rest[0] + " --> " + item[0]]
        zufall = zufall + 1
        item.remove(item[0])
        rest.remove(rest[0])

    return wunsch1, wunsch2, wunsch3, zufall, zuordnung


def überschreiben(wunsch1, wunsch2, wunsch3, zufall, zuordnung, item):
    cacheW1 = wunsch1
    cacheW2 = wunsch2
    cacheW3 = wunsch3
    cacheZufall = zufall
    cacheZuordnung = zuordnung
    übrig = item
    return cacheW1, cacheW2, cacheW3, cacheZufall, cacheZuordnung, übrig


# eingabe = int(input("Welches Szenario soll simuliert werden? 1, 2, 3, 4, 5, 6 oder 7? "))
eingabe = 4
if 1 <= eingabe <= 7:
    wichteln = "wichteln/wichteln" + str(eingabe) + ".txt"
datei = open(wichteln, 'r', encoding='utf8')
lines = datei.readlines()
personen = int(lines[0])

person = []
for p in range(1, personen + 1):
    individual = lines[p]
    person = person + [individual.split()]

gegenstände = []
for i in range(1, personen + 1):
    gegenstände = gegenstände + [str(i)]

# Zwichenspeicher für Ergebnisse
cacheW1 = 0
cacheW2 = 0
cacheW3 = 0
cacheZufall = 0
cacheZuordnung = []
übrig = []

# Die Liste wird so oft neu sortiert, bis jedes Element einmal an erster Stelle stand. Mit jeder dieser Listen wird ein Zuordnungsdurchlauf gestartet
for k in range(0, personen):
    if k > 0:
        person.append(person.pop(0))  # Sortieren der Liste: 1. wird letztes Element
    item = [] + gegenstände
    wunsch1, wunsch2, wunsch3, zufall, zuordnung = main(item)

    # wenn das Ergebnis eines Durchlaufes "gerechter" als das Zwichengespeicherte ist, wird der Zwichenspeicher mit diesem Ergebnis überschrieben. Dies geschieht in der Methode "überschreiben()"
    if wunsch1 > cacheW1:
        cacheW1, cacheW2, cacheW3, cacheZufall, cashZuordnung, übrig = überschreiben(wunsch1, wunsch2, wunsch3, zufall,
                                                                                     zuordnung, item)

    elif wunsch1 == cacheW1 and wunsch2 > cacheW2:
        cacheW1, cacheW2, cacheW3, cacheZufall, cacheZuordnung, übrig = überschreiben(wunsch1, wunsch2, wunsch3, zufall,
                                                                                      zuordnung, item)

    elif wunsch1 == cacheW1 and wunsch2 == cacheW2 and wunsch3 > cacheW3:
        cacheW1, cacheW2, cacheW3, cacheZufall, cacheZuordnung, übrig = überschreiben(wunsch1, wunsch2, wunsch3, zufall,
                                                                                      zuordnung, item)

print("Anzahl 1. Wünsche: " + str(cacheW1))
print("Anzahl 2. Wünsche: " + str(cacheW2))
print("Anzahl 3. Wünsche: " + str(cacheW3))
print("Anzahl zufällig zugeloster Gegenstände: " + str(cacheZufall))
print("Zuordnung nach dem Muster 'Person --> Gegenstand': " + str(cacheZuordnung))
print("Übrig gebiebene Gegenstände: " + str(übrig))
print("Dauer: " + str(datetime.now() - startTime))
datei.close()