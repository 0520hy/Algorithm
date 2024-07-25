def solution(number):
    tmp = list(number)
    intArr = list(map(int, tmp))
    return sum(intArr) % 9