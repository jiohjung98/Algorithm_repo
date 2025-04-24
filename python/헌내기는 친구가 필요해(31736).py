# 캠퍼스 크기 : N x M
# 이동 가능 경로 : 상하좌우
# 도연이가 만날 수 있는 사람의 수를 출력
# 아무도 만나지못하면 'TT' 출력

# 입력
# 첫째 줄 : N, M
# 둘째 줄 ~ N+1 줄 : 캠퍼스 정보
# 0 : 빈 공간, X : 벽, I : 도연이, P : 사람
# I는 한 번만 주어짐 -> I부터 bfs 시작

from collections import deque
import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
campus = [
    list(map(str, input().strip()))
    for _ in range(N)
]

visited = [[False] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    global cnt
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    cnt += 1
                queue.append((nx,ny))
                visited[nx][ny] = True
    return cnt

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            bfs(i,j)

if cnt > 0:
    print(cnt)
else:
    print('TT')