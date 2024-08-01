import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr = sorted(arr + list(map(int, input().split())), reverse=True)[:N]
print(arr[N-1])
