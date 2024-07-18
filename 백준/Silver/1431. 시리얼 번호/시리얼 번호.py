import sys

def sum_num(s):
    return sum(int(char) for char in s if char.isdigit())

N = int(sys.stdin.readline().strip())

arr = []
for _ in range(N):
    a = sys.stdin.readline().strip()
    arr.append(a)

arr.sort(key=lambda x: (len(x), sum_num(x), x))
for i in arr:
    print(i)
