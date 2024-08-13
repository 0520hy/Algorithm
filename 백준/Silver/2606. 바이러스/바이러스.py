# 1 N 컴퓨터 수
# 2 V 컴퓨터 쌍의 수
# 한 줄에 한 쌍씩 네트워크 상에서 직접 연결된 컴퓨터 번호 쌍

N = int(input())
V = int(input())

graph = [[] * (N+1) for _ in range(N+1)]

visited = [0] * (N+1)

for i in range(V):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt  = 0

def dfs(i):
    visited[i] = True
    global cnt
    cnt += 1
    for j in graph[i]:
        if not visited[j]:
            dfs(j)



dfs(1)
print(cnt - 1)