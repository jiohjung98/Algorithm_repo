t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt_arr = [0] * 101
    for a in arr:
        cnt_arr[100-a] += 1
    
    print(f'#{n} {100-cnt_arr.index(max(cnt_arr))}')