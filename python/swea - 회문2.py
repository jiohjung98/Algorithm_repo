def is_pal(arr, leng):
    for lst in arr:
        for i in range(100-leng+1):
            if lst[i:i+leng] == lst[i:i+leng][::-1]:
                return True
    return False

for tc in range(1, 11):
    n = input()
    arr1 = [input() for _ in range(100)]
    arr2 = [''.join(x) for x in zip(*arr1)]
    
    for leng in range(100, 1, -1):
        if is_pal(arr1, leng) or is_pal(arr2, leng):
            break
    print(f'#{n} {leng}')