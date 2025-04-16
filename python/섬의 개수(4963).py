# 갈 수 있는 범위 : 가로, 세로, 대각선
# 입력 마지막에 0 0 이 오면 입력 종료
# 1 : 땅 , 0 : 바다
from collections import deque

while True:
    w, h = tuple(map(int, input().split()))

    # 입력이 0,0이면 종료
    if w == 0 and h == 0:
        break

    graph = [
        list(map(int, input().split()))
        for _ in range(h)
    ]

    # 가로, 세로, 대각선 범위
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    # 방문 배열
    visited = [[0] * w for _ in range(h)]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = 1

        while queue:
            x, y = queue.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < h and ny >=0 and ny < w and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    
    cnt = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and visited[x][y] == 0:
                bfs(x,y)
                cnt += 1
    print(cnt)

# 3 2
# [
#     [1, 1, 1],
#     [1, 1, 1]
# ]