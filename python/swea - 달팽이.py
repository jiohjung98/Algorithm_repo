t = int(input())

for tc in range(1, t+1):
    n = int(input())
          #동  남  서  북
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
          #0 1 2 3 
    def in_range(x,y):
        return 0<=x and x < n and 0<=y and y < n
    
    arr = [
        [0] * n
        for _ in range(n)
    ]

    dir = 0
    x,y = 0,0

    arr[0][0] = 1

    for i in range(1, n*n):
        nx, ny = x + dxs[dir], y + dys[dir]

        if not in_range(nx,ny) or arr[nx][ny] != 0:
            dir = (dir+1) % 4
        
        x += dxs[dir]
        y += dys[dir]
        arr[x][y] = i+1
    
    print(f'#{tc}')

    for elem in arr:
        print(*elem, end=' ')
        print()        