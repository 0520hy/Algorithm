def solution(keymap, targets):
    answer = []

    
    for target in targets:
        total = 0
        for char in target:
            cnt = 101
            
            for key in keymap:
                if char in key:
                    clicks = key.index(char) +1
                    cnt = min(cnt, clicks)
                    
            if cnt == 101:
                total = -1
                break
            else:
                total += cnt
            
        answer.append(total)
                    
            
    return answer