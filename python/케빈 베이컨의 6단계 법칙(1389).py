from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0] * (n+1)

    while queue:
        now = queue.popleft()
        for next in arr[now]:
            # 방문 전이라면 
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)
    return sum(visited)

min_val = float('inf')
ans = 0
for i in range(1, n+1):
    total_distance = bfs(i)
    if total_distance < min_val:
        min_val = total_distance
        ans = i

print(ans)

