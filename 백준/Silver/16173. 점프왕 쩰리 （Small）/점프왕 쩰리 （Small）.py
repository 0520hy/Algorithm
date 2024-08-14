# N 게임 구역의 크기

N = int(input())
q = []
s = []

for _ in range(N):
    s.append(list(map(int, input().split())))

q.append([0,0])

while q:
    x, y = q.pop()

    i = s[x][y]

    if i == -1:
        print("HaruHaru")
        exit()
    if i == 0:
        continue

    if x + i < N:
        q.append([x+i, y])
    if y+i < N:
        q.append([x, y+i])

print("Hing")
