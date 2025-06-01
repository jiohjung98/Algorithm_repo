from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt_list = []

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            # 바이러스라면
            if tmp_graph[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))

    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    
    cnt_list.append(cnt)

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

makeWall(0)
print(max(cnt_list))