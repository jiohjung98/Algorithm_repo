from collections import deque

def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    row = len(maps)
    col = len(maps[0])
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
    if maps[row-1][col-1] != 1:
        return maps[row-1][col-1]
    else:
        return -1
    