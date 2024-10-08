def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in skip:
        alpha = alpha.replace(i, '')
    
    
    for j in s:
        answer += alpha[(alpha.index(j) + index) % len(alpha)]

    return answer