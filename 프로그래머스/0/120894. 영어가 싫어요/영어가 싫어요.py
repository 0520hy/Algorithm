def solution(numbers):
    num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for idx, val in enumerate(num):
        numbers = numbers.replace(val, str(idx))
    return int(numbers)