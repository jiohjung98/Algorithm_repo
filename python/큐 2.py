import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = deque()
for _ in range(n):
    x = input().split()
    if x[0] == 'push':
        data.append(int(x[1]))
    elif x[0]== 'pop':
        if len(data) != 0:
            print(data.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(data))
    elif x[0] == 'empty':
        if len(data) != 0:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if len(data) != 0:
            print(data[0])
        else:
            print(-1)
    else:
        if len(data) != 0:
            print(data[-1])
        else:
            print(-1)