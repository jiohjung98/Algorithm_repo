# 적록색약인 사람 : 빨강(R), 초록(G) 구분 못 함

from collections import deque

n = int(input())
graph = [
    list(map(str, input().strip()))
    for _ in range(n)
]

visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < n and ny >=0 and ny < n and visited[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1

# 적록색약이 아닌 사람 먼저 진행
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt1 += 1

# 방문 배열 초기화
for i in range(n):
    for j in range(n):
        visited[i][j] = 0

# 적록색약인 사람 배열 재조정
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)