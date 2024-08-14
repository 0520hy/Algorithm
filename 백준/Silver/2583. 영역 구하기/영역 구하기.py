# M * N
# K 직사각형의 좌표 개수

from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if (0 <= ny < M) and (0 <= nx < N) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                cnt += 1
    return cnt


for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] += 1

result = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            result.append(bfs(i, j))

print(len(result))
result.sort()
print(" ".join(map(str, result)))

