for tc in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))

    while arr[0] > 0:
        for i in range(1,6):
            arr[0] = arr[0] - i
            if arr[0] <= 0:
                break
            else:
                arr.append(arr[0])
                arr.remove(arr[0])
    arr.append(0)
    arr.remove(arr[0])

    for elem in arr:
        elem = str(elem)
    
    print(f'#{n}', *arr)