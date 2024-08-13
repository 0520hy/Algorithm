# 단지번호 붙이기
# 1 집이 있는 곳, 0 없는 곳
# N 총 단지 수 


def dfs(x, y):
    if x <= -1 or x >=N or y <= -1 or y >=N:
        return False
    if graph[x][y] == 1:
        global count
        graph[x][y] = 0
        count += 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x,y+1)
        return True
    return False


N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

answer = 0

counts = []  
for i in range(N):
    for j in range(N):
        count = 0 
        if dfs(i, j) == True:
            counts.append(count)

counts.sort()  
print(len(counts))  
for count in counts:
    print(count)  