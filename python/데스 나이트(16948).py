from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

graph = [[0] * n for _ in range(n)]

def bfs(x,y): 
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()

        if x == r2 and y == c2:
            return graph[x][y]
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return -1

print(bfs(r1,c1))