from collections import deque

# 방의 크기 n x m
n, m = map(int, input().split())

# start_dir : 0 - 북쪽, 1 - 동쪽, 2 - 남쪽, 3 - 서쪽
start_x, start_y, start_dir = map(int, input().split())

# 0 - 빈 칸, 1 - 벽
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 방문 배열
visited = [[0] * m for _ in range(n)]

# 방향 설정: 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

def bfs(x,y,d):
    global cnt
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 2
    cnt += 1

    while queue:
        x, y = queue.popleft()
        can_go_flag = 0

        for _ in range(4):
            # 현재 바라보고 있는 방향에서 반시계 방향 위치 확인
            d = (d+3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            
            # 1. 반시계로 돈 좌표가 범위에 안벗어나고, 벽이 아니고, 방문을 안했을 때
            if nx >= 0 and nx < n and ny >=0 and ny < m and arr[nx][ny] != 1 and visited[nx][ny] != 2:
                visited[nx][ny] = 2
                queue.append((nx,ny))
                cnt += 1
                # 위 if문이 성공했을 때 flag 설정
                can_go_flag = 1
                # 청소할 공간을 찾았으므로 탈출 후 새로 queue 돌기
                break

        # 한 칸 후진 
        if can_go_flag == 0:
            # 후진하는 좌표가 벽이 아니면
            if arr[x-dx[d]][y-dy[d]] != 1:
                queue.append((x-dx[d], y-dy[d]))
            # 후진하는 좌표가 벽이면
            else:
                print(cnt)
                break

bfs(start_x, start_y, start_dir)