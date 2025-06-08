import sys
input = sys.stdin.readline

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

answer = []
cnt = 0
def backtracking(idx):
    global cnt
    if sum(answer) == s and len(answer) > 0:
        cnt += 1
    
    for i in range(idx, n):
        answer.append(arr[i])
        backtracking(i+1)
        answer.pop()

backtracking(0)
print(cnt)