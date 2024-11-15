for tc in range(1, 2):
    n = int(input())
    arr = []
    for _ in range(8):
        a = list(map(int, input().split()))
        arr.append(a)
    break_point = n // 2
    cnt = 0
    for i in range(8):
        for j in range(8):
            if n % 2 == 0:
                if arr[i][j:j+break_point] == arr[i][j+break_point:j+n]:
                    cnt += 1
    print(f'#{tc} {cnt}')
                    