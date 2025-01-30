from collections import deque

N = int(input())

arr = [
    list(map(int, input().strip()))
    
    for _ in range(N)
]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
cnt = 0
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr):
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1

    answer.append(cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i,j)

print(len(answer))
answer.sort()
for elem in answer:
    print(elem)
