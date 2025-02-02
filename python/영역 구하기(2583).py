from collections import deque

M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            arr[j][i] = -1

size_arr = []

def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        arr[x][y] = 1
        size = 1

        while queue:
            x,y = queue.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if arr[nx][ny] == -1:
                     continue
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append((nx,ny))
                    size += 1
        size_arr.append(size)

for a in range(M):
        for b in range(N):
            if arr[a][b] == 0:
                bfs(a,b)
                cnt += 1

print(cnt)
size_arr.sort()
for elem in size_arr:
     print(elem, end=' ')