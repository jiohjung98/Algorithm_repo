for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if arr[j][i] == 1:
                flag = 1
            elif arr[j][i] == 2:
                if flag:
                    cnt += 1
                    flag = 0
    
    print(f'#{tc} {cnt}')
            