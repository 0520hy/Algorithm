def solution(slice, n):
    answer = n // slice
    if n % slice > 0:
        return n // slice +1
    return answer