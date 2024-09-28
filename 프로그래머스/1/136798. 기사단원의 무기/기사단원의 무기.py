import math

def solution(number, limit, power):
    div = []
    answer = 0
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                cnt += 1
                if j != i // j: 
                    cnt += 1
        div.append(cnt)
        
    for i in div:
        if i <= limit:
            answer += i
        else:
            answer += power

    return answer
