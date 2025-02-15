n = int(input())
arr = [[0] * 100 for _ in range(100)]

for i in range(n):
    y, x = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
    
ans = 0
for x in range(100):
    ans += arr[x].count(1)

print(ans)