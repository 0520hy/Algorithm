# 1 빵 2 야채 3 고기   1231
def solution(ingredient):
    answer = 0
    tmp = []
    
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == [1,2,3,1]:
            answer += 1
            tmp.pop()
            tmp.pop()
            tmp.pop()
            tmp.pop()
        
    return answer