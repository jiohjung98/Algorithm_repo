import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False] * n
answer = sys.maxsize

def backtracking(idx, depth):
    global answer 

    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]

        answer = min(answer, abs(start-link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtracking(i+1, depth+1)
            visited[i] = False

backtracking(0,0)
print(answer)