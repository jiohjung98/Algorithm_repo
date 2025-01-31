from collections import deque

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())

    graph = [
        [0] * M
        for _ in range(N)
    ]

    for j in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append([x,y])
        graph[x][y] = 0

        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx,ny])
    
    cnt = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                bfs(x,y)
                cnt += 1
    print(cnt)