for i in range(1, 11):
    n = int(input())
    arr  =[]
    for ii in range(100):
        a = list(map(int, input().split()))
        arr.append(a)
        
    sum_arr = []
    for j in range(100):
        sum_of_row = 0
        for jj in range(100):
            sum_of_row += arr[j][jj]
        sum_arr.append(sum_of_row)
           
    for k in range(100):
        sum_of_col = 0
        for w in range(100):
            sum_of_col += arr[w][k]
        sum_arr.append(sum_of_col)
        
    sum_of_v1 = 0
    for x in range(100):
        sum_of_v1 += arr[x][x]
    sum_arr.append(sum_of_v1)
        
    sum_of_v2 = 0
    for y in range(100):
        sum_of_v2 += arr[y][99-y]
    sum_arr.append(sum_of_v2)
        
    print('#' + str(i), max(sum_arr))
            