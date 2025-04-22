# 마당은 행(R)과 열(C)로 이루어진 직사각형
# '.'(점) : 빈 필드
# '#' : 울타리
# 'o' : 양
# 'v': 늑대
# 수평, 수직으로만 이동 가능 -> 같은 영역안에 속함
# 탈출할 수 있는 칸 : 어떤 영역에도 속하지 않음

# 영역 안의 양의 양 > 늑대 양:
# -> 양이 이김
# 그 반대의 경우(양의 수와 늑대의 수가 같을 때도):
# -> 늑대가 이김
# 남은 양의 수, 늑대의 수 구해라

# 한 묶음 안에서 양의 수와 늑대의 수를 구해야 함

from collections import deque
import sys
input = sys.stdin.readline

r, c = tuple(map(int, input().split()))
graph = [
    list(map(str, input().strip()))
    for _ in range(r)
]
visited = [[False] * c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

sheep_cnt_list = []
wolf_cnt_list = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    sheep_cnt = 0
    wolf_cnt = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < r and ny >= 0 and ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                queue.append((nx,ny))
                visited[nx][ny] = True

                if graph[nx][ny] == 'o':
                    sheep_cnt += 1
                    graph[nx][ny] = 'x'
                elif graph[nx][ny] == 'v':
                    wolf_cnt += 1
                    graph[nx][ny] = 'x'
    if sheep_cnt > wolf_cnt:
        sheep_cnt_list.append(sheep_cnt)
    else:
        wolf_cnt_list.append(wolf_cnt)

for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != 'o':
            bfs(i,j)

plus_wolf_cnt = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] == 'v':
            plus_wolf_cnt += 1

wolf_cnt_list.append(plus_wolf_cnt)
print(sum(sheep_cnt_list), sum(wolf_cnt_list))