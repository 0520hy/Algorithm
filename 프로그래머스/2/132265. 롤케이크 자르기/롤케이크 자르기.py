# 배열 잘라가며 양쪽 개수 set으로 비교해서 같으면 answer + 1 => 시간 초과

# def solution(topping):
#     answer = 0
#     for i in range(1, len(topping)):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             answer += 1 
#     return answer


# 왼쪽 set 오른쪽 Counter
# 왼쪽으로 토핑 옮겨가며 양쪽 개수 비교
from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for i in range(len(topping)):
        left.add(topping[i])
        right[topping[i]] -= 1
        
        if right[topping[i]] == 0:
            del right[topping[i]]
            
        if len(left) == len(right):
            answer += 1
    return answer