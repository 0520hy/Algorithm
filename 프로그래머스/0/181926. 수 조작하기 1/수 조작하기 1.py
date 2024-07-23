def solution(n, control):
    arr = list(control)
    for i in arr:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n