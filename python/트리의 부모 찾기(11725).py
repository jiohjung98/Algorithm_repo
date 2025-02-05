import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visited = [0] * (n+1)
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)

dfs(1)
print(*parent[2:], sep='\n')