import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

answer = []

def backtracking(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(idx, len(arr)):
        answer.append(arr[i])
        backtracking(i+1)
        answer.pop()


backtracking(0)
