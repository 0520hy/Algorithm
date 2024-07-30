def solution(array):
    answer = 0
    seven = str(7)
    
    for i in array:
        answer += str(i).count(seven)
    return answer