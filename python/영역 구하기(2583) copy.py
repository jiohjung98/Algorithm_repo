# 첫 줄 입력 : M, N, K
# 둘째 줄 부터 K개의 줄
# 한 줄에 하나씩 왼쪽 아래(x,y), 오른쪽 위(x,y) 좌표
from collections import deque

m, n, k = tuple(map(int, input().split()))
graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt_list = []

for _ in range(k):
    bottom_x, bottom_y, top_x, top_y = tuple(map(int, input().split()))

    for i in range(bottom_y, top_y):
        for j in range(bottom_x, top_x):
            # 직사각형 부분 1로 처리
            graph[i][j] = 1
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < m and ny >=0 and ny < n and visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
        
    cnt_list.append(cnt)
    
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == False:
            bfs(i,j)

cnt_list.sort()
print(len(cnt_list))
for elem in cnt_list:
    print(elem, end=' ')