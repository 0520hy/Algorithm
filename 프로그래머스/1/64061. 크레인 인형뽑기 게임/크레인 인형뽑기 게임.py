def solution(board, moves):
    answer = 0
    tmp = []
    
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                item = row[move - 1]
                row[move - 1] = 0
                
                if tmp and tmp[-1] == item:
                    tmp.pop()
                    answer += 2
                else:
                    tmp.append(item)
                break


    return answer