def solution(strArr):
    answer = [len(i) for i in strArr]
    arr = []
    for i in set(answer):
        arr.append(answer.count(i))
    return max(arr)