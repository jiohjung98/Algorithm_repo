# 입력 첫째 줄 : tc 개수
# [ 각 테스트 케이스 ]
# 1번째 줄 : 한 변의 길이 I (I*I)
# 2번째 줄 : 현재 있는 칸
# 3번째 줄 : 이동하려는 칸

from collections import deque

dx = [2, 1, -1, -2, 2, 1, -1, -2]
dy = [1, 2, -2, -1, -1, -2, 2, 1]

tc = int(input())
for _ in range(tc):
    I = int(input())
    start_x, start_y = tuple(map(int, input().split()))
    end_x, end_y = tuple(map(int, input().split()))
    visited = [[False] * I for _ in range(I)]
    graph = [[0] * I for _ in range(I)]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True

        while queue:
            x,y = queue.popleft()

            if x == end_x and y == end_y:
                print(graph[x][y])
                return
            
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx >= 0 and nx < I and ny >=0 and ny < I and visited[nx][ny] == False and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    
    bfs(start_x, start_y)