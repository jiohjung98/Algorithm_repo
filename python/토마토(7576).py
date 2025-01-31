from collections import deque

M, N = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 출발점이 여러개인 경우 모두 Queue에 미리 넣어야함
queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx,ny])

bfs()
ans = 0

for a in arr:
    for elem in a:
        if elem == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(a))

print(ans-1)