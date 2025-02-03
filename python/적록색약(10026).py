from collections import deque

N = int(input())

arr = [
    list(map(str, input().strip()))
    for _ in range(N)
]

visited = [[False] * (N) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == False:
                # 이전 색상이랑 같을 때
                if arr[x][y] == arr[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j)
            cnt1 += 1

# visited 배열 다시 False로 초기화
for i in range(N):
    for j in range(N):
        visited[i][j] = False

# 원본 배열 적록색약인 사람 기준으로 변경
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)