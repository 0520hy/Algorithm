def solution(N, stages):
    answer = []
    total_players = len(stages) 
    
    for i in range(1, N+1):
        st = sum(1 for j in stages if j >= i)
        per = sum(1 for j in stages if j == i)
        
        if st == 0: 
            failure_rate = 0
        else:
            failure_rate = per / st
        
        answer.append((i, failure_rate))

    answer.sort(key=lambda x: x[1], reverse=True)
    
    return [x[0] for x in answer]
