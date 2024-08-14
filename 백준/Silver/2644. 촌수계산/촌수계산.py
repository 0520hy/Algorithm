from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end):
    visited = [False] * (N + 1)
    queue = deque([(start, 0)]) 

    while queue:
        current, depth = queue.popleft()

        if current == end:
            return depth

        if not visited[current]:
            visited[current] = True

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.append((neighbor, depth + 1))

    return -1 

result = bfs(a, b)
print(result)
