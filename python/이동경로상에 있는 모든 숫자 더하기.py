n, t = tuple(map(int, input().split()))
direction_arr = input()

# 북동남서
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
cur_dir = 0
arr = [[0 for _ in range(n)] for _ in range(n)]
value = 1
for i in range(n):
    for j in range(n):
        arr[i][j] = value
        value += 1
x, y = (n-1)//2, (n-1)//2
ans = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(t):
    if direction_arr[i] == 'R':
        cur_dir = (cur_dir + 1) % 4
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        # nx = 0, ny = 1
    elif direction_arr[i] == 'L':
        cur_dir = (cur_dir + 3) % 4
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    else:
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if in_range(nx,ny):
           x += dxs[cur_dir]
           y += dys[cur_dir]
           ans += arr[x][y]
    
print(arr)
print(ans)