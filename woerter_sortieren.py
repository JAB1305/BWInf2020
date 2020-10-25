import random


def match(gap, word):  # Überprüft ob Wort und Lücke zusammen passen, gibt Boolean zurück
    match_bool = True
    gap = gap.replace("!", "").replace(".", "").replace("?", "").replace(",", "")
    if len(gap) == len(word):
        for i in range(len(gap)):
            gap_letter = gap[i]
            if gap_letter != "_":
                if not gap_letter == word[i]:
                    match_bool = False
    else:
        match_bool = False
    return match_bool


def sort(gaps, words_initial):
    # Sortiert anhand von zwei Listen die Wörter passend zu den Lücken und gibt die Lösung als Liste zurück
    solution = ""
    solution_dic = {}
    words = words_initial.copy()
    while len(words) != 0:
        words = words_initial.copy()
        random.shuffle(words)
        for g_index in range(len(gaps)):
            gap = gaps[g_index]
            for word in words:
                if match(gap, word):
                    words.remove(word)
                    final_word = list(gap)
                    for i in range(len(final_word)):
                        char = final_word[i]
                        if char == "_":
                            final_word[i] = word[i]
                    solution_dic[g_index] = "".join(final_word)
                    print(words)
                    break;
    for i in range(len(gaps)):
        solution = solution + " " + solution_dic[i]
    return solution


while True:
    entry = int(input("Welches Beispiel soll getestet werden? 1, 2, 3, 4 oder 5? "))
    if 1 <= entry <= 6:
        entry = entry - 1
        file_path = "raetsel/raetsel" + str(entry) + ".txt"
        file = open(file_path, 'r', encoding='utf8')
        lines = file.readlines()
        gaps_raw = lines[0]
        words_raw = lines[1]
        gaps = gaps_raw.split()
        words = words_raw.split()
        print(sort(gaps, words))
    else:
        input("Diese Beispiel existiert nicht!")
