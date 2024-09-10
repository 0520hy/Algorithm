def solution(a, b, n):
    answer = 0
    
    while (n >= a):
        rest = n % a
        n = (n // a) * b
        answer += n
        n += rest
    return answer