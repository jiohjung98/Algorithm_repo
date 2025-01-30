from collections import deque

a = int(input())
b = int(input())

graph = [[] for _ in range(a + 1)]

# 그래프 연결 정보 입력
for _ in range(b):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 연결

def bfs(v):
    queue = deque([v])
    visited = [False] * (a+1)
    visited[v] = True
    cnt = 0

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                cnt += 1
    print(cnt)

bfs(1)