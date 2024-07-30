def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    answer = my_string.split()
    return sum(map(int, answer))