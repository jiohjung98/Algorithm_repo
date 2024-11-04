n = int(input())

grid = []
for _ in range(n):
    g = list(map(int, input().split()))
    grid.append(g)

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == visited[x][y] == 0:
        return False
    return True

def dfs(x,y):
    # 상하좌우
    dxs, dys = [-1,1,0,0], [0,0,-1,1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

dfs(0,0)

print(visited)