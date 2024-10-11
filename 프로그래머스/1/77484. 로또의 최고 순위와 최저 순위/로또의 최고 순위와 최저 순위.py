def solution(lottos, win_nums):
    answer = []
    num = 0
    zero = lottos.count(0)
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0: 6}
    
    for i in lottos:
        if i in win_nums:
            num += 1
    
    if num == 6:
        return [1,1]
    else:
        answer.append(dic[(num+zero)])
        answer.append(dic[num])

        
    return answer