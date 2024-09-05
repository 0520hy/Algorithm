from itertools import combinations

def solution(dots):
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        for (x3, y3), (x4, y4) in combinations(dots, 2):
            if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
                continue

            if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
                return 1
    return 0
