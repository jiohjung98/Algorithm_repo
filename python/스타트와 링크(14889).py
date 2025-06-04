import sys
input = sys.stdin.readline

def backtracking(idx, depth):
    global answer

    # 절반까지 왔을 때
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
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                backtracking(i+1, depth+1)
                visited[i] = False


n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
answer = sys.maxsize
visited = [False] * n
backtracking(0,0)
print(answer)
