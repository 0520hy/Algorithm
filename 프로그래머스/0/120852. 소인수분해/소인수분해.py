def solution(n):
    answer = []
    factor = 2

    while n > 1:
        if n % factor == 0:
            if factor not in answer:
                answer.append(factor)
            n //= factor
        else:
            factor += 1

    return sorted(answer)
