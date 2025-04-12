from collections import deque

m, n = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
# 토마토가 익은 곳이면 탐색 시작
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >=0 and nx < n and ny >=0 and ny < m and graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()

ans = 0
for g in graph:
    for elem in g:
        if elem == 0:
            print(-1)
            exit()
    ans = max(ans, max(g))

print(ans-1)