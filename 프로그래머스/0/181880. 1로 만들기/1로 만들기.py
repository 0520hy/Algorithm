def solution(num_list):
    
    answer = 0
    
    for val in num_list:
        while val > 1:
            if val % 2 == 0:
                val = val // 2
                answer += 1
            else:
                val = (val-1) // 2
                answer += 1    
    return answer