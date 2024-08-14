import sys
input = sys.stdin.read

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, word, res):

    if depth == 5:
        res.add(word)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5: 
            dfs(nx, ny, depth + 1, word + data[nx][ny], res)


data = input().splitlines()
data = [row.split() for row in data]  
res = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, data[i][j], res)  

print(len(res))
