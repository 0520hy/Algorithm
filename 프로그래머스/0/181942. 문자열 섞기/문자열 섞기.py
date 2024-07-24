def solution(str1, str2):
    fir = list(str1)
    sec = list(str2)
    answer = []
    
    for i in range(len(fir)):
        answer.append(fir[i])
        answer.append(sec[i])

    return ''.join(answer)