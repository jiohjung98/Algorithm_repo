from collections import deque

n, m = tuple(map(int, input().split()))
graph = [
    list(map(int, input().strip()))
    for _ in range(n)
]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if (graph[nx][ny] == 0):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    print(graph[n-1][m-1])

bfs(0,0)