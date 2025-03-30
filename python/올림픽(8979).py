import sys
input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
idx = [arr[i][0] for i in range(n)].index(k)

for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break