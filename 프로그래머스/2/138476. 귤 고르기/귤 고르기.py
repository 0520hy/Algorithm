def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

                
    sorted_dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)

    
    for _, val in sorted_dic:
        if k <= 0:
            break
        k -= val
        answer += 1
        

        
    return answer