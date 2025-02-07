import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = tuple(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = tuple(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 정렬
for g in graph:
    g = g.sort()

cnt = 1
def dfs(graph, v):
    global cnt
    visited[v]= cnt

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i)

dfs(graph, r)

for i in range(1, n+1):
    print(visited[i])