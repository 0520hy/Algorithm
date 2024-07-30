import math

def solution(balls, share):
    if share > balls:
        return 0 

    return math.comb(balls, share)
