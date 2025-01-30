N, M, V = list(map(int, input().split()))

# 리스트 컴프리헨션 - 행렬 만들기
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs_visited_arr = [0] * (N+1)
bfs_visited_arr = [0] * (N+1)

# dfs - 재귀함수 이용
def dfs(V):
    dfs_visited_arr[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if (graph[V][i] == 1 and dfs_visited_arr[i] == 0):
            dfs(i)

# bfs - queue 이용
def bfs(V):
    queue = [V]
    bfs_visited_arr[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if (graph[V][i] == 1 and bfs_visited_arr[i] == 0):
                queue.append(i)
                bfs_visited_arr[i] = 1

dfs(V)
print()
bfs(V)