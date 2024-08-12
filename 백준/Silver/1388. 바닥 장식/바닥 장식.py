def count_wooden_planks(N, M, floor):
    visited = [[False] * M for _ in range(N)]
    count = 0

    def dfs(x, y, direction):
        visited[x][y] = True
        if direction == '-':
            if y + 1 < M and floor[x][y + 1] == '-' and not visited[x][y + 1]:
                dfs(x, y + 1, '-')
        elif direction == '|':
            if x + 1 < N and floor[x + 1][y] == '|' and not visited[x + 1][y]:
                dfs(x + 1, y, '|')

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                count += 1
                dfs(i, j, floor[i][j])

    return count


N, M = map(int, input().split())
floor = [input().strip() for _ in range(N)]


print(count_wooden_planks(N, M, floor))
