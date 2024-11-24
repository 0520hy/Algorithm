def solution(citations):

    for i in range(len(citations), -1, -1):
        answer = sum(j >= i for j in citations)
        if answer >= i:
            return i