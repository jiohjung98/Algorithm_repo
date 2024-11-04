for i in range(1, 11):
    n = int(input())
    arr =[]
    for _ in range(8):
        a = list(input())
        arr.append(a)
    
    cnt = 0
    half_num = n // 2

    for j in range(8):
        for jj in range(8-n+1):
            tmp_arr = arr[j][jj:jj+n]
            # 짝수
            if n % 2 == 0:
                left_arr = tmp_arr[:half_num]
                right_arr = tmp_arr[half_num:n]
            else:
                left_arr = tmp_arr[:half_num]
                right_arr = tmp_arr[half_num+1:n]
            if left_arr == right_arr[::-1]:
                cnt += 1
    
    for k in range(8):
        for kk in range(8-n+1):
            tmp_arr = []
            for kkk in range(n):
                tmp_val = arr[kk+kkk][k]
                tmp_arr.append(tmp_val)
            if n % 2 == 0:
                left_arr = tmp_arr[:half_num]
                right_arr = tmp_arr[half_num:n]
            else:
                left_arr = tmp_arr[:half_num]
                right_arr = tmp_arr[half_num+1:n]
            if left_arr == right_arr[::-1]:
                cnt += 1

    print('#'+ str(i), cnt)
        