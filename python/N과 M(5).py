import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

answer = []

def backtracking():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            backtracking()
            answer.pop()

backtracking()
