# 치즈 심화문제
# N : 세로 격자 수
# M : 가로 격자 수
# 공기 : 0, 치즈 : 1
# 치즈의 사방면 중 2곳 이상이 공기와 접촉 -> 한시간만에 녹음
# 치즈로 둘러쌓인 공기 -> 효력없음

from collections import deque
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    melt = []

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
                # 여기서 방문처리하면 틀림
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                
                elif graph[nx][ny] == 1:
                    cnt = 0
                    for j in range(4):
                        kx = nx + dx[j]
                        ky = ny + dy[j]

                        if kx >= 0 and kx < n and ky >= 0 and ky < m and graph[kx][ky] == 0 and visited[kx][ky]:
                            cnt += 1
                    if cnt >= 2:
                        melt.append((nx,ny))
    return melt

total_time = 0

while True:
    melt_list = bfs()

    if len(melt_list) == 0:
        break

    for x,y in melt_list:
        graph[x][y] = 0
    total_time += 1

print(total_time)