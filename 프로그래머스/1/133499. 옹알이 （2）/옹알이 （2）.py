def solution(babbling):

    answer = 0
    for i in babbling:
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
                continue
        else:
            i = i.replace('aya',' ').replace('ye',' ').replace('woo',' ').replace('ma',' ').replace(' ', '')
        if i == "":
            answer += 1
    return answer