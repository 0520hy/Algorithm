def solution(order):
    answer = str(order)
    return answer.count('3') + answer.count('6') + answer.count('9')