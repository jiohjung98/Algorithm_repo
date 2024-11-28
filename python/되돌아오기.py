n = int(input())

mapper = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}

dxs, dys = [1,-1,0,0], [0,0,-1,1]

start_x, start_y = 0,0
cnt = 0

for i in range(n):
    direction, distance = tuple(input().split())
    distance = int(distance)

    direct = mapper[direction]
    for j in range(distance):
        nx, ny =  dxs[direct],  dys[direct]
        start_x += nx
        start_y += ny

        cnt += 1
        if start_x == 0 and start_y == 0:
            print(cnt)
            break
        nx ,ny = 0, 0 
print(-1)

