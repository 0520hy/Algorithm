def solution(k, score):
    answer = []
    tmp = []

    for i in score:
        if len(tmp) < k:
            tmp.append(i)
        elif min(tmp) < i:
            tmp.remove(min(tmp))
            tmp.append(i)
        answer.append(min(tmp))
    
    return answer
