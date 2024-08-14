# N 노드의 개수

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

answer = [0]*(N+1)

def bfs():
    while queue:
        n = queue.popleft()
        for p in graph[n]:
            if answer[p] == 0:
                answer[p] = n
                queue.append(p)

bfs()
result = answer[2:]
for x in result:
    print(x)
