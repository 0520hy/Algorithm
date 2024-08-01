def solution(arr):
    answer = 0
    tmp = arr
    
    while(1):
        newArr = []
        for i in tmp:
            if i >= 50 and i % 2 == 0:
                i = i / 2
            elif i < 50 and i % 2 == 1:
                i = i * 2 + 1
            newArr.append(i)
        if tmp == newArr:
            break
        else:
            tmp = newArr
            answer += 1
            
    return answer