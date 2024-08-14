# N 정점의 개수
# M 간선의 개수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int, input().split())

if N == 0:
    print(0)
    sys.exit()

visited = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)


