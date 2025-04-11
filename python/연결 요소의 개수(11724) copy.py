# 탐색 과정이 재귀 호출로 구현되어 있고, 현재 노드에서 가능한 한 깊게 내려가고 이후에 돌아오는 구조
# -> DFS

# sys.setrecursionlimit(10**7) 의 필요성
# 기본 파이썬 재귀 깊이 제한은 약 1000단계 정도
# 하지만 DFS로 깊은 그래프를 탐색할 경우, 노드 수가 많으면 1000 이상 재귀 호출이 발생할 수 있음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = tuple(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
cnt = 0

def dfs(x):
    visited[x] = 1
    for elem in graph[x]:
        if visited[elem] == 0:
            visited[elem] = 1
            dfs(elem)

for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)