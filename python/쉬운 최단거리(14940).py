from collections import deque
import copy

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_copy = copy.deepcopy(arr)

arrive_x, arrive_y = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            arrive_x, arrive_y = i, j
            break

visited = [[0] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    arr[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and arr[nx][ny] != 0:
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = 1
                queue.append((nx,ny))

bfs(arrive_x, arrive_y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if arr_copy[i][j] == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = -1

for elem in arr:
    print(*elem)