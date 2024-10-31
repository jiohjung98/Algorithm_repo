T = int(input())
for i in range(T):
    k = 0
    cnt = 0
    x,y,n = tuple(map(int, input().split()))
    while k <= n:
        if x > y:
            y += x
            cnt += 1
            k = y
        else:
            x += y
            cnt += 1
            k = x
    print(cnt)
        