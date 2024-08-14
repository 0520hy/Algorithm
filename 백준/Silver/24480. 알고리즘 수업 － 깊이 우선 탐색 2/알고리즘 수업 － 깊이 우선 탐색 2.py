import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

def dfs(value):
    global cnt
    visited[value] = cnt    
    for v in sorted(graph[value], reverse=True):
        if visited[v] == 0:
            cnt += 1
            dfs(v)

cnt = 1

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
