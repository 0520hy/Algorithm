from collections import deque

N = int(input())
graph = []
maxHeight = 0 

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > maxHeight:
            maxHeight = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, v, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > v and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

answer = 0

for i in range(maxHeight):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)  
                cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)
