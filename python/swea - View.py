for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(arr)-1):
        left_arr = max(arr[i-2:i])
        right_arr = max(arr[i+1:i+3])
        max_arr = max(left_arr, right_arr)
        if arr[i]  > max_arr:
            cnt += arr[i] - max_arr
    print('#'+str(tc), cnt)