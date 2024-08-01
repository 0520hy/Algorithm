def solution(ineq, eq, n, m):
    if eq == "!":
        answer = str(n) + ineq + str(m)
    else: 
        answer = str(n) + ineq  + eq + str(m)
    return 1 if eval(answer) else 0