from collections import deque

n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

extent_arr = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    global extent
    extent = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                arr[nx][ny] = arr[x][y] + 1
                extent += 1
                queue.append((nx,ny))
    extent_arr.append(extent)
    
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i,j)
            cnt += 1

if extent_arr:
    print(cnt)
    print(max(extent_arr))
else:
    print(0)
    print(0)

# [[1, 2, 0, 1, 2],
#  [0, 3, 4, 0, 0],
#  [0, 0, 0, 0, 0],
#  [1, 0, 1, 2, 3],
#  [0, 0, 2, 3, 4],
#  [0, 0, 3, 4, 5]] 4