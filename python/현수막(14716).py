from collections import deque

M, N = tuple(map(int, input().split()))

graph = [
    list(map(int, input().split()))
    for _ in range(M)
]

visited = [[False] * (N) for _ in range(M)]
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < M and ny >= 0 and ny < N and visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

cnt = 0 
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)
            cnt += 1

print(cnt)