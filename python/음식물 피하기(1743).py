# 콘도미니엄 8층 : 학생들이 3끼 식사 해결하는 공간
# 몇몇 학생들 때문에 음식물이 통로 중간중간 떨어져있음
# 음식물 근처에 있는 것들이 뭉침 -> 큰 음식물 쓰레기 탄생
# 통로에 떨어진 음식물 피하기가 어려움
# 떨어진 음식물들 중에 제일 큰 음식물을 피하고자 함

# 입력
# 첫째 줄 : 세로 N, 가로 M, 음식물 쓰레기 개수 K
# 둘째 줄 ~ K+1줄 : 음식물 떨어져있는 좌표(r,c)

# 출력
# 가장 큰 음식물 크기

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = tuple(map(int, input().split()))
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(K):
    r,c = tuple(map(int, input().split()))
    graph[r-1][c-1] = 1

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
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
    cnt_list.append(cnt)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i,j)

print(max(cnt_list))