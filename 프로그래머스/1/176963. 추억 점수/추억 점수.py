# 인물과 추억 점수 dic
# 배열 돌면서 dic에 있으면 점수 합산 후 answer append

def solution(name, yearning, photo):
    
    score = dict(zip(name, yearning))
    answer = []
    
    for i in photo:
        sum = 0
        for j in i:
            if j in score:
                sum += score[j]
        answer.append(sum)
    return answer