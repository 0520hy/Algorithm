def solution(X, Y):
    answer = ''
    nums = (set(X)&set(Y))
    
    if not nums:
        return '-1'
    elif list(nums) == ['0']:
        return '0'
    
    num_list = sorted(list(nums), reverse = True)
    
    for i in num_list:
        answer += i * min(X.count(i), Y.count(i))
    return answer