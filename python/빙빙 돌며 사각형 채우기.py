alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_arr = list(alphabet)

n, m = tuple(map(int, input().split()))

# 동남서북
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

cur_dir = 0
x,y = 0,0

arr = [[0 for _ in range(m)] for _ in range(n)]
arr[0][0] = 'A'

def in_range(x,y):
    return 0<=x and x < n and 0<=y and y < m

for i in range(1, n*m):
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        cur_dir = (cur_dir + 1) % 4
    x += dxs[cur_dir]
    y += dys[cur_dir]

    z = i % (n*m)
    if z <= 25:
        arr[x][y] = alphabet[i % (n*m)]
    else:
        arr[x][y] = alphabet[(i % 26) % (n*m)]
for a in arr:
    for x in a:
        print(x, end=' ')
    print() 

print(len(alphabet_arr))