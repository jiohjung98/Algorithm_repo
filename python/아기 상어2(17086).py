# // N x M 공간 - 아기 상어 존재
# // 어떤 칸의 안전 거리 - 그 칸과 가장 거리가 가까운 아기 상어와의 거리
# // 이동은 인접합 8방향(대각선 포함) 가능
# // 안전 거리가 가장 큰 칸 구해라

# // 입력
# // 첫째 줄: N, M
# // 둘째 줄 ~ N+1번째 줄 : 공간 상태
# // 0 : 빈 칸, 1 : 아기 상어

# // 0의 입장에서 대각선으로 이동하다가 1을 만나면 종료
# // 이동할 때 마다 cnt++
# // 종료할 때 cnt 배열에 넣고
# // 마지막에 가장 큰 값 출력

from collections import deque
import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(N)
]

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,-1,1]
dist_list = []

def bfs(x,y):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((x,y,1))
    visited[x][y] = True

    while queue:
        x,y,dist = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    dist_list.append(dist)
                    return
                visited[nx][ny] = True
                queue.append((nx,ny, dist+1))

                    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            bfs(i,j)

print(max(dist_list))