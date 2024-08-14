# W 너비
# H 높이
# 1 땅, 0 바다

import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y):
    if x < 0 or x >= b or y < 0 or y >= a:
        return False
    
    if graph[x][y] == 0:
        return False
    
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    
while True:

    a,b = map(int,input().split())
    if (a,b) == (0,0): break

    graph = []
    for i in range(b):
        graph.append(list(map(int,input().split())))

    cnt = 0
    for i in range(b):
        for j in range(a):
            if dfs(i,j):
                cnt += 1
    print(cnt)