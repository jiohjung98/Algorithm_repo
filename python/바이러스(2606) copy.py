from collections import deque

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 상 연결되어있는 컴퓨터 쌍 수
graph = [[] for _ in range(n+1)] 

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    queue = deque([x])
    visited = [False] * (n+1)
    visited[x] = True
    cnt = 0

    while queue:
        y = queue.popleft()
        for k in graph[y]:
           if not visited[k]:
               visited[k] = True
               cnt += 1
               queue.append(k) 
    print(cnt)

bfs(1)
