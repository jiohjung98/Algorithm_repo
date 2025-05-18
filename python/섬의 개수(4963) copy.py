from collections import deque 
import sys
input = sys.stdin.readline

while True:
    w, h = tuple(map(int, input().split()))

    if w == 0 and h == 0:
        break

    graph = [
        list(map(int, input().split()))
        for _ in range(h)
    ]

    visited = [[False] * w for _ in range(h)]

    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,-1,1,-1,1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True

        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
        
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    
    print(cnt)