def solution(s):
    tmp = []
    li = s.split("},{")
    
    for i in li:
        tmp.append(i.replace("{","").replace("}","").split(","""))
        
    tmp.sort(key = len)
    answer = []
    
    for i in tmp:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return list(map(int, answer))


