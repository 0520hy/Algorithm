def solution(s):
    answer = 0
    s = s.split(' ')
    
    for idx,val in enumerate(s):
        if val != 'Z':
            answer += int(val)
        else:
            answer -= int(s[idx-1])
    return answer