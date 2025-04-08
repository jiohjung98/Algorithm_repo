from collections import deque

n = int(input())
graph = [
    list(map(int, input().strip()))
    for _ in range(n)
]

visited = [[False] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt_list = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < n and ny >=0 and ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx,ny))
    cnt_list.append(cnt)

total_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            total_cnt += 1

print(total_cnt)
cnt_list.sort()
for elem in cnt_list:
    print(elem, end='\n')