from collections import deque

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_rain = 0
for i in range(n):
    max_rain = max(max_rain, max(graph[i]))

visited = [[0] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt_arr = []

for i in range(1, max_rain):
    # 깊은 복사 
    rain_arr = list(map(list, graph))
    rain_visited = list(map(list, visited))
    for j in range(n):
        for k in range(n):
            # 최대 비 수보다 같거나 작으면 잠기는 지역
            if rain_arr[j][k] <= i:
                rain_arr[j][k] = 0
            else:
                rain_arr[j][k] = 1
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        rain_visited[x][y] = 1

        while queue:
            x, y = queue.popleft()
            
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]

                if nx >=0 and nx < n and ny >=0 and ny < n and rain_visited[nx][ny] == 0 and rain_arr[nx][ny] == 1:
                    queue.append((nx,ny))
                    rain_visited[nx][ny] = 1
    
    cnt = 0
    for x in range(n):
        for y in range(n):
            if rain_arr[x][y] == 1 and rain_visited[x][y] == 0:
                bfs(x,y)
                cnt += 1
    cnt_arr.append(cnt)

print(max(cnt_arr) if cnt_arr else 1)