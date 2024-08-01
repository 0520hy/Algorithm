def solution(code):
    answer = []
    mode = 0
    
    for i, char in enumerate(code):
        if char == '1':
            mode ^= 1
        elif i % 2 == mode:
            answer.append(char)

    return ''.join(answer) if answer else 'EMPTY'
