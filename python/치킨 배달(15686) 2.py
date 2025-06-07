import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
arr = []
home_list = []
chicken_list = []
cnt_list = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 1:
            home_list.append((i,j))
        elif arr[i][j] == 2:
            chicken_list.append((i,j))

visited = [False] * len(chicken_list)

def backtracking(idx, cnt):
    if cnt == m:
        total = 0
        for hx,hy in home_list:
            min_dist = sys.maxsize

            for i in range(len(chicken_list)):
                if visited[i]:
                    cx, cy = chicken_list[i]
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