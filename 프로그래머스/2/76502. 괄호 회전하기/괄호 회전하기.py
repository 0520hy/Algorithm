def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        
        while "()" in rotated or "[]" in rotated or "{}" in rotated:
            rotated = rotated.replace("()", "")
            rotated = rotated.replace("[]", "")
            rotated = rotated.replace("{}", "")

        if len(rotated) == 0:
                answer += 1
                
    return answer