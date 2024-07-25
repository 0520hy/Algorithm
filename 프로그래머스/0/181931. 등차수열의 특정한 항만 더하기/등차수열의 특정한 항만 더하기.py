def solution(a, d, included):
    arr = [a]
    sum = 0
    for i in range(1, len(included)):
        arr.append(a+d*i)
        
    for idx, val in enumerate(included):
        if val == True:
            sum += arr[idx]
    return sum