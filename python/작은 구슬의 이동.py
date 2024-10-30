n, t = tuple(map(int, input().split()))

r, c, d = tuple(input().split())

r = int(r)
c = int(c)

arr = [[0 for j in range(n)] for i in range(n)]
dxs, dys = [0,1,-1,0], [1,0,0,-1]

start_x = r
start_y = c

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

start_direction = mapper[d]

def if_in_range(x,y):
    return 0<= x < n and 0 <= y < n

while t > 0:
    nx, ny = start_x + dxs[start_direction], start_y + dys[start_direction]
    # nx = 0+0=0, ny = 2-1 = 1
    if not if_in_range(nx-1,ny-1):
        t -= 1
        start_direction = 3 - start_direction

    start_x, start_y = start_x + dxs[start_direction], start_y + dys[start_direction]
    t -= 1


print(start_x, start_y)