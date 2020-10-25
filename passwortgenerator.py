# Regel 1: 5 Silben, Vokale unf Konsonante im Wechsel
# Regel 2: Wort nach der dritten Silbe durch zweistellige Zahl trennen
# Regel 3: Zusaätzlich am Ende Sonderzeichen

import random;

vokale = ["a", "e", "i", "o", "u", "ö", "ü", "ä"]
konsonante = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x",
              "z", "sch"]
sonderzeichen = ["!", ".", "?", "#"]
zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def pw_generieren():
    pw = ""
    for i in range(3):
        pw = pw + random.choice(konsonante) + random.choice(vokale)
    pw = pw + random.choice(zahlen) + random.choice(
        zahlen)
    for i in range(2):
        pw = pw + random.choice(konsonante) + random.choice(vokale)
    pw = pw + random.choice(sonderzeichen)
    return pw


print(pw_generieren())
