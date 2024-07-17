import sys
N = int(sys.stdin.readline())

list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    list.append(num)

list.sort()

for i in list:
    print(i)
