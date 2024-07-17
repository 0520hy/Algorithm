def solution(money):
    cnt = money // 5500
    rest = money % 5500
    return [cnt, rest]