from collections import deque
import sys
input = sys.stdin.readline

n, m =  tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt_list = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx =  x + dx[i]
            ny =  y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    cnt_list.append(cnt)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j)


if len(cnt_list) > 0:
    print(len(cnt_list))
    print(max(cnt_list))
else:
    print(0)
    print(0)