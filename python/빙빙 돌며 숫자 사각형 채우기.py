n, m = tuple(map(int, input().split()))

dxs, dys = [0,1,0,-1], [1,0,-1,0]

arr = [[0 for _ in range(n)] for _ in range(m)]

x,y= 0,0
dir = 0

arr[x][y] = 1

def if_in_range(x,y):
    return 0<=x and x < n and 0<=y and y < n

for i in range(2, n*m+1):
    nx, ny = x + dxs[dir], y + dys[dir]
    if not if_in_range(nx,ny) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4
    x, y = x + dxs[dir], y + dys[dir]
    arr[x][y] = i


for j in range(n):
    for k in range(m):
        print(arr[j][k], end=' ')
    print()
