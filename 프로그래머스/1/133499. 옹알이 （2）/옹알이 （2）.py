import re

def solution(babbling):
    answer = 0
    
    pattern = re.compile(r'^(aya|ye|woo|ma)+$')

    for i in babbling:
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
            continue
        
        if pattern.match(i):
            answer += 1
    
    return answer
