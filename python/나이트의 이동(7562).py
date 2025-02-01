from collections import deque

T = int(input())
for _ in range(T):
    L = int(input())
    arr = [[0] * L for _ in range(L)]

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    def dfs(x,y):
        queue = deque()
        queue.append([x,y])
        arr[x][y] = 1
        while queue:
            x, y = queue.popleft()

            if x == end_x and y == end_y:
                    print(arr[x][y]-1)
                    return

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= L or ny < 0 or ny >= L:
                    continue

                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx,ny])
    dfs(start_x, start_y)