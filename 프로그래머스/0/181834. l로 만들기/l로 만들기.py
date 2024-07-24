def solution(myString):
    answer = [n if n > 'l' else 'l' for n in myString]
    return ''.join(answer)