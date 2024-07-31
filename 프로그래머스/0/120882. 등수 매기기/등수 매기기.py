def solution(score):
    arr = sorted([sum(i) for i in score], reverse = True)
    return [arr.index(sum(i))+1 for i in score]