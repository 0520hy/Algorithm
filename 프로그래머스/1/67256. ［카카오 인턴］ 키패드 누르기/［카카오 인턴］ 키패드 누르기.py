# def solution(numbers, hand):
#     left = [1,4,7,"*"]
#     mid = [2,5,8,0]
#     right = [3,6,9,"#"]
#     l = "*"
#     r = "#"
#     answer = ''
    
#     if hand == "right":
#         hand = "R"
#     else:
#         hand = "L"
    
    
#     for number in numbers:
#         if number in left:
#             answer += "L"
#             l = number
#         elif number in right:
#             answer += "R"
#             r = number
#         elif number in mid:
#             if abs(left.index(l) - mid.index(number)) > abs(right.index(r) - mid.index(number)):
#                 answer += "R"
#                 r = right[mid.index(number)]
#             elif abs(left.index(l) - mid.index(number)) < abs(right.index(r) - mid.index(number)):
#                 answer += "L"
#                 l = left[mid.index(number)]
#             else:
#                 answer += hand
            
    
#     return answer

def solution(numbers, hand):
    left = [1, 4, 7, "*"]
    mid = [2, 5, 8, 0]
    right = [3, 6, 9, "#"]

    l = "*"
    r = "#"
    answer = ''

    hand = "R" if hand == "right" else "L"

    for number in numbers:
        if number in left:
            answer += "L"
            l = number 
        elif number in right:
            answer += "R"
            r = number 
        else:
            left_dist = abs(mid.index(number) - mid.index(l)) if l in mid else abs(left.index(l) - mid.index(number)) + 1
            right_dist = abs(mid.index(number) - mid.index(r)) if r in mid else abs(right.index(r) - mid.index(number)) + 1

            if left_dist < right_dist:
                answer += "L"
                l = number
            elif left_dist > right_dist:
                answer += "R"
                r = number
            else:
                answer += hand
                if hand == "L":
                    l = number
                else:
                    r = number

    return answer
