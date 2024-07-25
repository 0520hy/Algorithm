def solution(myString, pat):
    answer = 0
    
    for idx, _ in enumerate(myString):
        if myString[idx:].startswith(pat):
            answer += 1
    return answer