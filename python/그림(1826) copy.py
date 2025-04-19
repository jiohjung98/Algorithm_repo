# 그림의 개수, 그림 중 가장 넓은 것의 너비 구하기 문제
# 그림 : 1로 연결된 것을 한 그림이라고 정의
# 가로, 세로로 연결된 것: 연결된 그림
# 대각선으로 연결된 것: 떨어진 그림
# 그림의 넓이 : 그림에 포함된 1의 개수

# 입력: 세로 크기 n, 가로 크기 m
# 두번째 줄 ~ n+1번째 줄: 그림 정보

from collections import deque
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

width_list = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    witdh = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < n and ny >=0 and ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                witdh += 1
    width_list.append(witdh)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j)

if len(width_list) > 0:
    print(len(width_list))
    print(max(width_list))
else:
    print(0)
    print(0)

    