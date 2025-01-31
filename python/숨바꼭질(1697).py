from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001

def bfs(start):
    queue = deque()
    queue.append([start, 0])

    while queue:
        cur, time = queue.popleft()

        if cur == K:
            return time

        for x in (cur-1, cur+1, cur*2):
            if 0<= x <= 100000 and not visited[x]:
                visited[x] = True
                queue.append([x, time+1])

print(bfs(N))