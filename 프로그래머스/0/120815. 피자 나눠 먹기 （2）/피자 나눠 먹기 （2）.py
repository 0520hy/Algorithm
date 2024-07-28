def solution(n):
    answer = 1
    while(1):
        if (6*answer) % n == 0:
            return answer
        answer += 1