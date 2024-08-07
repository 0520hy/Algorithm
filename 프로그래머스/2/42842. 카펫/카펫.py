def solution(brown, yellow):
    answer = []
    col = 0
    row = 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            col = yellow // i
            row = i
            if col*2 + row*2 + 4 == brown:
                answer.append(col + 2)
                answer.append(row + 2)
                
                answer.sort(reverse = True)
                return answer
