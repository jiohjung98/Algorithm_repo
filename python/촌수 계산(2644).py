n = int(input())
a, b = tuple(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

def dfs(current, target, cnt):
    visited[current] = True

    if current == target:
        print(cnt)
        exit(0)
    else:
        for neighbor in graph[current]:
            if not visited[neighbor]:
                dfs(neighbor, target, cnt + 1)

dfs(a, b, 0)
print(-1)