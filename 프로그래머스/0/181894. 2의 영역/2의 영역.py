def solution(arr):
    answer = []
    for idx, val in enumerate(arr):
        if val == 2:
            answer.append(idx)
    
    if len(answer) == 0:
        return [-1]
    elif len(answer) == 1:
        return [2]
    else:
        return arr[answer[0]:answer[-1]+1]
