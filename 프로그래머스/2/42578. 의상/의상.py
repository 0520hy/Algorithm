def solution(clothes):
    closet = {}
    
    for name, clo in clothes:
        if clo in closet.keys():
            closet[clo] += [name]
        else:
            closet[clo] = [name]
            
    answer = 1
    for _,i in closet.items():
        answer *= (len(i) + 1)
    return answer -1