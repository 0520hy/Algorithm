from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0
        userP = k
        
        for n, s in p:
            if userP >= n:
                userP -= s
                cnt += 1
                
        answer = max(answer, cnt)
        
    return max(answer, cnt)