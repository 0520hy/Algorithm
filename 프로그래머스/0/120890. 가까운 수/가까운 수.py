def solution(array, n):
    array.append(n)
    array.sort()
    num = array.index(n)
    
    if num == 0:
        return array[1]
    elif num == len(array) - 1:
        return array[-2]
    else:
        if n - array[num - 1] <= array[num + 1] - n:
            return array[num - 1]
        else:
            return array[num + 1]