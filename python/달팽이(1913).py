N = int(input())
find_num = int(input())

# 하, 우, 상, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [[0]*(N) for _ in range(N)]

# 시작 위치 설정
x, y = 0, 0
num = N**2
graph[x][y] = num

# 찾을 값 위치
find_x, find_y = 0, 0

# 초기 방향
dir_idx = 0

while num > 1:
    nx = x + dx[dir_idx]
    ny = y + dy[dir_idx]

    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
        num -= 1
        graph[nx][ny] = num
        x, y = nx, ny # x, y값 업데이트

        if num == find_num:
            find_x = nx
            find_y = ny

    else:
        dir_idx = (dir_idx + 1) % 4

for row in graph:
    print(*row)

print(find_x+1, find_y+1)