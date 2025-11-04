def solution(arr1, arr2):
    
    r, c1, c2 = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(c2)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer