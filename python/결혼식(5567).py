from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split()) 
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

def bfs(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        friend_num = queue.popleft()
        for people_num in graph[friend_num]:
            if visited[people_num] == 0:
                queue.append(people_num)
                visited[people_num] = visited[friend_num] + 1


bfs(1)
result = 0
for i in range(2, n+1):
    if 0 < visited[i] <= 3:
        result += 1
print(result)
