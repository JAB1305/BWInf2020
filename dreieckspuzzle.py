def solution_exists(puzzle):
    one_half_found = []
    two_halves = []
    for entry in puzzle:
        if entry in two_halves:
            print(entry)
            return False
        elif entry not in one_half_found:
            one_half_found.append(entry)
        else:
            one_half_found.remove(entry)
            two_halves.append(entry)
    if not len(one_half_found) == 0:
        return False
    return True

def find_solution(puzzle):
    return None