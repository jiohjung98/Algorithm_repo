# 시간초과
# 탐색 방식
# 1. backtracking으로 치킨집 M개를 선택하는 모든 조합 시도 (C(13, M) → 최대 1716가지)
# 2. 조합마다 arr을 copy.deepcopy해서 tmp_arr 생성
# 3. 모든 집(1)에서 BFS(dfs)로 가장 가까운 치킨집(2)을 찾음 → 각 집마다 BFS 한 번씩

# 복잡도 분석 (최악 기준)
# - 치킨집 조합: 최대 1716개
# - 집의 수: 최대 100개 (N=50, 2차원 배열)
# - 집마다 BFS: O(N²) → O(50²) = 2500
# - 총 연산: 1716 * 100 * 2500 = 약 4억 2900만 번(10⁸ 이상)
# - 파이썬에서는 연산이 약 10⁶ 이하이면 OK

# from collections import deque
# import copy
# import sys
# input = sys.stdin.readline

# n, m = tuple(map(int, input().split()))

# arr = []
# home_list = []
# chicken_list = []

# for i in range(n):
#     arr.append(list(map(int, input().split())))
#     for j in range(n):
#         if arr[i][j] == 1:
#             home_list.append((i,j))
#         elif arr[i][j] == 2:
#             chicken_list.append((i,j))

# visited = [False] * len(chicken_list)
# cnt_list = []
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def backtracking(idx, cnt):
#     # 선택된 치킨 집 개수가 m과 같으면
#     if cnt == m:
#         global tmp_arr
#         tmp_arr = copy.deepcopy(arr)
#         for i in range(len(visited)):
#             # 선택되지 않은 치킨집이면
#             if visited[i] == False:
#                 x,y = chicken_list[i]
#                 tmp_arr[x][y] = 0
        
#         total = 0
#         for x in range(n):
#             for y in range(n):
#                 if tmp_arr[x][y] == 1:
#                     total += dfs(x,y)

#         cnt_list.append(total)
#         return

#     for i in range(idx, len(chicken_list)):
#         if not visited[i]:
#             visited[i] = True
#             backtracking(i+1, cnt+1)
#             visited[i] = False

# def dfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     visited_local = [[False] * n for _ in range(n)]
#     visited_local[x][y] = True
#     distance = 0

#     while queue:
#         for _ in range(len(queue)):
#             x,y = queue.popleft()
#             if tmp_arr[x][y] == 2:
#                 return distance
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if 0<=nx<n and 0<=ny<n and not visited_local[nx][ny]:
#                     visited_local[nx][ny] = True
#                     queue.append((nx,ny))
#         distance += 1
#     return distance

# backtracking(0,0)
# print(cnt_list)

# dfs 사용하지않고 맨해튼 거리 사용
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

arr = []
home_list = []
chicken_list = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 1:
            home_list.append((i,j))
        elif arr[i][j] == 2:
            chicken_list.append((i,j))

visited = [False] * len(chicken_list)
cnt_list = []

def backtracking(idx, cnt):
    # 선택한 치킨집이 m개면
    if cnt == m:
        total = 0
        for hx, hy in home_list:
            min_dist = sys.maxsize

            for i in range(len(chicken_list)):
                # 현재 치킨집이 선택되었을 때
                if visited[i]:
                    # 치킨집 좌표
                    cx, cy = chicken_list[i]
                    # 맨해튼 거리 구하기(치킨집 좌표와 집좌표 사이 거리)
                    dist = abs(cx-hx) + abs(cy-hy)
                    min_dist = min(min_dist, dist)
            total += min_dist
        cnt_list.append(total)
        return
    
    for i in range(idx, len(chicken_list)):
        if not visited[i]:
            visited[i] = True
            backtracking(i+1, cnt+1)
            visited[i] = False

backtracking(0,0)
print(min(cnt_list))