from collections import deque
import copy

N = int(input())
arr =[]
cnt_arr = []
# 최대 비 수량
max_rain = 0
for _ in range(N):
    a = list(map(int, input().split()))
    max_rain = max(max_rain, max(a))
    arr.append(a)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(1, max_rain):
    # 깊은 복사 방법 두 가지 
    # rain_arr = copy.deepcopy(arr)
    rain_arr = list(map(list, arr)) 
    for j in range(N):
        for k in range(N):
            if arr[j][k] <= i:
                rain_arr[j][k] = 0
            else:
                rain_arr[j][k] = 1
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        # 방문 처리
        rain_arr[x][y] = 2

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if rain_arr[nx][ny] == 0:
                    continue
                if rain_arr[nx][ny] == 1:
                    rain_arr[nx][ny] = 2
                    queue.append((nx,ny))
    cnt = 0
    for a in range(N):
        for b in range(N):
            if rain_arr[a][b] == 1:
                bfs(a,b)
                cnt += 1
    cnt_arr.append(cnt)

print(max(cnt_arr) if cnt_arr else 1)