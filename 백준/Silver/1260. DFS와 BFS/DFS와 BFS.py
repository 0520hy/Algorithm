# N 정점의 개수
# M 간선의 개수
# V 탐색을 시작할 정점의 번호
# M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어짐

from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visitedDfs = [0]*(N+1)
visitedBfs = [0]*(N+1)

def dfs(V):
    visitedDfs[V] = 1
    print(V, end=' ')
    for i in range (1, N+1):
        if graph[V][i] == 1 and visitedDfs[i] == 0:
            dfs(i)



def bfs(V):
    queue = deque([V])
    visitedBfs[V] = 1

    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range (1, N+1):
            if(visitedBfs[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visitedBfs[i] = 1

dfs(V)
print()
bfs(V)