def solution(picture, k):
    answer = []
    
    for i in picture:
        tmp = ""
        for j in i:
            tmp += j*k
        for count in range(k):
            answer.append(tmp)
    
    return answer