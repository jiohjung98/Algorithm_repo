from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        # 방문 처리
        graph[x][y] = 2

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >=0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 2
    cnt = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)