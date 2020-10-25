def main(sortedList, words, gaps):
    for a in range(len(gaps)):
        wert = gaps[a]  # das a. Listenelement der Liste der Lücken wird der Variable "wert" zugewiesen

        # Es wird überprüft, ob (und wenn ja welches) Satzzeichen am Ende des Strings "wert" steht
        ende = 0
        if wert[len(wert) - 1] == ",":
            ende = 1
        if wert[len(wert) - 1] == "!":
            ende = 2
        if wert[len(wert) - 1] == ".":
            ende = 3

        for m in range(len(words)):
            new = ""
            text = words[m]  # das m. Element der Liste der Lösungswörter wird der Variable "text" zugewiesen

            # wenn die Länge der Lücken (ohne Satzzeichen) der Länge der Wörter entspricht, wird in der Funktion "newWord" weiter geprüft, ob das Wort in die Lücke passt
            if ende == 0:
                if len(wert) == len(text):
                    new = newWord(wert, text, new)
            else:
                if len(wert) == len(text) + 1:
                    new = newWord(wert, text, new)

            # entspricht die Variable "new" der Variable "text", wird ans Ende des Wortes (wenn nötig) das benötigte Satzzeichen gehangen, und ...
            if new == text:
                if ende == 1:
                    new = new + ","
                if ende == 2:
                    new = new + "!"
                if ende == 3:
                    new = new + "."
                sortedList = sortedList + [new]  # ... "new" wird der sortierten Liste hinzugefügt
                words.remove(text)  # ... "text" wird aus der Liste der Llsungswörter entfernt
                break
    return sortedList, words


def newWord(wert, text, new):
    # Jedes Zeichen des Strings "wert" muss entweder ein "-" sein, oder dem Buchstaben des Strings "text" entsprechen
    for i in range(len(text)):
        if wert[i] == text[i] or wert[i] == "_":
            new = new + text[
                i]  # ist dies der Fall, wird dem String "new" der Buchstabe an i. Stelle des Strings "text" hinzugefügt
        else:
            new = ""
    return new


eingabe = int(input("Welches Beispiel soll getestet werden? 1, 2, 3, 4 oder 5? "))
if eingabe >= 1 and eingabe <= 5:
    eingabe = eingabe - 1
    raetsel = "raetsel" + str(eingabe) + ".txt"
datei = open(raetsel, 'r', encoding='utf8')
lines = datei.readlines()
lücken = lines[0]
wörter = lines[1]

gaps = lücken.split()
words = wörter.split()
sortedList = []

# sind noch Elemente in der Liste der Lösungswörter, d.h. es konnten noch nicht alle Wörter in Lücken einsortiert werden bzw. es ist der erste Durchlauf, wird ein (weiterer) Durchlauf gestartet
while len(words) > 0:
    for x in range(len(sortedList)):
        # alle Satzzeichen werden von den Elementen der sortierten Liste entfernt
        sortedList[x] = sortedList[x].replace(",", "")
        sortedList[x] = sortedList[x].replace("!", "")
        sortedList[x] = sortedList[x].replace(".", "")
    words = sortedList + words  # die sortierte Liste wird der Liste der Lösungswörter hinzugefügt
    sortedList = []  # die sortierte Liste wird zurückgesetzt
    words[0], words[len(words) - 1] = words[len(words) - 1], words[0]  # Das 1. und letzte Element der Liste der Lösungswörter wird vertauscht
    sortedList, words = main(sortedList, words, gaps)  # der Sortiervorgang wird gestartet

ausgabe = ""
for element in sortedList:
    ausgabe = ausgabe + element + " "

ausgabe = ausgabe[0:len(ausgabe) - 1]
print("Lösung: " + ausgabe)
print("Nicht zugewiesene Wörter: " + str(words))

datei.close()