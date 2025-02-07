# 방법 1 - dfs
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# graph_reverse = [[] for _ in range(n+1)]

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph_reverse[y].append(x)
    
# s, t = tuple(map(int, input().split()))

# def dfs(node, graph, visited):
#     if visited[node] == 1:
#         return
#     visited[node] = 1
#     for neighbor in graph[node]:
#         dfs(neighbor, graph, visited)
#     return


# visited_s_to_t = [0] * (n+1)
# visited_s_to_t[t] = 1
# dfs(s, graph, visited_s_to_t)

# visited_t_to_s = [0] * (n+1)
# visited_t_to_s[s] = 1
# dfs(t, graph, visited_t_to_s)


# visited_s_to_t_reverse = [0] * (n+1)
# dfs(s, graph_reverse, visited_s_to_t_reverse)

# visited_t_to_s_reverse = [0] * (n+1)
# dfs(t, graph_reverse, visited_t_to_s_reverse)

# cnt = 0
# for i in range(1, n+1):
#     if visited_s_to_t[i] and visited_t_to_s[i] and visited_s_to_t_reverse[i] and visited_t_to_s_reverse[i]:
#         cnt += 1

# print(cnt-2)



# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# graph_reverse = [[] for _ in range(n+1)]

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph_reverse[y].append(x)
    
# s, t = tuple(map(int, input().split()))

# def dfs(node, graph, visited):
#     if visited[node] == 1:
#         return
#     visited[node] = 1
#     for neighbor in graph[node]:
#         dfs(neighbor, graph, visited)
#     return


# visited_s_to_t = [0] * (n+1)
# visited_s_to_t[t] = 1
# dfs(s, graph, visited_s_to_t)

# visited_t_to_s = [0] * (n+1)
# visited_t_to_s[s] = 1
# dfs(t, graph, visited_t_to_s)


# visited_s_to_t_reverse = [0] * (n+1)
# dfs(s, graph_reverse, visited_s_to_t_reverse)

# visited_t_to_s_reverse = [0] * (n+1)
# dfs(t, graph_reverse, visited_t_to_s_reverse)

# cnt = 0
# for i in range(1, n+1):
#     if visited_s_to_t[i] and visited_t_to_s[i] and visited_s_to_t_reverse[i] and visited_t_to_s_reverse[i]:
#         cnt += 1

# print(cnt-2)


# 방법 2 - bfs
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_reverse[y].append(x)

s, t = map(int, input().split())

def bfs(node, graph, visited):
    queue = deque()
    queue.append(node)
    visited[node] = 1

    while queue:
        now = queue.popleft()
        for neighbor in graph[now]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = 1

visited_s_to_t = [0] * (n+1)
visited_s_to_t[t] = 1 # 마지막 도착지 1로 미리 설정
bfs(s, graph, visited_s_to_t)

visited_t_to_s = [0] * (n+1)
visited_t_to_s[s] = 1 # 마지막 도착지 1로 미리 설정
bfs(t, graph, visited_t_to_s) 

visited_s_to_t_reverse = [0] * (n+1)
bfs(s, graph, visited_s_to_t_reverse)

visited_t_to_s_reverse = [0] * (n+1)
bfs(t, graph, visited_t_to_s_reverse) 

cnt = 0
for i in range(1, n+1):
    if visited_s_to_t[i] and visited_t_to_s[i] and visited_s_to_t_reverse[i] and visited_t_to_s_reverse[i]:
        cnt += 1

print(cnt-2)