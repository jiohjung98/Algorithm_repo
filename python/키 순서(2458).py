# 나한테 오는 노드(나보다 작음) + 내가 갈 수 있는 노드(나보다 큼) = n-1 -> 키가 몇 번째인지 알 수 있음
# 플로이드 와샬 알고리즘

import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x][y] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

answer = 0
for i in range(1, n+1):
    bigger = sum(graph[i][1:])
    smaller = sum(graph[j][i] for j in range(1, n+1))
    if bigger + smaller == n-1:
        answer += 1

print(answer)