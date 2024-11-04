for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    while n > 0:
        max_value = max(arr)
        min_value = min(arr)
        arr[arr.index(max_value)] -= 1
        arr[arr.index(min_value)] += 1
        n -= 1
    print('#'+str(i), max(arr) - min(arr))