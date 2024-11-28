import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    a = input().rstrip()
    if len(a) != 1:
        x, y = a.split( )
        stack.append(y)
    else:
        if int(a) == 2:
            if len(stack) != 0:
                print(int(stack[-1]))
                stack.pop(-1)
            else:
                print(-1)
        elif int(a) == 3:
            print(len(stack))
        elif int(a) == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)