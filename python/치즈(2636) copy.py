# 치즈(2636)

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
    # 가장 자리는 항상 공기이므로 (0,0) 여기서부터 시작
    queue.append((0,0))
    visited[0][0] = True
    # 이번 BFS에서 녹일 치즈
    melt = []

    while queue:
        x,y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < n and ny >=0 and ny < m and not visited[nx][ny]:
                visited[nx][ny] = True

                # 탐색 좌표가 공기라면
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                # 탐색 좌표가 치즈라면
                elif graph[nx][ny] == 1:
                    melt.append((nx,ny))
    return melt

total_time = 0
last_cheese_cnt = 0

while True:
    melt_list = bfs()

    # 더 이상 녹일 치즈 리스트가 없으면 종료
    if len(melt_list) == 0:
        break
    
    last_cheese_cnt = len(melt_list)
    for x,y in melt_list:
        # 공기랑 맞닿은 가장 자리 치즈 좌표 0으로 변경
        graph[x][y] = 0

    total_time += 1

print(total_time)
print(last_cheese_cnt)