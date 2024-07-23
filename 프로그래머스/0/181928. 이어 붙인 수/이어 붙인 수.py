def solution(num_list):
    odd = ''
    even = ''
    for idx, val in enumerate(num_list):
        if val % 2 == 0:
            even += str(val)
        else:
            odd += str(val)
    return int(even) + int(odd)