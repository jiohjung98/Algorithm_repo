from collections import deque

M, N, K = tuple(map(int, input().split()))

# 3차원 배열 선언
graph = [
    [list(map(int, input().split())) for _ in range(N)]
    for _ in range(K)
]

queue = deque()

# 좌,우,상,하,앞,뒤
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(K):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx >= 0 and nx < M and ny >=0 and ny < N and nz >=0 and nz < K and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

bfs()
ans = 0

for g in graph:
    for a in g:
        for elem in a:
            if elem == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(a))

print(ans-1)