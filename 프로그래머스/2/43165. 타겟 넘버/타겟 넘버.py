def solution(numbers, target):
    answer = 0
    tmp = []
    v = [0]
    
    for num in numbers:
        tmp = []
        for i in v:
            tmp.append(i + num)
            tmp.append(i - num)
        v = tmp
    
    for s in v:
        if s == target:
            answer += 1
        
    return answer