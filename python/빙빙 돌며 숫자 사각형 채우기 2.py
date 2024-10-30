n, m = tuple(map(int, input().split()))

arr = [[0 for _ in range(m)] for _ in range(n)]

# 동남서북
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
#     0, 1, 2, 3
# 3 -> 0
# 0 -> 1
# 1 -> 2
# 2 -> 3

start_dir = 1
x, y = 0,0

def in_range(x,y):
    return 0<=x and x < n and 0<=y and y < m

arr[0][0] = 1

for i in range(1, n*m):
    nx, ny = x + dxs[start_dir], y + dys[start_dir]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        start_dir = (start_dir+3) % 4

    x += dxs[start_dir]
    y += dys[start_dir]
    arr[x][y] = i+1


print(arr)
