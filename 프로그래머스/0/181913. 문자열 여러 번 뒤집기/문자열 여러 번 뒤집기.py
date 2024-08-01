def solution(my_string, queries):
    my_string = list(my_string)
    
    for start, end in queries:
        my_string[start:end+1] = my_string[start:end+1][::-1]
    
    return ''.join(my_string)
