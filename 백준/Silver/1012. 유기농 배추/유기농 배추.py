# T 테스트케이스 개수
# M 가로 N 세로 K 배추가 심어져 있는 위치의 개수

from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1: 
                        queue.append([nx, ny])
                        graph[nx][ny] = 0

for _ in range(T):  
    m, n, k = map(int, input().split())
    graph = [[0]*(n) for _ in range(m)] 
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1 
        
    cnt = 0
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                cnt+=1 
    print(cnt)