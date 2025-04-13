# 좌표가 0인 곳에 1(벽)로 3개를 채웠을 때 탐색 진행
# 매 탐색에서 안전 공간 최대값을 업데이트
# 매 탐색마다 원본 그래프로 다시 반영해야 함
# 방문한 것 저장하는 배열도 매 탐색마다 초기화를 진행해야 함


import sys
input = sys.stdin.readline
from collections import deque
import copy

# 지도 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >=0 and nx < n and ny >=0 and ny < m and tmp_graph[nx][ny] == 0):
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))
    
    cnt = 0
    global answer
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    
    answer = max(cnt, answer)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

# 전역 변수로 answer를 사용하려면 함수 외부에서 초기값을 반드시 선언해줘야 함!!
answer = 0
makeWall(0)
print(answer)