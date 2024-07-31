def solution(n):
    answer = 0
    count = 0
    num = 1

    while count < n:
        if '3' not in str(num) and num % 3 != 0:
            count += 1
            if count == n:
                answer = num
        num += 1
    
    return answer