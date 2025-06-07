import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
answer = []

def backtracking(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, n+1):
        answer.append(i)
        backtracking(i)
        answer.pop()

backtracking(1)