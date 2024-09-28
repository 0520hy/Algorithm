def solution(number, limit, power):
    div = [0] * (number + 1)
    answer = 0
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            div[j] += 1
    
    for i in div[1:]:  
        if i <= limit:
            answer += i
        else:
            answer += power

    return answer
