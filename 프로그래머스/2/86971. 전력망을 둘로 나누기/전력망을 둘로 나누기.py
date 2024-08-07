from collections import deque

def bfs_count_nodes(start, graph, visited):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        node = q.popleft()
        cnt += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return cnt

def solution(n, wires):
    answer = float("inf")
    graph = [[] for _ in range(n + 1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        
        visited = [False] * (n + 1)
        node_count = bfs_count_nodes(s, graph, visited)
        difference = abs((n - node_count) - node_count)
        answer = min(answer, difference)
        
        graph[s].append(e)
        graph[e].append(s)
    
    return answer
